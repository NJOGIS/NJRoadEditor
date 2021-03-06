# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'batchnames.ui'

from PyQt4 import QtCore, QtGui
import sys
import os
import pickle
import traceback


##########################################################################################################
##########################################################################################################
##########################################################################################################
# THIS SECTION AUTOGENERATED BY pyuic4 from reading ui file 'batchnames.ui'
# When making changes to batchnames.ui, replace the data in this section with code from generated design
# script

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
        Dialog.resize(1303, 781)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.segList = QtGui.QListWidget(self.groupBox)
        self.segList.setGeometry(QtCore.QRect(10, 20, 221, 281))
        self.segList.setAlternatingRowColors(True)
        self.segList.setObjectName(_fromUtf8("segList"))
        self.removeButton = QtGui.QPushButton(self.groupBox)
        self.removeButton.setGeometry(QtCore.QRect(14, 310, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.removeButton.setFont(font)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 10, 1021, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.useNamesButton = QtGui.QPushButton(self.groupBox_2)
        self.useNamesButton.setGeometry(QtCore.QRect(860, 310, 141, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Images/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.useNamesButton.setIcon(icon)
        self.useNamesButton.setObjectName(_fromUtf8("useNamesButton"))
        self.segNamesTable = QtGui.QTableWidget(self.groupBox_2)
        self.segNamesTable.setGeometry(QtCore.QRect(15, 21, 991, 281))
        self.segNamesTable.setAlternatingRowColors(True)
        self.segNamesTable.setRowCount(0)
        self.segNamesTable.setColumnCount(3)
        self.segNamesTable.setObjectName(_fromUtf8("segNamesTable"))
        item = QtGui.QTableWidgetItem()
        self.segNamesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.segNamesTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.segNamesTable.setHorizontalHeaderItem(2, item)
        self.segNamesTable.horizontalHeader().setStretchLastSection(True)
        self.segNamesTable.verticalHeader().setStretchLastSection(False)
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 350, 1291, 19))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 370, 1281, 401))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.updateNamesButton = QtGui.QPushButton(self.groupBox_3)
        self.updateNamesButton.setGeometry(QtCore.QRect(1120, 370, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.updateNamesButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.updateNamesButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Images/dbcommit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateNamesButton.setIcon(icon1)
        self.updateNamesButton.setObjectName(_fromUtf8("updateNamesButton"))
        self.newNamesTable = QtGui.QTableWidget(self.groupBox_3)
        self.newNamesTable.setGeometry(QtCore.QRect(50, 20, 1221, 341))
        self.newNamesTable.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.newNamesTable.setAlternatingRowColors(True)
        self.newNamesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.newNamesTable.setRowCount(0)
        self.newNamesTable.setColumnCount(14)
        self.newNamesTable.setObjectName(_fromUtf8("newNamesTable"))
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.newNamesTable.setHorizontalHeaderItem(13, item)
        self.newNamesTable.horizontalHeader().setCascadingSectionResizes(True)
        self.newNamesTable.horizontalHeader().setDefaultSectionSize(110)
        self.newNamesTable.horizontalHeader().setStretchLastSection(False)
        self.newNamesTable.verticalHeader().setDefaultSectionSize(30)
        self.newNamesTable.verticalHeader().setStretchLastSection(False)
        self.statusBar = QtGui.QLabel(self.groupBox_3)
        self.statusBar.setGeometry(QtCore.QRect(20, 370, 1081, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.statusBar.setFont(font)
        self.statusBar.setFrameShape(QtGui.QFrame.Box)
        self.statusBar.setText(_fromUtf8(""))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.addNewButton = QtGui.QPushButton(self.groupBox_3)
        self.addNewButton.setGeometry(QtCore.QRect(6, 19, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addNewButton.setFont(font)
        self.addNewButton.setIconSize(QtCore.QSize(32, 32))
        self.addNewButton.setObjectName(_fromUtf8("addNewButton"))
        self.delNewButton = QtGui.QPushButton(self.groupBox_3)
        self.delNewButton.setGeometry(QtCore.QRect(6, 65, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delNewButton.setFont(font)
        self.delNewButton.setIconSize(QtCore.QSize(32, 32))
        self.delNewButton.setObjectName(_fromUtf8("delNewButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Segments:", None))
        self.removeButton.setText(_translate("Dialog", "Remove Selected", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Selected Segment Names:", None))
        self.useNamesButton.setToolTip(_translate("Dialog", "Use these SEG_NAMES as the new names", None))
        self.useNamesButton.setText(_translate("Dialog", "Use These Names", None))
        self.segNamesTable.setSortingEnabled(True)
        item = self.segNamesTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "TYPE", None))
        item = self.segNamesTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "RANK", None))
        item = self.segNamesTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "NAME_FULL", None))
        self.groupBox_3.setTitle(_translate("Dialog", "New Names:", None))
        self.updateNamesButton.setToolTip(_translate("Dialog", "Commit changes to the DB", None))
        self.updateNamesButton.setText(_translate("Dialog", "Update Names", None))
        self.newNamesTable.setSortingEnabled(True)
        item = self.newNamesTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "TYPE", None))
        item = self.newNamesTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "RANK", None))
        item = self.newNamesTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "NAME_FULL", None))
        item = self.newNamesTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "PRE_DIR", None))
        item = self.newNamesTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "PRE_TYPE", None))
        item = self.newNamesTable.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "PRE_MOD", None))
        item = self.newNamesTable.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "NAME", None))
        item = self.newNamesTable.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "SUF_TYPE", None))
        item = self.newNamesTable.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "SUF_MOD", None))
        item = self.newNamesTable.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "SUF_DIR", None))
        item = self.newNamesTable.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "DATA_SRC_TYPE_ID", None))
        item = self.newNamesTable.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "SHIELD_TYPE_ID", None))
        item = self.newNamesTable.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "SHIELD_SUBTYPE_ID", None))
        item = self.newNamesTable.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "SHIELD_NAME", None))
        self.addNewButton.setToolTip(_translate("Dialog", "Add a New Name", None))
        self.addNewButton.setText(_translate("Dialog", "+", None))
        self.delNewButton.setToolTip(_translate("Dialog", "Delete Name", None))
        self.delNewButton.setText(_translate("Dialog", "-", None))

# END Design script class
##########################################################################################################
##########################################################################################################
##########################################################################################################





class BatchEditNames(QtGui.QDialog, Ui_Dialog):
    def __init__(self, workSpace, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.wkSpace = workSpace.replace("'","")
        self.setWindowTitle("Batch Edit Names")
        self.domains = {'DATA_SRC_TYPE_ID': {'':None,'NJDOT SLD':1,'Tiger':2,'County':3,'MOD IV':4,'Other':5,'NJOIT':6,'TAXMAP':7},
                        'TYPE':             {'':None,'Local':'L','Highway':'H'},
                        'SHIELD_TYPE_ID':   {'':None,'Atlantic City Expressway':'ACE','Garden State Parkway':'GSP','NJ Turnpike':'TPK',
                                            'Palisades Parkway':'PIP','Interstate':'INT','US Route':'USR','State Route':'STR',
                                            'County Route':'COR','Atlantic City Brigantine Connector':'ACB'},
                        'SHIELD_SUBTYPE_ID':{'Main Route':'M','Alternate Route':'A','Business Route':'B','Express Route':'E',
                                            'Truck Route':'T','Spur Route':'S','Connector Route':'C','Bypass Route':'Y'}}
        self.namesref = {}
        self.sessionLog = []
        self.highwayrows = []
        #self.statusBar.setStyleSheet('color: red')
        self.lockeditem = QtGui.QTableWidgetItem()
        self.lockeditem.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
        self.segList.itemClicked.connect(self.updatesegnames)
        self.removeButton.clicked.connect(self.removeseg)
        self.addNewButton.clicked.connect(self.addname)
        self.delNewButton.clicked.connect(self.delname)
        self.useNamesButton.clicked.connect(self.addselectednames)
        self.updateNamesButton.clicked.connect(self.postnames)
        self.newNamesTable.cellChanged.connect(self.updatelistener)
        self.listening = False

        self.loadnames()
        self.loadsegs()
        self.messageWidget = QtGui.QWidget()
        self.listening = True

    def repainttable(self):
        listeningFlag = self.listening
        if self.listening:
            self.listening = False
            tblRows = self.newNamesTable.rowCount()
            for row in xrange(0,tblRows):
                if str(self.newNamesTable.cellWidget(row,0).currentText()) == 'Highway':

                    shieldval = str(self.newNamesTable.cellWidget(row,11).currentText())
                    if shieldval == 'Atlantic City Expressway':
                        self.newNamesTable.item(row,6).setText('Atlantic City')
                        self.newNamesTable.item(row,7).setText('Expressway')
                    if shieldval == 'Atlantic City Brigantine Connector':
                        self.newNamesTable.item(row,6).setText('Atlantic City Brigantine')
                    if shieldval == 'County Route':
                        self.newNamesTable.item(row,4).setText('County Route')
                    if shieldval == 'Garden State Parkway':
                        self.newNamesTable.item(row,6).setText('Garden State')
                        self.newNamesTable.item(row,7).setText('Parkway')
                    if shieldval == 'Interstate':
                        self.newNamesTable.item(row,4).setText('Interstate')
                    if shieldval == 'Palisades Parkway':
                        self.newNamesTable.item(row,6).setText('Palisades Interstate')
                        self.newNamesTable.item(row,7).setText('Parkway')
                    if shieldval == 'State Route':
                        self.newNamesTable.item(row,4).setText('State Highway')
                    if shieldval == 'NJ Turnpike':
                        self.newNamesTable.item(row,6).setText('New Jersey')
                        self.newNamesTable.item(row,7).setText('Turnpike')
                    if shieldval == 'US Route':
                        self.newNamesTable.item(row,4).setText('US Highway')
                    subtypeval = self.domains['SHIELD_SUBTYPE_ID'][str(self.newNamesTable.cellWidget(row,12).currentText())]
                    if subtypeval =='A':
                        self.newNamesTable.item(row,8).setText('Alternate')
                    if subtypeval =='B':
                        self.newNamesTable.item(row,8).setText('Business')
                    if subtypeval =='C':
                        self.newNamesTable.item(row,8).setText('Connector')
                    if subtypeval =='E':
                        self.newNamesTable.item(row,8).setText('Express')
                    if subtypeval =='S':
                        self.newNamesTable.item(row,8).setText('Spur')
                    if subtypeval =='T':
                        self.newNamesTable.item(row,8).setText('Truck')
                    if subtypeval =='Y':
                        self.newNamesTable.item(row,8).setText('Bypass')
                    if subtypeval is None:
                        self.newNamesTable.item(row,8).setText('')
                    namefull = self.concat(self.newNamesTable.item(row, 3).text(),
                                           self.newNamesTable.item(row, 4).text(),
                                           self.newNamesTable.item(row, 5).text(),
                                           self.newNamesTable.item(row, 6).text(),
                                           self.newNamesTable.item(row, 7).text(),
                                           self.newNamesTable.item(row, 8).text(),
                                           self.newNamesTable.item(row, 9).text())
                    self.newNamesTable.item(row,2).setText(namefull)
                    self.newNamesTable.cellWidget(row,11).setDisabled(False)
                    self.newNamesTable.cellWidget(row,12).setDisabled(False)
                    self.newNamesTable.item(row,13).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
                    self.newNamesTable.item(row,2).setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)


                if str(self.newNamesTable.cellWidget(row,0).currentText()) == 'Local':
                    self.newNamesTable.cellWidget(row,11).setCurrentIndex(0)
                    self.newNamesTable.cellWidget(row,11).setDisabled(True)
                    self.newNamesTable.cellWidget(row,12).setCurrentIndex(5)
                    self.newNamesTable.cellWidget(row,12).setDisabled(True)
                    self.newNamesTable.item(row,13).setText('')
                    self.newNamesTable.item(row,13).setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
                    if str(self.newNamesTable.item(row,4).text()) in ['US Highway','State Highway', 'County Route','Interstate'] or \
                        any(i in str(self.newNamesTable.item(row, 2).text()) for i in ['Palisades Interstate', 'New Jersey Turnpike','Garden State Parkway','Atlantic City Expressway']):

                        self.newNamesTable.item(row,2).setText('')
                        self.newNamesTable.item(row,3).setText('')
                        self.newNamesTable.item(row,4).setText('')
                        self.newNamesTable.item(row,5).setText('')
                        self.newNamesTable.item(row,6).setText('')
                        self.newNamesTable.item(row,7).setText('')
                        self.newNamesTable.item(row,8).setText('')
                        self.newNamesTable.item(row,9).setText('')
                    self.newNamesTable.item(row,2).setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)

        self.newNamesTable.repaint()
        self.listening = listeningFlag
        return

    def updatelistener(self, row, column):
        #print 'updatelistener fired'
        if self.listening:
            self.listening = False
            # If row is of Type='Highway' and SHIELD_NAME or NAME is updated- make them match
            if str(self.newNamesTable.cellWidget(row, 0).currentText()) == 'Highway':
                if self.newNamesTable.horizontalHeaderItem(column).text() == 'SHIELD_NAME':
                    #print 'update name from Shield Name'
                    self.newNamesTable.item(row,6).setText(str(self.newNamesTable.item(row, column).text()))
                if self.newNamesTable.horizontalHeaderItem(column).text() == 'NAME':
                    #print 'update shield name from name'
                    self.newNamesTable.item(row,13).setText(str(self.newNamesTable.item(row, column).text()))
            if column in [3,4,5,6,7,8,9,13]:
                #print 'names columns update fired'
                namefull = self.concat(self.newNamesTable.item(row, 3).text(),
                                       self.newNamesTable.item(row, 4).text(),
                                       self.newNamesTable.item(row, 5).text(),
                                       self.newNamesTable.item(row, 6).text(),
                                       self.newNamesTable.item(row, 7).text(),
                                       self.newNamesTable.item(row, 8).text(),
                                       self.newNamesTable.item(row, 9).text())
                self.newNamesTable.item(row,2).setText(namefull)
            self.listening = True

    def postnames(self):
        newnames = []
        errors = []
        hwys = []
        locals = []
        errorflag = False
        tblRows = self.newNamesTable.rowCount()
        for row in xrange(0,tblRows):
            newname = {}

            if str(self.newNamesTable.cellWidget(row,0).currentText()) != '': # Only check rows with TYPE filled in

                rdtype = self.domains['TYPE'][str(self.newNamesTable.cellWidget(row,0).currentText())]
                try:
                    rank = int(self.newNamesTable.item(row,1).text())
                except:
                    errorflag = True
                    errors.append('Rank must be an integer in row: ' + str(row + 1))
                    break
                predir = self.scruboutput(str(self.newNamesTable.item(row,3).text()))
                pretype = self.scruboutput(str(self.newNamesTable.item(row,4).text()))
                premod = self.scruboutput(str(self.newNamesTable.item(row,5).text()))
                name = self.scruboutput(str(self.newNamesTable.item(row,6).text()))
                suftype = self.scruboutput(str(self.newNamesTable.item(row,7).text()))
                sufmod = self.scruboutput(str(self.newNamesTable.item(row,8).text()))
                sufdir = self.scruboutput(str(self.newNamesTable.item(row,9).text()))
                datasrctype = self.domains['DATA_SRC_TYPE_ID'][str(self.newNamesTable.cellWidget(row,10).currentText())]
                shieldtype = self.domains['SHIELD_TYPE_ID'][str(self.newNamesTable.cellWidget(row,11).currentText())]
                shieldsubtype = self.domains['SHIELD_SUBTYPE_ID'][str(self.newNamesTable.cellWidget(row,12).currentText())]
                shieldname = self.scruboutput(str(self.newNamesTable.item(row,13).text()))
                namefull = self.concat(predir,pretype,premod,name,suftype,sufmod,sufdir)
                if rdtype == 'L': # Add rank to local
                    locals.append(rank)
                if rdtype == 'H':
                    hwys.append(rank)
                    if shieldtype in ['',None]:
                        errorflag = True
                        errors.append('Highway must have a SHIELD_TYPE_ID in row: ' + str(row + 1))
                    #if shieldsubtype in ['',None]:
                    #    errorflag = True
                    #    errors.append('Highway must have a SHIELD_SUBTYPE_ID in row: ' + str(row + 1))
                    if len(str(shieldname)) > 5:
                        errorflag = True
                        errors.append('SHIELD_NAME exceeds max length in row: ' + str(row + 1))

                localcount = 1
                for x in sorted(locals):
                    if x != localcount:
                        errorflag = True
                        errors.append('Improper ranking in local roadnames')
                    localcount +=1
                hwycount = 1
                for x in sorted(hwys):
                    if x != hwycount:
                        errorflag = True
                        errors.append('Improper ranking in hwy roadnames')
                    hwycount += 1
                if name in ['',None]:
                    errorflag = True
                    errors.append('Road must have a NAME in row: ' + str(row + 1))
                if datasrctype in ['',None]:
                    errorflag = True
                    errors.append('Road must have a DATA_SRC_TYPE_ID in row: ' + str(row + 1))

                if not errorflag:
                    newname['type'] = rdtype
                    newname['rank'] = rank
                    newname['predir'] = predir
                    newname['pretype'] = pretype
                    newname['premod'] = premod
                    newname['name'] = name
                    newname['suftype'] = suftype
                    newname['sufmod'] = sufmod
                    newname['sufdir'] = sufdir
                    newname['datasrctype'] = datasrctype
                    newname['shieldtype'] = shieldtype
                    newname['shieldsubtype'] = shieldsubtype
                    newname['shieldname'] = shieldname
                    newname['namefull'] = namefull
                    newnames.append(newname)
        if errorflag:
            errortext = ""
            for i in list(set(errors)):
                errortext += "\n -" + i + ""
            msgBox = QtGui.QMessageBox.critical(self.messageWidget, "Validation", "Please fix the following errors: \n" + errortext )

        if not errorflag:
            #If no errors, we are good to post data to output pickle
            outputNames = {}
            outputNames['segs'] = [str(i.text()) for i in self.segList.findItems("", QtCore.Qt.MatchContains)]
            outputNames['names'] = newnames

            batchnames_path = os.path.join(self.wkSpace, "batchnames.p")
            if os.path.exists(batchnames_path):
                os.remove(batchnames_path)

            output_path = os.path.join(self.wkSpace, "batchnames_output.p")
            if os.path.exists(output_path):
                os.remove(output_path)
            try:
                with open(output_path, 'wb') as output:
                    pickle.dump(outputNames, output, -1)
                #sys.stdout.write("OK")
                #sys.stdout.flush()
                self.close()
            except Exception, e:
                self.statusBar.setText('Error: Could not save names to output file: ' + str(e))

    def concat(self,*args):
        return ' '.join([str(x) for x in args if str(x) not in ['None','',' ']])

    def createQComboBoxItem_Type(self, type):
        comboBox = QtGui.QComboBox()
        comboBox.setEditable(False)

        if type == 'TYPE':
            comboBox.addItems(sorted(self.domains['TYPE'].keys()))
        if type == 'DATA_SRC_TYPE_ID':
            comboBox.addItems(sorted(self.domains['DATA_SRC_TYPE_ID'].keys()))
        if type == 'SHIELD_TYPE_ID':
            comboBox.addItems(sorted(self.domains['SHIELD_TYPE_ID'].keys()))
        if type == 'SHIELD_SUBTYPE_ID':
            comboBox.addItems(sorted(self.domains['SHIELD_SUBTYPE_ID'].keys()))

        comboBox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        return comboBox


    def addname(self):
        self.listening = False
        rowPosition = self.newNamesTable.rowCount()
        self.newNamesTable.insertRow(rowPosition)

        typecombo = self.createQComboBoxItem_Type('TYPE')
        typecombo.currentIndexChanged.connect( lambda: self.repainttable() )

        datasrccombo = self.createQComboBoxItem_Type('DATA_SRC_TYPE_ID')

        shieldcombo = self.createQComboBoxItem_Type('SHIELD_TYPE_ID')
        shieldcombo.currentIndexChanged.connect( lambda: self.repainttable() )

        shieldsubcombo = self.createQComboBoxItem_Type('SHIELD_SUBTYPE_ID')
        shieldsubcombo.currentIndexChanged.connect( lambda: self.repainttable() )

        self.newNamesTable.setCellWidget(rowPosition,0,typecombo) # TYPE field
        self.newNamesTable.setItem(rowPosition,1,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,2,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,3,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,4,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,5,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,6,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,7,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,8,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,9,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setItem(rowPosition,13,QtGui.QTableWidgetItem(''))
        self.newNamesTable.setCellWidget(rowPosition,10,datasrccombo) # DATA_SRC_TYPE_ID field
        self.newNamesTable.setCellWidget(rowPosition,11,shieldcombo) # SHIELD_TYPE_ID field
        self.newNamesTable.setCellWidget(rowPosition,12,shieldsubcombo) # SHIELD_SUBTYPE_ID field
        self.newNamesTable.cellWidget(rowPosition,12).setCurrentIndex(5) # 5 = index for 'Main Route' (DEFAULT)
        self.listening = True

        return

    def delname(self):
        self.listening= False
        self.newNamesTable.removeRow(self.newNamesTable.currentRow())
        self.listening = True
        return


    def addselectednames(self):
        print 'add selected called'
        self.listening = False
        try:
            if self.segList.selectedItems():
                seg = str(self.segList.selectedItems()[0].text())
                names = self.namesref[seg]['names']
                self.clearnewnames()
                typeref = {v: k for k,v in self.domains['TYPE'].iteritems()}
                datasrctyperef = {v: k for k,v in self.domains['DATA_SRC_TYPE_ID'].iteritems()}
                shieldtyperef = {v: k for k,v in self.domains['SHIELD_TYPE_ID'].iteritems()}
                shieldsubtyperef = {v: k for k,v in self.domains['SHIELD_SUBTYPE_ID'].iteritems()}
                rowPosition = self.newNamesTable.rowCount()
                for name in names:
                    self.newNamesTable.insertRow(rowPosition)
                    typecombo = self.createQComboBoxItem_Type('TYPE')
                    typecombo.currentIndexChanged.connect( lambda: self.repainttable() )
                    self.newNamesTable.setCellWidget(rowPosition,0,typecombo) # TYPE field
                    typeindex = self.newNamesTable.cellWidget(rowPosition,0).findText(typeref[name['type']])
                    if typeindex >= 0:
                        self.newNamesTable.cellWidget(rowPosition,0).setCurrentIndex(typeindex)
                    rankitem = QtGui.QTableWidgetItem(self.scrubinput(name['rank']))
                    namefullitem = QtGui.QTableWidgetItem(self.scrubinput(name['namefull']))
                    prediritem = QtGui.QTableWidgetItem(self.scrubinput(name['predir']))
                    pretypeitem = QtGui.QTableWidgetItem(self.scrubinput(name['pretype']))#pretypeitem = QtGui.QTableWidgetItem(str(name['pretype']))
                    premoditem = QtGui.QTableWidgetItem(self.scrubinput(name['premod']))
                    nameitem = QtGui.QTableWidgetItem(self.scrubinput(name['name']))
                    suftypeitem = QtGui.QTableWidgetItem(self.scrubinput(name['suftype']))
                    sufmoditem = QtGui.QTableWidgetItem(self.scrubinput(name['sufmod']))
                    sufdiritem = QtGui.QTableWidgetItem(self.scrubinput(name['sufdir']))
                    shieldnameitem = QtGui.QTableWidgetItem(self.scrubinput(name['shieldname']))
                    self.newNamesTable.setItem(rowPosition,1,rankitem)
                    self.newNamesTable.setItem(rowPosition,2,namefullitem)
                    self.newNamesTable.setItem(rowPosition,3,prediritem)
                    self.newNamesTable.setItem(rowPosition,4,pretypeitem)
                    self.newNamesTable.setItem(rowPosition,5,premoditem)
                    self.newNamesTable.setItem(rowPosition,6,nameitem)
                    self.newNamesTable.setItem(rowPosition,7,suftypeitem)
                    self.newNamesTable.setItem(rowPosition,8,sufmoditem)
                    self.newNamesTable.setItem(rowPosition,9,sufdiritem)
                    self.newNamesTable.setItem(rowPosition,13,shieldnameitem)
                    datasrccombo = self.createQComboBoxItem_Type('DATA_SRC_TYPE_ID')
                    self.newNamesTable.setCellWidget(rowPosition,10,datasrccombo) # TYPE field
                    datasrcindex = self.newNamesTable.cellWidget(rowPosition,10).findText(datasrctyperef[name['datasrctype']])
                    if datasrcindex >= 0:
                        self.newNamesTable.cellWidget(rowPosition,10).setCurrentIndex(datasrcindex)
                    shieldcombo = self.createQComboBoxItem_Type('SHIELD_TYPE_ID')
                    shieldcombo.currentIndexChanged.connect( lambda: self.repainttable() )
                    self.newNamesTable.setCellWidget(rowPosition,11,shieldcombo) # TYPE field
                    shieldindex = self.newNamesTable.cellWidget(rowPosition,11).findText(shieldtyperef[name['shieldtype']])
                    if shieldindex >= 0:
                        self.newNamesTable.cellWidget(rowPosition,11).setCurrentIndex(shieldindex)
                    subshieldcombo = self.createQComboBoxItem_Type('SHIELD_SUBTYPE_ID')
                    subshieldcombo.currentIndexChanged.connect( lambda: self.repainttable() )
                    self.newNamesTable.setCellWidget(rowPosition,12,subshieldcombo) # TYPE field
                    subshieldindex = self.newNamesTable.cellWidget(rowPosition,12).findText(shieldsubtyperef.get(name['shieldsubtype'],''))
                    if subshieldindex == -1:
                        self.newNamesTable.cellWidget(rowPosition,12).setCurrentIndex(5)
                    elif subshieldindex != -1:
                        self.newNamesTable.cellWidget(rowPosition,12).setCurrentIndex(subshieldindex)
                    print typeref[name['type']]
                    if typeref[name['type']] == 'Local':
                        print 'local record!'
                        self.newNamesTable.cellWidget(rowPosition,11).setCurrentIndex(0)
                        self.newNamesTable.cellWidget(rowPosition,11).setDisabled(True)
                        self.newNamesTable.cellWidget(rowPosition,12).setCurrentIndex(5)
                        self.newNamesTable.cellWidget(rowPosition,12).setDisabled(True)
                        self.newNamesTable.item(rowPosition,13).setText('')
                        self.newNamesTable.item(rowPosition,13).setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
                    rowPosition +=1
                self.repainttable()

        except Exception as e:
            pass

        self.listening = True

    def loadsegs(self):
        try:
            self.segList.addItems(self.namesref.keys())
        except:
            pass
        return

    def removeseg(self):
        try:
            for item in self.segList.selectedItems():
                self.segList.takeItem(self.segList.row(item))
        except:
            pass
        return

    def loadnames(self):
        batchnames_path = os.path.join(self.wkSpace, "batchnames.p")
        if os.path.exists(batchnames_path):
            with open(batchnames_path,'rb') as namespick:
                self.namesref = pickle.load(namespick)
                #print self.namesref
        else:
            self.statusBar.setText('Error: Could not find batchnames.p at ' + str(self.wkSpace))
            self.useNamesButton.setEnabled(False)
            self.updateNamesButton.setEnabled(False)
        return

    def scrubinput(self,val):
        if val is None:
            val = ''
        return str(val)

    def scruboutput(self,val):
        if str(val) == '':
            return None
        else:
            return val

    def clearsegnames(self):
        self.segNamesTable.setRowCount(0)

    def clearnewnames(self):
        self.newNamesTable.setRowCount(0)

    def updatesegnames(self,seg):
        self.clearsegnames()
        segguid = str(seg.text())
        rownum = 0
        self.segNamesTable.setRowCount(len(self.namesref[segguid]['names']))
        for i, name in enumerate(self.namesref[segguid]['names']):
            newrow = [name['type'],name['rank'],name['namefull']]
            for j, col in enumerate(newrow):
                item = QtGui.QTableWidgetItem(self.scrubinput(col))
                self.segNamesTable.setItem(i,j,item)


##########################################################################################################################################



def main():
    global wkSpace
    #print "calling comment tool"
    #sys.stdout.write('calling main')
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication

    form = BatchEditNames(wkSpace) # We set the form to be our ExampleApp (design)
    #print "set comment tool form"
    form.show()                         # Show the form
    #print "showed the form"
    sys.exit(app.exec_())                       # and execute the app



if __name__ == '__main__':              # if we're running file directly and not importing it
    import os, sys
    global wkSpace
    #file = "C:/Projects/Parcels/testfile.txt"
    #sys.stdout = open(file, 'w')
    #print 'starting main process'
    wkSpace = sys.argv[1]
    main()                              # run the main function
    #print 'running standalone'