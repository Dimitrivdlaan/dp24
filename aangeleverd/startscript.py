from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

# Databaseconfiguratie
host = "localhost"
port = 3306  # Standaard MariaDB/MySQL-poort, kan ook 3307 zijn
database = "hr"
user = "root"
password = "password"
view_name = "view_kpi_waardering_rit"  # de view voor jouw kpi-story


def create_db_engine():
    return create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


def load_db_ratings(engine) -> tuple[pd.Series, str]:
    """Haal de eerste 6 waarderingen uit de databaseview op.

    Probeert eerst de opgegeven view_name, daarna een fallback met de 'vieuw_' spelling.
    """

    view_candidates = [view_name, "vieuw_kpi_waardering_rit"]
    errors: list[str] = []

    for candidate in view_candidates:
        try:
            df = pd.read_sql(f"SELECT * FROM {candidate} LIMIT 6", con=engine)
        except Exception as exc:
            errors.append(f"{candidate}: {exc}")
            continue

        kolom = "waardering_norm"
        if kolom not in df.columns:
            raise RuntimeError(
                f"Kolom '{kolom}' ontbreekt in view {candidate}. "
                f"Beschikbare kolommen: {list(df.columns)}"
            )

        ratings = df[kolom].dropna().head(4)
        if ratings.empty:
            raise RuntimeError(f"Geen waarderingen gevonden in de view {candidate}.")

        return ratings.reset_index(drop=True), candidate

    raise RuntimeError(
        "Kon geen data ophalen uit de views. Probeer view_namen te controleren. Fouten: "
        + " | ".join(errors)
    )


def load_shuttle_log(path: Path) -> pd.Series:
    """Lees het shuttle_log JSON-bestand en pak de eerste 6 waarderingen."""

    try:
        df = pd.read_json(path)
    except ValueError as exc:
        raise RuntimeError(f"Kon shuttle_log niet inlezen: {exc}") from exc

    if "gemiddelde_waardering_rit" not in df.columns:
        raise RuntimeError("Kolom 'gemiddelde_waardering_rit' ontbreekt in shuttle_log.")

    ratings = df["gemiddelde_waardering_rit"].dropna().head(4)
    if ratings.empty:
        raise RuntimeError("Geen waarderingen gevonden in shuttle_log.")

    return ratings.reset_index(drop=True)


def plot_ratings(series_json: pd.Series, series_db: pd.Series, db_label: str) -> None:
    """Plot twee lijnen: shuttle_log en database-view (beide 6 waarderingen)."""

    plt.figure(figsize=(7, 4))

    x_json = range(1, len(series_json) + 1)
    x_db = range(1, len(series_db) + 1)

    plt.plot(x_json, series_json, marker="o", label="Shuttle log")
    plt.plot(x_db, series_db, marker="s", label=f"View: {db_label}")

    plt.title("Eerste 4 waarderingen")
    plt.xlabel("Index")
    plt.ylabel("Gemiddelde waardering")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    log_path = Path(__file__).resolve().parent / "shuttle_log (1).json"

    engine = create_db_engine()

    ratings_json = load_shuttle_log(log_path)
    ratings_db, used_view = load_db_ratings(engine)

    plot_ratings(ratings_json, ratings_db, used_view)


if __name__ == "__main__":
    main()