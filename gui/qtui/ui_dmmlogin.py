# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dmmlogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 733)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 325))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(130, 0))
        self.label.setMaximumSize(QtCore.QSize(161, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_dmm_account = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dmm_account.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.lineEdit_dmm_account.setObjectName("lineEdit_dmm_account")
        self.horizontalLayout.addWidget(self.lineEdit_dmm_account)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(130, 0))
        self.label_2.setMaximumSize(QtCore.QSize(161, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_dmm_passwd = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dmm_passwd.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.lineEdit_dmm_passwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_dmm_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_dmm_passwd.setObjectName("lineEdit_dmm_passwd")
        self.horizontalLayout_2.addWidget(self.lineEdit_dmm_passwd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_use_proxy = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_use_proxy.setMinimumSize(QtCore.QSize(130, 0))
        self.checkBox_use_proxy.setMaximumSize(QtCore.QSize(161, 16777215))
        self.checkBox_use_proxy.setObjectName("checkBox_use_proxy")
        self.horizontalLayout_3.addWidget(self.checkBox_use_proxy)
        self.lineEdit_proxy_url = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_proxy_url.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.lineEdit_proxy_url.setObjectName("lineEdit_proxy_url")
        self.horizontalLayout_3.addWidget(self.lineEdit_proxy_url)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(130, 0))
        self.label_3.setMaximumSize(QtCore.QSize(161, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_edge_path = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_edge_path.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.lineEdit_edge_path.setObjectName("lineEdit_edge_path")
        self.horizontalLayout_4.addWidget(self.lineEdit_edge_path)
        self.comboBox_browser_type = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_browser_type.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.comboBox_browser_type.setObjectName("comboBox_browser_type")
        self.comboBox_browser_type.addItem("")
        self.comboBox_browser_type.addItem("")
        self.comboBox_browser_type.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_browser_type)
        self.pushButton_select_edge = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_select_edge.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.pushButton_select_edge.setObjectName("pushButton_select_edge")
        self.horizontalLayout_4.addWidget(self.pushButton_select_edge)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_help = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_help.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_5.addWidget(self.pushButton_help)
        self.pushButton_login = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_login.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_5.addWidget(self.pushButton_login)
        self.pushButton_login_cache = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_login_cache.setEnabled(False)
        self.pushButton_login_cache.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.pushButton_login_cache.setObjectName("pushButton_login_cache")
        self.horizontalLayout_5.addWidget(self.pushButton_login_cache)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.checkBox_open_browser_window = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_open_browser_window.setObjectName("checkBox_open_browser_window")
        self.verticalLayout.addWidget(self.checkBox_open_browser_window, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 3)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_logs = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_logs.setEnabled(True)
        self.textEdit_logs.setReadOnly(True)
        self.textEdit_logs.setObjectName("textEdit_logs")
        self.verticalLayout_3.addWidget(self.textEdit_logs)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fast Login"))
        self.groupBox.setTitle(_translate("MainWindow", "Fast Login Config"))
        self.label.setText(_translate("MainWindow", "DMM Account"))
        self.label_2.setText(_translate("MainWindow", "DMM Password"))
        self.checkBox_use_proxy.setText(_translate("MainWindow", "HTTP Proxy"))
        self.lineEdit_proxy_url.setPlaceholderText(_translate("MainWindow", "e.g. 127.0.0.1:8123"))
        self.label_3.setText(_translate("MainWindow", "WebDriver"))
        self.lineEdit_edge_path.setText(_translate("MainWindow", "msedgedriver.exe"))
        self.comboBox_browser_type.setItemText(0, _translate("MainWindow", "Edge"))
        self.comboBox_browser_type.setItemText(1, _translate("MainWindow", "Chrome"))
        self.comboBox_browser_type.setItemText(2, _translate("MainWindow", "Firefox"))
        self.pushButton_select_edge.setText(_translate("MainWindow", "select"))
        self.pushButton_help.setText(_translate("MainWindow", "Help"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.pushButton_login_cache.setText(_translate("MainWindow", "Login With Cache"))
        self.checkBox_open_browser_window.setText(_translate("MainWindow", "Open Browser Window"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Notes"))
        self.label_4.setText(_translate("MainWindow", "Launching game directly without opening DMM Game Player."))
        self.label_5.setText(_translate("MainWindow", "The launcher cannot automatically update the game.\n"
"If there is a game update, you need to download it in DMM Game Player\n"
" mannually."))
        self.label_6.setText(_translate("MainWindow", "Original project: https://github.com/MiddleRed/UmamusumeLauncher"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Login Logs"))
