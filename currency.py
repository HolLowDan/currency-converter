import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from currency_converter import CurrencyConverter


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 414)
        MainWindow.setStyleSheet("background-color: #6FE7DD;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1022, 151))
        self.frame.setStyleSheet("background-color: #3490DE;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 30, 541, 91))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #C5FB62;\n""font: 63 48pt \"Lucida Fax\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(880, 20, 120, 120))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("libra.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 120, 120))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("currency.png"))
        self.label_3.setObjectName("label_3")
        self.input_val = QtWidgets.QLineEdit(self.centralwidget)
        self.input_val.setGeometry(QtCore.QRect(30, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_val.setFont(font)
        self.input_val.setStyleSheet("background-color: #3490DE;;\n""")
        self.input_val.setText("")
        self.input_val.setAlignment(QtCore.Qt.AlignCenter)
        self.input_val.setObjectName("input_val")
        self.input_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.input_nom.setGeometry(QtCore.QRect(30, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_nom.setFont(font)
        self.input_nom.setStyleSheet("background-color: #3490DE;;\n""")
        self.input_nom.setText("")
        self.input_nom.setAlignment(QtCore.Qt.AlignCenter)
        self.input_nom.setObjectName("input_nom")
        self.output_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.output_nom.setGeometry(QtCore.QRect(470, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_nom.setFont(font)
        self.output_nom.setStyleSheet("background-color: #3490DE;;\n""")
        self.output_nom.setText("")
        self.output_nom.setReadOnly(True)
        self.output_nom.setAlignment(QtCore.Qt.AlignCenter)
        self.output_nom.setObjectName("output_nom")
        self.output_val = QtWidgets.QLineEdit(self.centralwidget)
        self.output_val.setGeometry(QtCore.QRect(470, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_val.setFont(font)
        self.output_val.setStyleSheet("background-color: #3490DE;\n""")
        self.output_val.setText("")
        self.output_val.setAlignment(QtCore.Qt.AlignCenter)
        self.output_val.setObjectName("output_val")
        self.but_conver = QtWidgets.QPushButton(self.centralwidget)
        self.but_conver.setGeometry(QtCore.QRect(320, 230, 111, 91))
        self.but_conver.setStyleSheet("background-color:#6639A6;\n""font: 14pt \"MS Shell Dlg 2\";")
        self.but_conver.setObjectName("but_conver")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(740, 170, 271, 191))
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowTitle("Конвертер")
        MainWindow.setWindowIcon(QIcon("currency.png"))
        self.input_val.setPlaceholderText("Из данной валюты")
        self.input_nom.setPlaceholderText("Номиналом")
        self.output_val.setPlaceholderText("В эту валюту")
        self.output_nom.setPlaceholderText("Будет")
        self.but_conver.clicked.connect(self.converted)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http:/"
                                                    "/www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta"
                                                    " name=\"qrichtext\" content=\"1\" /><style type=\"text/css\""
                                                    ">\n""p, li { white-space: pre-wrap; }\n""</style></head><body "
                                                    "style=\" font-family:\'Lucida Fax\'; font-size:48pt; font-weigh"
                                                    "t:56; font-style:normal;\">\n""<p align=\"center\" style=\" mar"
                                                    "gin-top:12px; margin-bottom:12px; margin-left:0px; margin-right"
                                                    ":0px; -qt-block-indent:0; text-indent:0px;\">Конвертор валют</p"
                                                    "></body></html>"))
        self.but_conver.setText(_translate("MainWindow", "Перевести"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "USD -- Доллар США"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "EUR -- Евро"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "RUB -- Российский рубль"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "CNY -- Китайский юань"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "JPY -- Японская иена"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "GBP -- Фунт Стерлингов"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "BGN -- Болгарский Лев"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "CYP -- Кипрский фунт"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "CZK -- Чешская крона"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "DKK -- Датская крона"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "EEK -- Эстонская крона"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "HUF -- Венгерский форинт"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "LTL -- Литовский лит"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "LVL -- Латвийский лат"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "MTL -- Мальтийская лира"))
        item = self.listWidget.item(15)
        item.setText(_translate("MainWindow", "PLN -- Польский злотый"))
        item = self.listWidget.item(16)
        item.setText(_translate("MainWindow", "ROL -- Старый Румынский лей"))
        item = self.listWidget.item(17)
        item.setText(_translate("MainWindow", "RON -- Румынский лей"))
        item = self.listWidget.item(18)
        item.setText(_translate("MainWindow", "SEK -- Шведская крона"))
        item = self.listWidget.item(19)
        item.setText(_translate("MainWindow", "SIT -- Словенский толар"))
        item = self.listWidget.item(20)
        item.setText(_translate("MainWindow", "SKK -- Словацкая крон"))
        item = self.listWidget.item(21)
        item.setText(_translate("MainWindow", "CHF -- Швейцарский франк"))
        item = self.listWidget.item(22)
        item.setText(_translate("MainWindow", "ISK -- Исландская крона"))
        item = self.listWidget.item(23)
        item.setText(_translate("MainWindow", "NOK -- Норвежская крона"))
        item = self.listWidget.item(24)
        item.setText(_translate("MainWindow", "HRK -- Хорватская куна"))
        item = self.listWidget.item(25)
        item.setText(_translate("MainWindow", "TRL -- Турецкая (старая) лира"))
        item = self.listWidget.item(26)
        item.setText(_translate("MainWindow", "TRY -- Турецкая (новая) лира"))
        item = self.listWidget.item(27)
        item.setText(_translate("MainWindow", "AUD -- Австралийский доллар"))
        item = self.listWidget.item(28)
        item.setText(_translate("MainWindow", "BRL -- Бразильский реал"))
        item = self.listWidget.item(29)
        item.setText(_translate("MainWindow", "CAD -- Канадский доллар"))
        item = self.listWidget.item(30)
        item.setText(_translate("MainWindow", "HKD -- Гонконгский доллар"))
        item = self.listWidget.item(31)
        item.setText(_translate("MainWindow", "IDR -- Индонезийская рупия"))
        item = self.listWidget.item(32)
        item.setText(_translate("MainWindow", "ILS -- Новый израильский шекель"))
        item = self.listWidget.item(33)
        item.setText(_translate("MainWindow", "INR -- Индийская рупия"))
        item = self.listWidget.item(34)
        item.setText(_translate("MainWindow", "KRW -- Южнокорейская вона"))
        item = self.listWidget.item(35)
        item.setText(_translate("MainWindow", "MXN -- Мексиканское песо"))
        item = self.listWidget.item(36)
        item.setText(_translate("MainWindow", "MYR -- Малайзийский ринггит"))
        item = self.listWidget.item(37)
        item.setText(_translate("MainWindow", "NZD -- Новозеландский доллар"))
        item = self.listWidget.item(38)
        item.setText(_translate("MainWindow", "PHP -- Филиппинское песо"))
        item = self.listWidget.item(39)
        item.setText(_translate("MainWindow", "SGD -- Сингапурский доллар"))
        item = self.listWidget.item(40)
        item.setText(_translate("MainWindow", "THB -- Тайский бат"))
        item = self.listWidget.item(41)
        item.setText(_translate("MainWindow", "ZAR -- Южноафриканский рэнд"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def converted(self):
        check_mass = ["USD", "EUR", "ZAR", "THB", "PHP", 'NZD', 'NZD', 'MYR', 'MXN', 'KRW', 'INR', 'ILS', 'IDR', 'HKD',
                      'CAD', 'BRL', 'AUD', 'TRY', 'TRL', 'HRK', 'NOK', 'ISK', 'CHF', 'SKK', 'SIT', "RUB", "CNY", "JPY",
                      "GBP", "BGN", "CYP", "CZK", "DKK", "EEK", "HUF", "LTL", "LVL", "MTL", "PLN", "ROL", "RON", "SEK"]
        c = CurrencyConverter()
        input_val = self.input_val.text()
        input_nom = self.input_nom.text()
        output_val = self.output_val.text()
        try:
            if str(input_val) in check_mass and input_nom.isdigit() and output_val in check_mass:
                output_num = round(c.convert(int(input_nom), input_val, output_val), 2)
            else:
                raise Exception
        except Exception:
            output_num = "Неверный Формат"
        self.output_nom.setText(str(output_num))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
