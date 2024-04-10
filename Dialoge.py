import sys
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Aufgabe X")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(800,200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        # ...
        self.button1 = QPushButton("Beispiel 1: Info Dialog")
        self.button2 = QPushButton("Beispiel 2: About Dialog")
        self.button3 = QPushButton("Beispiel 3: warnung")
        self.button4 = QPushButton("Beispiel 4: Kritischer Fehler")
        self.button5 = QPushButton("Beispiel 5: Frage")
        self.button6 = QPushButton("Beispiel 6: File öffnen")
        self.button7 = QPushButton("Beispiel 7: File speichern")
        self.button8 = QPushButton("Beispiel 8: mehrere Files öffnen")
        self.button9 = QPushButton("Beispiel 9: zahlen einlesen")
        self.button10 = QPushButton("Beispiel 10: Get Item, Dropdown")
        self.button11 = QPushButton("Beispiel 11: Text einlesen")
        self.button12 = QPushButton("Beispiel 12: Farbauswahl")


        ## Layout füllen
        # ...
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.addWidget(self.button9)
        layout.addWidget(self.button10)
        layout.addWidget(self.button11)
        layout.addWidget(self.button12)

        ## Fenster anzeigen
        self.show()


    def createConnects(self):
        self.button1.clicked.connect(self.beispiel1)
        self.button1.setStyleSheet("background-color: #993333")
        self.button2.clicked.connect(self.beispiel2)
        self.button2.setStyleSheet("background-color: #339933")
        self.button3.clicked.connect(self.beispiel3)
        self.button4.clicked.connect(self.beispiel4)
        self.button5.clicked.connect(self.beispiel5)
        self.button6.clicked.connect(self.beispiel6)
        self.button7.clicked.connect(self.beispiel7)
        self.button8.clicked.connect(self.beispiel8)
        self.button9.clicked.connect(self.beispiel9)
        self.button10.clicked.connect(self.beispiel10)
        self.button11.clicked.connect(self.beispiel11)
        self.button12.clicked.connect(self.beispiel12)

    def beispiel1(self):
        QMessageBox.information(self,"Titel","Hier ist eine Information<br/>zweite Zeile")
    def beispiel2(self):   
        QMessageBox.about(self,"Titel","Text")
    def beispiel3(self):
        QMessageBox.warning(self, "Titel","Vorsicht speicher fast voll!!!")
    
    def beispiel4(self):
        QMessageBox.critical(self,"Titel","Datei kannn nicht gespeichert werden")

    def beispiel5(self):
        antwort = QMessageBox.question(self,"Titel","Ist Python eine gute Programmiersprache?",QMessageBox.Cancel,QMessageBox.Yes)
        if antwort == QMessageBox.Yes:
            QMessageBox.information(self,"Titel","super")
        if antwort == QMessageBox.No:
            QMessageBox.critical(self,"Titel","Schade")
            self.close()
    
    def beispiel6(self):
        filename,typ = QFileDialog.getOpenFileName(self, "Datei öffnen","","Alle (*.*);;Python (*.py);;Text (*.txt)")
        if filename != "":
            datei = open(filename, encoding="utf-8)")
            inhalt = datei.read()
            print(inhalt)
            datei.close()
        else:
           QMessageBox.warning(self,"Warnugn","Der Dialog wurde Abgebrochen")
    
    def beispiel7(self):
        filename,typ = QFileDialog.getSaveFileName(self,"Datei speichern","","Alle(*.*)")
        print(filename)
    
    def beispiel8(self):
        filename,typ = QFileDialog.getOpenFileNames(self,"Dateien öffnen","","Alle (*.*)")

        print(filename)
    
    def beispiel9(self):
        ##wert, ok = QInputDialog.getInt(self,"Titel", "Was gibt 2+3?")
        wert, ok = QInputDialog.getDouble(self,"Titel","Was ergiebt 1.0+4.0")
        print(wert)
        print(ok)

        if ok:
            if wert == 5:
                QMessageBox.information(self,"","Richtig")
            else:
                QMessageBox.information(self,"","Falsch")
    def beispiel10(self):
        wert,ok = QInputDialog.getItem(self,"Titel", "Welche Schlange ist am giftigsten?",["Python", "Kobra","Mamba","Elefant",""],4)
        print(wert)

    def beispiel11(self):
        ##wert, ok = QInputDialog.getText(self,"Titel", "Wie heissen Sie?", QLineEdit.Normal)
        ##wert, ok = QInputDialog.getText(self,"Titel", "Wie lautet das Passwort", QLineEdit.Password)
        wert, ok = QInputDialog.getText(self,"Titel", "Wie lautet das Passwort", QLineEdit.NoEcho)
        if ok and wert=="geheim":
            QMessageBox.information(self,"","Richtig")
        else:
            QMessageBox.information(self,"","Falsch")
    
    def beispiel12(self):
        farbe = QColorDialog.getColor()
        print(farbe.name())
        print(farbe.red(),farbe.green(),farbe.blue())
        self.button12.setStyleSheet(f"background-color:{farbe.name()}")

        font,ok = QFontDialog.getFont()
        print(font)
        self.button12.setFont(font)



def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()