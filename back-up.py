from imports import *


class homedashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        heading = QLabel("Home Dashboard")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)

        # ============================================================
        # GRID MET 6 GEKLEURDE VAKJES
        # ============================================================
        
        grid_widget = QWidget()
        grid_layout = QGridLayout()
        
        # Eerste rij
        grid_layout.addWidget(self.create_vakje_1(), 0, 0)
        grid_layout.addWidget(self.create_vakje_2(), 0, 1)
        grid_layout.addWidget(self.create_vakje_3(), 0, 2)
        
        # Tweede rij
        grid_layout.addWidget(self.create_vakje_4(), 1, 0)
        grid_layout.addWidget(self.create_vakje_5(), 1, 1)
        grid_layout.addWidget(self.create_vakje_6(), 1, 2)
        
        grid_widget.setLayout(grid_layout)
        layout.addWidget(grid_widget)
        
        # ============================================================

        btn_waardering = QPushButton("Bekijk details (Waardering)")
        btn_waardering.setFont(QFont("Arial", 12))
        btn_waardering.clicked.connect(self.ga_naar_waardering)
        layout.addWidget(btn_waardering)

        btn_vertraging = QPushButton("Bekijk details (Vertraging)")
        btn_vertraging.setFont(QFont("Arial", 12))
        btn_vertraging.clicked.connect(self.ga_naar_vertraging)
        layout.addWidget(btn_vertraging)

        btn_incidenten = QPushButton("Bekijk details (Incidenten)")
        btn_incidenten.setFont(QFont("Arial", 12))
        btn_incidenten.clicked.connect(self.ga_naar_incidenten)
        layout.addWidget(btn_incidenten)

        btn_beschikbaarheid = QPushButton("Bekijk details (Beschikbaarheid)")
        btn_beschikbaarheid.setFont(QFont("Arial", 12))
        btn_beschikbaarheid.clicked.connect(self.ga_naar_beschikbaarheid)
        layout.addWidget(btn_beschikbaarheid)

        btn_bezettingsgraad = QPushButton("Bekijk details (Bezettingsgraad)")
        btn_bezettingsgraad.setFont(QFont("Arial", 12))
        btn_bezettingsgraad.clicked.connect(self.ga_naar_bezettingsgraad)
        layout.addWidget(btn_bezettingsgraad)

        btn_snelheid = QPushButton("Bekijk details (Snelheid)")
        btn_snelheid.setFont(QFont("Arial", 12))
        btn_snelheid.clicked.connect(self.ga_naar_snelheid)
        layout.addWidget(btn_snelheid)
        
        
   
        
        
        
        
        










        
        self.setLayout(layout)

    # ============================================================
    # VAKJE 1 - ROOD
    # ============================================================
    def create_vakje_1(self):
        vakje = QWidget()
        layout = QVBoxLayout()
        
        title = QLabel("Vakje 1")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        beschrijving = QLabel("Dit is vakje 1\nVoeg hier je code in")
        beschrijving.setFont(QFont("Arial", 10))
        beschrijving.setAlignment(Qt.AlignmentFlag.AlignCenter)
        beschrijving.setWordWrap(True)
        layout.addWidget(beschrijving)
        
        btn = QPushButton("Knop 1")
        btn.setFont(QFont("Arial", 10))
        btn.clicked.connect(self.vakje_1_action)
        layout.addWidget(btn)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet("border: 3px solid red; padding: 10px;")
        return vakje
    
    def vakje_1_action(self):
        # VOEG HIER JE CODE IN
        print("Vakje 1 knop geklikt")

    # ============================================================
    # VAKJE 2 - BLAUW
    # ============================================================
    def create_vakje_2(self):
        vakje = QWidget()
        layout = QVBoxLayout()
        
        title = QLabel("Vakje 2")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        beschrijving = QLabel("Dit is vakje 2\nVoeg hier je code in")
        beschrijving.setFont(QFont("Arial", 10))
        beschrijving.setAlignment(Qt.AlignmentFlag.AlignCenter)
        beschrijving.setWordWrap(True)
        layout.addWidget(beschrijving)
        
        btn = QPushButton("Knop 2")
        btn.setFont(QFont("Arial", 10))
        btn.clicked.connect(self.vakje_2_action)
        layout.addWidget(btn)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet("border: 10px solid blue; padding: 10px;")
        return vakje
    
    def vakje_2_action(self):
        # VOEG HIER JE CODE IN
        print("Vakje 2 knop geklikt")

    # ============================================================
    # VAKJE 3 - GROEN
    # ============================================================
    def create_vakje_3(self):
        vakje = QWidget()
        layout = QVBoxLayout()
        
        title = QLabel("Vakje 3")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        beschrijving = QLabel("Dit is vakje 3\nVoeg hier je code in")
        beschrijving.setFont(QFont("Arial", 10))
        beschrijving.setAlignment(Qt.AlignmentFlag.AlignCenter)
        beschrijving.setWordWrap(True)
        layout.addWidget(beschrijving)
        
        btn = QPushButton("Knop 3")
        btn.setFont(QFont("Arial", 10))
        btn.clicked.connect(self.vakje_3_action)
        layout.addWidget(btn)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet("border: 3px solid green; padding: 10px;")
        return vakje
    
    def vakje_3_action(self):
        # VOEG HIER JE CODE IN
        print("Vakje 3 knop geklikt")

    # ============================================================
    # VAKJE 4 - ORANJE
    # ============================================================
    def create_vakje_4(self):
        vakje = QWidget()
        layout = QVBoxLayout()
        
        title = QLabel("Vakje 4")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        beschrijving = QLabel("Dit is vakje 4\nVoeg hier je code in")
        beschrijving.setFont(QFont("Arial", 10))
        beschrijving.setAlignment(Qt.AlignmentFlag.AlignCenter)
        beschrijving.setWordWrap(True)
        layout.addWidget(beschrijving)
        
        btn = QPushButton("Knop 4")
        btn.setFont(QFont("Arial", 10))
        btn.clicked.connect(self.vakje_4_action)
        layout.addWidget(btn)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet("border: 3px solid orange; padding: 10px;")
        return vakje
    
    def vakje_4_action(self):
        # VOEG HIER JE CODE IN
        print("Vakje 4 knop geklikt")

    # ============================================================
    # VAKJE 5 - PAARS
    # ============================================================
    def create_vakje_5(self):
        vakje = QWidget()
        layout = QVBoxLayout()
        
        title = QLabel("Vakje 5")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        beschrijving = QLabel("Dit is vakje 5\nVoeg hier je code in")
        beschrijving.setFont(QFont("Arial", 10))
        beschrijving.setAlignment(Qt.AlignmentFlag.AlignCenter)
        beschrijving.setWordWrap(True)
        layout.addWidget(beschrijving)
        
        btn = QPushButton("Knop 5")
        btn.setFont(QFont("Arial", 10))
        btn.clicked.connect(self.vakje_5_action)
        layout.addWidget(btn)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet("border: 3px solid purple; padding: 10px;")
        return vakje
    
    def vakje_5_action(self):
        # VOEG HIER JE CODE IN
        print("Vakje 5 knop geklikt")

    # ============================================================
    # VAKJE 6 - ROZE
    # ============================================================
    def create_vakje_6(self):
        vakje = QWidget()
        layout = QVBoxLayout()
        
        title = QLabel("Vakje 6")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        beschrijving = QLabel("Dit is vakje 6\nVoeg hier je code in")
        beschrijving.setFont(QFont("Arial", 10))
        beschrijving.setAlignment(Qt.AlignmentFlag.AlignCenter)
        beschrijving.setWordWrap(True)
        layout.addWidget(beschrijving)
        
        btn = QPushButton("Knop 6")
        btn.setFont(QFont("Arial", 10))
        btn.clicked.connect(self.vakje_6_action)
        layout.addWidget(btn)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet("border: 3px solid pink; padding: 10px;")
        return vakje
    
    def vakje_6_action(self):
        # VOEG HIER JE CODE IN
        print("Vakje 6 knop geklikt")

    # ============================================================














    # ============================================================

    def ga_naar_waardering(self):
        try:
            from waardering_rit import waarderingrit
            self.home_window = waarderingrit()
            self.home_window.show()
            self.hide()
        except Exception as e:
            print("Fout bij openen waarderingdashboard:", e)

    def ga_naar_vertraging(self):
        try:
            from vertraging_bezoeker import vertraging
            self.home_window = vertraging()
            self.home_window.show()
            self.hide()
        except Exception as e:
            print("Fout bij openen vertragingdashboard:", e)

    def ga_naar_incidenten(self):
        try:
            from incidenten_reductie import incidenten
            self.home_window = incidenten()
            self.home_window.show()
            self.hide()
        except Exception as e:
            print("Fout bij openen incidentendashboard:", e)

    def ga_naar_beschikbaarheid(self):
        try:
            from beschikbaarheid_trein import beschikbaarheid
            self.home_window = beschikbaarheid()
            self.home_window.show()
            self.hide()
        except Exception as e:
            print("Fout bij openen beschikbaarheidsdashboard:", e)

    def ga_naar_bezettingsgraad(self):
        try:
            from bezettingsgraad_trein import bezettingsgraad
            self.home_window = bezettingsgraad()
            self.home_window.show()
            self.hide()
        except Exception as e:
            print("Fout bij openen bezettingsgraaddashboard:", e)
    
    
    def ga_naar_snelheid(self):
        try:
            from snelheid_route import snelheid
            self.home_window = snelheid()
            self.home_window.show()
            self.hide()
        except Exception as e:
            print("Fout bij openen snelheiddashboard:", e)





   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = homedashboard()
    window.show()
    sys.exit(app.exec())