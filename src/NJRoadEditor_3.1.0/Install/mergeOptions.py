#-------------------------------------------------------------------------------
# Name:         mergeOptions.py
# Purpose:      Ask the user who they are
#
# Author:       NJ Office of GIS
# Contact:      njgin@oit.nj.gov
#
# Created:      8/6/2015
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
import tkFont
import ttk as tk
import os
class MergeOptions(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        #self.pack()

        # Fonts
        heads = tkFont.Font(name='heads', size=16)
        body = tkFont.Font(name='body', size=10)


        # Label(self.parent, wraplength = 350, font = 'heads', bg = 'white', text="Merge").pack()
        Label(self.parent, wraplength = 350, font = 'body', bg = 'white', text="\nRun the merge tool. "
                                                                               "Both original "
                                                                               "segments are "
                                                                 "moved to SEGMENT_CHANGE. The target segment "
                                                                 "will retain all of it's attributes and "
                                                                 "relationships with other tables. "
                                                                 "A new SEG_GUID is assigned after the merge is "
                                                                 "complete."
                                                                 "").grid(row=0, sticky='ew', padx=25)

        Button(self.parent, text='Merge', font = 'heads', relief=GROOVE, bg = 'light sky blue',
               command=self.merge).grid(row=1,padx=25, pady=10)
        tk.Separator(self.parent, orient=HORIZONTAL).grid(row=2, sticky='ew', padx=25)

        Label(self.parent, wraplength = 350, font = 'body', bg = 'white', text="\nRun the merge tool in cleanup mode. This will not assign a new SEG_GUID to the target segment, or move the original segments to SEGMENT_CHANGE. The attributes/relationships of the target segment are retained."
                                                         "").grid(row=3, sticky='ew', padx=25)

        Button(self.parent, text='Cleanup Merge', relief=GROOVE, command=self.cleanup).grid(row=4,padx=25, pady=10)
        # Button(self.parent, text='Cancel', command=self.cancel).pack()

        # Button(self, text='Merge', command=self.merge).pack(side=LEFT, fill=X,padx=5,pady=10)
        # Button(self, text='Cleanup Merge', command=self.cleanup).pack(side=LEFT, fill=X,padx=5,pady=10)
        # Button(self, text='Cancel', command=self.cancel).pack(side=LEFT,fill=X,padx=5,pady=10)

    def onPress(self):
        pass
        #pick = self.var.get()
        #print('you pressed', pick)

    def merge(self):
        sys.stdout.write('Merge***')
        self.parent.destroy()

    def cleanup(self):
        sys.stdout.write('Cleanup***')
        self.parent.destroy()

    def cancel(self):
        sys.stdout.write('Cancel***')
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("Merge Road Segments")
    root.iconbitmap(os.path.join(os.path.dirname(__file__),'gis_logo_stackT.ico'))
    root.configure(background = 'white')
    merge_ui = MergeOptions(root)
    root.mainloop()
