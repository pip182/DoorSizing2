# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created: Sat Jan 18 22:18:13 2014
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(479, 205)
        self.saveButton = QtGui.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(360, 170, 101, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(20, 170, 101, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 441, 141))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.outputButton = QtGui.QToolButton(self.formLayoutWidget)
        self.outputButton.setObjectName(_fromUtf8("outputButton"))
        self.gridLayout.addWidget(self.outputButton, 2, 2, 1, 1)
        self.listsButton = QtGui.QToolButton(self.formLayoutWidget)
        self.listsButton.setObjectName(_fromUtf8("listsButton"))
        self.gridLayout.addWidget(self.listsButton, 1, 2, 1, 1)
        self.listsEdit = QtGui.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.listsEdit.setFont(font)
        self.listsEdit.setObjectName(_fromUtf8("listsEdit"))
        self.gridLayout.addWidget(self.listsEdit, 1, 1, 1, 1)
        self.outputEdit = QtGui.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.outputEdit.setFont(font)
        self.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        self.gridLayout.addWidget(self.outputEdit, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.oversizeBox = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.oversizeBox.setFont(font)
        self.oversizeBox.setDecimals(6)
        self.oversizeBox.setSingleStep(0.015625)
        self.oversizeBox.setObjectName(_fromUtf8("oversizeBox"))
        self.gridLayout.addWidget(self.oversizeBox, 0, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.toolNumBox = QtGui.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.toolNumBox.setFont(font)
        self.toolNumBox.setObjectName(_fromUtf8("toolNumBox"))
        self.gridLayout.addWidget(self.toolNumBox, 3, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Configure Application", None))
        self.saveButton.setText(_translate("Dialog", "OK", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))
        self.outputButton.setText(_translate("Dialog", "...", None))
        self.listsButton.setText(_translate("Dialog", "...", None))
        self.label_2.setText(_translate("Dialog", "Job Folder Location", None))
        self.label_3.setText(_translate("Dialog", "Output Folder", None))
        self.label.setText(_translate("Dialog", "Oversize Amount", None))
        self.oversizeBox.setSuffix(_translate("Dialog", "\"", None))
        self.label_4.setText(_translate("Dialog", "Default Tool #", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

