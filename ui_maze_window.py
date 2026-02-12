# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maze_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QGraphicsView, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionAPropos = QAction(MainWindow)
        self.actionAPropos.setObjectName(u"actionAPropos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.controlGroup = QGroupBox(self.centralwidget)
        self.controlGroup.setObjectName(u"controlGroup")
        self.controlGroup.setMinimumWidth(300)
        self.controlGroup.setMaximumWidth(350)
        self.verticalLayout = QVBoxLayout(self.controlGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dimensionsGroup = QGroupBox(self.controlGroup)
        self.dimensionsGroup.setObjectName(u"dimensionsGroup")
        self.formLayout = QFormLayout(self.dimensionsGroup)
        self.formLayout.setObjectName(u"formLayout")
        self.widthLabel = QLabel(self.dimensionsGroup)
        self.widthLabel.setObjectName(u"widthLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.widthLabel)

        self.widthSpinBox = QSpinBox(self.dimensionsGroup)
        self.widthSpinBox.setObjectName(u"widthSpinBox")
        self.widthSpinBox.setMinimum(5)
        self.widthSpinBox.setMaximum(50)
        self.widthSpinBox.setValue(15)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.widthSpinBox)

        self.heightLabel = QLabel(self.dimensionsGroup)
        self.heightLabel.setObjectName(u"heightLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.heightLabel)

        self.heightSpinBox = QSpinBox(self.dimensionsGroup)
        self.heightSpinBox.setObjectName(u"heightSpinBox")
        self.heightSpinBox.setMinimum(5)
        self.heightSpinBox.setMaximum(50)
        self.heightSpinBox.setValue(15)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.heightSpinBox)


        self.verticalLayout.addWidget(self.dimensionsGroup)

        self.obstaclesGroup = QGroupBox(self.controlGroup)
        self.obstaclesGroup.setObjectName(u"obstaclesGroup")
        self.verticalLayout_2 = QVBoxLayout(self.obstaclesGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.obstacleTypeLabel = QLabel(self.obstaclesGroup)
        self.obstacleTypeLabel.setObjectName(u"obstacleTypeLabel")

        self.verticalLayout_2.addWidget(self.obstacleTypeLabel)

        self.obstacleTypeCombo = QComboBox(self.obstaclesGroup)
        self.obstacleTypeCombo.addItem("")
        self.obstacleTypeCombo.addItem("")
        self.obstacleTypeCombo.addItem("")
        self.obstacleTypeCombo.addItem("")
        self.obstacleTypeCombo.addItem("")
        self.obstacleTypeCombo.setObjectName(u"obstacleTypeCombo")

        self.verticalLayout_2.addWidget(self.obstacleTypeCombo)

        self.densityLabel = QLabel(self.obstaclesGroup)
        self.densityLabel.setObjectName(u"densityLabel")

        self.verticalLayout_2.addWidget(self.densityLabel)

        self.densitySpinBox = QDoubleSpinBox(self.obstaclesGroup)
        self.densitySpinBox.setObjectName(u"densitySpinBox")
        self.densitySpinBox.setMaximum(1.000000000000000)
        self.densitySpinBox.setSingleStep(0.050000000000000)
        self.densitySpinBox.setValue(0.200000000000000)

        self.verticalLayout_2.addWidget(self.densitySpinBox)


        self.verticalLayout.addWidget(self.obstaclesGroup)

        self.rewardsGroup = QGroupBox(self.controlGroup)
        self.rewardsGroup.setObjectName(u"rewardsGroup")
        self.formLayout_2 = QFormLayout(self.rewardsGroup)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.stepCostLabel = QLabel(self.rewardsGroup)
        self.stepCostLabel.setObjectName(u"stepCostLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.stepCostLabel)

        self.stepCostSpinBox = QDoubleSpinBox(self.rewardsGroup)
        self.stepCostSpinBox.setObjectName(u"stepCostSpinBox")
        self.stepCostSpinBox.setMinimum(-100.000000000000000)
        self.stepCostSpinBox.setMaximum(0.000000000000000)
        self.stepCostSpinBox.setValue(-1.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.stepCostSpinBox)

        self.goalRewardLabel = QLabel(self.rewardsGroup)
        self.goalRewardLabel.setObjectName(u"goalRewardLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.goalRewardLabel)

        self.goalRewardSpinBox = QDoubleSpinBox(self.rewardsGroup)
        self.goalRewardSpinBox.setObjectName(u"goalRewardSpinBox")
        self.goalRewardSpinBox.setMaximum(1000.000000000000000)
        self.goalRewardSpinBox.setValue(100.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.goalRewardSpinBox)

        self.bonusCheckBox = QCheckBox(self.rewardsGroup)
        self.bonusCheckBox.setObjectName(u"bonusCheckBox")
        self.bonusCheckBox.setChecked(True)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.bonusCheckBox)

        self.numBonusLabel = QLabel(self.rewardsGroup)
        self.numBonusLabel.setObjectName(u"numBonusLabel")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.numBonusLabel)

        self.numBonusSpinBox = QSpinBox(self.rewardsGroup)
        self.numBonusSpinBox.setObjectName(u"numBonusSpinBox")
        self.numBonusSpinBox.setMinimum(0)
        self.numBonusSpinBox.setMaximum(20)
        self.numBonusSpinBox.setValue(5)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.numBonusSpinBox)

        self.bonusValueLabel = QLabel(self.rewardsGroup)
        self.bonusValueLabel.setObjectName(u"bonusValueLabel")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.bonusValueLabel)

        self.bonusValueSpinBox = QDoubleSpinBox(self.rewardsGroup)
        self.bonusValueSpinBox.setObjectName(u"bonusValueSpinBox")
        self.bonusValueSpinBox.setMaximum(100.000000000000000)
        self.bonusValueSpinBox.setValue(10.000000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.bonusValueSpinBox)


        self.verticalLayout.addWidget(self.rewardsGroup)

        self.generateButton = QPushButton(self.controlGroup)
        self.generateButton.setObjectName(u"generateButton")

        self.verticalLayout.addWidget(self.generateButton)

        self.algorithmGroup = QGroupBox(self.controlGroup)
        self.algorithmGroup.setObjectName(u"algorithmGroup")
        self.verticalLayout_3 = QVBoxLayout(self.algorithmGroup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.solveAStarButton = QPushButton(self.algorithmGroup)
        self.solveAStarButton.setObjectName(u"solveAStarButton")

        self.verticalLayout_3.addWidget(self.solveAStarButton)

        self.solveDijkstraButton = QPushButton(self.algorithmGroup)
        self.solveDijkstraButton.setObjectName(u"solveDijkstraButton")

        self.verticalLayout_3.addWidget(self.solveDijkstraButton)

        self.compareButton = QPushButton(self.algorithmGroup)
        self.compareButton.setObjectName(u"compareButton")

        self.verticalLayout_3.addWidget(self.compareButton)

        self.showExplorationCheckBox = QCheckBox(self.algorithmGroup)
        self.showExplorationCheckBox.setObjectName(u"showExplorationCheckBox")
        self.showExplorationCheckBox.setChecked(False)

        self.verticalLayout_3.addWidget(self.showExplorationCheckBox)


        self.verticalLayout.addWidget(self.algorithmGroup)

        self.clearButton = QPushButton(self.controlGroup)
        self.clearButton.setObjectName(u"clearButton")

        self.verticalLayout.addWidget(self.clearButton)

        self.statsText = QTextEdit(self.controlGroup)
        self.statsText.setObjectName(u"statsText")
        self.statsText.setMaximumHeight(150)
        self.statsText.setReadOnly(True)

        self.verticalLayout.addWidget(self.statsText)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.controlGroup)

        self.mazeView = QGraphicsView(self.centralwidget)
        self.mazeView.setObjectName(u"mazeView")
        self.mazeView.setRenderHints(QPainter.Antialiasing|QPainter.SmoothPixmapTransform|QPainter.TextAntialiasing)

        self.horizontalLayout.addWidget(self.mazeView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        self.menuFichier.addAction(self.actionQuitter)
        self.menuAide.addAction(self.actionAPropos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"R\u00e9solution de Labyrinthe - A* et Dijkstra", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionAPropos.setText(QCoreApplication.translate("MainWindow", u"\u00c0 propos", None))
        self.controlGroup.setTitle(QCoreApplication.translate("MainWindow", u"Contr\u00f4les", None))
        self.dimensionsGroup.setTitle(QCoreApplication.translate("MainWindow", u"Dimensions du Labyrinthe", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"Largeur:", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Hauteur:", None))
        self.obstaclesGroup.setTitle(QCoreApplication.translate("MainWindow", u"Obstacles", None))
        self.obstacleTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Type d'obstacles:", None))
        self.obstacleTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Al\u00e9atoire", None))
        self.obstacleTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Murs verticaux", None))
        self.obstacleTypeCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Murs horizontaux", None))
        self.obstacleTypeCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Motif complexe", None))
        self.obstacleTypeCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Aucun obstacle", None))

        self.densityLabel.setText(QCoreApplication.translate("MainWindow", u"Densit\u00e9 (0.0 - 1.0):", None))
        self.rewardsGroup.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9compenses", None))
        self.stepCostLabel.setText(QCoreApplication.translate("MainWindow", u"Co\u00fbt par pas:", None))
        self.goalRewardLabel.setText(QCoreApplication.translate("MainWindow", u"R\u00e9compense but:", None))
        self.bonusCheckBox.setText(QCoreApplication.translate("MainWindow", u"Ajouter bonus:", None))
        self.numBonusLabel.setText(QCoreApplication.translate("MainWindow", u"Nombre bonus:", None))
        self.bonusValueLabel.setText(QCoreApplication.translate("MainWindow", u"Valeur bonus:", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer Labyrinthe", None))
        self.algorithmGroup.setTitle(QCoreApplication.translate("MainWindow", u"Algorithmes", None))
        self.solveAStarButton.setText(QCoreApplication.translate("MainWindow", u"R\u00e9soudre avec A*", None))
        self.solveDijkstraButton.setText(QCoreApplication.translate("MainWindow", u"R\u00e9soudre avec Dijkstra", None))
        self.compareButton.setText(QCoreApplication.translate("MainWindow", u"Comparer les deux", None))
        self.showExplorationCheckBox.setText(QCoreApplication.translate("MainWindow", u"Afficher l'exploration", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Effacer le chemin", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
    # retranslateUi

