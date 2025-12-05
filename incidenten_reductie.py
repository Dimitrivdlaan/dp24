from imports import *


class incidenten_reductie(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        heading = QLabel("Incidenten Reductie (%)")
        heading.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(heading)
        
        # Hier moet de code ! ! ! < - - - & - - - >
        
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = incidenten_reductie()
    window.show()
    sys.exit(app.exec())