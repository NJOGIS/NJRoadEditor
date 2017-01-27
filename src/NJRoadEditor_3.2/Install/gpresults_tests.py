#-------------------------------------------------------------------------------
# Name:         gpresults_tests.py
#
# Author:       NJ Office of GIS
# Contact:      njgin@oit.nj.gov
#
# Created:      9/22/2014
# Copyright:    (c) NJ Office of GIS 2015
# Licence:      GPLv3
#-------------------------------------------------------------------------------

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  It can be found in the ~Install\GPLv3_License.txt
# If not, see <http://www.gnu.org/licenses/>.

#-------------------------------------------------------------------------------

from Tkinter import *
import os, re

class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                 # make me expandable
        self.makewidgets()
        self.settext(text, file)

    def makewidgets(self):
        sbar = Scrollbar(self)
        #xsbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)

        sbar.pack(side=RIGHT, fill=Y)                    # pack first=clip last
        #xsbar.pack(side=BOTTOM, fill=X)                    # pack first=clip last
        text.pack(side=TOP, expand=YES, fill=BOTH)      # text clipped first

        sbar.config(command=text.yview)                  # xlink sbar and text
        #xsbar.config(command=text.xview, orient=HORIZONTAL)
        text.config(yscrollcommand=sbar.set)             # move one moves other
        #text.config(xscrollcommand=xsbar.set)             # move one moves other

        self.text = text

    def settext(self, text='', file=None):
        if file:
            #text = open(file, 'r').read()
            textfile = open(file, 'r')
            text = textfile.read()
            textfile.close()
            self.text.delete('1.0', END)
            textfile = open(file, 'r')
            cc = float(1)
            for textline in textfile.readlines():
                print cc, textline
                warn = re.search(r'WARNING', textline)
                err = re.search(r'ERROR', textline)
                self.text.insert(END, textline)
                print(str(cc) + '000')
                if warn:
                    self.text.tag_add('green', str(cc), str(int(cc)) + '.1000')
                    self.text.tag_config('green', foreground='medium sea green')
                elif err:
                    self.text.tag_add('red', str(cc), str(int(cc)) + '.1000')
                    self.text.tag_config('red', foreground='red')

                cc += 1
            textfile.close()

        #self.text.delete('1.0', END)                     # delete current text
        #self.text.insert('1.0', text)                    # add at line 1, col 0
        #self.text.tag_add('green', '2.0', '2.1000')
        #self.text.tag_config('green', foreground='medium sea green')
        #self.text.mark_set(INSERT, '1.0')                # set insert cursor
        self.text.focus()                                # save user a click
        self.text.configure(state=DISABLED)

    def gettext(self):                                   # returns a string
        return self.text.get('1.0', END+'-1c')           # first through last

if __name__ == '__main__':
    root = Tk()
    root.geometry("1000x300")
    root.title("Geoprocessing Results")
    root.iconbitmap(os.path.join(os.path.dirname(__file__),'gis_logo_stack.ico'))

    #logfile = sys.argv[1]

    logfile = os.path.join(r'C:\Users\oaxfarr\Documents\ArcGIS\Default.gdb\SegmentGeoprocessing.log')
    st = ScrolledText(file=logfile)
    def show(event):
        print(repr(st.gettext()))                        # show as raw string
    root.bind('<Key-Escape>', show)                      # esc = dump text
    root.mainloop()
