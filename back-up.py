from imports import *
from kleuren import *



class homedashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 65, 0, 0)
        heading = QLabel("Home Dashboard")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)
        
        grid_widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)  
        grid_layout.setSpacing(30) 
        grid_layout.addWidget(self.create_vakje_1(), 0, 0)
        grid_layout.addWidget(self.create_vakje_2(), 0, 1)
        grid_layout.addWidget(self.create_vakje_3(), 0, 2)
        grid_layout.addWidget(self.create_vakje_4(), 1, 0)
        grid_layout.addWidget(self.create_vakje_5(), 1, 1)
        grid_layout.addWidget(self.create_vakje_6(), 1, 2)
        grid_widget.setLayout(grid_layout)
        layout.addWidget(grid_widget)
        

        

        

        self.setLayout(layout)
    
    
    def create_vakje_1(self):
        vakje = QWidget()
        vakje.setObjectName("vakje1")
        layout = QVBoxLayout()
        
        title = QLabel("Beschikbaarheid Trein%")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: " + BLUE_50 + "; border-radius: 10px; padding: 8px; color: " + BLUE_700 + ";")
        title.setMaximumWidth(350)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        
        afbeelding = QLabel()
        afbeelding.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("bar-chart.png")
        afbeelding.setPixmap(pixmap.scaledToWidth(220, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(afbeelding)
        
        btn_beschikbaarheid = QPushButton("          Bekijk details ->          ")
        btn_beschikbaarheid.setFont(QFont("Arial", 14))
        btn_beschikbaarheid.clicked.connect(self.ga_naar_beschikbaarheid)
        btn_beschikbaarheid.setFixedWidth(350)
        layout.addWidget(btn_beschikbaarheid, alignment=Qt.AlignmentFlag.AlignCenter)
        

        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(250)
        vakje.setStyleSheet(
            "#vakje1 { border: 3px solid " + BLUE_200 + "; padding: 12px; border-radius: 16px; background-color: white; } "
            "#vakje1 QLabel { border: none; } "
            "#vakje1 QPushButton { border: none; background: " + BLUE_700 + "; padding: 8px; color: white ; border-radius: 8px; }"
        )
        return vakje
    




    def create_vakje_2(self):
        vakje = QWidget()
        vakje.setObjectName("vakje2")
        layout = QVBoxLayout()
        
        title = QLabel("Wachttijd per bezoeker (minuten)")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: " + YELLOW_50 + "; ; border-radius: 10px; padding: 8px; color: " + YELLOW_600 + ";")
        title.setMaximumWidth(350)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)














        
      
        afbeelding = QLabel()
        afbeelding.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("bar-chart.png")
        afbeelding.setPixmap(pixmap.scaledToWidth(220, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(afbeelding)
        
        btn_vertraging = QPushButton("          Bekijk details ->          ")
        btn_vertraging.setFont(QFont("Arial", 14))
        btn_vertraging.clicked.connect(self.ga_naar_vertraging)
        btn_vertraging.setFixedWidth(350)
        layout.addWidget(btn_vertraging, alignment=Qt.AlignmentFlag.AlignCenter)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet(
            "#vakje2 { border: 3px solid " + YELLOW_200 + "; padding: 12px; border-radius: 16px; background-color: white;} "
            "#vakje2 QLabel { border: none; } "
            "#vakje2 QPushButton { border: none; background: transparent; padding: 6px; }"
            "#vakje2 QPushButton { border: none; background: " + YELLOW_600 + "; padding: 8px; color: white ; border-radius: 8px; }"
        )
        return vakje
    
  



    def create_vakje_3(self):
        vakje = QWidget()
        vakje.setObjectName("vakje3")
        layout = QVBoxLayout()
        
        title = QLabel("Incidenten Reductie (%)")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: " + RED_50 + "; ; border-radius: 10px; padding: 8px; color: " + RED_600 + ";")
        title.setMaximumWidth(350)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)


        afbeelding = QLabel()
        afbeelding.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("bar-chart.png")
        afbeelding.setPixmap(pixmap.scaledToWidth(220, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(afbeelding)
        
        btn_incidenten = QPushButton("          Bekijk details ->          ")
        btn_incidenten.setFont(QFont("Arial", 12))
        btn_incidenten.clicked.connect(self.ga_naar_incidenten)
        btn_incidenten.setFixedWidth(350)
        layout.addWidget(btn_incidenten, alignment=Qt.AlignmentFlag.AlignCenter)

        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet(
           
            "#vakje3 { border: 3px solid " + RED_200 + "; padding: 12px; border-radius: 16px; background-color: white;} "
            "#vakje3 QLabel { border: none; } "
            "#vakje3 QPushButton { border: none; background: transparent; padding: 6px; }"
            "#vakje3 QPushButton { border: none; background: " + RED_600 + "; padding: 8px; color: white ; border-radius: 8px; }"
        )
        return vakje
    



    def create_vakje_4(self):
        vakje = QWidget()
        vakje.setObjectName("vakje4")
        layout = QVBoxLayout()
        
        title = QLabel("bezettingsgraad trein (%)")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: " + ORANGE_50 + "; ; border-radius: 10px; padding: 8px; color: " + ORANGE_600 + ";")
        title.setMaximumWidth(350)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
       
        afbeelding = QLabel()
        afbeelding.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("bar-chart.png")
        afbeelding.setPixmap(pixmap.scaledToWidth(220, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(afbeelding)
        
        btn_bezettingsgraad = QPushButton("          Bekijk details ->          ")
        btn_bezettingsgraad.setFont(QFont("Arial", 12))
        btn_bezettingsgraad.clicked.connect(self.ga_naar_bezettingsgraad)
        btn_bezettingsgraad.setFixedWidth(350)
        layout.addWidget(btn_bezettingsgraad, alignment=Qt.AlignmentFlag.AlignCenter)

        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet(
            "#vakje4 { border: 3px solid " + ORANGE_200 + "; padding: 12px; border-radius: 16px; background-color: white;} "
            "#vakje4 QLabel { border: none; } "
            "#vakje4 QPushButton { border: none; background: transparent; padding: 6px; }"
            "#vakje4 QPushButton { border: none; background: " + ORANGE_600 + "; padding: 8px; color: white ; border-radius: 8px; }"
        )
        return vakje
 

   
    def create_vakje_5(self):
        vakje = QWidget()
        vakje.setObjectName("vakje5")
        layout = QVBoxLayout()
        
        title = QLabel("Waardering rit (1-10)")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: " + GREEN_50 + "; ; border-radius: 10px; padding: 8px; color: " + GREEN_600 + ";")
        title.setMaximumWidth(350)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        
        afbeelding = QLabel()
        afbeelding.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("bar-chart.png")
        afbeelding.setPixmap(pixmap.scaledToWidth(220, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(afbeelding)
        
        btn_waardering = QPushButton("          Bekijk details ->          ")
        btn_waardering.setFont(QFont("Arial", 12))
        btn_waardering.clicked.connect(self.ga_naar_waardering)
        btn_waardering.setFixedWidth(350)
        layout.addWidget(btn_waardering, alignment=Qt.AlignmentFlag.AlignCenter)
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet(
            
            "#vakje5 { border: 3px solid " + GREEN_200 + "; padding: 12px; border-radius: 16px; background-color: white;} "
            "#vakje5 QLabel { border: none; } "
            "#vakje5 QPushButton { border: none; background: transparent; padding: 6px; }"
            "#vakje5 QPushButton { border: none; background: " + GREEN_600 + "; padding: 8px; color: white ; border-radius: 8px; }"
        )
        return vakje
    
   

    def create_vakje_6(self):
        vakje = QWidget()
        vakje.setObjectName("vakje6")
        layout = QVBoxLayout()
        
        title = QLabel("Snelheid route (km/u)")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: " + PURPLE_50 + "; ; border-radius: 10px; padding: 8px; color: " + PURPLE_600 + ";")
        title.setMaximumWidth(350)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
  
        afbeelding = QLabel()
        afbeelding.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("bar-chart.png")
        afbeelding.setPixmap(pixmap.scaledToWidth(220, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(afbeelding)

        btn_snelheid = QPushButton("          Bekijk details ->          ")
        btn_snelheid.setFont(QFont("Arial", 12))
        btn_snelheid.clicked.connect(self.ga_naar_snelheid)
        btn_snelheid.setFixedWidth(350)
        layout.addWidget(btn_snelheid, alignment=Qt.AlignmentFlag.AlignCenter)
        
        
        
        vakje.setLayout(layout)
        vakje.setMinimumHeight(150)
        vakje.setStyleSheet(
            
            "#vakje6 { border: 3px solid " + PURPLE_200 + "; padding: 12px; border-radius: 16px; background-color: white;} "
            "#vakje6 QLabel { border: none; } "
            "#vakje6 QPushButton { border: none; background: transparent; padding: 6px; }"
            "#vakje6 QPushButton { border: none; background: " + PURPLE_600 + "; padding: 8px; color: white ; border-radius: 8px; }"
        )
        return vakje
    
 
















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
