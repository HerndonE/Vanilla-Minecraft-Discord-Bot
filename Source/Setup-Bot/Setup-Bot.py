# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.9
"""
Author     : Ethan Herndon
Date       : 1/23/24
Filename   : Setup-Bot.py
Desc       : Configurator to set up the Discord bot.
References :
"""
import json
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox


class Ui_Form(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/mcd-icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setEnabled(True)
        Form.resize(1100, 600)
        Form.setMinimumSize(QtCore.QSize(1100, 600))
        Form.setMaximumSize(QtCore.QSize(1100, 600))
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 530, 1161, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.listWidget.setPalette(palette)
        self.listWidget.setObjectName("listWidget")
        self.applyButton = QtWidgets.QPushButton(Form)
        self.applyButton.setGeometry(QtCore.QRect(640, 549, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applyButton.setFont(font)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.get_stuff)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(790, 549, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(self.cancel_setup)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(260, 0, 841, 531))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 261, 531))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("Images/mcd_cabin.png"))
        self.label.setObjectName("label")
        self.IPAdressTextEdit = QtWidgets.QTextEdit(Form)
        self.IPAdressTextEdit.setGeometry(QtCore.QRect(560, 194, 500, 23))
        self.IPAdressTextEdit.setObjectName("IPAdressTextEdit")
        self.passwordTextEdit = QtWidgets.QTextEdit(Form)
        self.passwordTextEdit.setGeometry(QtCore.QRect(560, 232, 500, 23))
        self.passwordTextEdit.setObjectName("passwordTextEdit")
        self.portTextEdit = QtWidgets.QTextEdit(Form)
        self.portTextEdit.setGeometry(QtCore.QRect(560, 270, 500, 23))
        self.portTextEdit.setObjectName("portTextEdit")
        self.logFileTextEdit = QtWidgets.QTextEdit(Form)
        self.logFileTextEdit.setGeometry(QtCore.QRect(560, 308, 500, 23))
        self.logFileTextEdit.setObjectName("logFileTextEdit")
        self.APITextEdit = QtWidgets.QTextEdit(Form)
        self.APITextEdit.setGeometry(QtCore.QRect(560, 346, 500, 23))
        self.APITextEdit.setObjectName("APITextEdit")
        self.chatChannelTextEdit = QtWidgets.QTextEdit(Form)
        self.chatChannelTextEdit.setGeometry(QtCore.QRect(560, 384, 500, 23))
        self.chatChannelTextEdit.setObjectName("chatChannelTextEdit")
        self.activityChannelTextEdit = QtWidgets.QTextEdit(Form)
        self.activityChannelTextEdit.setGeometry(QtCore.QRect(560, 420, 500, 23))
        self.activityChannelTextEdit.setObjectName("activityChannelTextEdit")
        self.clearlButton = QtWidgets.QPushButton(Form)
        self.clearlButton.setGeometry(QtCore.QRect(940, 549, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.clearlButton.setFont(font)
        self.clearlButton.setObjectName("clearlButton")
        self.clearlButton.clicked.connect(self.clear_setup)

        self.retranslate_ui(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslate_ui(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Minecraft Discord Bot Configurator"))
        self.applyButton.setText(_translate("Form", "Apply"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                            "type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; "
                                            "font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:18pt; "
                                            "font-weight:600;\">Minecraft Discord Bot Configurator</span><span "
                                            "style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; "
                                            "font-weight:600;\"><br /></span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Before running the "
                                            "Minecraft Discord Bot, enter the appropriate values below for your "
                                            "Minecraft Discord Bot. This process can take some period of time to "
                                            "complete. </span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Click "
                                            "&quot;Apply&quot; to continue, &quot;Cancel&quot; to exit Configurator, "
                                            "or &quot;Clear&quot; all text fields.</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt; "
                                            "font-weight:600;\">Server IP Address</span><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt; "
                                            "font-weight:600;\">Server Password</span><span style=\" font-family:\'MS "
                                            "Shell Dlg 2\'; font-size:12pt;\">:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt; "
                                            "font-weight:600;\">Server Port</span><span style=\" font-family:\'MS "
                                            "Shell Dlg 2\'; font-size:12pt;\">:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt; "
                                            "font-weight:600;\">Server Log File Directory</span><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt; "
                                            "font-weight:600;\">Discord API Key</span><span style=\" font-family:\'MS "
                                            "Shell Dlg 2\'; font-size:12pt;\">:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt; "
                                            "font-weight:600;\">Discord Minecraft Chat Channel</span><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:12pt; "
                                            "font-weight:600;\">Discord Minecraft Activity Channel</span><span "
                                            "style=\" font-family:\'MS Shell Dlg 2\'; "
                                            "font-size:12pt;\">:</span></p></body></html>"))
        self.clearlButton.setText(_translate("Form", "Clear"))

    def cancel_setup(self):
        # Close the main window
        Form.close()

    def clear_setup(self):
        self.IPAdressTextEdit.clear()
        self.passwordTextEdit.clear()
        self.portTextEdit.clear()
        self.logFileTextEdit.clear()
        self.APITextEdit.clear()
        self.chatChannelTextEdit.clear()
        self.activityChannelTextEdit.clear()

    def get_stuff(self):
        setup_information = [[f"Server IP address", self.IPAdressTextEdit.toPlainText()],
                             [f"Server Password", self.passwordTextEdit.toPlainText()],
                             [f"Server Port", self.portTextEdit.toPlainText()],
                             [f"Server Log File Directory", self.logFileTextEdit.toPlainText()],
                             [f"Discord API Key", self.APITextEdit.toPlainText()],
                             [f"Discord Minecraft Chat Channel", self.chatChannelTextEdit.toPlainText()],
                             [f"Discord Minecraft Activity Channel", self.activityChannelTextEdit.toPlainText()]]

        is_empty_text_field, print_empty_text_field = [], []

        for i in range(len(setup_information)):
            if setup_information[i][1] == "":
                is_empty_text_field.append(setup_information[i])

        if len(is_empty_text_field) > 0:
            for j in range(len(is_empty_text_field)):
                print_empty_text_field.append(f"{is_empty_text_field[j][0]} ")
            messagebox.showwarning("Error!", f"Enter the for {', '.join(print_empty_text_field)}")
            return

        self.apply_changes(setup_information)

    def apply_changes(self, setup_information):
        config_file = f"{os.getcwd()}\\Bot Settings\\config.json"
        with open(config_file) as f:
            configuration_information = json.load(f)
            configuration_information[0]["Rcon_Information"]['IP_Address'] = setup_information[0][1]
            configuration_information[0]["Rcon_Information"]['Password'] = setup_information[1][1]
            configuration_information[0]["Rcon_Information"]['Port'] = int(setup_information[2][1])
            configuration_information[0]['Log_File_Directory'] = setup_information[3][1]
            configuration_information[0]['Discord_API'] = setup_information[4][1]
            configuration_information[0]["Channels"]['Discord_Minecraft_Chat'] = int(setup_information[5][1])
            configuration_information[0]["Channels"]['Discord_Minecraft_Activity'] = int(setup_information[6][1])

        with open(config_file, 'w') as f:
            json.dump([configuration_information[0]], f, sort_keys=True, indent=4)

        Form.close()
        messagebox.showinfo(title="Bot initialization", message="Discord Bot will now start.")
        self.start_bot()

    def start_bot(self):
        subprocess.call([f"{os.getcwd()}\\Discord-Minecraft-Bot.exe"])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec_())
