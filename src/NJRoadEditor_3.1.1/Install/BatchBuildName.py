#-------------------------------------------------------------------------------
# Name:         BatchBuildName
# Purpose:      module for NJRoadEditor python add-in
#
# Author:       NJ Office of GIS
# Contact:      njgin@oit.nj.gov
#
# Created:      6/24/2014
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

import os, sys
import arcpy
from multiprocessing import Process, Lock, Queue, Pipe
import time
import traceback, datetime
os.sys.path.append(os.path.dirname(__file__))
import erebus
import numpy as np

def editprocess(workspace, table, fields, rows, values, lock, pipe, stoped = True):
    edit = arcpy.da.Editor(workspace)
    edit.startEditing()
    edit.startOperation()

##    pipe.send(['message from child process {0}'.format(rows[3])])
##    pipe.close()

    start = rows[1]
    end = rows[2]
    nn = values

    with lock:
        print 'child process {0} started on {1}...'.format(rows[3], rows[0])

    try:
        with arcpy.da.UpdateCursor(table, [fields]) as cursor:
            i = 0
            for row in cursor:
                if i >= start and i <= end:
                    row[0] = rows[3] #values[i]
                    cursor.updateRow(row)
                    i += 1

        edit.stopOperation()
        edit.stopEditing(True)
    except:
        trace = traceback.format_exc()
        pipe.send(['Message from child process {0}: Process failed. Traceback: {1}'.format(rows[3], trace)])
        pipe.close()

        with lock:
            print arcpy.GetMessages()

    pipe.send(['First Message from child process {0}: Process succeeded'.format(rows[3])])
    #pipe.send(['Second Message from child process {0}: Process succeeded'.format(rows[3])])
    pipe.close()

    with lock:
        print 'child process {0} completed on {1}'.format(rows[3], rows[0])



def editprocessProd(workspace, table, fields, values, lock, stop_ed=True):
    edit = arcpy.da.Editor(workspace)
    edit.startEditing()
    #edit.startOperation()

    try:
        for value in values:
            edit.startOperation()
            sqlquery = "%s = '%s'" % ("GLOBALID", value[1])

            with arcpy.da.UpdateCursor(table, [fields], sqlquery) as cursor:
                for row in cursor:
                    row[0] = value[0]
                    cursor.updateRow(row)

            edit.stopOperation()
        edit.stopEditing(stop_ed)
    except arcpy.ExecuteError:
        try: row; del row
        except: pass
        try: cursor; del cursor
        except: pass
        try: edit.stopOperation()
        except: pass
        try: edit.stopEditing()
        except: pass
        with lock:
            print arcpy.GetMessages()


def editprimenameProd(workspace, table, fields, namekeeper, pipe, lock, stop_ed=True):
    print os.environ.get("USERNAME").lower()
    #file = open(os.path.join(r"C:\Users\oaxfarr\Documents\Scratch", workspace.split("\\")[1].split(".")[0] + ".txt"), "w+")
    file = open(os.path.join(r"C:\Users", os.environ.get("USERNAME").lower(), r"Documents\ArcGIS\Default.gdb", workspace.split("\\")[1].split(".")[0] + ".txt"), "w+")   #C:\Users\oaxfarr\Documents\ArcGIS\Default.gdb
    file.write('Process Started at {0}\n'.format(str(datetime.datetime.now())))
    file.close()
    edit = arcpy.da.Editor(workspace)
    edit.startEditing()

    try:
        rowcounter = 0
        updatecounter = 0
        for key,value in namekeeper.iteritems():  #{u'{0B41DB6A-1708-11E3-B5F2-0062151309FF}': u'Ventura Dr'}
            edit.startOperation()
            sqlquery = "%s = '%s'" % ("SEG_GUID", key)
            with arcpy.da.UpdateCursor(table, [fields], sqlquery) as cursor:
                for row in cursor:
                    row[0] = value
                    cursor.updateRow(row)
                    updatecounter += 1
            edit.stopOperation()
            rowcounter += 1
            if updatecounter in (1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000,21000,22000,23000,24000,25000,26000,27000,28000,29000,30000,31000,32000,33000,34000,35000,36000,37000,38000,39000,40000,41000,42000,43000,44000,45000,46000,47000,48000,49000,50000,51000,52000,53000,54000,55000):
                with open(os.path.join(r"C:\Users\oaxfarr\Documents\Scratch", workspace.split("\\")[1].split(".")[0] + ".txt"), "a") as file:
                    file.write("Updates: {0}, Time: {1}\n".format(updatecounter, str(datetime.datetime.now())))
##                if updatecounter == 10000:
##                    break
                edit.stopEditing(stop_ed)
                edit = arcpy.da.Editor(workspace)
                edit.startEditing()



##            if rowcounter == 1000:
##                break
        edit.stopEditing(stop_ed)
        pipe.send(['Message from child process {0}: Number of rows {1}, Number of updates: {2}'.format(workspace, str(rowcounter), str(updatecounter))])
        pipe.close()

    except:
        try: row; del row
        except: pass
        try: cursor; del cursor
        except: pass
        try: edit.stopOperation()
        except: pass
        try: edit.stopEditing()
        except: pass
        with lock:
            print arcpy.GetMessages()






if __name__ == '__main__':

    print sys.argv
    print len(sys.argv)


    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################

    if sys.argv[1] == 'segname_production':

        #segnametab = os.path.join(r'Database Connections\road_child0.sde', sys.argv[2].upper() + '.SEG_NAME')
        segnametab = os.path.join(sys.argv[3], sys.argv[2].upper() + '.SEG_NAME')

        i = 0
        fullname = []
        sn_globalid = []
        #print('Building fullname started at {0}'.format(str(datetime.datetime.now())))
        with arcpy.da.SearchCursor(segnametab, ["PRE_DIR","PRE_TYPE","PRE_MOD","NAME","SUF_TYPE","SUF_DIR","SUF_MOD","GLOBALID"]) as cursor:
            for row in cursor:
##                nnn = erebus.FullName(row[0],row[1],row[2],row[3],row[4],row[5],row[6]).concatenate()
##                if nnn:
                fullname.append(erebus.FullName(row[0],row[1],row[2],row[3],row[4],row[5],row[6]).concatenate())
                sn_globalid.append(row[7])
                i += 1

        #print('Building fullname ended at {0}'.format(str(datetime.datetime.now())))
        #print('fullname rows test: {0}'.format(fullname[0:5]))

        # which rows actually need to be replaced??
        i = 0
        zz = np.zeros((len(fullname),), dtype=np.int)
        print('Pruning fullname started at {0}'.format(str(datetime.datetime.now())))
        with arcpy.da.SearchCursor(segnametab, ["SEG_GUID","NAME_FULL"]) as cursor:
            for row in cursor:
                if fullname[i] != row[1] and fullname[i]:
                    zz[i] = 1
                i += 1
        print('Pruning fullname completed at {0}. The number of rows to be replaced is {1}'.format(str(datetime.datetime.now()), str(zz.sum())))


        nameglobal = zip(fullname,sn_globalid, zz)
        #print('Variable nameglobal: {0}'.format(nameglobal[0:5]))

##[(u'Lightning Division Memorial Highway', u'{00000D6E-179A-4BC1-A002-94824C9A6E3E}'), (u'Interstate 78', u'{00001636-B494-4E26-B849-6E4B0D8BDF6B}'), (u'Lightening Division Memorial Highway', u'{00001686-D7FE-4B1C-B2B1-EBC68B7AD304}'), (u'Interstate 78', u'{00002F9E-CCEB-41D4-A0A8-1F73160C8980}'), (u'Us Highway 22', u'{0000324F-B612-4BE5-ADD7-7A6805CC75EB}')]

        # Prune nameglobal so that only the rows that need to be updated are included
        nameglobal_prune = []
        for ng in nameglobal:
            if ng[2] == 1:
                nameglobal_prune.append(ng)

        print('Pruning nameglobal completed at {0}. The number of rows to be replaced is {1}'.format(str(datetime.datetime.now()), len(nameglobal_prune)))
        ####################################################################
        ## Define Variables


        #workspace = r'Database Connections\ROAD@gis7t@1525.sde'
        #table = r'Database Connections\ROAD@gis7t@1525.sde\ROAD.SEG_NAME'
        fields = 'NAME_FULL'
        # "workspace", "start", "end", "table"

        v_names = ['road_child0', 'road_child1', 'road_child2','road_child3' ,'road_child4' ,'road_child5' ,'road_child6' ,'road_child7']
        wksps = []
        tables = []
        for v_name in v_names:
            wksps.append(os.path.join('Database Connections', v_name + '.sde'))
            tables.append(os.path.join('Database Connections', v_name + '.sde', sys.argv[2].upper() + '.SEG_NAME'))

        # break up the job
        steps = np.round(np.linspace(start=0, stop = len(nameglobal_prune), num = 9))  #array([      0.,   85333.,  170666.,  255998.,  341331.,  426664., 511996.,  597329.,  682662.])
        steps = steps.astype(np.int)
        steps = steps.tolist()
        starts = steps[0:8]
        ends = steps[1:9]

        inputsvars = zip(wksps, starts, ends, tables)
        print('\nVariable inputvars to be sent to the 8 processes: {0}'.format(inputsvars))  ## [('Database Connections\\road_child0.sde', 0, 85333, 'Database Connections\\road_child0.sde\\ROAD.SEG_NAME'), ('Database Connections\\road_child1.sde', 85333, 170666, 'Database Connections\\road_child1.sde\\ROAD.SEG_NAME'), ('Database Connections\\road_child2.sde', 170666, 255998, 'Database Connections\\road_child2.sde\\ROAD.SEG_NAME'), ('Database Connections\\road_child3.sde', 255998, 341331, 'Database Connections\\road_child3.sde\\ROAD.SEG_NAME'), ('Database Connections\\road_child4.sde', 341331, 426664, 'Database Connections\\road_child4.sde\\ROAD.SEG_NAME')]

        lock2 = Lock()

        ####################################################################
        ## Run the processes
        print('Main editing process starting...')

        if ends[0] == 0:
            print('\n**No edits need to be made**')
        else:
            # (workspace, table, fields, values, lock, stop_ed = True)
            gg = 0
            ps = []
            for inv in inputsvars:
                if gg == 7:
                    end = inv[2] + 1
                else:
                    end = inv[2]
                print('\nChild process: "{0}" started at {1}...'.format(inv[0], str(datetime.datetime.now())))

                #('Database Connections\\road_child0.sde', 0, 85333, 'Database Connections\\road_child0.sde\\ROAD.SEG_NAME')
                #editprocessProd(workspace, table, fields, values, lock, stop_ed=True)

                p = Process(target=editprocessProd, args=(inv[0], inv[3], fields, nameglobal_prune[inv[1]:end], lock2))
                p.start()
                gg += 1
                ps.append(p)

            b = 0
            for p in ps:
                print 'p joining...'
                p.join()
                print('child process {0} ended at {1}...'.format(inputsvars[b], str(datetime.datetime.now())))
                b += 1

            with lock2:
                print('Main editing process exit.')



    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################

    if sys.argv[1] == 'primename_production':
        #segnametab = os.path.join(r'Database Connections\road_child0.sde', sys.argv[2].upper() + '.SEG_NAME')
        #segmentfc = os.path.join(r'Database Connections\road_child0.sde', sys.argv[2].upper() + '.Centerline', sys.argv[2].upper() + '.SEGMENT')

        segnametab = os.path.join(sys.argv[3], sys.argv[2].upper() + '.SEG_NAME')
        segmentfc = os.path.join(sys.argv[3], sys.argv[2].upper() + '.Centerline', sys.argv[2].upper() + '.SEGMENT')

        rr = 0
        namekeeperL = {} # this will be
        namekeeperH = {}
        with arcpy.da.SearchCursor(segnametab, ["SEG_GUID", "RANK", "NAME_TYPE_ID","PRE_DIR","PRE_TYPE","PRE_MOD","NAME","SUF_TYPE","SUF_DIR","SUF_MOD"]) as cursor:
            for row in cursor:
                if row[1] == 1 and row[2] == 'L':
                    fullname = erebus.FullName(row[3],row[4],row[5],row[6],row[7],row[8],row[9]).concatenate()
                    namekeeperL[row[0]] = [fullname, str(row[1]) + str(row[2])]
                if row[1] == 1 and row[2] == 'H':
                    fullname = erebus.FullName(row[3],row[4],row[5],row[6],row[7],row[8],row[9]).concatenate()
                    namekeeperH[row[0]] = [fullname, str(row[1]) + str(row[2])]

        ########################################################################
        ## Make namekeeper for both
        namekeeper = namekeeperL   # {'{FF04CCE0-1707-11E3-B5F2-0062151309FF}': [fullname, 'L1']}

        for i in range(len(namekeeperH)):
            try:
                namekeeper[namekeeperH.keys()[i]]
            except:
                namekeeper[namekeeperH.keys()[i]] = namekeeperH[namekeeperH.keys()[i]]


        print('namekeeperL: {0}\nlength of namekeeperL: {1}'.format(namekeeperL.items()[0], len(namekeeperL)))
        print('namekeeperH: {0}\nlength of namekeeperH: {1}'.format(namekeeperH.items()[0], len(namekeeperH)))
        print('namekeeper: {0}\nlength of namekeeper: {1}'.format(namekeeper.items()[0], len(namekeeper)))

        ########################################################################
        ## Keep only namekeepr that is different from PRIME_NAME

        pn = {}
        with arcpy.da.SearchCursor(segmentfc, ["SEG_GUID", "PRIME_NAME"]) as cursor:
            for row in cursor:
                pn[row[0]] = row[1]
        print('pn: {0}\nlength of pn: {1}'.format(pn.items()[0], len(pn)))

        pn_pruned = {}
        for key,value in pn.iteritems():
            if value:
                try:
                    if value != namekeeper[key][0]:
                        pn_pruned[key] = namekeeper[key][0]
                except KeyError:
                    pass

        if not pn_pruned:
            print('\n**No edits will be made, PRIME_NAME values are all unabreviated and in sync with SEG_NAME**')
        else:
            print('pn_pruned: {0}\nlength of pn_pruned: {1}'.format(pn_pruned.items()[0], len(pn_pruned)))

            ################################################
            ## set up the job environment

            v_names = ['road_child0', 'road_child1', 'road_child2','road_child3' ,'road_child4' ,'road_child5' ,'road_child6' ,'road_child7']
            wksps = []
            tables = []
            for v_name in v_names:
                wksps.append(os.path.join('Database Connections', v_name + '.sde'))
                tables.append(os.path.join('Database Connections', v_name + '.sde', sys.argv[2].upper() + '.Centerline' , sys.argv[2].upper() + '.SEGMENT'))


            ################################################
            ## break up the job
            steps = np.round(np.linspace(start=0, stop = len(pn_pruned), num = 9))  #array([      0.,   85333.,  170666.,  255998.,  341331.,  426664., 511996.,  597329.,  682662.])
            steps = steps.astype(np.int)
            steps = steps.tolist()
            starts = steps[0:8]
            ends = steps[1:9]

            inputsvars = zip(wksps, starts, ends, tables)  #('Database Connections\\road_child0.sde', 0, 85333, 'Database Connections\\road_child0.sde\\ROAD.SEGMENT')
            print('Variable inputvars for PRIME_NAME: {0}'.format(inputsvars))   ## Variable inputvars for PRIME_NAME: [('Database Connections\\road_child0.sde', 0, 53768, 'Database Connections\\road_child0.sde\\ROAD.SEGMENT'), ('Database Connections\\road_child1.sde', 53768, 107535, 'Database Connections\\road_child1.sde\\ROAD.SEGMENT'), ('Database Connections\\road_child2.sde', 107535, 161303, 'Database Connections\\road_child2.sde\\ROAD.SEGMENT'), ('Database Connections\\road_child3.sde', 161303, 215070, 'Database Connections\\road_child3.sde\\ROAD.SEGMENT'), ('Database Connections\\road_child4.sde', 215070, 268838, 'Database Connections\\road_child4.sde\\ROAD.SEGMENT'), ('Database Connections\\road_child5.sde', 268838, 322606, 'Database Connections\\road_child5.sde\\ROAD.SEGMENT'), ('Database Connections\\road_child6.sde', 322606, 376373, 'Database Connections\\road_child6.sde\\ROAD.SEGMENT'), ('Database Connections\\road_child7.sde', 376373, 430141, 'Database Connections\\road_child7.sde\\ROAD.SEGMENT')]

            ####################################################################
            ## Run the processes
            print('Main editing process starting on PRIME_NAME...')

            if ends[0] == 0:
                print('No edits will be made, PRIME_NAME values are all unabreviated and in sync with SEG_NAME')
            else:

    ##            file = open(os.path.join(r"C:\Users\oaxfarr\Documents\Scratch", "Updates.txt"), "w+")
    ##            file.write('inputvars is: {0}\n'.format(inputsvars))
    ##            file.close()


                lock2 = Lock()
                fields = 'PRIME_NAME'
                gg = 0
                parent_connections = []
                ps = []
                for inv in inputsvars:
                    if gg == 7:
                        end = inv[2] + 1
                    else:
                        end = inv[2]
                    print('\nChild process: "{0}" started at {1}...'.format(inv[0], str(datetime.datetime.now())))
                    parent_connection, child_connection = Pipe()
                    parent_connections.append(parent_connection)
                    p = Process(target=editprimenameProd, args=(inv[0], inv[3], fields, dict(pn_pruned.items()[inv[1]:end]), child_connection, lock2))   #editprimenameProd(workspace, table, fields, namekeeper, lock, stop_ed=True)
                    print(dict(pn_pruned.items()[inv[1]:inv[1]+1]))  #{u'{0B41DB6A-1708-11E3-B5F2-0062151309FF}': u'Ventura Dr'}
                    p.start()
                    gg += 1
                    ps.append(p)


        ##        kr = True
        ##        cc = []
        ##        while kr:
        ##            if len(cc) == 8:
        ##                if cc[0] == True and cc[1] == True and cc[2] == True and cc[3] == True and cc[4] == True and cc[5] == True and cc[7] == True and cc[7] == True:
        ##                    break
        ##            hh = 0
        ##            for parent_connection in parent_connections:
        ##                if parent_connection.poll():
        ##                    with lock2:
        ##                         print 'Parent received message: %s' % parent_connection.recv()
        ##                    parent_connection.close()
        ##                    cc.append(True)
        ##                else:
        ##                    with lock2:
        ##                        print 'no messages from child {0}...'.format(str(hh))
        ##                if len(cc) == 8:
        ##                    if cc[0] == True and cc[1] == True and cc[2] == True and cc[3] == True and cc[4] == True and cc[5] == True and cc[7] == True and cc[7] == True:
        ##                        break
        ##                hh += 1
        ##            time.sleep(60)



                b = 0
                for p in ps:
                    print 'p joining...'
                    p.join()
                    print('child process {0} ended at {1}...'.format(inputsvars[b], str(datetime.datetime.now())))
                    b += 1

                with lock2:
                    print('Main editing process exit.')

    ##            for parent_connection in parent_connections:
    ##                if parent_connection.poll():
    ##                    with lock2:
    ##                         print 'Parent received message: %s' % parent_connection.recv()
    ##                    parent_connection.close()




    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################


    # things have changed up above, so this needs to be redone...
    if sys.argv[1] == 'test':

        #workspace = r'Database Connections\ROAD@gis7t@1525.sde'
        #table = r'Database Connections\ROAD@gis7t@1525.sde\ROAD.SEG_NAME'
        fields = 'NAME_FULL'
        testrows = [[r'Database Connections\road_child0.sde',0,9,'first', r'Database Connections\road_child0.sde\ROAD.SEG_NAME'],
            [r'Database Connections\road_child1.sde',0,9,'middle', r'Database Connections\road_child1.sde\ROAD.SEG_NAME'],
            [r'Database Connections\road_child2.sde',0,9,'last', r'Database Connections\road_child2.sde\ROAD.SEG_NAME'],
            [r'Database Connections\road_child3.sde',0,9,'last', r'Database Connections\road_child3.sde\ROAD.SEG_NAME'],
            [r'Database Connections\road_child4.sde',0,9,'last', r'Database Connections\road_child4.sde\ROAD.SEG_NAME'],
            [r'Database Connections\road_child5.sde',0,9,'last', r'Database Connections\road_child5.sde\ROAD.SEG_NAME'],
            [r'Database Connections\road_child6.sde',0,9,'last', r'Database Connections\road_child6.sde\ROAD.SEG_NAME'],
            [r'Database Connections\road_child7.sde',0,9,'last', r'Database Connections\road_child7.sde\ROAD.SEG_NAME']]
        values = 'OGIS'
        lock2 = Lock()

        ############################################################################
        print('Main editing process starting...')

        ps = []
        parent_connections = []
        for rows in testrows:
            parent_connection, child_connection = Pipe()
            parent_connections.append(parent_connection)
            p = Process(target=editprocess, args=(rows[0], rows[4], fields, rows, values, lock2, child_connection))
            p.start()
            ps.append(p)



        kr = True
        cc = []
        while kr:
            if len(cc) == 8:
                if cc[0] == True and cc[1] == True and cc[2] == True and cc[3] == True and cc[4] == True and cc[5] == True and cc[7] == True and cc[7] == True:
                    break
            hh = 0
            for parent_connection in parent_connections:
                if parent_connection.poll():
                    with lock2:
                         print 'Parent received message: %s' % parent_connection.recv()
                    parent_connection.close()
                    cc.append(True)
                else:
                    with lock2:
                        print 'no messages from child {0}...'.format(str(hh))
                if len(cc) == 8:
                    if cc[0] == True and cc[1] == True and cc[2] == True and cc[3] == True and cc[4] == True and cc[5] == True and cc[7] == True and cc[7] == True:
                        break
                hh += 1
            time.sleep(5)



        for p in ps:
            with lock2:
                print 'p joining...'
            p.join()



        with lock2:
            print('Main editing process exit.')