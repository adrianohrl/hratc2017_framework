# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jan 14 16:30:55 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1020, 600)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.mineDetectedLB = QtGui.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 159, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 159, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.mineDetectedLB.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mineDetectedLB.setFont(font)
        self.mineDetectedLB.setObjectName(_fromUtf8("mineDetectedLB"))
        self.horizontalLayout.addWidget(self.mineDetectedLB)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.wrongMinesDetectedLB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.wrongMinesDetectedLB.setFont(font)
        self.wrongMinesDetectedLB.setObjectName(_fromUtf8("wrongMinesDetectedLB"))
        self.horizontalLayout.addWidget(self.wrongMinesDetectedLB)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.startStopPB = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startStopPB.setIcon(icon)
        self.startStopPB.setObjectName(_fromUtf8("startStopPB"))
        self.horizontalLayout.addWidget(self.startStopPB)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.explodedMinesLB = QtGui.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.explodedMinesLB.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.explodedMinesLB.setFont(font)
        self.explodedMinesLB.setObjectName(_fromUtf8("explodedMinesLB"))
        self.horizontalLayout.addWidget(self.explodedMinesLB)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.timeLB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.timeLB.setFont(font)
        self.timeLB.setObjectName(_fromUtf8("timeLB"))
        self.horizontalLayout.addWidget(self.timeLB)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.mapwidget = QtGui.QWidget(self.centralwidget)
        self.mapwidget.setAutoFillBackground(True)
        self.mapwidget.setObjectName(_fromUtf8("mapwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mapwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem6 = QtGui.QSpacerItem(20, 371, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.coilsPlot = QtGui.QWidget(self.mapwidget)
        self.coilsPlot.setMinimumSize(QtCore.QSize(200, 100))
        self.coilsPlot.setObjectName(_fromUtf8("coilsPlot"))
        self.horizontalLayout_2.addWidget(self.coilsPlot)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.mapwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuVisualization = QtGui.QMenu(self.menubar)
        self.menuVisualization.setObjectName(_fromUtf8("menuVisualization"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setMouseTracking(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfiguration = QtGui.QAction(MainWindow)
        self.actionConfiguration.setObjectName(_fromUtf8("actionConfiguration"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionWrongMinesDetected = QtGui.QAction(MainWindow)
        self.actionWrongMinesDetected.setCheckable(True)
        self.actionWrongMinesDetected.setChecked(True)
        self.actionWrongMinesDetected.setObjectName(_fromUtf8("actionWrongMinesDetected"))
        self.actionMinesDetected = QtGui.QAction(MainWindow)
        self.actionMinesDetected.setCheckable(True)
        self.actionMinesDetected.setChecked(True)
        self.actionMinesDetected.setObjectName(_fromUtf8("actionMinesDetected"))
        self.actionExplodedMines = QtGui.QAction(MainWindow)
        self.actionExplodedMines.setCheckable(True)
        self.actionExplodedMines.setChecked(True)
        self.actionExplodedMines.setObjectName(_fromUtf8("actionExplodedMines"))
        self.actionTrueMines = QtGui.QAction(MainWindow)
        self.actionTrueMines.setCheckable(True)
        self.actionTrueMines.setChecked(True)
        self.actionTrueMines.setObjectName(_fromUtf8("actionTrueMines"))
        self.actionRobot = QtGui.QAction(MainWindow)
        self.actionRobot.setCheckable(True)
        self.actionRobot.setChecked(True)
        self.actionRobot.setObjectName(_fromUtf8("actionRobot"))
        self.actionCoilsSignal = QtGui.QAction(MainWindow)
        self.actionCoilsSignal.setCheckable(True)
        self.actionCoilsSignal.setChecked(True)
        self.actionCoilsSignal.setObjectName(_fromUtf8("actionCoilsSignal"))
        self.actionRobotPath = QtGui.QAction(MainWindow)
        self.actionRobotPath.setCheckable(True)
        self.actionRobotPath.setChecked(True)
        self.actionRobotPath.setObjectName(_fromUtf8("actionRobotPath"))
        self.actionCoveredArea = QtGui.QAction(MainWindow)
        self.actionCoveredArea.setCheckable(True)
        self.actionCoveredArea.setChecked(True)
        self.actionCoveredArea.setObjectName(_fromUtf8("actionCoveredArea"))
        self.menuFile.addAction(self.actionConfiguration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuVisualization.addAction(self.actionMinesDetected)
        self.menuVisualization.addAction(self.actionWrongMinesDetected)
        self.menuVisualization.addAction(self.actionExplodedMines)
        self.menuVisualization.addAction(self.actionTrueMines)
        self.menuVisualization.addSeparator()
        self.menuVisualization.addAction(self.actionRobot)
        self.menuVisualization.addAction(self.actionRobotPath)
        self.menuVisualization.addAction(self.actionCoveredArea)
        self.menuVisualization.addSeparator()
        self.menuVisualization.addAction(self.actionCoilsSignal)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuVisualization.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionCoilsSignal, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.coilsPlot.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "HRATC 2014 Simulator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Mines detected:", None, QtGui.QApplication.UnicodeUTF8))
        self.mineDetectedLB.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Wrong mines detected:", None, QtGui.QApplication.UnicodeUTF8))
        self.wrongMinesDetectedLB.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.startStopPB.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Exploded mines:", None, QtGui.QApplication.UnicodeUTF8))
        self.explodedMinesLB.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Elapsed time:", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLB.setText(QtGui.QApplication.translate("MainWindow", "00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVisualization.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfiguration.setText(QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfiguration.setShortcut(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWrongMinesDetected.setText(QtGui.QApplication.translate("MainWindow", "Wrong mines detected", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWrongMinesDetected.setShortcut(QtGui.QApplication.translate("MainWindow", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMinesDetected.setText(QtGui.QApplication.translate("MainWindow", "Mines detected", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMinesDetected.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExplodedMines.setText(QtGui.QApplication.translate("MainWindow", "Exploded mines", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExplodedMines.setShortcut(QtGui.QApplication.translate("MainWindow", "F4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrueMines.setText(QtGui.QApplication.translate("MainWindow", "True mines", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrueMines.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRobot.setText(QtGui.QApplication.translate("MainWindow", "Robot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRobot.setShortcut(QtGui.QApplication.translate("MainWindow", "F6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCoilsSignal.setText(QtGui.QApplication.translate("MainWindow", "Coil\'s signal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCoilsSignal.setShortcut(QtGui.QApplication.translate("MainWindow", "F8, Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRobotPath.setText(QtGui.QApplication.translate("MainWindow", "Robot\'s path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRobotPath.setShortcut(QtGui.QApplication.translate("MainWindow", "F7", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCoveredArea.setText(QtGui.QApplication.translate("MainWindow", "Covered area", None, QtGui.QApplication.UnicodeUTF8))
