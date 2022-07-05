from HtmlEncoderScreen import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class App(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.encodeButton.clicked.connect(self.encodeString)

    def encodeString(self):
        unencodedString = self.ui.textEditUnencoded.toPlainText()
        encodedString = ""
        for i in unencodedString:
            if(i == '"'):
                encodedString += "&quot;"
            elif(i == "'"):
                encodedString += "&apos;"
            elif(i == "&"):
                encodedString += "&amp;"
            elif(i == "<"):
                encodedString += "&lt;"
            elif(i == ">"):
                encodedString += "&gt;"
            elif(i == " "):
                encodedString += "&nbsp;"
            elif(i == "¡"):
                encodedString += "&iexcl;"
            elif(i == "¢"):
                encodedString += "&cent;"
            elif(i == "£"):
                encodedString += "&pound;"
            elif(i == "¤"):
                encodedString += "&curren;"
            elif(i == "¥"):
                encodedString += "&yen;"
            elif(i == "¦"):
                encodedString += "&brvbar;"
            elif(i == "§"):
                encodedString += "&sect;"
            elif(i == "¨"):
                encodedString += "&uml;"
            elif(i == "©"):
                encodedString += "&copy;"
            elif(i == "ª"):
                encodedString += "&ordf;"
            elif(i == "«"):
                encodedString += "&laquo;"
            elif(i == "¬"):
                encodedString += "&not;"
            elif(i == "®"):
                encodedString += "&reg;"
            elif(i == "¯"):
                encodedString += "&macr;"
            elif(i == "°"):
                encodedString += "&deg;"
            elif(i == "±"):
                encodedString += "&plusmn;"
            elif(i == "²"):
                encodedString += "&sup2;"
            elif(i == "³"):
                encodedString += "&sup3;"
            elif(i == "´"):
                encodedString += "&acute;"
            elif(i == "µ"):
                encodedString += "&micro;"
            elif(i == "¶"):
                encodedString += "&para;"
            elif(i == "·"):
                encodedString += "&middot;"
            elif(i == "¸"):
                encodedString += "&cedil;"
            elif(i == "¹"):
                encodedString += "&sup1;"
            elif(i == "º"):
                encodedString += "&ordm;"
            elif(i == "»"):
                encodedString += "&raquo;"
            elif(i == "¼"):
                encodedString += "&frac14;"
            elif(i == "½"):
                encodedString += "&frac12;"
            elif(i == "¾"):
                encodedString += "&frac34;"
            elif(i == "¿"):
                encodedString += "&iquest;"
            elif(i == "×"):
                encodedString += "&times;"
            elif(i == "÷"):
                encodedString += "&divide;"
            else:
                encodedString += i
        self.ui.textEditEncoded.setPlainText(encodedString)


def program():
    program = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(program.exec_())

program()