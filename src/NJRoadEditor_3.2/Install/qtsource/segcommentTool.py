from PyQt4 import QtCore, QtGui
import sys # socket, subprocess # We need sys so that we can pass argv to QApplication
import os
import pickle
import segcommentUI




class CommentTool(QtGui.QDialog, segcommentUI.Ui_Comment):
    def __init__(self, workSpace, parent=None):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        #global entityMods, entity, entityOld
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.segmentcomments = {}
        self.wkSpace = workSpace.replace("'","")
        self.setWindowTitle("Add Comments")
        self.load_comments()
        self.completeDate.setDate(QtCore.QDate.currentDate())
        # Events
        self.cancelButton.clicked.connect(self.reject)
        self.updateButton.clicked.connect(self.submitclose)
        self.newcommentButton.clicked.connect(self.add_newcomment)
        self.delButton.clicked.connect(self.del_comment)
        self.completeCheck.clicked.connect(self.check_date)
        self.sessionLog = []




    def check_date(self):
        self.completeDate.setEnabled(self.completeCheck.isChecked())

    def load_comments(self):
        comments_path = os.path.join(self.wkSpace, "segcommentlist.p")
        if os.path.exists(comments_path):
            with open(comments_path,'rb') as commentspick:
                self.segmentcomments = pickle.load(commentspick)
        else:
            self.statusBar.setText('Error: Could not find segcommentlist.p at ' + str(comments_path))
            self.disable_comments()
        return

    def disable_comments(self):
        self.newcommentButton.setEnabled(False)
        self.delButton.setEnabled(False)
        self.updateButton.setEnabled(False)

    def smart_concat(self,*args):
        newconcat = ' '.join([str(x) for x in args if x not in [None,' ','','None']])
        return newconcat

    def add_newcomment(self):
        edittype = unicode(self.edittypeBox.currentText())
        editcat = unicode(self.editcategoryBox.currentText())
        editcomment = self.commentText.toPlainText()

        newcomment = self.smart_concat(edittype,editcat,editcomment)
        self.commentList.addItems([newcomment])
        self.commentList.repaint()
        print 'OK'
        return

    def del_comment(self):
        self.commentList.takeItem(self.commentList.row(self.commentList.currentItem()))

    def submitclose(self):
        newcommentlist = [str(self.commentList.item(i).text()) for i in range(self.commentList.count())]

        if len(newcommentlist) > 0:
            newcommentpickle = self.segmentcomments
            newcommentpickle['comments'] = newcommentlist
            if self.completeCheck.isChecked():
                finaldate = self.completeDate.date().toPyDate()
                newcommentpickle['finaldate'] = finaldate
            elif self.completeCheck.isChecked() == False:
                newcommentpickle['finaldate'] = None

            comments_path = os.path.join(self.wkSpace, "segcommentlist.p")
            if os.path.exists(comments_path):
                os.remove(comments_path)
            try:
                with open(comments_path, 'wb') as output:
                    pickle.dump(newcommentpickle, output, -1)
                sys.stdout.write("OK")
                sys.stdout.flush()
                self.close()
            except Exception, e:
                self.statusBar.setText('Error: Could not save comments to file')

        elif len(newcommentlist) == 0:
            # If no new comments, tell the user
            self.statusBar.setText('No new comments have been added. Please add a comment')





def main():
    global wkSpace

    #print "calling comment tool"
    #sys.stdout.write('calling main')
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication

    form = CommentTool(wkSpace) # We set the form to be our ExampleApp (design)
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
