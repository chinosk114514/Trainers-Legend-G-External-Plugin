# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 669)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 431))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_config_settings = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_config_settings.setGeometry(QtCore.QRect(70, 40, 221, 71))
        self.pushButton_config_settings.setObjectName("pushButton_config_settings")
        self.pushButton_fast_reboot = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fast_reboot.setEnabled(False)
        self.pushButton_fast_reboot.setGeometry(QtCore.QRect(70, 240, 221, 71))
        self.pushButton_fast_reboot.setObjectName("pushButton_fast_reboot")
        self.pushButton_discord_rpc = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_discord_rpc.setGeometry(QtCore.QRect(70, 140, 221, 71))
        self.pushButton_discord_rpc.setObjectName("pushButton_discord_rpc")
        self.pushButton_fast_login = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fast_login.setEnabled(False)
        self.pushButton_fast_login.setGeometry(QtCore.QRect(70, 340, 221, 71))
        self.pushButton_fast_login.setObjectName("pushButton_fast_login")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 550, 371, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_about_father = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_about_father.setGeometry(QtCore.QRect(60, 20, 251, 28))
        self.pushButton_about_father.setObjectName("pushButton_about_father")
        self.pushButton_about_this = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_about_this.setGeometry(QtCore.QRect(60, 60, 251, 28))
        self.pushButton_about_this.setObjectName("pushButton_about_this")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 450, 371, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_plugin_update = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_plugin_update.setEnabled(False)
        self.pushButton_plugin_update.setGeometry(QtCore.QRect(259, 25, 91, 51))
        self.pushButton_plugin_update.setObjectName("pushButton_plugin_update")
        self.label_version_now = QtWidgets.QLabel(self.groupBox_3)
        self.label_version_now.setGeometry(QtCore.QRect(22, 28, 241, 16))
        self.label_version_now.setObjectName("label_version_now")
        self.label_version_latest = QtWidgets.QLabel(self.groupBox_3)
        self.label_version_latest.setGeometry(QtCore.QRect(22, 57, 241, 16))
        self.label_version_latest.setObjectName("label_version_latest")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trainers-Legend-G External Plugin"))
        self.groupBox.setTitle(_translate("MainWindow", "Trainers-Legend-G External Plugin"))
        self.pushButton_config_settings.setText(_translate("MainWindow", "Config Settings"))
        self.pushButton_fast_reboot.setText(_translate("MainWindow", "Game Fast Reboot"))
        self.pushButton_discord_rpc.setText(_translate("MainWindow", "Discord RPC"))
        self.pushButton_fast_login.setText(_translate("MainWindow", "Game Fast Login"))
        self.groupBox_2.setTitle(_translate("MainWindow", "About"))
        self.pushButton_about_father.setText(_translate("MainWindow", "Github - Trainers-Legend-G"))
        self.pushButton_about_this.setText(_translate("MainWindow", "Github - This Plugin"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Plugin Version"))
        self.pushButton_plugin_update.setText(_translate("MainWindow", "Update"))
        self.label_version_now.setText(_translate("MainWindow", "version_now"))
        self.label_version_latest.setText(_translate("MainWindow", "version_latest"))
