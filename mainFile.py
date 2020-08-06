from PyQt4 import QtGui
import sys
import Login

class phishing(QtGui.QMainWindow, Login.Ui_frmLogin):
    def __init__(self, parent=None):
        super(phishing, self).__init__(parent)
        self.setupUi(self)
        self.btnlogin.clicked.connect(self.is_user_empty);
        self.btnlogin.clicked.connect(self.is_password_empty);
#        self.btnlogin.clicked.connect(self.is_text_empty);
#        self.btnlogin.clicked.connect(self.is_text_empty);
                
    def is_user_empty(self):
        text = self.txtuserName.text()
        if text == '':
            QMessageBox.warning(self.w,"the user is empty!")
            
    def is_password_empty(self):
        text = self.txtuserName.text()
        if text == '':
            print('the password is empty!')
        
        
def main():
    app = QtGui.QApplication(sys.argv) 
    form = phishing()                 
    form.show()                         
    app.exec_()
#    exit(app.exec_())
    
if __name__ == "__main__":
    main()
