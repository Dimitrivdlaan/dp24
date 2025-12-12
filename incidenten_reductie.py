from imports import *
from pathlib import Path


class incidenten(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        heading = QLabel("Incidenten Reductie (%)")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)
       
        btn_terug = QPushButton("Terug naar Home")
        btn_terug.setFont(QFont("Arial", 16))
        btn_terug.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; "
            "border-radius: 12px; padding: 10px 18px;"
        )
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
    window = incidenten()
    window.show()
    sys.exit(app.exec())