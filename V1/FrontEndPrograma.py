# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrontEndProyecto.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(936, 629)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Triangular)
        self.actionArchivo = QAction(MainWindow)
        self.actionArchivo.setObjectName(u"actionArchivo")
        self.actionAbrir_CSV = QAction(MainWindow)
        self.actionAbrir_CSV.setObjectName(u"actionAbrir_CSV")
        self.actionCerrar = QAction(MainWindow)
        self.actionCerrar.setObjectName(u"actionCerrar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_parametros = QFrame(self.centralwidget)
        self.frame_parametros.setObjectName(u"frame_parametros")
        self.frame_parametros.setGeometry(QRect(0, 10, 421, 241))
        self.frame_parametros.setStyleSheet(u"#frame_parametros {\n"
"    background-color: #B9B9BD;\n"
"    border: 1.5px solid #4a76a8;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_parametros.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_parametros.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_parametros)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 221, 31))
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        brush2 = QBrush(QColor(169, 169, 176, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        self.label_7.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Noto Sans Mono"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_7.setFont(font1)
        self.label_5 = QLabel(self.frame_parametros)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 140, 221, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        self.label_5.setPalette(palette2)
        self.label_5.setFont(font1)
        self.textEdit_4 = QTextEdit(self.frame_parametros)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(260, 40, 104, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        brush3 = QBrush(QColor(154, 153, 150, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush3)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush3)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        self.textEdit_4.setPalette(palette3)
        self.textEdit_4.setStyleSheet(u"background-color: #A9A9B0;\n"
"border: 1.5px solid #4a76a8;\n"
"border-radius: 7px;")
        self.label_6 = QLabel(self.frame_parametros)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 40, 221, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        self.label_6.setPalette(palette4)
        self.label_6.setFont(font1)
        self.textEdit_3 = QTextEdit(self.frame_parametros)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(260, 140, 104, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush3)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush3)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        self.textEdit_3.setPalette(palette5)
        self.textEdit_3.setStyleSheet(u"background-color: #A9A9B0;\n"
"border: 1.5px solid #4a76a8;\n"
"border-radius: 7px;")
        self.textEdit_5 = QTextEdit(self.frame_parametros)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(260, 90, 104, 31))
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush3)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush3)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        self.textEdit_5.setPalette(palette6)
        self.textEdit_5.setStyleSheet(u"background-color: #A9A9B0;\n"
"border: 1.5px solid #4a76a8;\n"
"border-radius: 7px;")
        self.pushbutton_actualizar = QPushButton(self.frame_parametros)
        self.pushbutton_actualizar.setObjectName(u"pushbutton_actualizar")
        self.pushbutton_actualizar.setGeometry(QRect(90, 200, 241, 24))
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        brush4 = QBrush(QColor(74, 118, 168, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush4)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush5)
#endif
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush4)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush5)
#endif
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush1)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush4)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush5)
#endif
        self.pushbutton_actualizar.setPalette(palette7)
        font2 = QFont()
        font2.setFamilies([u"Noto Sans Mono"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushbutton_actualizar.setFont(font2)
        self.pushbutton_actualizar.setStyleSheet(u"QPushButton {\n"
"background-color: #4a76a8;\n"
"border: 1.5px solid #A9A9B0;\n"
"border-radius: 7px;\n"
"color: #000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #799AC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #1a365d;\n"
"}")
        self.label_parametros = QLabel(self.frame_parametros)
        self.label_parametros.setObjectName(u"label_parametros")
        self.label_parametros.setGeometry(QRect(10, 10, 401, 21))
        self.label_parametros.setStyleSheet(u"color: #3D57AD;\n"
"font-weight: bold;\n"
"border: 1.5px solid #B9B9BD;\n"
"background-color: #A9A9B0;")
        self.label_parametros.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_enlace = QFrame(self.centralwidget)
        self.frame_enlace.setObjectName(u"frame_enlace")
        self.frame_enlace.setGeometry(QRect(0, 250, 421, 81))
        self.frame_enlace.setStyleSheet(u"#frame_enlace {\n"
"    background-color: #B9B9BD;\n"
"    border: 1.5px solid #4a76a8;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_enlace.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_enlace.setFrameShadow(QFrame.Shadow.Raised)
        self.label_enlace = QLabel(self.frame_enlace)
        self.label_enlace.setObjectName(u"label_enlace")
        self.label_enlace.setGeometry(QRect(10, 10, 401, 21))
        self.label_enlace.setStyleSheet(u"color: #3D57AD;\n"
"font-weight: bold;\n"
"border: 1.5px solid #B9B9BD;\n"
"background-color: #A9A9B0;")
        self.label_enlace.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo_enlace = QComboBox(self.frame_enlace)
        self.combo_enlace.setObjectName(u"combo_enlace")
        self.combo_enlace.setGeometry(QRect(70, 40, 291, 24))
        self.combo_enlace.setStyleSheet(u"QComboBox {\n"
"background-color: #A9A9B0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"background-color: #909099;\n"
"}\n"
"")
        self.combo_enlace.setEditable(True)
        self.frame_parametros_2 = QFrame(self.centralwidget)
        self.frame_parametros_2.setObjectName(u"frame_parametros_2")
        self.frame_parametros_2.setGeometry(QRect(0, 330, 421, 141))
        self.frame_parametros_2.setStyleSheet(u"#frame_parametros_2 {\n"
"    background-color: #B9B9BD;\n"
"    border: 1.5px solid #4a76a8;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_parametros_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_parametros_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_parametros_3 = QLabel(self.frame_parametros_2)
        self.label_parametros_3.setObjectName(u"label_parametros_3")
        self.label_parametros_3.setGeometry(QRect(10, 10, 401, 21))
        self.label_parametros_3.setStyleSheet(u"color: #3D57AD;\n"
"font-weight: bold;\n"
"border: 1.5px solid #B9B9BD;\n"
"background-color: #A9A9B0;")
        self.label_parametros_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_parametros_3 = QFrame(self.centralwidget)
        self.frame_parametros_3.setObjectName(u"frame_parametros_3")
        self.frame_parametros_3.setGeometry(QRect(420, 10, 421, 161))
        self.frame_parametros_3.setStyleSheet(u"#frame_parametros_3 {\n"
"    background-color: #B9B9BD;\n"
"    border: 1.5px solid #4a76a8;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_parametros_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_parametros_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_parametros_4 = QLabel(self.frame_parametros_3)
        self.label_parametros_4.setObjectName(u"label_parametros_4")
        self.label_parametros_4.setGeometry(QRect(10, 10, 401, 21))
        self.label_parametros_4.setStyleSheet(u"color: #3D57AD;\n"
"font-weight: bold;\n"
"border: 1.5px solid #B9B9BD;\n"
"background-color: #A9A9B0;")
        self.label_parametros_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.widget = QWidget(self.frame_parametros_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 401, 111))
        self.widget.setStyleSheet(u"background-color: #ffffff;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 401, 111))
        self.widget_2.setStyleSheet(u"background-color: #ffffff;")
        self.frame_parametros_6 = QFrame(self.centralwidget)
        self.frame_parametros_6.setObjectName(u"frame_parametros_6")
        self.frame_parametros_6.setGeometry(QRect(420, 170, 421, 161))
        self.frame_parametros_6.setStyleSheet(u"#frame_parametros_6 {\n"
"    background-color: #B9B9BD;\n"
"    border: 1.5px solid #4a76a8;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_parametros_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_parametros_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_parametros_7 = QLabel(self.frame_parametros_6)
        self.label_parametros_7.setObjectName(u"label_parametros_7")
        self.label_parametros_7.setGeometry(QRect(10, 10, 401, 21))
        self.label_parametros_7.setStyleSheet(u"color: #3D57AD;\n"
"font-weight: bold;\n"
"border: 1.5px solid #B9B9BD;\n"
"background-color: #A9A9B0;")
        self.label_parametros_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.widget_3 = QWidget(self.frame_parametros_6)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 40, 401, 111))
        self.widget_3.setStyleSheet(u"background-color: #ffffff;")
        self.frame_parametros_7 = QFrame(self.centralwidget)
        self.frame_parametros_7.setObjectName(u"frame_parametros_7")
        self.frame_parametros_7.setGeometry(QRect(420, 330, 421, 161))
        self.frame_parametros_7.setStyleSheet(u"#frame_parametros_7{\n"
"    background-color: #B9B9BD;\n"
"    border: 1.5px solid #4a76a8;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_parametros_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_parametros_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_parametros_8 = QLabel(self.frame_parametros_7)
        self.label_parametros_8.setObjectName(u"label_parametros_8")
        self.label_parametros_8.setGeometry(QRect(10, 10, 401, 21))
        self.label_parametros_8.setStyleSheet(u"color: #3D57AD;\n"
"font-weight: bold;\n"
"border: 1.5px solid #B9B9BD;\n"
"background-color: #A9A9B0;")
        self.label_parametros_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.widget_4 = QWidget(self.frame_parametros_7)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 40, 401, 111))
        self.widget_4.setStyleSheet(u"background-color: #ffffff;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 936, 21))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"background-color: #4a76a8;\n"
"}\n"
"\n"
"QMenuBar::item:hover {\n"
"background-color: #799AC9;\n"
"}\n"
"\n"
"QMenu::item {\n"
"background-color: #4a76a8;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"background-color: #799AC9;\n"
"}")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuArchivo.setAutoFillBackground(False)
        self.menuArchivo.setStyleSheet(u"QMenu {\n"
"background-color: #000000;\n"
"}")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_CSV)
        self.menuArchivo.addAction(self.actionCerrar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ejemplo", None))
        MainWindow.setWindowFilePath("")
        self.actionArchivo.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.actionAbrir_CSV.setText(QCoreApplication.translate("MainWindow", u"Abrir CSV", None))
        self.actionCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Umbral SNR (dB)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Umbral BER", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Umbral potencia (dBm)", None))
        self.pushbutton_actualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_parametros.setText(QCoreApplication.translate("MainWindow", u"PAR\u00c1METROS", None))
        self.label_enlace.setText(QCoreApplication.translate("MainWindow", u"ENLACE A ANALIZAR", None))
        self.label_parametros_3.setText(QCoreApplication.translate("MainWindow", u"INFORME", None))
        self.label_parametros_4.setText(QCoreApplication.translate("MainWindow", u"POTENCIA RECIBIDA (dBm)", None))
        self.label_parametros_7.setText(QCoreApplication.translate("MainWindow", u"RELACION SE\u00d1AL-RUIDO (SNR)", None))
        self.label_parametros_8.setText(QCoreApplication.translate("MainWindow", u"TASA DE ERRORES (BER)", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

