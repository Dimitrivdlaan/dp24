from imports import *


class bezettingsgraad(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        heading = QLabel("Bezettingsgraad Trein")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)


        btn_terug = QPushButton("Terug naar Home")
        btn_terug.setFont(QFont("Arial", 12))
        btn_terug.clicked.connect(self.go_home)
        layout.addWidget(btn_terug)
        self.setLayout(layout)

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
    window = bezettingsgraad()
    window.show()
    sys.exit(app.exec())