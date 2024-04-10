import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Programmierung")

        layout = QFormLayout()
        self.vnLine = QLineEdit()
        self.nLine = QLineEdit()
        self.Geb = QDateEdit()
        self.Geb.setDisplayFormat("dd/MM/yyyy")
        self.AdresseL = QLineEdit()
        self.PLZLine = QLineEdit()
        self.OLine = QLineEdit()
        self.Land = QComboBox()
        self.Land.addItems(["Schweiz","Deutschland","Österreich"])
        self.button1 = QPushButton("Save")
        self.button1.clicked.connect(self.save_data)

        layout.addRow("Vorname", self.vnLine)
        layout.addRow("Name", self.nLine)
        layout.addRow("Geburtstag", self.Geb)
        layout.addRow("Adresse", self.AdresseL)
        layout.addRow("Postleitzahl", self.PLZLine)
        layout.addRow("Ort", self.OLine)
        layout.addRow("Land", self.Land)
        layout.addRow(self.button1)

        center = QWidget()
        center.setLayout(layout)
        
        self.setCentralWidget(center)

        self.create_menu()

        self.show()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_data)
        file_menu.addAction(save_action)

        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

    def save_data(self):
        data = [
            self.vnLine.text(),
            self.nLine.text(),
            self.Geb.date().toString(Qt.ISODate),
            self.AdresseL.text(),
            self.PLZLine.text(),
            self.OLine.text(),
            self.Land.currentText()
        ]
        data_str = ','.join(data)
        with open('output.txt', 'w') as file:
            file.write(data_str)

app = QApplication([])
w = Fenster()
sys.exit(app.exec_())
