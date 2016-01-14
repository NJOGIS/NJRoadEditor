#-------------------------------------------------------------------------------
# Name:         userRadio.py
# Purpose:      Ask the user who they are
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
import os
class Demo(Frame):
    def __init__(self, parent=None, choices=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        Label(self, text="Please Select Who You Are\n").pack(side=TOP)
        self.var = StringVar()
        for who in choices:
            Radiobutton(self, text=who, command=self.onPress, variable=self.var, value=who).pack(anchor=NW)  #
        self.var.set(choices[0]) # select last to start
        Button(self, text='OK', command=self.ok).pack(side=LEFT, fill=X,padx=5,pady=10)
        Button(self, text='Cancel', command=self.cancel).pack(side=LEFT,fill=X,padx=5,pady=10)

    def onPress(self):
        pass
        #pick = self.var.get()
        #print('you pressed', pick)

    def ok(self):
        user = self.var.get()
        sys.stdout.write('OK***' + user)
        self.parent.destroy()

    def cancel(self):
        sys.stdout.write('Cancel***')
        self.parent.destroy()

if __name__ == '__main__':
    choices = ['NJ OIT', 'NJ DOT', 'County', 'Other']
    root = Tk()
    root.geometry("200x200")
    root.title("User")
    root.iconbitmap(os.path.join(os.path.dirname(__file__),'gis_logo_stackT.ico'))
    radio = Demo(root, choices)
    root.mainloop()