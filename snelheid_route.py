from imports import *


class snelheid_route(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        heading = QLabel("snelheid route")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)
        
        # Hier moet de code ! ! ! < - - - & - - - >
        
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = snelheid_route()
    window.show()
    sys.exit(app.exec())