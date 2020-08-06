# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmLogin(object):
    def setupUi(self, frmLogin):
        frmLogin.setObjectName(_fromUtf8("frmLogin"))
        frmLogin.resize(375, 174)
        frmLogin.setWindowOpacity(1.0)
        self.btnlogin = QtGui.QPushButton(frmLogin)
        self.btnlogin.setGeometry(QtCore.QRect(200, 120, 81, 27))
        self.btnlogin.setObjectName(_fromUtf8("btnlogin"))
        self.btncancel = QtGui.QPushButton(frmLogin)
        self.btncancel.setGeometry(QtCore.QRect(288, 120, 81, 27))
        self.btncancel.setObjectName(_fromUtf8("btncancel"))
        self.label = QtGui.QLabel(frmLogin)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(frmLogin)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtuserName = QtGui.QLineEdit(frmLogin)
        self.txtuserName.setGeometry(QtCore.QRect(110, 30, 261, 27))
        self.txtuserName.setObjectName(_fromUtf8("txtuserName"))
        self.txtpassord = QtGui.QLineEdit(frmLogin)
        self.txtpassord.setEnabled(True)
        self.txtpassord.setGeometry(QtCore.QRect(110, 70, 261, 27))
        self.txtpassord.setEchoMode(QtGui.QLineEdit.Password)
        self.txtpassord.setObjectName(_fromUtf8("txtpassord"))

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)

    def retranslateUi(self, frmLogin):
        frmLogin.setWindowTitle(_translate("frmLogin", "Login Form", None))
        self.btnlogin.setText(_translate("frmLogin", "Login", None))
        self.btncancel.setText(_translate("frmLogin", "Cancel", None))
        self.label.setText(_translate("frmLogin", "User Name:", None))
        self.label_2.setText(_translate("frmLogin", "Password:", None))


#if __name__ == "__main__":
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    frmLogin = QtGui.QDialog()
#    ui = Ui_frmLogin()
#    ui.setupUi(frmLogin)
#    frmLogin.show()
#    sys.exit(app.exec_())

