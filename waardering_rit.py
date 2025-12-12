from imports import *
from pathlib import Path


class waarderingrit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        heading = QLabel("Waardering Rit (1–10)")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)
        
       
        try:
            canvas = self.create_chart()
            layout.addWidget(canvas)
        except Exception as e:
            error_label = QLabel(f"Fout bij laden grafiek: {e}")
            error_label.setStyleSheet("color: red;")
            layout.addWidget(error_label)
        
        btn_terug = QPushButton("Terug naar Home")
        btn_terug.setFont(QFont("Arial", 16))
        btn_terug.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; "
            "border-radius: 12px; padding: 10px 18px;"
        )
        btn_terug.clicked.connect(self.go_home)
        layout.addWidget(btn_terug)
        self.setLayout(layout)

    def create_chart(self):
        engine = create_engine("mysql+pymysql://root:password@localhost:3306/hr")
        
        
        shuttle = pd.read_json(Path(__file__).parent / "shuttle_log (1).json")["gemiddelde_waardering_rit"].dropna().head(4)
        db = pd.read_sql("SELECT waardering_norm FROM view_kpi_waardering_rit", engine)["waardering_norm"].dropna().head(4)
        
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(range(1, len(shuttle) + 1), shuttle, marker="o", linewidth=2, label="Shuttle")
        ax.plot(range(1, len(db) + 1), db, marker="s", linewidth=2, label="Machinisten")
        ax.set_title("Eerste 4 waarderingen - Shuttle vs Machinisten", fontsize=14, fontweight="bold")
        ax.set_xlabel("Index")
        ax.set_ylabel("Waardering")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        
        return QFigureCanvas(fig)

    def go_home(self):
        try:
            from home import homedashboard
            self.home_window = homedashboard()
            self.home_window.show()
            self.hide()
        except Exception as e:
            print("Fout bij terug naar home:", e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = waarderingrit()
    window.show()
    sys.exit(app.exec())