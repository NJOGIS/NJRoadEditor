#-------------------------------------------------------------------------------
# Name:         EditSegment.py
#
# Author:       NJ Office of GIS
# Contact:      njgin@oit.nj.gov
#
# Created:      12/15/2014
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

import Tkinter as Tk
import ttk as tk
import os, sys, pickle, traceback, datetime, socket, logging
from ToolTip import ToolTip
import tkMessageBox as Tkm
os.sys.path.append(os.path.dirname(__file__))
import erebus

class SegmentCanvas(Tk.Canvas):
    def __init__(self, parent=None, SegmentNumber = None, scratchPath = None, FpSegment = None, Domains = None, USER = None):
        Tk.Canvas.__init__(self, parent)

        import os, logging, traceback, re
        #####################################
        #LOGGER
        self.logger = logging.getLogger('TkUI')
        self.logger.setLevel(logging.DEBUG)

        # create a file handler
        filehandlerpath = os.path.join(scratchPath, 'TkUI.log')
##        if os.path.exists(filehandlerpath):
##            os.remove(filehandlerpath)
        self.handler = logging.FileHandler(filehandlerpath)
        self.handler.setLevel(logging.DEBUG)

        # create a logging format
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

        self.logger.info('SegmentCanvas Class Called...')




        ########################################################################
        ########################################################################
        ##### Initial setup
        ########################################################################

        try:
            import os, sys, pickle, traceback

            self.Fp = FpSegment
            self.message_dict = {'addrlfr': {'error': False, 'value': False}, 'addrlto': {'error': False, 'value': False}, 'addrrfr': {'error': False, 'value': False}, 'addrrto': {'error': False, 'value': False}, 'zipcodeL': {'error': False, 'value': False}, 'zipcodeR': {'error': False, 'value': False}, 'zipnameL': {'error': False, 'value': False}, 'zipnameR': {'error': False, 'value': False}, 'muniidL': {'error': False, 'value': False}, 'muniidR': {'error': False, 'value': False}, 'elevfr': {'error': False, 'value': False}, 'elevto': {'error': False, 'value': False}, 'acctype':{'error': False, 'value': False}, 'surftype': {'error': False, 'value': False}, 'stattype': {'error': False, 'value': False}, 'symbtype': {'error': False, 'value': False}, 'travtype': {'error': False, 'value': False}, 'juristype': {'error': False, 'value': False}, 'oitrevtype': {'error': False, 'value': False}, 'dotrevtype': {'error': False, 'value': False}}

            self.error_image = Tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),'error20.gif'))  # os.path.join(os.path.dirname(__file__),'error20.gif')
            self.trans_image = Tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),'trans20.gif'))
            self.warn_image = Tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),'warn20.gif'))
            self.greenbar_image = Tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),'greenbar20.gif'))

            #Domains = {u'TRAVEL_DIR_TYPE': {u'I': u'Increasing', u'B': u'Both', u'D': u'Decreasing'}, u'SURFACE_TYPE': {u'I': u'Improved', u'UNK': u'Unknown', u'U': u'Unimproved'}, u'SEGMENT_TYPE': {u'P': u'Primary', u'S': u'Secondary', u'E': u'Express', u'AD': u'Acceleration/Deceleration', u'ES': u'Express Secondary'}, u'Munic_arc_Vertex_Rules': {2: u'Rule_2', -1: u'Free Representation'}, u'CHANGE_TYPE': {u'R': u'Removed', u'M': u'Modified'}, u'SHIELD_SUBTYPE': {u'A': u'Alternate Route', u'C': u'Connector Route', u'B': u'Business Route', u'E': u'Express Route', u'M': u'Main Route', u'S': u'Spur Route', u'T': u'Truck Route', u'Y': u'Bypass Route'}, u'ROUTE_TYPE': {1: u'Interstate', 2: u'US Route', 3: u'State Route', 4: u'Highway Authority Route', 5: u'500 Series Route', 6: u'Other County Route', 7: u'Local Road', 8: u'Ramp', 9: u'Alley', 10: u'Park / Military'}, u'LRS_TYPE': {1: u'NJDOT Multi-Centerline', 2: u'NJDOT Parent', 3: u'NJDOT Flipped', 4: u'MMS Milepost Markers', 5: u'NJTA'}, u'JURIS_TYPE': {u'UNK': u'Unknown', u'PRI': u'Private', u'PUB': u'Public'}, u'SHIELD_TYPE': {u'GSP': u'Garden State Parkway', u'COR': u'County Route', u'ACE': u'Atlantic City Expressway', u'ACB': u'Atlantic City Brigantine Connector', u'INT': u'Interstate', u'TPK': u'NJ Turnpike', u'USR': u'US Route', u'STR': u'State Route', u'PIP': u'Palisades Parkway'}, u'ACCESS_TYPE': {u'UNK': u'Unknown', u'R': u'Restricted', u'N': u'Non-Restricted'}, u'DATA_SOURCE_TYPE': {1: u'NJDOT SLD', 2: u'Tiger', 3: u'County', 4: u'MOD IV', 5: u'Other', 6: u'NJOIT', 7: u'TAXMAP'}, u'PCODE_TYPE': {u'NLP': u'NLP', u'ART': u'ART', u'PD': u'PD', u'CRT': u'CRT', u'NNP': u'NNP'}, u'ELEV_TYPE': {0: u'At Grade', 1: u'Level 1', 2: u'Level 2', 3: u'Level 3'}, u'GNIS_NAME': {u'885309': u'Town of Morristown, Morris', u'885430': u'Borough of Wallington, Bergen', u'885431': u'Borough of Wanaque, Passaic', u'1729722': u'Township of Fairfield, Essex', u'885433': u'Borough of Watchung, Somerset', u'885434': u'Borough of Wenonah, Gloucester', u'885435': u'Borough of West Cape May, Cape May', u'885436': u'Town of Westfield, Union', u'885437': u'Borough of West Long Branch, Monmouth', u'885438': u'Town of West New York, Hudson', u'885439': u'Borough of Woodland Park, Passaic', u'882250': u'Township of Washington, Warren', u'882130': u'Township of Quinton, Salem', u'885298': u'Borough of Metuchen, Middlesex', u'885299': u'Borough of Middlesex, Middlesex', u'885294': u'Borough of Maywood, Bergen', u'885295': u'Borough of Medford Lakes, Burlington', u'885296': u'Borough of Mendham, Morris', u'885297': u'Borough of Merchantville, Camden', u'885290': u'Borough of Mantoloking, Ocean', u'885291': u'Borough of Manville, Somerset', u'885292': u'City of Margate City, Atlantic', u'885293': u'Borough of Matawan, Monmouth', u'882210': u'Township of Jefferson, Morris', u'882309': u'Township of Wyckoff, Bergen', u'882308': u'Township of Saddle Brook, Bergen', u'882307': u'Township of Rochelle Park, Bergen', u'882118': u'Township of Marlboro, Monmouth', u'882119': u'Township of Holmdel, Monmouth', u'882112': u'Township of Wall, Monmouth', u'882113': u'Township of Howell, Monmouth', u'882110': u'Township of Bordentown, Burlington', u'882111': u'Township of Neptune, Monmouth', u'882116': u'Township of Freehold, Monmouth', u'882117': u'Township of Manalapan, Monmouth', u'882114': u'Township of Upper Freehold, Monmouth', u'882115': u'Township of Millstone, Monmouth', u'885203': u'Borough of Edgewater, Bergen', u'885202': u'Borough of Eatontown, Monmouth', u'885201': u'Borough of East Rutherford, Bergen', u'885200': u'City of East Orange, Essex', u'885207': u'Borough of Elmwood Park, Bergen', u'885206': u'Borough of Elmer, Salem', u'885205': u'City of Elizabeth, Union', u'885204': u'City of Egg Harbor City, Atlantic', u'885209': u'City of Englewood, Bergen', u'885208': u'Borough of Emerson, Bergen', u'885289': u'Borough of Manasquan, Monmouth', u'885161': u'Borough of Bloomingdale, Passaic', u'885165': u'City of Bordentown, Burlington', u'885168': u'Borough of Branchville, Sussex', u'885280': u'City of Linwood, Atlantic', u'885432': u'Borough of Washington, Warren', u'882053': u'Township of Mullica, Atlantic', u'882052': u'Township of Galloway, Atlantic', u'885274': u'Borough of Lawnside, Camden', u'882050': u'Township of Weymouth, Atlantic', u'885272': u'Borough of Laurel Springs, Camden', u'882056': u'Township of Hopewell, Cumberland', u'882055': u'Township of Upper Deerfield, Cumberland', u'885378': u'Borough of Roseland, Essex', u'885377': u'Borough of Roosevelt, Monmouth', u'885376': u'Borough of Rocky Hill, Somerset', u'885375': u'Borough of Rockleigh, Bergen', u'882058': u'Township of Greenwich, Cumberland', u'885373': u'Borough of Riverton, Burlington', u'885372': u'Borough of River Edge, Bergen', u'885371': u'Borough of Riverdale, Morris', u'885279': u'Borough of Lindenwold, Camden', u'2381010': u'Borough of Caldwell, Essex', u'882170': u'Township of Franklin, Somerset', u'880741': u'Township of South Orange Village, Essex', u'882171': u'Township of Bridgewater, Somerset', u'885159': u'Borough of Bernardsville, Somerset', u'885158': u'Borough of Berlin, Camden', u'885153': u'Borough of Beachwood, Ocean', u'885152': u'Borough of Beach Haven, Ocean', u'885151': u'City of Bayonne, Hudson', u'885150': u'Borough of Bay Head, Ocean', u'885157': u'Borough of Bergenfield, Bergen', u'885156': u'Town of Belvidere, Warren', u'885155': u'Borough of Belmar, Monmouth', u'885154': u'Borough of Bellmawr, Camden', u'882044': u'Township of Lower, Cape May', u'885448': u'Borough of Woodbury Heights, Gloucester', u'885362': u'Borough of Prospect Park, Passaic', u'882071': u'Township of Ocean, Ocean', u'885363': u'City of Rahway, Union', u'882070': u'Township of Barnegat, Ocean', u'885365': u'Borough of Raritan, Somerset', u'1723212': u'Township of Upper Pittsgrove, Salem', u'882248': u'Township of Harmony, Warren', u'882249': u'Township of Mansfield, Warren', u'882246': u'Township of White, Warren', u'882247': u'Township of Oxford, Warren', u'882244': u'Township of Independence, Warren', u'882245': u'Township of Liberty, Warren', u'882242': u'Township of Hope, Warren', u'882243': u'Township of Allamuchy, Warren', u'882240': u'Township of Frelinghuysen, Warren', u'882241': u'Township of Knowlton, Warren', u'885368': u'Village of Ridgefield Park, Bergen', u'885440': u'Borough of Westville, Gloucester', u'885445': u'Borough of Wildwood Crest, Cape May', u'885444': u'City of Wildwood, Cape May', u'882239': u'Township of Hardwick, Warren', u'882145': u'Township of South Harrison, Gloucester', u'882144': u'Township of Woolwich, Gloucester', u'882147': u'Township of Mantua, Gloucester', u'882146': u'Township of Harrison, Gloucester', u'882141': u'Township of East Greenwich, Gloucester', u'882140': u'Township of Washington, Gloucester', u'882143': u'Township of Logan, Gloucester', u'882142': u'Township of Greenwich, Gloucester', u'882062': u'Township of Commercial, Cumberland', u'882063': u'Township of Maurice River, Cumberland', u'882060': u'Township of Lawrence, Cumberland', u'882061': u'Township of Downe, Cumberland', u'882149': u'Township of Deptford, Gloucester', u'882148': u'Township of West Deptford, Gloucester', u'882064': u'Township of Elsinboro, Salem', u'882065': u'Township of Lower Alloways Creek, Salem', u'878839': u'Borough of North Caldwell, Essex', u'882097': u'Township of Delran, Burlington', u'882096': u'Township of Cinnaminson, Burlington', u'882095': u'Township of Moorestown, Burlington', u'885330': u'Borough of Oakland, Bergen', u'885337': u'Borough of Oradell, Bergen', u'885336': u'Borough of Old Tappan, Bergen', u'882091': u'Township of Lumberton, Burlington', u'882090': u'Township of Southampton, Burlington', u'885339': u'Borough of Palmyra, Burlington', u'885338': u'Borough of Palisades Park, Bergen', u'882136': u'Township of Oldmans, Salem', u'882099': u'Township of Willingboro, Burlington', u'882098': u'Township of Riverside, Burlington', u'885238': u'Borough of Haddonfield, Camden', u'882137': u'Township of Monroe, Gloucester', u'885232': u'Borough of Glen Gardner, Hunterdon', u'885233': u'Borough of Glen Rock, Bergen', u'885230': u'Borough of Gibbsboro, Camden', u'885231': u'Borough of Glassboro, Gloucester', u'885236': u'City of Hackensack, Bergen', u'885237': u'Town of Hackettstown, Warren', u'885234': u'City of Gloucester City, Camden', u'885235': u'Town of Guttenberg, Hudson', u'882132': u'Township of Pilesgrove, Salem', u'882133': u'Township of Mannington, Salem', u'885311': u'Borough of Mountainside, Union', u'885259': u'Borough of Hopatcong, Sussex', u'885315': u'Borough of Neptune City, Monmouth', u'882139': u'Township of Elk, Gloucester', u'885346': u'Borough of Pemberton, Burlington', u'885347': u'Borough of Pennington, Mercer', u'885344': u'Borough of Paulsboro, Gloucester', u'885345': u'Borough of Peapack and Gladstone, Somerset', u'885342': u'City of Passaic, Passaic', u'885343': u'City of Paterson, Passaic', u'885429': u'Borough of Waldwick, Bergen', u'885341': u'Borough of Park Ridge, Bergen', u'885427': u'Borough of Victory Gardens, Morris', u'885426': u'City of Ventnor City, Atlantic', u'885425': u'Borough of Upper Saddle River, Bergen', u'885424': u'City of Union City, Hudson', u'885423': u'Borough of Union Beach, Monmouth', u'885422': u'Borough of Tuckerton, Ocean', u'885421': u'City of Trenton, Mercer', u'885349': u'City of Perth Amboy, Middlesex', u'885229': u'Borough of Garwood, Union', u'885181': u'Borough of Carteret, Middlesex', u'885420': u'Borough of Totowa, Passaic', u'1729742': u'Township of City of Orange, Essex', u'885162': u'Borough of Bloomsbury, Hunterdon', u'885163': u'Borough of Bogota, Bergen', u'885160': u'City of Beverly, Burlington', u'885288': u'Borough of Magnolia, Camden', u'885166': u'Borough of Bound Brook, Somerset', u'885167': u'Borough of Bradley Beach, Monmouth', u'885164': u'Town of Boonton, Morris', u'885220': u'Borough of Flemington, Hunterdon', u'885283': u'Village of Loch Arbour, Monmouth', u'885282': u'Borough of Little Silver, Monmouth', u'885281': u'Borough of Little Ferry, Bergen', u'885169': u'City of Bridgeton, Cumberland', u'885287': u'Borough of Madison, Morris', u'885286': u'Borough of Longport, Atlantic', u'885285': u'City of Long Branch, Monmouth', u'885284': u'Borough of Lodi, Bergen', u'885379': u'Borough of Roselle, Union', u'882109': u'Township of Chesterfield, Burlington', u'882108': u'Township of Mansfield, Burlington', u'882101': u'Township of Edgewater Park, Burlington', u'882100': u'Township of Delanco, Burlington', u'882103': u'Township of Westampton, Burlington', u'882102': u'Township of Burlington, Burlington', u'882105': u'Township of Eastampton, Burlington', u'882104': u'Township of Mount Holly, Burlington', u'882107': u'Township of Florence, Burlington', u'882106': u'Township of Springfield, Burlington', u'882192': u'Township of East Hanover, Morris', u'882193': u'Township of Morris, Morris', u'882190': u'Township of Tewksbury, Hunterdon', u'882191': u'Township of Lebanon, Hunterdon', u'882196': u'Township of Long Hill, Morris', u'882197': u'Township of Mount Olive, Morris', u'882194': u'Township of Chatham, Morris', u'882195': u'Township of Harding, Morris', u'882198': u'Township of Washington, Morris', u'882199': u'Township of Chester, Morris', u'882202': u'Township of Mine Hill, Morris', u'882203': u'Township of Roxbury, Morris', u'882200': u'Township of Mendham, Morris', u'882201': u'Township of Randolph, Morris', u'882206': u'Township of Parsippany-Troy Hills, Morris', u'882207': u'Township of Montville, Morris', u'882204': u'Township of Denville, Morris', u'882205': u'Township of Boonton, Morris', u'882208': u'Township of Pequannock, Morris', u'882209': u'Township of Rockaway, Morris', u'885265': u'Borough of Keansburg, Monmouth', u'885264': u'City of Jersey City, Hudson', u'885308': u'Borough of Morris Plains, Morris', u'885266': u'Town of Kearny, Hudson', u'885261': u'Borough of Interlaken, Monmouth', u'885260': u'Borough of Hopewell, Mercer', u'885263': u'Borough of Jamesburg, Middlesex', u'885262': u'Borough of Island Heights, Ocean', u'885302': u'Borough of Millstone, Somerset', u'885303': u'Borough of Milltown, Middlesex', u'885300': u'Borough of Midland Park, Bergen', u'885301': u'Borough of Milford, Hunterdon', u'885306': u'Borough of Montvale, Bergen', u'885268': u'Borough of Keyport, Monmouth', u'885304': u'City of Millville, Cumberland', u'885305': u'Borough of Monmouth Beach, Monmouth', u'885271': u'City of Lambertville, Hunterdon', u'2743608': u'Princeton, Mercer', u'885416': u'Borough of Tavistock, Camden', u'885417': u'Borough of Tenafly, Bergen', u'885414': u'Borough of Sussex, Sussex', u'885415': u'Borough of Swedesboro, Gloucester', u'885412': u'City of Summit, Union', u'885413': u'Borough of Surf City, Ocean', u'885410': u'Borough of Stone Harbor, Cape May', u'885411': u'Borough of Stratford, Camden', u'885418': u'Borough of Teterboro, Bergen', u'885419': u'Borough of Tinton Falls, Monmouth', u'1729716': u'Township of Verona, Essex', u'1729717': u'Township of West Caldwell, Essex', u'1729714': u'Township of Bloomfield, Essex', u'1729715': u'Township of Nutley, Essex', u'1729713': u'Township of Belleville, Essex', u'1729718': u'Township of West Orange, Essex', u'882259': u'Township of Walpack, Sussex', u'882258': u'Township of Vernon, Sussex', u'882255': u'Township of Sandyston, Sussex', u'882254': u'Township of Pohatcong, Warren', u'882257': u'Township of Wantage, Sussex', u'882256': u'Township of Montague, Sussex', u'882251': u'Township of Franklin, Warren', u'882068': u'Township of Eagleswood, Ocean', u'882253': u'Township of Greenwich, Warren', u'882252': u'Township of Lopatcong, Warren', u'882069': u'Township of Stafford, Ocean', u'885139': u'Borough of Alpine, Bergen', u'885138': u'Borough of Alpha, Warren', u'885135': u'Borough of Allendale, Bergen', u'885134': u'City of Absecon, Atlantic', u'885137': u'Borough of Allentown, Monmouth', u'885136': u'Borough of Allenhurst, Monmouth', u'885141': u'City of Asbury Park, Monmouth', u'882079': u'Township of Jackson, Ocean', u'882078': u'Township of Plumsted, Ocean', u'882172': u'Township of Green Brook, Somerset', u'882173': u'Township of Warren, Somerset', u'882174': u'Township of Bernards, Somerset', u'882175': u'Township of Branchburg, Somerset', u'882176': u'Township of Bedminster, Somerset', u'882177': u'Township of Clinton, Hunterdon', u'882178': u'Township of Readington, Hunterdon', u'882179': u'Township of Raritan, Hunterdon', u'882073': u'Township of Berkeley, Ocean', u'882072': u'Township of Lacey, Ocean', u'882075': u'Township of Brick, Ocean', u'882074': u'Township of Toms River, Ocean', u'882077': u'Township of Manchester, Ocean', u'882076': u'Township of Lakewood, Ocean', u'882082': u'Township of Evesham, Burlington', u'885180': u'Borough of Carlstadt, Bergen', u'885228': u'City of Garfield, Bergen', u'885182': u'Borough of Chatham, Morris', u'885183': u'Borough of Chesilhurst, Camden', u'885184': u'Borough of Chester, Morris', u'885185': u'Borough of Clayton, Gloucester', u'885186': u'Borough of Clementon, Camden', u'885187': u'Borough of Cliffside Park, Bergen', u'885221': u'Borough of Florham Park, Morris', u'885189': u'Town of Clinton, Hunterdon', u'885223': u'Borough of Fort Lee, Bergen', u'885222': u'Borough of Folsom, Atlantic', u'885225': u'Borough of Franklin Lakes, Bergen', u'885224': u'Borough of Franklin, Sussex', u'885227': u'Borough of Frenchtown, Hunterdon', u'885226': u'Borough of Freehold, Monmouth', u'885360': u'City of Port Republic, Atlantic', u'885267': u'Borough of Kenilworth, Union', u'885244': u'Borough of Harrington Park, Bergen', u'885355': u'City of Plainfield, Union', u'885354': u'Borough of Pitman, Gloucester', u'885357': u'Borough of Point Pleasant, Ocean', u'885356': u'City of Pleasantville, Atlantic', u'885351': u'Borough of Pine Beach, Ocean', u'885350': u'Town of Phillipsburg, Warren', u'885353': u'Borough of Pine Valley, Camden', u'885352': u'Borough of Pine Hill, Camden', u'885452': u'Borough of Woodstown, Salem', u'885453': u'Borough of Wrightstown, Burlington', u'885450': u'Borough of Woodlynne, Camden', u'885451': u'Borough of Wood-Ridge, Bergen', u'885359': u'Borough of Pompton Lakes, Passaic', u'885358': u'Borough of Point Pleasant Beach, Ocean', u'885333': u'Borough of Ocean Gate, Ocean', u'885332': u'City of Ocean City, Cape May', u'1729723': u'Township of Pittsgrove, Salem', u'885331': u'Borough of Oaklyn, Camden', u'1729720': u'Township of Montclair, Essex', u'882604': u'Township of Middletown, Monmouth', u'882094': u'Township of Maple Shade, Burlington', u'882602': u'Township of Colts Neck, Monmouth', u'882603': u'Township of Shrewsbury, Monmouth', u'882601': u'Township of Ocean, Monmouth', u'882093': u'Township of Mount Laurel, Burlington', u'882092': u'Township of Hainesport, Burlington', u'885335': u'Borough of Ogdensburg, Sussex', u'885269': u'Borough of Kinnelon, Morris', u'885334': u'Borough of Oceanport, Monmouth', u'885188': u'City of Clifton, Passaic', u'885307': u'Borough of Moonachie, Bergen', u'885241': u'Borough of Hamburg, Sussex', u'885171': u'City of Brigantine, Atlantic', u'885170': u'Borough of Brielle, Monmouth', u'885173': u'Borough of Buena, Atlantic', u'885172': u'Borough of Brooklawn, Camden', u'885175': u'Borough of Butler, Morris', u'885174': u'City of Burlington, Burlington', u'885177': u'City of Camden, Camden', u'885176': u'Borough of Califon, Hunterdon', u'885179': u'Borough of Cape May Point, Cape May', u'885178': u'City of Cape May, Cape May', u'885240': u'Borough of Haledon, Passaic', u'885239': u'Borough of Haddon Heights, Camden', u'885382': u'Borough of Runnemede, Camden', u'885383': u'Borough of Rutherford, Bergen', u'885380': u'Borough of Roselle Park, Union', u'885381': u'Borough of Rumson, Monmouth', u'885386': u'Borough of Sayreville, Middlesex', u'885387': u'Borough of Sea Bright, Monmouth', u'885384': u'Borough of Saddle River, Bergen', u'885385': u'City of Salem, Salem', u'885388': u'Borough of Sea Girt, Monmouth', u'885389': u'City of Sea Isle City, Cape May', u'882181': u'Township of West Amwell, Hunterdon', u'882180': u'Township of East Amwell, Hunterdon', u'882183': u'Township of Kingwood, Hunterdon', u'882182': u'Township of Delaware, Hunterdon', u'882185': u'Township of Holland, Hunterdon', u'882184': u'Township of Franklin, Hunterdon', u'882187': u'Township of Hanover, Morris', u'882186': u'Township of Alexandria, Hunterdon', u'882189': u'Township of Bethlehem, Hunterdon', u'882188': u'Township of Union, Hunterdon', u'882211': u'Township of Hillside, Union', u'885318': u'City of New Brunswick, Middlesex', u'882213': u'Township of Springfield, Union', u'882212': u'Township of Union, Union', u'882215': u'Township of Winfield, Union', u'882214': u'Township of Cranford, Union', u'882217': u'Township of Scotch Plains, Union', u'882216': u'Township of Clark, Union', u'882219': u'Township of Livingston, Essex', u'882218': u'Township of Berkeley Heights, Union', u'885319': u'Borough of Newfield, Gloucester', u'885251': u'Borough of High Bridge, Hunterdon', u'885252': u'Borough of Highland Park, Middlesex', u'885253': u'Borough of Highlands, Monmouth', u'885254': u'Borough of Hightstown, Mercer', u'885255': u'Borough of Hillsdale, Bergen', u'885256': u'Borough of Hi-Nella, Camden', u'885257': u'City of Hoboken, Hudson', u'885258': u'Borough of Ho-Ho-Kus, Bergen', u'885310': u'Borough of Mountain Lakes, Morris', u'885313': u'Borough of Mount Ephraim, Camden', u'885312': u'Borough of Mount Arlington, Morris', u'882138': u'Township of Franklin, Gloucester', u'885314': u'Borough of National Park, Gloucester', u'885317': u'City of Newark, Essex', u'885316': u'Borough of Netcong, Morris', u'885250': u'Borough of Helmetta, Middlesex', u'885405': u'Borough of Spotswood, Middlesex', u'885404': u'Borough of South Toms River, Ocean', u'885407': u'Borough of Spring Lake Heights, Monmouth', u'885406': u'Borough of Spring Lake, Monmouth', u'885401': u'Borough of South Bound Brook, Somerset', u'885400': u'Borough of Lake Como, Monmouth', u'885403': u'Borough of South River, Middlesex', u'885402': u'Borough of South Plainfield, Middlesex', u'885409': u'Borough of Stockton, Hunterdon', u'885408': u'Borough of Stanhope, Sussex', u'882066': u'Township of Long Beach, Ocean', u'882134': u'Township of Pennsville, Salem', u'882067': u'Township of Little Egg Harbor, Ocean', u'2390559': u'Borough of Glen Ridge, Essex', u'2390558': u'Borough of Essex Fells, Essex', u'882135': u'Township of Carneys Point, Salem', u'882268': u'Township of Fredon, Sussex', u'882269': u'Township of Hardyston, Sussex', u'882260': u'Township of Lafayette, Sussex', u'882261': u'Township of Hampton, Sussex', u'882262': u'Township of Stillwater, Sussex', u'882263': u'Township of Byram, Sussex', u'882264': u'Township of Green, Sussex', u'882265': u'Township of Sparta, Sussex', u'882266': u'Township of Andover, Sussex', u'882267': u'Township of Frankford, Sussex', u'882314': u'Township of Wayne, Passaic', u'882315': u'Township of West Milford, Passaic', u'882317': u'Township of Blairstown, Warren', u'882310': u'Township of River Vale, Bergen', u'882311': u'Township of Washington, Bergen', u'882312': u'Township of Mahwah, Bergen', u'882313': u'Township of Little Falls, Passaic', u'882169': u'Township of Hillsborough, Somerset', u'882168': u'Township of Montgomery, Somerset', u'882167': u'Township of Piscataway, Middlesex', u'882166': u'Township of Edison, Middlesex', u'882165': u'Township of Woodbridge, Middlesex', u'882164': u'Township of North Brunswick, Middlesex', u'882163': u'Township of East Brunswick, Middlesex', u'882162': u'Township of South Brunswick, Middlesex', u'882161': u'Township of Plainsboro, Middlesex', u'882160': u'Township of Cranbury, Middlesex', u'885214': u'Borough of Fair Lawn, Bergen', u'885215': u'Borough of Fairview, Bergen', u'885216': u'Borough of Fanwood, Union', u'885217': u'Borough of Far Hills, Somerset', u'885210': u'Borough of Englewood Cliffs, Bergen', u'885211': u'Borough of Englishtown, Monmouth', u'885212': u'City of Estell Manor, Atlantic', u'885213': u'Borough of Fair Haven, Monmouth', u'882131': u'Township of Alloway, Salem', u'885218': u'Borough of Farmingdale, Monmouth', u'885219': u'Borough of Fieldsboro, Burlington', u'885199': u'Borough of East Newark, Hudson', u'885198': u'Borough of Dunellen, Middlesex', u'885197': u'Borough of Dumont, Bergen', u'885196': u'Town of Dover, Morris', u'885195': u'Borough of Demarest, Bergen', u'885194': u'Borough of Deal, Monmouth', u'885193': u'Borough of Cresskill, Bergen', u'885192': u'City of Corbin City, Atlantic', u'885191': u'Borough of Collingswood, Camden', u'885190': u'Borough of Closter, Bergen', u'885340': u'Borough of Paramus, Bergen', u'885428': u'City of Vineland, Cumberland', u'885449': u'Borough of Woodcliff Lake, Bergen', u'882045': u'Township of Middle, Cape May', u'882046': u'Township of Dennis, Cape May', u'882047': u'Township of Upper, Cape May', u'885364': u'Borough of Ramsey, Bergen', u'885348': u'Borough of Penns Grove, Salem', u'885366': u'Borough of Red Bank, Monmouth', u'885367': u'Borough of Ridgefield, Bergen', u'885441': u'Borough of West Wildwood, Cape May', u'885369': u'Village of Ridgewood, Bergen', u'885443': u'Borough of Wharton, Morris', u'885442': u'Borough of Westwood, Bergen', u'882048': u'Township of Buena Vista, Atlantic', u'882049': u'Township of Hamilton, Atlantic', u'885447': u'City of Woodbury, Gloucester', u'885446': u'Borough of Woodbine, Cape May', u'885276': u'Borough of Leonia, Bergen', u'885277': u'Borough of Lincoln Park, Morris', u'882051': u'Township of Egg Harbor, Atlantic', u'885275': u'Borough of Lebanon, Hunterdon', u'882057': u'Township of Stow Creek, Cumberland', u'885273': u'Borough of Lavallette, Ocean', u'885270': u'Borough of Lakehurst, Ocean', u'877363': u'Township of Irvington, Essex', u'882054': u'Township of Deerfield, Cumberland', u'885327': u'Borough of Northvale, Bergen', u'885148': u'Borough of Barnegat Light, Ocean', u'885149': u'Borough of Barrington, Camden', u'885144': u'Borough of Audubon, Camden', u'885145': u'Borough of Audubon Park, Camden', u'885146': u'Borough of Avalon, Cape May', u'885147': u'Borough of Avon-by-the-Sea, Monmouth', u'885140': u'Borough of Andover, Sussex', u'882059': u'Township of Fairfield, Cumberland', u'885142': u'City of Atlantic City, Atlantic', u'885143': u'Borough of Atlantic Highlands, Monmouth', u'885374': u'Borough of Rockaway, Morris', u'885278': u'City of Linden, Union', u'885370': u'Borough of Ringwood, Passaic', u'885391': u'Borough of Seaside Park, Ocean', u'885390': u'Borough of Seaside Heights, Ocean', u'885393': u'Borough of Shiloh, Cumberland', u'885392': u'Town of Secaucus, Hudson', u'885395': u'Borough of Shrewsbury, Monmouth', u'885394': u'Borough of Ship Bottom, Ocean', u'885397': u'City of Somers Point, Atlantic', u'885396': u'Borough of Somerdale, Camden', u'885399': u'City of South Amboy, Middlesex', u'885398': u'Borough of Somerville, Somerset', u'882088': u'Township of New Hanover, Burlington', u'882089': u'Township of Pemberton, Burlington', u'882224': u'Township of Weehawken, Hudson', u'882225': u'Township of Lyndhurst, Bergen', u'882226': u'Township of South Hackensack, Bergen', u'882227': u'Township of Teaneck, Bergen', u'882220': u'Township of Maplewood, Essex', u'882221': u'Township of Millburn, Essex', u'882222': u'Township of Cedar Grove, Essex', u'882223': u'Township of North Bergen, Hudson', u'882156': u'Township of Haddon, Camden', u'882157': u'Township of Pennsauken, Camden', u'882154': u'Township of Gloucester, Camden', u'882155': u'Township of Cherry Hill, Camden', u'882152': u'Township of Berlin, Camden', u'882153': u'Township of Voorhees, Camden', u'882150': u'Township of Winslow, Camden', u'882151': u'Township of Waterford, Camden', u'885248': u'Borough of Haworth, Bergen', u'882158': u'Township of Old Bridge, Middlesex', u'882159': u'Township of Monroe, Middlesex', u'885247': u'Borough of Hasbrouck Heights, Bergen', u'885246': u'Borough of Harvey Cedars, Ocean', u'885245': u'Town of Harrison, Hudson', u'885324': u'City of Northfield, Atlantic', u'885325': u'Borough of North Haledon, Passaic', u'885326': u'Borough of North Plainfield, Somerset', u'882128': u'Township of Ewing, Mercer', u'885320': u'Borough of New Milford, Bergen', u'885321': u'Borough of New Providence, Union', u'885322': u'Town of Newton, Sussex', u'885323': u'Borough of North Arlington, Bergen', u'882084': u'Township of Shamong, Burlington', u'885328': u'City of North Wildwood, Cape May', u'885329': u'Borough of Norwood, Bergen', u'885242': u'Town of Hammonton, Atlantic', u'882123': u'Township of East Windsor, Mercer', u'882122': u'Township of Robbinsville, Mercer', u'882121': u'Township of Aberdeen, Monmouth', u'882120': u'Township of Hazlet, Monmouth', u'882127': u'Township of Hamilton, Mercer', u'882126': u'Township of Lawrence, Mercer', u'885249': u'Borough of Hawthorne, Passaic', u'882124': u'Township of West Windsor, Mercer', u'882080': u'Township of Woodland, Burlington', u'882081': u'Township of Tabernacle, Burlington', u'882129': u'Township of Hopewell, Mercer', u'882083': u'Township of Medford, Burlington', u'885243': u'Borough of Hampton, Hunterdon', u'882085': u'Township of Washington, Burlington', u'882086': u'Township of Bass River, Burlington', u'882087': u'Township of North Hanover, Burlington'}, u'REVIEW_TYPE': {u'I': u'Incoming', u'D': u'Draft', u'F': u'Final'}, u'SYMBOL_TYPE': {608: u'Other County Ramp', 400: u'State Highway', 700: u'Local Road', 100: u'Highway Authority Route', 708: u'Local Ramp', 200: u'Interstate', 300: u'US Highway', 108: u'Highway Authority Ramp', 208: u'Interstate Ramp', 600: u'Other County Route', 308: u'US Highway Ramp', 408: u'State Highway Ramp', 500: u'County 500 Route', 900: u'Alley', 508: u'County 500 Ramp'}, u'EDIT_TYPE': {1: u'Add', 2: u'Modify', 3: u'Delete'}, u'NAME_TYPE': {u'H': u'Highway Name', u'L': u'Local Name'}, u'STATUS_TYPE': {u'A': u'Active', u'P': u'Planned', u'U': u'Under Construction'}}
            self.grid(row=0, column=0, sticky='nswe')

            self.frm = tk.Frame(self, relief = 'flat')
            #self.create_window(0, 0, window=self.frm, anchor='nw')


            # Setup some styling
            Lstyle =  tk.Style()
            Lstyle.configure("BW.TLabel", font="Helvitica 9")

            tk.Style().configure("TButton", padding=0, relief="flat", background="#ccc", font='Helvitica 9')

            labelpadX = 5; labelpadY = 0; labelipadX = 75; labelipadY = 0
            entrypadX = 5; entrypadY=2
            buttonpadX = 5; buttonpadY=20
            comboipadX = 55; comboipadY = 0
            rpadx = 0; rpady= 0

            ## Update display to get correct dimensions
            self.frm.update_idletasks()
            ## Configure size of canvas's scrollable zone
            self.configure(scrollregion=(0, 0, self.frm.winfo_width(), self.frm.winfo_height()), relief='flat', highlightthickness=0)


            ########################################################################
            ########################################################################
            ##### Parameter Definitions
            ########################################################################

            # SEG_ID
            ##########################
            self.label_segid = tk.Label(self.frm, text='SEG_ID:', style="BW.TLabel").grid(row=0,column=0, sticky='w', pady=labelpadY, padx=labelpadX) #.pack(anchor='w', pady=labelpadY, padx=labelpadX)

            ############
            self.segid = Tk.StringVar()
            if self.Fp['SEG_ID']:
                self.segid.set(self.Fp['SEG_ID'])

            self.entry_segid = Tk.Entry(self.frm, textvariable=self.segid, state=Tk.DISABLED)
            self.entry_segid.grid(row=1,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)  #.pack(anchor='w', fill=Tk.X, pady=entrypadY, padx=entrypadX)


            # PRIME_NAME
            ##########################
            self.label_primename = tk.Label(self.frm, text='PRIME_NAME:', style="BW.TLabel").grid(row=2,column=0, sticky='w', pady=labelpadY, padx=labelpadX) #.pack(anchor='w', pady=labelpadY, padx=labelpadX)

            ############
            self.primename = Tk.StringVar()
            if self.Fp['PRIME_NAME']:
                self.primename.set(self.Fp['PRIME_NAME'])
            self.entry_primename = Tk.Entry(self.frm, textvariable=self.primename, state=Tk.DISABLED)
            self.entry_primename.grid(row=3,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)  #.pack(anchor='w', fill=Tk.X, pady=entrypadY, padx=entrypadX), state=Tk.DISABLED

            # ADDR_L_FR
            ##########################
            self.label_addrlfr = tk.Label(self.frm, text='ADDR_L_FR:', style="BW.TLabel").grid(row=4,column=0, sticky='w', pady=labelpadY, padx=labelpadX)    #pack(anchor='w', pady=labelpadY, padx=labelpadX)
            ############
            self.button_addrlfr = Tk.Button(self.frm, relief='flat', image=self.trans_image)  #.grid(row=5,column=2)
            self.button_addrlfr.grid(row=5,column=2)
            self.tip_addrlfr = ToolTip(self.button_addrlfr, follow_mouse=1, text="", state='disabled')
            ############
            def isInt_3(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_addrlfr.config(image=self.trans_image)
                    self.message_dict['addrlfr']['error'] = False
                    try: self.tip_addrlfr.configure(state = 'disabled')
                    except: pass
                    return True
                elif changeval.isdigit():
                    self.button_addrlfr.config(image=self.trans_image)
                    self.message_dict['addrlfr']['error'] = False
                    try: self.tip_addrlfr.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            isInt_Command_3 = self.register(isInt_3)

            def notInt_3():
                self.button_addrlfr.config(image=self.error_image)
                self.message_dict['addrlfr']['error'] = True
                self.tip_addrlfr.configure(state='normal', text='Value should numeric.')

            notInt_Command_3 = self.register(notInt_3)


            ############
            self.addrlfr = Tk.StringVar()
##            if Address_to_Split:
##                if Address_to_Split['ADDR_L_FR']:
##                    if Address_to_Split['ADDR_L_FR'][1]: # This is true, so it is an interpolated value!
##                        self.addrlfr.set(Address_to_Split['ADDR_L_FR'][0])
##                    elif not Address_to_Split['ADDR_L_FR'][1]: # this is false, there is a value, but it is the original value
##                        self.addrlfr.set(Address_to_Split['ADDR_L_FR'][0])
##                        # hang a warning!!
##                        self.button_addrlfr.config(image=self.warn_image)
##                        self.tip_addrlfr.configure(state='normal', text='Just so you know, this is the original value, not the geocoded interpolated value.')
    ##
            if self.Fp['ADDR_L_FR']:
                self.addrlfr.set(self.Fp['ADDR_L_FR'])
            self.entry_addrlfr = Tk.Entry(self.frm, textvariable=self.addrlfr, validate='focus', vcmd = (isInt_Command_3, '%d', '%i', '%S', '%P'), invalidcommand = (notInt_Command_3))
            self.entry_addrlfr.grid(row=5,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)  #.pack(anchor='w', fill=Tk.X, pady=entrypadY, padx=entrypadX)
            self.tip_addrlfr_desc = ToolTip(self.entry_addrlfr, follow_mouse=1, text="(Integer) Address left from. The address ranges are interpolated using a geocoder. If the geocoder fails (for whatever reason), the default value will inherited from original segment.")


            # ADDR_L_TO
            ##########################
            self.label_addrlto = tk.Label(self.frm, text='ADDR_L_TO:', style="BW.TLabel").grid(row=6,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_addrlto = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_addrlto.grid(row=7,column=2)
            self.tip_addrlto = ToolTip(self.button_addrlto, follow_mouse=1, text="", state='disabled')
            ############
            def isInt_4(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_addrlto.config(image=self.trans_image)
                    self.message_dict['addrlto']['error'] = False
                    try: self.tip_addrlto.configure(state = 'disabled')
                    except: pass
                    return True
                elif changeval.isdigit():
                    self.button_addrlto.config(image=self.trans_image)
                    self.message_dict['addrlto']['error'] = False
                    try: self.tip_addrlto.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            isInt_Command_4 = self.register(isInt_4)

            def notInt_4():
                self.button_addrlto.config(image=self.error_image)
                self.message_dict['addrlto']['error'] = True
                self.tip_addrlto.configure(state='normal', text='Value should numeric.')

            notInt_Command_4 = self.register(notInt_4)


            ############
            self.addrlto = Tk.StringVar()

##            if Address_to_Split:
##                if Address_to_Split['ADDR_L_TO']:
##                    if Address_to_Split['ADDR_L_TO'][1]: # This is true, so it is an interpolated value!
##                        self.addrlto.set(Address_to_Split['ADDR_L_TO'][0])
##                    elif not Address_to_Split['ADDR_L_TO'][1]: # this is false, there is a value, but it is the original value
##                        self.addrlto.set(Address_to_Split['ADDR_L_TO'][0])
##                        # hang a warning!!
##                        self.button_addrlto.config(image=self.warn_image)
##                        self.tip_addrlto.configure(state='normal', text='Just so you know, this is the original value, not the geocoded interpolated value.')

            if self.Fp['ADDR_L_TO']:
                self.addrlto.set(self.Fp['ADDR_L_TO'])

            self.entry_addrlto = Tk.Entry(self.frm, textvariable=self.addrlto, validate='focus', vcmd = (isInt_Command_4, '%d', '%i', '%S', '%P'), invalidcommand = (notInt_Command_4))
            self.entry_addrlto.grid(row=7,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)
            self.tip_addrlto_desc = ToolTip(self.entry_addrlto, follow_mouse=1, text="(Integer) Address left to. The address ranges are interpolated using a geocoder. If the geocoder fails (for whatever reason), the default value will inherited from original segment.")


            # ADDR_R_FR
            ##########################
            self.label_addrrfr = tk.Label(self.frm, text='ADDR_R_FR:', style="BW.TLabel").grid(row=8,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_addrrfr = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_addrrfr.grid(row=9,column=2)
            self.tip_addrrfr = ToolTip(self.button_addrrfr, follow_mouse=1, text="", state='disabled')
            ############
            def isInt_5(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_addrrfr.config(image=self.trans_image)
                    self.message_dict['addrrfr']['error'] = False
                    try: self.tip_addrrfr.configure(state = 'disabled')
                    except: pass
                    return True
                elif changeval.isdigit():
                    self.button_addrrfr.config(image=self.trans_image)
                    self.message_dict['addrrfr']['error'] = False
                    try: self.tip_addrrfr.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            isInt_Command_5 = self.register(isInt_5)

            def notInt_5():
                self.button_addrrfr.config(image=self.error_image)
                self.message_dict['addrrfr']['error'] = True
                self.tip_addrrfr.configure(state='normal', text='Value should numeric.')

            notInt_Command_5 = self.register(notInt_5)

            ############
            self.addrrfr = Tk.StringVar()

##            if Address_to_Split:
##                if Address_to_Split['ADDR_R_FR']:
##                    if Address_to_Split['ADDR_R_FR'][1]: # This is true, so it is an interpolated value!
##                        self.addrrfr.set(Address_to_Split['ADDR_R_FR'][0])
##                    elif not Address_to_Split['ADDR_R_FR'][1]: # this is false, there is a value, but it is the original value
##                        self.addrrfr.set(Address_to_Split['ADDR_R_FR'][0])
##                        # hang a warning!!
##                        self.button_addrrfr.config(image=self.warn_image)
##                        self.tip_addrrfr.configure(state='normal', text='Just so you know, this is the original value, not the geocoded interpolated value.')
    ##
            if self.Fp['ADDR_R_FR']:
                self.addrrfr.set(self.Fp['ADDR_R_FR'])
            self.entry_addrrfr = Tk.Entry(self.frm, textvariable=self.addrrfr, validate='focus', vcmd = (isInt_Command_5, '%d', '%i', '%S', '%P'), invalidcommand = (notInt_Command_5))
            self.entry_addrrfr.grid(row=9,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)
            self.tip_addrrfr_desc = ToolTip(self.entry_addrrfr, follow_mouse=1, text="(Integer) Address right from. The address ranges are interpolated using a geocoder. If the geocoder fails (for whatever reason), the default value will inherited from original segment.")



            # ADDR_R_TO
            ##########################
            self.label_addrrto = tk.Label(self.frm, text='ADDR_R_TO:', style="BW.TLabel").grid(row=10,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_addrrto = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_addrrto.grid(row=11,column=2)
            self.tip_addrrto = ToolTip(self.button_addrrto, follow_mouse=1, text="", state='disabled')
            ############
            def isInt_6(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_addrrto.config(image=self.trans_image)
                    self.message_dict['addrrto']['error'] = False
                    try: self.tip_addrrto.configure(state = 'disabled')
                    except: pass
                    return True
                elif changeval.isdigit():
                    self.button_addrrto.config(image=self.trans_image)
                    self.message_dict['addrrto']['error'] = False
                    try: self.tip_addrrto.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            isInt_Command_6 = self.register(isInt_6)

            def notInt_6():
                self.button_addrrto.config(image=self.error_image)
                self.message_dict['addrrto']['error'] = True
                self.tip_addrrto.configure(state='normal', text='Value should numeric.')

            notInt_Command_6 = self.register(notInt_6)



            ############
            self.addrrto = Tk.StringVar()

##            if Address_to_Split:
##                if Address_to_Split['ADDR_R_TO']:
##                    if Address_to_Split['ADDR_R_TO'][1]: # This is true, so it is an interpolated value!
##                        self.addrrto.set(Address_to_Split['ADDR_R_TO'][0])
##                    elif not Address_to_Split['ADDR_R_TO'][1]: # this is false, there is a value, but it is the original value
##                        self.addrrto.set(Address_to_Split['ADDR_R_TO'][0])
##                        # hang a warning!!
##                        self.button_addrrto.config(image=self.warn_image)
##                        self.tip_addrrto.configure(state='normal', text='Just so you know, this is the original value, not the geocoded interpolated value.')
    ##
            if self.Fp['ADDR_R_TO']:
                self.addrrto.set(self.Fp['ADDR_R_TO'])
            self.entry_addrrto = Tk.Entry(self.frm, textvariable=self.addrrto, validate='focus', vcmd = (isInt_Command_6, '%d', '%i', '%S', '%P'), invalidcommand = (notInt_Command_6))
            self.entry_addrrto.grid(row=11,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)
            self.tip_addrrto_desc = ToolTip(self.entry_addrrto, follow_mouse=1, text="(Integer) Address right to. The address ranges are interpolated using a geocoder. If the geocoder fails (for whatever reason), the default value will inherited from original segment.")


            # ZIPCODE_L, integer
            ##########################
            self.label_zipcodeL = tk.Label(self.frm, text='ZIPCODE_L:', style="BW.TLabel").grid(row=12,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_zipcodeL = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_zipcodeL.grid(row=13,column=2)
            self.tip_zipcodeL = ToolTip(self.button_zipcodeL, follow_mouse=1, text="", state='disabled')
            ############
            def isInt(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_zipcodeL.config(image=self.trans_image)
                    self.message_dict['zipcodeL']['error'] = False
                    try: self.tip_zipcodeL.configure(state = 'disabled')
                    except: pass
                    return True
                elif changeval.isdigit() and len(changeval) == 5:
                    self.button_zipcodeL.config(image=self.trans_image)
                    self.message_dict['zipcodeL']['error'] = False
                    try: self.tip_zipcodeL.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            isInt_Command = self.register(isInt)

            def notInt():
                self.button_zipcodeL.config(image=self.error_image)
                self.message_dict['zipcodeL']['error'] = True
                self.tip_zipcodeL.configure(state='normal', text='Value should be 5 digits and only contain numeric values.')

            notInt_Command = self.register(notInt)


            ############
            self.zipcodeL = Tk.StringVar()
            if self.Fp['ZIPCODE_L']:
                self.zipcodeL.set(self.Fp['ZIPCODE_L'])

            self.entry_zipcodeL = Tk.Entry(self.frm, textvariable=self.zipcodeL, validate='focus', vcmd = (isInt_Command, '%d', '%i', '%S', '%P'), invalidcommand = (notInt_Command))
            self.entry_zipcodeL.grid(row=13,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)
            self.tip_zipcodeL_desc = ToolTip(self.entry_zipcodeL, follow_mouse=1, text="(Integer) Zipcode on the left side of the road. Value should be 5 digits and only contain numeric values.")



            # ZIPCODE_R, integer
            ##########################
            self.label_zipcodeR = tk.Label(self.frm, text='ZIPCODE_R:', style="BW.TLabel").grid(row=14,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_zipcodeR = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_zipcodeR.grid(row=15,column=2)
            self.tip_zipcodeR = ToolTip(self.button_zipcodeR, follow_mouse=1, text="", state='disabled')
            ############
            def isInt_8(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_zipcodeR.config(image=self.trans_image)
                    self.message_dict['zipcodeR']['error'] = False
                    try: self.tip_zipcodeR.configure(state = 'disabled')
                    except: pass
                    return True
                elif changeval.isdigit() and len(changeval) == 5:
                    self.button_zipcodeR.config(image=self.trans_image)
                    self.message_dict['zipcodeR']['error'] = False
                    try: self.tip_zipcodeR.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            isInt_Command_8 = self.register(isInt_8)

            def notInt_8():
                self.button_zipcodeR.config(image=self.error_image)
                self.message_dict['zipcodeR']['error'] = True
                self.tip_zipcodeR.configure(state='normal', text='Value should be 5 digits and only contain numeric values.')

            notInt_Command_8 = self.register(notInt_8)


            ############
            self.zipcodeR = Tk.StringVar()
            if self.Fp['ZIPCODE_R']:
                self.zipcodeR.set(self.Fp['ZIPCODE_R'])
            self.entry_zipcodeR = Tk.Entry(self.frm, textvariable=self.zipcodeR, validate='focus', vcmd = (isInt_Command_8, '%d', '%i', '%S', '%P'), invalidcommand = (notInt_Command_8))
            self.entry_zipcodeR.grid(row=15,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)
            self.tip_zipcodeR_desc = ToolTip(self.entry_zipcodeR, follow_mouse=1, text="(Integer) Zipcode on the right side of the road. Value should be 5 digits and only contain numeric values.")


            # ZIPNAME_L, string
            ##########################
            self.label_zipnameL = tk.Label(self.frm, text='ZIPNAME_L:', style="BW.TLabel").grid(row=16,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_zipnameL = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_zipnameL.grid(row=17,column=2)
            self.tip_zipnameL = ToolTip(self.button_zipnameL, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_9(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_zipnameL.config(image=self.trans_image)
                    self.message_dict['zipnameL']['error'] = False
                    try: self.tip_zipnameL.configure(state = 'disabled')
                    except: pass
                    return True
                elif re.match("^[A-Za-z\s]*$",changeval):
                    self.button_zipnameL.config(image=self.trans_image)
                    self.message_dict['zipnameL']['error'] = False
                    try: self.tip_zipnameL.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            is_Str_Command_9 = self.register(is_Str_9)

            def notStr_9():
                self.button_zipnameL.config(image=self.error_image)
                self.message_dict['zipnameL']['error'] = True
                self.tip_zipnameL.configure(state='normal', text='Value should be text and not contain numbers.')

            notStr_Command_9 = self.register(notStr_9)


            ############
            self.zipnameL = Tk.StringVar()
            if self.Fp['ZIPNAME_L']:
                self.zipnameL.set(self.Fp['ZIPNAME_L'])
            self.entry_zipnameL = Tk.Entry(self.frm, textvariable=self.zipnameL, validate='focus', vcmd = (is_Str_Command_9, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_9))
            self.entry_zipnameL.grid(row=17,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)
            self.tip_zipnameL_desc = ToolTip(self.entry_zipnameL, follow_mouse=1, text="(Text) Zipcode name on the left side of the road. Example: 'Neptune'.")


            # ZIPNAME_R, string
            ##########################
            self.label_zipnameR = tk.Label(self.frm, text='ZIPNAME_R:', style="BW.TLabel").grid(row=18,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_zipnameR = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_zipnameR.grid(row=19,column=2)
            self.tip_zipnameR = ToolTip(self.button_zipnameR, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_10(why, where, what, changeval):
                #print why, where, what, changeval

                if changeval == '':
                    self.button_zipnameR.config(image=self.trans_image)
                    self.message_dict['zipnameR']['error'] = False
                    try: self.tip_zipnameR.configure(state = 'disabled')
                    except: pass
                    return True
                elif re.match("^[A-Za-z\s]*$",changeval):
                    self.button_zipnameR.config(image=self.trans_image)
                    self.message_dict['zipnameR']['error'] = False
                    try: self.tip_zipnameR.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    return False

            is_Str_Command_10 = self.register(is_Str_10)

            def notStr_10():
                self.button_zipnameR.config(image=self.error_image)
                self.message_dict['zipnameR']['error'] = True
                self.tip_zipnameR.configure(state='normal', text='Value should be text and not contain numbers.')

            notStr_Command_10 = self.register(notStr_10)


            ############
            self.zipnameR = Tk.StringVar()
            if self.Fp['ZIPNAME_R']:
                self.zipnameR.set(self.Fp['ZIPNAME_R'])
            self.entry_zipnameR = Tk.Entry(self.frm, textvariable=self.zipnameR, validate='focus', vcmd = (is_Str_Command_10, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_10))
            self.entry_zipnameR.grid(row=19,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = labelipadX, ipady = labelipadY)
            self.tip_zipnameR_desc = ToolTip(self.entry_zipnameR, follow_mouse=1, text="(Text) Zipcode name on the right side of the road. Example: 'Neptune'.")

            # MUNI_ID_L, string
            ##########################
            self.label_muniidL = tk.Label(self.frm, text='MUNI_ID_L:', style="BW.TLabel").grid(row=20,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_muniidL = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_muniidL.grid(row=21,column=2)
            self.tip_muniidL = ToolTip(self.button_muniidL, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_11(why, where, what, changeval, DD = Domains['GNIS_NAME'].values()):
                #print why, where, what, changeval
                DD.append('')
                if changeval in DD:
                    self.button_muniidL.config(image=self.trans_image)
                    self.message_dict['muniidL']['error'] = False
                    self.message_dict['muniidL']['value'] = True
                    try: self.tip_muniidL.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['muniidL']['value'] = False
                    return False

            is_Str_Command_11 = self.register(is_Str_11)

            def notStr_11():
                self.button_muniidL.config(image=self.error_image)
                self.message_dict['muniidL']['error'] = True
                self.tip_muniidL.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_11 = self.register(notStr_11)


            ############
            self.muniidL = Tk.StringVar()
            if self.Fp['MUNI_ID_L']:
                self.muniidL.set(self.Fp['MUNI_ID_L'])
                self.message_dict['muniidL']['value'] = True # set the validation to true

            gnis = Domains['GNIS_NAME'].values()
            gnis2 = sorted(gnis, key = lambda item: item.split(',')[1] + item.split(',')[0])



            self.combo_muniidL = tk.Combobox(self.frm, textvariable=self.muniidL, values=gnis2, validate='focus', validatecommand = (is_Str_Command_11, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_11))
            self.combo_muniidL.grid(row=21,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            #self.r_button_muniidL = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)  #.grid(row=5,column=2)
            #self.r_button_muniidL.grid(row=21,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_muniidL_desc = ToolTip(self.combo_muniidL, follow_mouse=1, text="(Domain) Municipal ID on the left side of the road.")



            # MUNI_ID_R, string
            ##########################
            self.label_muniidR = tk.Label(self.frm, text='MUNI_ID_R:', style="BW.TLabel").grid(row=22,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_muniidR = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_muniidR.grid(row=23,column=2)
            self.tip_muniidR = ToolTip(self.button_muniidR, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_12(why, where, what, changeval, DD = Domains['GNIS_NAME'].values()):
                #print why, where, what, changeval
                DD.append('')
                if changeval in DD:
                    self.button_muniidR.config(image=self.trans_image)
                    self.message_dict['muniidR']['error'] = False
                    self.message_dict['muniidR']['value'] = True
                    try: self.tip_muniidR.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['muniidR']['value'] = False
                    return False

            is_Str_Command_12 = self.register(is_Str_12)

            def notStr_12():
                self.button_muniidR.config(image=self.error_image)
                self.message_dict['muniidR']['error'] = True
                self.tip_muniidR.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_12 = self.register(notStr_12)


            ############
            self.muniidR = Tk.StringVar()
            if self.Fp['MUNI_ID_R']:
                self.muniidR.set(self.Fp['MUNI_ID_R'])
                self.message_dict['muniidR']['value'] = True  # set the validation to true
            self.combo_muniidR = tk.Combobox(self.frm, textvariable=self.muniidR, values=gnis2, validate='focus', validatecommand = (is_Str_Command_12, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_12))
            self.combo_muniidR.grid(row=23,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            #self.r_button_muniidR = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)  #.grid(row=5,column=2)
            #self.r_button_muniidR.grid(row=23,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_muniidR_desc = ToolTip(self.combo_muniidR, follow_mouse=1, text="(Domain) Municipal ID on the right side of the road.")


            # ELEV_TYPE_ID_FR, string
            ##########################
            self.label_elevfr = tk.Label(self.frm, text='ELEV_TYPE_ID_FR:', style="BW.TLabel").grid(row=24,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_elevfr = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_elevfr.grid(row=25,column=2)
            self.tip_elevfr = ToolTip(self.button_elevfr, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_13(why, where, what, changeval, DD = Domains['ELEV_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_elevfr.config(image=self.trans_image)
                    self.message_dict['elevfr']['error'] = False
                    self.message_dict['elevfr']['value'] = True
                    try: self.tip_elevfr.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['elevfr']['value'] = False
                    return False

            is_Str_Command_13 = self.register(is_Str_13)

            def notStr_13():
                self.button_elevfr.config(image=self.error_image)
                self.message_dict['elevfr']['error'] = True
                self.tip_elevfr.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_13 = self.register(notStr_13)


            ############
            self.elevfr = Tk.StringVar()
            if self.Fp['ELEV_TYPE_ID_FR']:
                self.elevfr.set(self.Fp['ELEV_TYPE_ID_FR'])
                self.message_dict['elevfr']['value'] = True  # set the validation to true

##            if Elev_to_Split:
##                if Elev_to_Split['ELEV_TYPE_ID_FR']:
##                    self.elevfr.set(Elev_to_Split['ELEV_TYPE_ID_FR'])
##                    self.message_dict['elevfr']['value'] = True  # set the validation to true, ie there is a value
##                else:
##                    self.button_elevfr.config(image=self.error_image)
##                    self.message_dict['elevfr']['error'] = True
##                    self.tip_elevfr.configure(state='normal', text='Please choose a value from the dropdown list.')

            self.combo_elevfr = tk.Combobox(self.frm, textvariable=self.elevfr, values=Domains['ELEV_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_13, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_13))
            self.combo_elevfr.grid(row=25,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_elevfr = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)  #.grid(row=5,column=2)
            self.r_button_elevfr.grid(row=25,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_elevfr_desc = ToolTip(self.combo_elevfr, follow_mouse=1, text="(Domain) Elevation type id from.")


            # ELEV_TYPE_ID_TO, string
            ##########################
            self.label_elevto = tk.Label(self.frm, text='ELEV_TYPE_ID_TO:', style="BW.TLabel").grid(row=26,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_elevto = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_elevto.grid(row=27,column=2)
            self.tip_elevto = ToolTip(self.button_elevto, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_14(why, where, what, changeval, DD = Domains['ELEV_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_elevto.config(image=self.trans_image)
                    self.message_dict['elevto']['error'] = False
                    self.message_dict['elevto']['value'] = True
                    try: self.tip_elevto.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['elevto']['value'] = False
                    return False

            is_Str_Command_14 = self.register(is_Str_14)

            def notStr_14():
                self.button_elevto.config(image=self.error_image)
                self.message_dict['elevto']['error'] = True
                self.tip_elevto.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_14 = self.register(notStr_14)


            ############
            self.elevto = Tk.StringVar()
            if self.Fp['ELEV_TYPE_ID_TO']:
                self.elevto.set(self.Fp['ELEV_TYPE_ID_TO'])
                self.message_dict['elevto']['value'] = True  # set the validation to true

##
##            if Elev_to_Split:
##                if Elev_to_Split['ELEV_TYPE_ID_TO']:
##                    self.elevto.set(Elev_to_Split['ELEV_TYPE_ID_TO'])
##                    self.message_dict['elevto']['value'] = True  # set the validation to true, ie there is a value
##                else:
##                    self.button_elevto.config(image=self.error_image)
##                    self.message_dict['elevto']['error'] = True
##                    self.tip_elevto.configure(state='normal', text='Please choose a value from the dropdown list.')

            self.combo_elevto = tk.Combobox(self.frm, textvariable=self.elevto, values=Domains['ELEV_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_14, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_14))
            self.combo_elevto.grid(row=27,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_elevto = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_elevto.grid(row=27,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_elevto_desc = ToolTip(self.combo_elevto, follow_mouse=1, text="(Domain) Elevation type id to.")



            # ACC_TYPE_ID, string
            ##########################
            self.label_acctype = tk.Label(self.frm, text='ACC_TYPE_ID:', style="BW.TLabel").grid(row=28,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_acctype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_acctype.grid(row=29,column=2)
            self.tip_acctype = ToolTip(self.button_acctype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_15(why, where, what, changeval, DD = Domains['ACCESS_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_acctype.config(image=self.trans_image)
                    self.message_dict['acctype']['error'] = False
                    self.message_dict['acctype']['value'] = True
                    try: self.tip_acctype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['acctype']['value'] = False
                    return False

            is_Str_Command_15 = self.register(is_Str_15)

            def notStr_15():
                self.button_acctype.config(image=self.error_image)
                self.message_dict['acctype']['error'] = True
                self.tip_acctype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_15 = self.register(notStr_15)


            ############
            self.acctype = Tk.StringVar()
            if self.Fp['ACC_TYPE_ID']:
                self.acctype.set(self.Fp['ACC_TYPE_ID'])
                self.message_dict['acctype']['value'] = True  # set the validation to true
            self.combo_acctype = tk.Combobox(self.frm, textvariable=self.acctype, values=Domains['ACCESS_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_15, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_15))
            self.combo_acctype.grid(row=29,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_acctype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_acctype.grid(row=29,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_acctype_desc = ToolTip(self.combo_acctype, follow_mouse=1, text="(Domain) Access type id.")

            # SURF_TYPE_ID, string
            ##########################
            self.label_surftype = tk.Label(self.frm, text='SURF_TYPE_ID:', style="BW.TLabel").grid(row=30,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_surftype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_surftype.grid(row=31,column=2)
            self.tip_surftype = ToolTip(self.button_surftype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_16(why, where, what, changeval, DD = Domains['SURFACE_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_surftype.config(image=self.trans_image)
                    self.message_dict['surftype']['error'] = False
                    self.message_dict['surftype']['value'] = True
                    try: self.tip_surftype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['surftype']['value'] = False
                    return False

            is_Str_Command_16 = self.register(is_Str_16)

            def notStr_16():
                self.button_surftype.config(image=self.error_image)
                self.message_dict['surftype']['error'] = True
                self.tip_surftype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_16 = self.register(notStr_16)


            ############
            self.surftype = Tk.StringVar()
            if self.Fp['SURF_TYPE_ID']:
                self.surftype.set(self.Fp['SURF_TYPE_ID'])
                self.message_dict['surftype']['value'] = True  # set the validation to true
            self.combo_surftype = tk.Combobox(self.frm, textvariable=self.surftype, values=Domains['SURFACE_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_16, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_16))
            self.combo_surftype.grid(row=31,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_surftype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_surftype.grid(row=31,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_surftype_desc = ToolTip(self.combo_surftype, follow_mouse=1, text="(Domain) Surface type id.")


            # STATUS_TYPE_ID, string
            ##########################
            self.label_stattype = tk.Label(self.frm, text='STATUS_TYPE_ID:', style="BW.TLabel").grid(row=32,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_stattype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_stattype.grid(row=33,column=2)
            self.tip_stattype = ToolTip(self.button_stattype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_17(why, where, what, changeval, DD = Domains['STATUS_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_stattype.config(image=self.trans_image)
                    self.message_dict['stattype']['error'] = False
                    self.message_dict['stattype']['value'] = True
                    try: self.tip_stattype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['stattype']['value'] = False
                    return False

            is_Str_Command_17 = self.register(is_Str_17)

            def notStr_17():
                self.button_stattype.config(image=self.error_image)
                self.message_dict['stattype']['error'] = True
                self.tip_stattype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_17 = self.register(notStr_17)


            ############
            self.stattype = Tk.StringVar()
            if self.Fp['STATUS_TYPE_ID']:
                self.stattype.set(self.Fp['STATUS_TYPE_ID'])
                self.message_dict['stattype']['value'] = True  # set the validation to true
            self.combo_stattype = tk.Combobox(self.frm, textvariable=self.stattype, values=Domains['STATUS_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_17, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_17))
            self.combo_stattype.grid(row=33,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_stattype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_stattype.grid(row=33,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_stattype_desc = ToolTip(self.combo_stattype, follow_mouse=1, text="(Domain) Status type id.")



            # SYMBOL_TYPE_ID, string
            ##########################
            self.label_symbtype = tk.Label(self.frm, text='SYMBOL_TYPE_ID:', style="BW.TLabel").grid(row=34,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_symbtype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_symbtype.grid(row=35,column=2)
            self.tip_symbtype = ToolTip(self.button_symbtype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_18(why, where, what, changeval, DD = Domains['SYMBOL_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_symbtype.config(image=self.trans_image)
                    self.message_dict['symbtype']['error'] = False
                    self.message_dict['symbtype']['value'] = True
                    try: self.tip_symbtype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['symbtype']['value'] = False
                    return False

            is_Str_Command_18 = self.register(is_Str_18)

            def notStr_18():
                self.button_symbtype.config(image=self.error_image)
                self.message_dict['symbtype']['error'] = True
                self.tip_symbtype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_18 = self.register(notStr_18)


            ############
            self.symbtype = Tk.StringVar()
            if self.Fp['SYMBOL_TYPE_ID']:
                self.symbtype.set(self.Fp['SYMBOL_TYPE_ID'])
                self.message_dict['symbtype']['value'] = True  # set the validation to true
            self.combo_symbtype = tk.Combobox(self.frm, textvariable=self.symbtype, values=Domains['SYMBOL_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_18, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_18))
            self.combo_symbtype.grid(row=35,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_symbtype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_symbtype.grid(row=35,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_symbtype_desc = ToolTip(self.combo_symbtype, follow_mouse=1, text="(Domain) Symbol type id.")


            # TRAVEL_DIR_TYPE_ID, string
            ##########################
            self.label_travtype = tk.Label(self.frm, text='TRAVEL_DIR_TYPE_ID:', style="BW.TLabel").grid(row=36,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_travtype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_travtype.grid(row=37,column=2)
            self.tip_travtype = ToolTip(self.button_travtype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_19(why, where, what, changeval, DD = Domains['TRAVEL_DIR_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_travtype.config(image=self.trans_image)
                    self.message_dict['travtype']['error'] = False
                    self.message_dict['travtype']['value'] = True
                    try: self.tip_travtype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['travtype']['value'] = False
                    return False

            is_Str_Command_19 = self.register(is_Str_19)

            def notStr_19():
                self.button_travtype.config(image=self.error_image)
                self.message_dict['travtype']['error'] = True
                self.tip_travtype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_19 = self.register(notStr_19)


            ############
            self.travtype = Tk.StringVar()
            if self.Fp['TRAVEL_DIR_TYPE_ID']:
                self.travtype.set(self.Fp['TRAVEL_DIR_TYPE_ID'])
                self.message_dict['travtype']['value'] = True  # set the validation to true
            self.combo_travtype = tk.Combobox(self.frm, textvariable=self.travtype, values=Domains['TRAVEL_DIR_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_19, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_19))
            self.combo_travtype.grid(row=37,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_travtype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_travtype.grid(row=37,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_travtype_desc = ToolTip(self.combo_travtype, follow_mouse=1, text="(Domain) Travel direction type id.")


            # JURIS_TYPE_ID, string
            ##########################
            self.label_juristype = tk.Label(self.frm, text='JURIS_TYPE_ID:', style="BW.TLabel").grid(row=38,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_juristype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_juristype.grid(row=39,column=2)
            self.tip_juristype = ToolTip(self.button_juristype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_20(why, where, what, changeval, DD = Domains['JURIS_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_juristype.config(image=self.trans_image)
                    self.message_dict['juristype']['error'] = False
                    self.message_dict['juristype']['value'] = True
                    try: self.tip_juristype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['juristype']['value'] = False
                    return False

            is_Str_Command_20 = self.register(is_Str_20)

            def notStr_20():
                self.button_juristype.config(image=self.error_image)
                self.message_dict['juristype']['error'] = True
                self.tip_juristype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_20 = self.register(notStr_20)


            ############
            self.juristype = Tk.StringVar()
            if self.Fp['JURIS_TYPE_ID']:
                self.juristype.set(self.Fp['JURIS_TYPE_ID'])
                self.message_dict['juristype']['value'] = True  # set the validation to true
            self.combo_juristype = tk.Combobox(self.frm, textvariable=self.juristype, values=Domains['JURIS_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_20, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_20))
            self.combo_juristype.grid(row=39,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_juristype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_juristype.grid(row=39,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_juristype_desc = ToolTip(self.combo_juristype, follow_mouse=1, text="(Domain) Jurisdiction type id.")


            # OIT_REV_TYPE_ID, string
            ##########################
            self.label_oitrevtype = tk.Label(self.frm, text='OIT_REV_TYPE_ID:', style="BW.TLabel").grid(row=40,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_oitrevtype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_oitrevtype.grid(row=41,column=2)
            self.tip_oitrevtype = ToolTip(self.button_oitrevtype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_21(why, where, what, changeval, DD = Domains['REVIEW_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_oitrevtype.config(image=self.trans_image)
                    self.message_dict['oitrevtype']['error'] = False
                    self.message_dict['oitrevtype']['value'] = True
                    try: self.tip_oitrevtype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['oitrevtype']['value'] = False
                    return False

            is_Str_Command_21 = self.register(is_Str_21)

            def notStr_21():
                self.button_oitrevtype.config(image=self.error_image)
                self.message_dict['oitrevtype']['error'] = True
                self.tip_oitrevtype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_21 = self.register(notStr_21)


            ############
            self.oitrevtype = Tk.StringVar()
    ##        if self.Fp['OIT_REV_TYPE_ID']:
    ##            self.oitrevtype.set(self.Fp['OIT_REV_TYPE_ID'])
    ##            self.message_dict['oitrevtype']['value'] = True  # set the validation to true

            # Validation rule: If it is OIT, then make this value 'Final'. If this is DOT, then make this value 'Draft'
            if USER in ['NJ OIT', 'NJ DOT', 'County', 'Other']:
                usedict = {'NJ OIT': 'Final', 'NJ DOT': 'Draft', 'County': 'Incoming', 'Other': 'Draft'}
                self.oitrevtype.set(usedict[USER])
                self.message_dict['oitrevtype']['value'] = True
            else:   # this is not OIT, so it must be Baker, or somebody else
                self.oitrevtype.set('Draft')
                self.message_dict['oitrevtype']['value'] = True


            self.combo_oitrevtype = tk.Combobox(self.frm, textvariable=self.oitrevtype, values=Domains['REVIEW_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_21, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_21))
            self.combo_oitrevtype.grid(row=41,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_oitrevtype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_oitrevtype.grid(row=41,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_oitrevtype_desc = ToolTip(self.combo_oitrevtype, follow_mouse=1, text="(Domain) OIT review type id.")


            # DOT_REV_TYPE_ID, string
            ##########################
            self.label_dotrevtype = tk.Label(self.frm, text='DOT_REV_TYPE_ID:', style="BW.TLabel").grid(row=42,column=0, sticky='w', pady=labelpadY, padx=labelpadX)

            self.button_dotrevtype = Tk.Button(self.frm, relief='flat', image=self.trans_image)
            self.button_dotrevtype.grid(row=43,column=2)
            self.tip_dotrevtype = ToolTip(self.button_dotrevtype, follow_mouse=1, text="", state='disabled')
            ############
            def is_Str_22(why, where, what, changeval, DD = Domains['REVIEW_TYPE'].values()):
                #print why, where, what, changeval

                if changeval in DD:
                    self.button_dotrevtype.config(image=self.trans_image)
                    self.message_dict['dotrevtype']['error'] = False
                    self.message_dict['dotrevtype']['value'] = True
                    try: self.tip_dotrevtype.configure(state = 'disabled')
                    except: pass
                    return True
                else:
                    self.message_dict['dotrevtype']['value'] = False
                    return False

            is_Str_Command_22 = self.register(is_Str_22)

            def notStr_22():
                self.button_dotrevtype.config(image=self.error_image)
                self.message_dict['dotrevtype']['error'] = True
                self.tip_dotrevtype.configure(state='normal', text='Please choose a value from the dropdown list.')

            notStr_Command_22 = self.register(notStr_22)


            ############
            self.dotrevtype = Tk.StringVar()
    ##        if self.Fp['DOT_REV_TYPE_ID']:
    ##            self.dotrevtype.set(self.Fp['DOT_REV_TYPE_ID'])
    ##            self.message_dict['dotrevtype']['value'] = True  # set the validation to true

            # Validation rule: If it is OIT, then make this value 'Final'. If this is DOT, then make this value 'Draft'
            if USER in ['NJ OIT', 'NJ DOT', 'County', 'Other']:
                usedict = {'NJ OIT': 'Draft', 'NJ DOT': 'Final', 'County': 'Draft', 'Other': 'Draft'}
                self.dotrevtype.set(usedict[USER])
                self.message_dict['dotrevtype']['value'] = True
            else:   # this is not OIT, so it must be Baker, or somebody else
                self.dotrevtype.set('Draft')
                self.message_dict['dotrevtype']['value'] = True

            self.combo_dotrevtype = tk.Combobox(self.frm, textvariable=self.dotrevtype, values=Domains['REVIEW_TYPE'].values(), validate='focus', validatecommand = (is_Str_Command_22, '%d', '%i', '%S', '%P'), invalidcommand = (notStr_Command_22))
            self.combo_dotrevtype.grid(row=43,column=0,columnspan=2, pady=entrypadY, padx=entrypadX, ipadx = comboipadX, ipady = comboipadY)

            self.r_button_dotrevtype = Tk.Button(self.frm, relief='flat', image=self.greenbar_image)
            self.r_button_dotrevtype.grid(row=43,column=1, sticky='e',padx = rpadx, pady=rpady)
            self.tip_dotrevtype_desc = ToolTip(self.combo_dotrevtype, follow_mouse=1, text="(Domain) OIT review type id.")

            ########################################################################
            ########################################################################
            ##### Ok, Tool Info, Cancel
            ########################################################################
            def ok_validation(messages):

                # self.message_dict = {'addrlfr': {'error': False, 'value': False}}
                # first look to see if there are any error messages on any of the fields
                # then, check to see if all the required fields are populated
                any_errors = False
                req_fields = True
                report = {'validated': False, 'details': {'error': '', 'required': ''}}

                for f,val in messages.iteritems():
                    if val['error'] == True:
                        any_errors = True
                        report['details']['error'] = 'One or more fields has an error, please check all fields'

    ##            if messages['muniidL']['value'] == False:  # if the value for this feield has not been switches from false (default) to True, it throws an error.
    ##                req_fields = False
    ##                report['details']['required'] = report['details']['required'] + 'MUNI_ID_L  '
    ##            if messages['muniidR']['value'] == False:
    ##                req_fields = False
    ##                report['details']['required'] = report['details']['required'] + 'MUNI_ID_R  '
                if messages['elevfr']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'ELEV_FR  '
                if messages['elevto']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'ELEV_TO  '
                if messages['acctype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'ACC_TYPE  '
                if messages['surftype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'SURF_TYPE  '
                if messages['stattype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'STATUS_TYPE  '
                if messages['symbtype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'SYMBOL_TYPE  '
                if messages['travtype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'TRAV_TYPE  '
                if messages['juristype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'JURIS_TYPE  '
                if messages['oitrevtype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'OIT_REV_TYPE  '
                if messages['dotrevtype']['value'] == False:
                    req_fields = False
                    report['details']['required'] = report['details']['required'] + 'DOT_REV_TYPE  '

                if any_errors == False and req_fields == True:
                    report['validated'] = True
                    return report
                else:
                    return report



            def ok():
                self.logger.info('OK button pressed. SEG_GUID: {0}'.format(FpSegment['SEG_GUID']))
                ok_report = ok_validation(self.message_dict)   #report = {'validated': False, 'details': {'error': '', 'required': ''}}

                if ok_report['validated'] == False:

                    if ok_report['details']['error'] and ok_report['details']['required']:
                        Tkm.showerror('Validation Error', 'Field Errors: {0} \n\nMissing Required Fields: {1}'.format(ok_report['details']['error'], ok_report['details']['required'].replace('  ',', ')))
                    elif ok_report['details']['error'] and not ok_report['details']['required']:
                        Tkm.showerror('Validation Error', 'Field Errors: {0}'.format(ok_report['details']['error']))
                    elif not ok_report['details']['error'] and ok_report['details']['required']:
                        Tkm.showerror('Validation Error', 'Missing Required Fields: {0}'.format(ok_report['details']['required'].replace('  ',', ')))

                elif ok_report['validated'] == True:  # the user hit ok, and all of the fields look good...
                    try:
                        # Compile all of the field inputs into a Footprint object to pass back to the ArcMap process
                        self.Fields = {}
                        try: self.Fields['ADDR_L_FR'] = int(self.addrlfr.get())
                        except: self.Fields['ADDR_L_FR'] = None

                        try: self.Fields['ADDR_L_TO'] = int(self.addrlto.get())
                        except: self.Fields['ADDR_L_TO'] = None

                        try: self.Fields['ADDR_R_FR'] = int(self.addrrfr.get())
                        except: self.Fields['ADDR_R_FR'] = None

                        try: self.Fields['ADDR_R_TO'] = int(self.addrrto.get())
                        except: self.Fields['ADDR_R_TO'] = None

                        try: self.Fields['ZIPCODE_L'] = self.zipcodeL.get()
                        except: self.Fields['ZIPCODE_L'] = None

                        try: self.Fields['ZIPCODE_R'] = self.zipcodeR.get()
                        except: self.Fields['ZIPCODE_R'] = None

                        try: self.Fields['ZIPNAME_L'] = self.zipnameL.get()
                        except: self.Fields['ZIPNAME_L'] = None

                        try: self.Fields['ZIPNAME_R'] = self.zipnameR.get()
                        except: self.Fields['ZIPNAME_R'] = None

                        try:
                            self.Fields['MUNI_ID_L'] = self.muniidL.get()
                            if self.muniidL.get() == '':
                                self.Fields['MUNI_ID_L'] = None
                        except:
                            self.Fields['MUNI_ID_L'] = None

                        try:
                            self.Fields['MUNI_ID_R'] = self.muniidR.get()
                            if self.muniidR.get() == '':
                                self.Fields['MUNI_ID_R'] = None
                        except:
                            self.Fields['MUNI_ID_R'] = None

                        self.Fields['ELEV_TYPE_ID_FR'] = self.elevfr.get()
                        self.Fields['ELEV_TYPE_ID_TO'] = self.elevto.get()
                        self.Fields['ACC_TYPE_ID'] = self.acctype.get()
                        self.Fields['SURF_TYPE_ID'] = self.surftype.get()
                        self.Fields['STATUS_TYPE_ID'] = self.stattype.get()
                        self.Fields['SYMBOL_TYPE_ID'] = self.symbtype.get()
                        self.Fields['TRAVEL_DIR_TYPE_ID'] = self.travtype.get()
                        self.Fields['JURIS_TYPE_ID'] = self.juristype.get()
                        self.Fields['OIT_REV_TYPE_ID'] = self.oitrevtype.get()
                        self.Fields['DOT_REV_TYPE_ID'] = self.dotrevtype.get()

                        # Make self fields, just like Footprint, so it can be converted back to coded values
                        SplitFields = {'SEGMENT': [self.Fields]}
                        SplitFieldsDC = erebus.DomainConverter(Domains)
                        SplitFieldsCoded = SplitFieldsDC.ToCoded(SplitFields)

                        sys.stdout.write('OK***' + str(SplitFieldsCoded))

                        parent.destroy()

                        #['oitrevtype', 'juristype', 'addrlto', 'zipcodeR', 'muniidL','travtype', 'zipnameL','addrrfr', 'acctype', 'elevto', 'dotrevtype', 'addrlfr', 'stattype', 'zipnameR', 'elevfr', 'zipcodeL',
                        # 'muniidR', 'addrrto', 'surftype', 'symbtype']


    ##                    if SegmentNumber == '1':
    ##                        SplitOutput = {'SegmentNumber': 1, 'ADDR_L_FR': 5}
    ##                        output_path = os.path.join(scratchPath, "Split_Result_1.p")
    ##                    if SegmentNumber == '2':
    ##                        SplitOutput = {'SegmentNumber': 2, 'ADDR_L_FR': 5}
    ##                        output_path = os.path.join(scratchPath, "Split_Result_2.p")
    ##
    ##
    ##                    with open(output_path, 'wb') as output:
    ##                        pickle.dump(SplitOutput, output, -1)
    ##                    sys.stdout.write('OK')

                        self.logger.removeHandler(self.handler)

                    except:
                        self.logger.removeHandler(self.handler)
                        sys.stdout.write('error***' + traceback.format_exc())
                        parent.destroy()



            self.Bok = tk.Button(self.frm, text='OK', command=ok)
            self.Bok.grid(row=44,column=0, sticky='w', padx = buttonpadX, pady = buttonpadY)

            ##########################
            def tool_info():
                self.logger.info('Tool Info button pressed')
                help_split_path = os.path.join(os.path.dirname(__file__),'EditSegment.html')
                os.startfile(help_split_path)
            self.toolinfo = tk.Button(self.frm, text='Tool Info', command=tool_info)
            self.toolinfo.grid(row=44,column=0,sticky='e', padx = 0, pady = buttonpadY)  #default is 5 and 20



            ##########################
            def cancel():
                self.logger.info('Cancel button pressed. SEG_GUID: {0}'.format(FpSegment['SEG_GUID']))
                self.logger.removeHandler(self.handler)
                parent.destroy()

            self.cancel = tk.Button(self.frm, text='Cancel', command=cancel)
            self.cancel.grid(row=44,column=1, columnspan= 2, sticky='e', padx = 5, pady = buttonpadY)

            ########################################################################
            ########################################################################
            ## Create the frame window in the canvas

            self.create_window(0, 0, window=self.frm, anchor='nw')


            ########################################################################
            ########################################################################
            ### Create backround color for all of the required fields
            #self.combo_dotrevtype.configure(background = 'black')

        except:
            trace = traceback.format_exc()
            self.logger.exception(trace)
            self.logger.removeHandler(self.handler)


if __name__ == '__main__':

    SegmentNumber = sys.argv[1]
    scratchPath = sys.argv[2]
    Footprint = eval(sys.argv[3])  # {'SEGMENT_COMMENTS': [], 'SEG_GUID': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}', 'SLD_ROUTE': [{u'SIGN_NAME': None, u'UPDATE_USER': u'DM_EDIT', u'OBJECTID': 537377, u'SLD_COMMENT': None, u'SLD_DIRECTION': None, u'SRI': u'15331433__', u'ROUTE_TYPE_ID': 7, u'SLD_NAME': u'NNP', u'UPDATEDATE': datetime.datetime(2013, 6, 6, 9, 36, 56), u'GLOBALID': u'{AA82C335-E827-4141-A5FC-15D81223DCF7}'}], 'SEGMENT_TRANS': [{u'UPDATE_USER': u'OAXFARR', u'GLOBALID': u'{C9EC9A5E-2249-4104-BD47-1915778F2A75}', u'OBJECTID': 7192, u'SEG_GUID_ARCH': u'{A9ADE866-8958-4A68-9E6D-F1F23553C161}', u'SEG_ID_NEW': None, u'SEG_ID_ARCH': 284356, u'UPDATEDATE': datetime.datetime(2014, 6, 18, 19, 9, 46), u'SEG_GUID_NEW': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}'}], 'LINEAR_REF': [{u'MILEPOST_TO': 0.53, u'MILEPOST_FR': 0.296, u'UPDATE_USER': u'OAXFARR', u'GLOBALID': u'{3C28C3F6-EFF1-4637-BEF6-9C02A73DE81C}', u'OBJECTID': 1859714, u'SEG_GUID': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}', u'SRI': u'15331433__', u'UPDATEDATE': datetime.datetime(2014, 6, 18, 19, 9, 45), u'SEG_ID': 284356, u'SEG_TYPE_ID': u'P', u'RCF': None, u'LRS_TYPE_ID': 1}, {u'MILEPOST_TO': 0.53, u'MILEPOST_FR': 0.296, u'UPDATE_USER': u'OAXFARR', u'GLOBALID': u'{4C7D83F1-55FD-4E37-A01E-EBC00A36B810}', u'OBJECTID': 2540239, u'SEG_GUID': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}', u'SRI': u'15331433__', u'UPDATEDATE': datetime.datetime(2014, 6, 18, 19, 9, 45), u'SEG_ID': 284356, u'SEG_TYPE_ID': u'P', u'RCF': None, u'LRS_TYPE_ID': 3}, {u'MILEPOST_TO': 0.296, u'MILEPOST_FR': 0.53, u'UPDATE_USER': u'OAXFARR', u'GLOBALID': u'{4340115A-D0DF-4CD1-8351-A0F0E0DB4E87}', u'OBJECTID': 2049559, u'SEG_GUID': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}', u'SRI': u'15331433__', u'UPDATEDATE': datetime.datetime(2014, 6, 18, 19, 9, 45), u'SEG_ID': 284356, u'SEG_TYPE_ID': u'P', u'RCF': None, u'LRS_TYPE_ID': 2}], 'SEGMENT_CHANGE': [{u'UPDATE_USER': u'OAXFARR', u'GLOBALID': u'{4D34B734-26DA-406D-99BE-DDA1685309A0}', u'OBJECTID': 11949, u'SEG_GUID_ARCH': u'{A9ADE866-8958-4A68-9E6D-F1F23553C161}', u'CHANGE_ID': None, u'SHAPE.STLength()': 1444.2099705057376, u'COMMENTS': None, u'SHAPE': (565475.2778627565, 342316.6699573836), u'SEG_ID_ARCH': 284356, u'UPDATEDATE': datetime.datetime(2014, 6, 18, 19, 9, 46), u'CHANGE_TYPE_ID': u'R'}], 'SEG_NAME': [{u'DATA_SRC_TYPE_ID': 2, u'UPDATE_USER': u'OAXFARR', u'PRE_DIR': None, u'PRE_MOD': None, u'OBJECTID': 1403139, u'NAME_TYPE_ID': u'L', u'SEG_GUID': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}', u'NAME_FULL': u'Bengal Boulevard', u'RANK': 1, u'SEG_ID': 284356, u'SUF_MOD': None, u'PRE_TYPE': None, u'SUF_DIR': None, u'SUF_TYPE': u'Boulevard', u'UPDATEDATE': datetime.datetime(2014, 6, 18, 19, 9, 45), u'GLOBALID': u'{65A1FE44-ED69-4EB4-84B5-FBE24F09B1BA}', u'NAME': u'Bengal'}, {u'DATA_SRC_TYPE_ID': 2, u'UPDATE_USER': u'OAXFARR', u'PRE_DIR': None, u'PRE_MOD': None, u'OBJECTID': 1403140, u'NAME_TYPE_ID': u'L', u'SEG_GUID': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}', u'NAME_FULL': u'Rosehill Road', u'RANK': 2, u'SEG_ID': 284356, u'SUF_MOD': None, u'PRE_TYPE': None, u'SUF_DIR': None, u'SUF_TYPE': u'Road', u'UPDATEDATE': datetime.datetime(2014, 6, 18, 19, 9, 45), u'GLOBALID': u'{738CC78C-5B7D-420E-994B-F7AE30BBAAAE}', u'NAME': u'Rosehill'}], 'SEGMENT': [{u'ZIPNAME_R': u'BARNEGAT', u'TRAVEL_DIR_TYPE_ID': u'B', u'ADDR_R_FR': 172, u'SEG_ID': 284356, u'ADDR_L_TO': None, u'ZIPNAME_L': u'BARNEGAT', u'JURIS_TYPE_ID': u'PUB', u'OBJECTID': 574437, u'DOT_REV_TYPE_ID': u'F', u'SHAPE': (565660.8755947626, 342210.5093997336), u'SHAPE.STLength()': 1014.7184573452001, u'SYMBOL_TYPE_ID': 700, u'UPDATE_USER': u'OAXFARR', u'ACC_TYPE_ID': u'N', u'ZIPCODE_L': u'08005', u'SURF_TYPE_ID': u'I', u'MUNI_ID_L': u'882070', u'STATUS_TYPE_ID': u'A', u'ELEV_TYPE_ID_TO': 0, u'UPDATEDATE': datetime.datetime(2014, 7, 17, 13, 34, 12), u'ZIPCODE_R': u'08005', u'OIT_REV_TYPE_ID': u'F', u'ELEV_TYPE_ID_FR': 0, u'PRIME_NAME': u'Bengal Blvd', u'SEG_GUID': u'{F44D578B-84D7-4C26-A306-4C9953DC1C8C}', u'GLOBALID': u'{1118CB4E-C21C-40CA-B5D1-EA875CAD00A0}', u'ADDR_L_FR': None, u'MUNI_ID_R': u'882070', u'ADDR_R_TO': 192}], 'SEG_SHIELD': []}
    Domains = eval(sys.argv[4])

    if Domains == None:
        #get Split1_Footprint back
        domains_path = os.path.join(scratchPath, "domains.p")
        if os.path.exists(domains_path):
            with open(domains_path,'rb') as domains_open:
                Domains = pickle.load(domains_open)

    # convert the coded values in footprint to domain values, for initial population of the tool fields
    DC = erebus.DomainConverter(Domains)
    Footprint_domain = DC.ToDomain(Footprint)

    # Get the segment Dictionary
    FpSegment = Footprint_domain['SEGMENT'][0]
    #print Footprint_domain
    # Convert to Domain

    root = Tk.Tk()
    #splitcanv = SplitCanvas(root, SegmentNumber = 1, scratchPath = 'Fake')
    root.minsize(200,400)
    root.geometry("330x800")
    root.title("Edit Segment")
    root.iconbitmap(os.path.join(os.path.dirname(__file__),'gis_logo_stackT.ico'))

    ## Grid sizing behavior in window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Get the user
    USER = ''
    njre_config_path = os.path.join(os.path.dirname(__file__), 'njre_config.p')  #['NJ OIT', 'NJ DOT', 'County', 'Other']
    if os.path.exists(njre_config_path):
        with open(njre_config_path,'rb') as njreconfig:
            USER = pickle.load(njreconfig)

    # launch the UI
    splitcanv = SegmentCanvas(root, SegmentNumber, scratchPath, FpSegment, Domains, USER)

    splitcanv.configure(width=320, height=800)
    splitcanv.configure(scrollregion=(0,0,320, 1100))
    splitcanv.grid(row=0, column=1, sticky='nswe')  # 0,0

    ## Scrollbars for canvas
    hScroll = tk.Scrollbar(root, orient=Tk.HORIZONTAL, command=splitcanv.xview)
    hScroll.grid(row=1, column=0, columnspan = 2, sticky='we') # 1,0  row=1, column=0,
    vScroll = tk.Scrollbar(root, orient=Tk.VERTICAL, command=splitcanv.yview)
    vScroll.grid(row=0, column=2, sticky='ns')  # 0,1
    splitcanv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)

    root.mainloop()
