#-------------------------------------------------------------------------------
# Name:         Identify
# Purpose:      module for NJRoadEditor python add-in
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
import ttk
import tkFont, datetime, os, sys

def Identify(Records):
    p=Tk()
    p.minsize(400,400)
    p.geometry("500x800")
    p.title('Identify')
    p.iconbitmap(os.path.join(os.path.dirname(__file__),'gis_logo_stackT.ico'))
    t=ttk.Treeview(p)
    t["columns"]=("first","second")
    ysb = ttk.Scrollbar(p, orient='vertical', command=t.yview)
    t.configure(yscroll=ysb.set)


    t.column("first",width=120)   # anchor='center'
    t.column("second",width=120)

    t.heading("first",text="Field")
    t.heading("second",text="Value")

    # SEGMENT
    position = {'SEGMENT': 0, 'SEG_NAME': 1, 'SEG_SHIELD': 2, 'LINEAR_REF': 3, 'SLD_ROUTE': 4, 'SEGMENT_COMMENTS': 5, 'SEGMENT_TRANS': 6, 'SEGMENT_CHANGE': 7}
    for key,value in Records.iteritems():  # this is the main through the dict
        t.insert("","end", key, text=key)
        for i,v in enumerate(value): # go through
            for vv in v:
                if i in (1,3,5,7,9):
                    t.insert(key, "end", text="", values=(vv[0],vv[1]), tags = ('oddrow',))
                else:
                    t.insert(key, "end", text="", values=(vv[0],vv[1]))
    for key, value in position.iteritems():
        t.move(key,"",value)

    t.tag_configure('oddrow', background='grey')
    t.tag_configure("ttk")


    t.pack(side=LEFT, fill='both', expand=True)
    ysb.pack(side=LEFT, fill='both')
    p.mainloop()

if __name__ == '__main__':
    recs = eval(sys.argv[1])
    if type(recs) is dict:
        Identify(recs)
##    recs = {'SEGMENT_TRANS': [], 'SEGMENT_CHANGE': [], 'SEGMENT_COMMENTS': [], 'SLD_ROUTE': [[(u'OBJECTID', 542936), (u'SRI', u'15000618__'), (u'ROUTE_TYPE_ID', 6), (u'SLD_NAME', u'OCEAN COUNTY 618'), (u'SLD_COMMENT', u'Ocean County-Berkeley and Lacey Ref # 19'), (u'SLD_DIRECTION', u'West to East'), (u'SIGN_NAME', u'VETERANS BLVD'), (u'UPDATE_USER', u'DM_EDIT'), (u'UPDATEDATE', datetime.datetime(2013, 6, 6, 9, 36, 56)), (u'GLOBALID', u'{93FA48EC-12CC-43BC-A290-D3658D69E301}')]], 'LINEAR_REF': [[(u'OBJECTID', 2499985), (u'SEG_ID', 406048), (u'SEG_GUID', u'{123BA874-1708-11E3-B5F2-0062151309FF}'), (u'SRI', u'15000618__'), (u'LRS_TYPE_ID', 3), (u'SEG_TYPE_ID', u'P'), (u'MILEPOST_FR', 3.804), (u'MILEPOST_TO', 6.417), (u'RCF', None), (u'UPDATE_USER', u'DM_EDIT'), (u'UPDATEDATE', datetime.datetime(2013, 6, 6, 9, 36, 47)), (u'GLOBALID', u'{7DD345D8-6812-4674-AA09-EF45FB7D3FD7}')], [(u'OBJECTID', 2131335), (u'SEG_ID', 406048), (u'SEG_GUID', u'{123BA874-1708-11E3-B5F2-0062151309FF}'), (u'SRI', u'15000618__'), (u'LRS_TYPE_ID', 2), (u'SEG_TYPE_ID', u'P'), (u'MILEPOST_FR', 6.417), (u'MILEPOST_TO', 3.804), (u'RCF', None), (u'UPDATE_USER', u'DM_EDIT'), (u'UPDATEDATE', datetime.datetime(2013, 6, 6, 9, 36, 40)), (u'GLOBALID', u'{5F48955C-ADF8-4531-B96D-9A761F77022C}')], [(u'OBJECTID', 1708174), (u'SEG_ID', 406048), (u'SEG_GUID', u'{123BA874-1708-11E3-B5F2-0062151309FF}'), (u'SRI', u'15000618__'), (u'LRS_TYPE_ID', 1), (u'SEG_TYPE_ID', u'P'), (u'MILEPOST_FR', 3.804), (u'MILEPOST_TO', 6.417), (u'RCF', None), (u'UPDATE_USER', u'DM_EDIT'), (u'UPDATEDATE', datetime.datetime(2013, 6, 6, 9, 36)), (u'GLOBALID', u'{4BA30B68-2030-4458-9189-6350CE6C5A30}')]], 'SEG_NAME': [[(u'OBJECTID', 1959960), (u'SEG_ID', 406048), (u'SEG_GUID', u'{123BA874-1708-11E3-B5F2-0062151309FF}'), (u'NAME_TYPE_ID', u'L'), (u'RANK', 1), (u'NAME_FULL', u'Pinewald Keswick Road'), (u'PRE_DIR', None), (u'PRE_TYPE', None), (u'PRE_MOD', None), (u'NAME', u'Pinewald Keswick'), (u'SUF_TYPE', u'Road'), (u'SUF_DIR', None), (u'SUF_MOD', None), (u'DATA_SRC_TYPE_ID', 2), (u'UPDATE_USER', None), (u'UPDATEDATE', datetime.datetime(2012, 7, 27, 9, 41)), (u'GLOBALID', u'{1D5CCE68-A791-49C3-9660-B09CAE5938C2}')], [(u'OBJECTID', 1913714), (u'SEG_ID', 406048), (u'SEG_GUID', u'{123BA874-1708-11E3-B5F2-0062151309FF}'), (u'NAME_TYPE_ID', u'H'), (u'RANK', 1), (u'NAME_FULL', u'County Route 618'), (u'PRE_DIR', None), (u'PRE_TYPE', u'County Route'), (u'PRE_MOD', None), (u'NAME', u'618'), (u'SUF_TYPE', None), (u'SUF_DIR', None), (u'SUF_MOD', None), (u'DATA_SRC_TYPE_ID', 1), (u'UPDATE_USER', None), (u'UPDATEDATE', datetime.datetime(2012, 7, 27, 9, 41)), (u'GLOBALID', u'{4DF887CA-571F-475C-A569-1689FC3BF084}')]], 'SEGMENT': [[(u'OBJECTID', 659567), (u'SEG_ID', 406048), (u'SEG_GUID', u'{123BA874-1708-11E3-B5F2-0062151309FF}'), (u'PRIME_NAME', u'Pinewald Keswick Rd'), (u'ADDR_L_FR', None), (u'ADDR_L_TO', None), (u'ADDR_R_FR', None), (u'ADDR_R_TO', None), (u'ZIPCODE_L', u'08757'), (u'ZIPCODE_R', u'08757'), (u'ZIPNAME_L', u'TOMS RIVER'), (u'ZIPNAME_R', u'TOMS RIVER'), (u'MUNI_ID_L', u'882073'), (u'MUNI_ID_R', u'882073'), (u'ELEV_TYPE_ID_FR', 0), (u'ELEV_TYPE_ID_TO', 0), (u'ACC_TYPE_ID', u'N'), (u'SURF_TYPE_ID', u'I'), (u'STATUS_TYPE_ID', u'A'), (u'SYMBOL_TYPE_ID', 600), (u'TRAVEL_DIR_TYPE_ID', u'B'), (u'JURIS_TYPE_ID', u'PUB'), (u'OIT_REV_TYPE_ID', u'F'), (u'DOT_REV_TYPE_ID', u'F'), (u'UPDATE_USER', u'OAXMITC'), (u'UPDATEDATE', datetime.datetime(2013, 10, 4, 13, 37, 11)), (u'GLOBALID', u'{284125DC-5758-4BCF-8E0C-DC82B5D210D0}'), (u'SHAPE', (564982.5511185463, 392169.0787184376)), (u'SHAPE.STLength()', 13788.737390626895)]], 'SEG_SHIELD': [[(u'OBJECTID', 266499), (u'SEG_ID', 406048), (u'SEG_GUID', u'{123BA874-1708-11E3-B5F2-0062151309FF}'), (u'RANK', 1), (u'SHIELD_TYPE_ID', u'COR'), (u'SHIELD_SUBTYPE_ID', u'M'), (u'SHIELD_NAME', u'618'), (u'DATA_SRC_TYPE_ID', 1), (u'UPDATE_USER', None), (u'UPDATEDATE', datetime.datetime(2012, 7, 27, 9, 41, 59)), (u'GLOBALID', u'{22780177-92A3-463B-BFB1-132B40063CE6}')]]}
##    Identify(recs)

