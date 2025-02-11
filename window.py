import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


# our custom main window subclass
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")
		button = QPushButton("Press Me!")

		# Set the central widget of the Window.
		self.setCentralWidget(button)


# make app, passing command line args
# this object will hold the event loop, which governs all user interaction for the app
# events are key presses, mouse clicks and movements
app = QApplication(sys.argv)

# make and show basic window
# Windows are top level components that all other components will be children of
# It has no parents and every app needs at least one
# Any widget can be a window, even like a button , but thats stupid
# general idea is to nest widgets / components within each other
# good parent widget is QMainWindow, which we can customize by making a subclass
window = MainWindow()
window.show() # Windows are hidden by default

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.