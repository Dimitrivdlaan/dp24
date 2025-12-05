from imports import *


class waardering_rit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        heading = QLabel("Waardering Rit (1–10)")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)
        
        # Hier moet de code ! ! ! < - - - & - - - >
        
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = waardering_rit()
    window.show()
    sys.exit(app.exec())