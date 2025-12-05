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
        layout.addWidget(btn_incidenten)

        btn_bezettingsgraad = QPushButton("Bekijk details (Bezettingsgraad)")
        btn_bezettingsgraad.setFont(QFont("Arial", 12))
        btn_bezettingsgraad.clicked.connect(self.ga_naar_bezettingsgraad)
        layout.addWidget(btn_bezettingsgraad)

        btn_snelheid = QPushButton("Bekijk details (Snelheid)")
        btn_snelheid.setFont(QFont("Arial", 12))
        btn_snelheid.clicked.connect(self.ga_naar_snelheid)
        layout.addWidget(btn_snelheid)
        
        
   
        
        
        
        
        
        
        self.setLayout(layout)

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