#  create_dicts_misc2.py
#  purpose and function - parse input of street names into a set of fields compliant with the
#  FGDC thoroughfare standard using a list of keywords in a data table to look up any abbreviations
#  this code is in development
#  date created 20130829
#  date revised, author & description of revision (repeat as needed)
#  code author: christian jacqz, MassGIS, Information Technology Division, Commmonwealth of Massachusetts
#  email    christian.jacqz@state.ma.us
# *****************************************************************************************************
#  copyright to thie code is owned by Commonwealth of Massachusetts. License is hereby granted to any
#  GOVERNMENT OR NON-COMMERCIAL entity to use, extend, adapt and distribute this code (including modules referenced
#  in import statements that are not part of standard python and numpy distributions) subject to the termns of the
#  Mozilla Public License, version 1.1 found at http://www.mozilla.org/MPL/.  Commercial entities may also
#  use this code under the same license BUT ONLY while performing services under contract to a government entity
#  in which case this header, all code and any derivatives must be provided to the government entity at the time of use.
#  Other commercial use is prohibited unless express written permission is obtained.
#  This header and license must be retained in any redistribution including all derivative products.
#  *******************************************************************************************************

# NUMBER LOOKUP - this standardizes 1-10 as spelled out, greater as numbered
# num_lookup routine above translates any single token number input to standard output
# see code below for adding hyphens so pairs of tokens also translate correctly
def create_num_lookup():
    num_lookup = {}
    lt_twenty = {
        1:('FIRST','1ST'),
        2:('SECOND','2ND'),
        3:('THIRD','3RD'),
        4:('FOURTH','4TH'),
        5:('FIFTH','5TH'),
        6:('SIXTH','6TH'),
        7:('SEVENTH','7TH'),
        8:('EIGHTH','8TH'),
        9:('NINTH','9TH'),
        10:('TENTH','10TH'),
        11:('ELEVENTH','11TH'),
        12:('TWELFTH','12TH'),
        13:('THIRTEENTH','13TH'),
        14:('FOURTEENTH','14TH'),
        15:('FIFTEENTH','15TH'),
        16:('SIXTEENTH','16TH'),
        17:('SEVENTEENTH','17TH'),
        18:('EIGHTEENTH','18TH'),
        19:('NINETEENTH','19TH')
    }

    even_tens = {
        20:('TWENTIETH','20TH'),
        30:('THIRTIETH','30TH'),
        40:('FORTIETH','40TH'),
        50:('FIFTIETH','50TH'),
        60:('SIXTIETH','60TH'),
        70:('SEVENTIETH','70TH'),
        80:('EIGHTIETH','80TH'),
        90:('NINETIETH','90TH')
    }

    between_tens = {
        2:('TWENTY-',''),
        3:('THIRTY-',''),
        4:('FORTY-',''),
        5:('FIFTY-',''),
        6:('SIXTY-',''),
        7:('SEVENTY-',''),
        8:('EIGHTY-',''),
        9:('NINETY-','')
    }

    for i in range(1,100):
        if i < 20:
            num_lookup[lt_twenty[i][1]]=lt_twenty[i][0]
        elif not i%10:
            num_lookup[even_tens[i][1]]=even_tens[i][0]
        else:
            text = between_tens[i/10][0]+lt_twenty[i%10][0]
            number = str(i/10)+lt_twenty[i%10][1]
            num_lookup[number]=text
    return num_lookup

# THIS IS THE DICTIONARY for TUPLES of allowable domain seqnences
# FOR A GIVEN NUMBER OF TOKENS, LOOK UP THE SET OF TUPLES
# THAT REPRESENTs LEGAL ASSIGNMENTS OF TOKENS TO DOMAINS
# fields are:
# pm pre-modifier
# pd pre-directional
# hpd highway pre-directional (north -> northbound)
# pt pre-type
# hpt highway pre-type
# bn basename, bt base-type all map to the basename field
# example of bt would be "BROADWAY"  a one-word street name that's implicitly typed
# hpd highway pre-directional (north -> northbound)
# pt pre-type
# hpt highway pre-type
# st post type
# sd post directional
# sm post modifier eg. "Alternate" or "Extended" when separated from name as per PIDF-LO def
# create dictionary, keyed on total count of tokens, of lists of allowable domain sequences

def create_dctdsl():
    dl =['PM','PD','HPD','PT','HPT','BT','BN','ST','HST','SD','HSD','SM']
    # create dictionary, keyed on total count of tokens, of lists of allowable domain sequences
    dctdsl = {}
    for pm in range(2):
        for pd in range(2):
            for hpd in range(2):
                for pt in range(2):   # could be one name
                    for hpt in range(2):
                        for bt in range(2):  # basename that is also type
                            for bn in range(6):  # five possible basenames could be none if bt
                                for st in range(3):  #0,1,2
                                    for hst in range(2):
                                        for sd in range(2):
                                            for hsd in range(2):
                                                for sm in range(6):   # tried editing change 2 to 6 to test qa function
                                                    # total number of tokens used as key for dictionary
                                                    nt = pm + pd + hpd + pt + hpt + bn + bt + st + hst + sd + hsd + sm
                                                    # rules for highway and non-highway types or directionals
                                                    h1 = hpt + hpd + hst + hsd
                                                    p1 = pd + pt + st + sd
                                                    # h1 * p1 == 0  -- can't mix and match highway and non-highway types or dirs
                                                    p2 = pd + sd
                                                    # p2 < 2  -- can't have two directionals, review manually
                                                    h2 = hpd + hsd
                                                    h3 = hpt + hst
                                                    # h2 <= h3 < 2 -- have to have either highway pre or post type to have at most one highway dir
                                                    n1 = bool(bn) + bt
                                                    # n1 == 1   either a basetype or basename but not both
                                                    t1 = bt + bool(pt+st) + hst + hpt

                                                    # t1 == 1  either a basetype or pre and/or post type or highway pre or post type
                                                    p3 = bool(pd + pt)*1
                                                    s2 = bool(sd + st)*2
                                                    sm1 = bool(sm)*1
                                                    hptn = hpt*bn   # not more than one bn with hpt
                                                    hptb = hpt + bt

                                                    # separate pm by pd or pt from name  pm <= p3, sm <= s2
                                                # if t1 == 1 and p2 < 2 and h1 * p1 == 0 and h2 <= h3 < 2 and n1 == 1 and pm <= p3 and sm1 <= s2 and h1 < 3 and p1 < 3:
                                                # take out requirement that have a type - what happens?
                                                    if p2 < 2 and h1 * p1 == 0 and h2 <= h3 < 2 and n1 == 1 and pm <= p3 and sm1 <= s2 and h1 < 3 and p1 < 3 and hptn <= 1 and hptb <=1 :

                                                        can = []
                                                        ct = (pm,pd,hpd,pt,hpt,bt,bn,st,hst,sd,hsd,sm)
                                                        for di in range(12):
                                                            can += [dl[di]]*ct[di]
                                                        if dctdsl.has_key(nt):
                                                            dctdsl[nt].append(can)
                                                        else:
                                                            dctdsl[nt] = [can]
                                                        #if can[0] == 'HPT':
                                                         #   print can, hpd, bn, hptn

    dctdsl[2].append(['BT','ST'])
    dctdsl[3].append(['PM','HPT','BN'])
    dctdsl[4].append(['BN','ST','ST','SD'])
    dctdsl[4].append(['PM','PT','BN','SD'])
    dctdsl[3].append(['HPT','BN','SM'])
    dctdsl[4].append(['HPT','BN','SM','SM'])
    dctdsl[5].append(['HPT','BN','SM','SM','SM'])
    dctdsl[6].append(['HPT','BN','SM','SM','SM','SM'])
    dctdsl[4].append(['HPT','BN','HSD','SM'])
    dctdsl[5].append(['HPT','BN','HSD','SM','SM'])
    dctdsl[6].append(['HPT','BN','HSD','SM','SM','SM'])



    return dctdsl

# for testing
# dctdsl = create_dctdsl()
# for i in range(1,5):
#    d = dctdsl[i]
#    for dd in d:
#        print dd
pass

def intl(l):
    for i in range(len(l)):
        try:
            l[i] = int(l[i])
        except ValueError:
            pass
    return l

def create_key_lists(input_keywds):
    fk = open(input_keywds,'r')
    krl = [r.split('\t')[1:-1] for r in fk.readlines()]
    kd = {}
    max_k = 0
    for kr in krl[1:]:   #skip the first record of field headings
        t = kr[0]
        kr = intl(kr)
        if kd.has_key(t):
            kd[t].append(kr)
        else:
            kd[t] = [kr]
    return kd  # no longer return pairs, after implementing grouping algorithm
