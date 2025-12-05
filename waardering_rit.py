from imports import *


class WaarderingDash(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		layout = QVBoxLayout()
		heading = QLabel("Waardering Dashboard")
		heading.setFont(QFont("Arial", 28, QFont.Weight.Bold))
		heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		layout.addWidget(heading)

		info = QLabel("Dit is de waardering pagina. Sluit dit venster om terug te gaan.")
		info.setWordWrap(True)
		layout.addWidget(info)

		self.setLayout(layout)
		self.setWindowTitle("Waardering")
		self.resize(600, 400)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WaarderingDash()
	window.show()
	sys.exit(app.exec())
