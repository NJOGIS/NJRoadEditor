#  fgdc_parser.py
#  purpose and function - parse input of street names into a set of fields compliant with the
#  FGDC thoroughfare standard using a list of keywords in a data table to look up any abbreviations
#  dependancies ? works with python 2.7 probably works with earlier but numpy must be installed (as it is with ArcGIS 10)
#  revised 20130829 to deal with concatenating types and directionals for highways - "south" -> "southbound" post-mod
#  code author: christian jacqz, MassGIS, Information Technology Division, Commmonwealth of Massachusetts
#  email    christian.jacqz@state.ma.us
# *****************************************************************************************************
#  copyright to thie code is owned by Commonwealth of Massachusetts. License is hereby granted to any
#  GOVERNMENT OR NON-COMMERCIAL entity to use, extend, adapt and distribute this code (including modules referenced
#  in import statements that are not part of standard python and numpy distributions) subject to the terms of the
#  Mozilla Public License, version 1.1 found at http://www.mozilla.org/MPL/.  Commercial entities may also
#  use this code under the same license BUT ONLY while performing services under contract to a government entity
#  in which case this header, all code and any derivatives must be provided to the government entity at the time of use.
#  Other commercial use is prohibited unless express written permission is obtained.
#  This header and license must be retained in any redistribution including all derivative products.
import os, sys, re, csv, traceback
import numpy as np

class ParseName(object):
    """Parse a one-line road name into seven parts."""

    def __init__(self, name):
        from create_dicts_misc2 import create_dctdsl, create_num_lookup
        #global thisdir
        #print 'ThisFile  ', fgdc_parser.__path__
        self.name = name
        #print self.name
        #print os.path.dirname(__file__)
        #print os.path.join(thisdir, 'keywords_flipped.csv')
        self.keywordsfile = os.path.join(os.path.dirname(__file__), 'keywords_flipped.csv')
        # turn this into a list of tuples.
        domain_list = []
        infile = open(self.keywordsfile, 'r')
        reader = csv.reader(infile)
        for line in reader:
            domain_list.append(line)

        # in order to speed up processing, the domains are loaded into memory
        # and indexed by both complete phrase and initial word of the input
        self.domain_indexed_by_initial_token = {}
        self.domain_indexed_by_complete_phrase = {}

        for domain_record in domain_list:
            input_string = domain_record[0]
            initial_token = input_string.split()[0]
            number_tokens = len(input_string.split(' '))
            if input_string in self.domain_indexed_by_complete_phrase:
                self.domain_indexed_by_complete_phrase[input_string].append(list(domain_record))
            else:
                self.domain_indexed_by_complete_phrase[input_string]= [list(domain_record)]
            domain_record.insert(0,number_tokens)
            if initial_token in self.domain_indexed_by_initial_token:
                self.domain_indexed_by_initial_token[initial_token].append(domain_record)
            else:
                self.domain_indexed_by_initial_token[initial_token]=[domain_record]

        # the routine in this attached script creates the list of all allowable "sequences" of type
        self.dctdsl = create_dctdsl()
        # also create a lookup table to standardize all forms of numbers
        self.num_lookup = create_num_lookup()

    def parse(self):

        try:

            # the following section sets up some regular expression matching
            # the compiled regular expressions are used for specialized matching rather than lookup
            # this section as well could be customized by jurisdiction

            # words ending in "way" are generically allowed to be "base types" or one-word feature names like
            # BROADWAY, MARWAY
            re_way = re.compile('\w+WAY$')
            # take apart hypenated words - this might be turned off
            # re_split = re.compile(r'[^\w\-\']+')
            re_route = re.compile('((ROUTE)|(RTE)|(RT)) \d+\w*$')
            re_padding = re.compile(' +')

            # use numpy arrays for querying combinations of candidate interpretations along different axes
            # the following list is an expanded list of FGDC elements because
            # base types (one word feature names) and highway directionals (e.g. North=Northbound) and types (Interstate, U.S. and State Highways)
            # need to be distinguished for parsing
            # the basetypes, highway directional and highway types map back to base name, pre and post directionals and pre and post types respectively
            # what's given in the dictionaries below is the positional index 1-7 for the fgdc element
            element_types = {'PM':1, 'PD':2, 'HPD':7, 'PT':3, 'HPT':3, 'BN':4, 'BT':4, 'ST':5, 'HST':5, 'SD':6, 'HSD':7, 'SM':7}
            fgdc_elements = ['PM','PD','PT','BN','ST','SD','SM']


            parse = [None] * 7			# what to insert for nulls
            street_name = self.name.upper()
            # street_name = ' '.join(str_rec[1])
            street_name = re_padding.sub(street_name,' ').strip()
            # print street_name
            street_name = street_name.replace("'",'')
            street_name = street_name.replace('.','')
            street_name = street_name.replace('\'','')
            street_name_tokens = street_name.split()
            #print 'street name', street_name
            # next section sets any word sequence found as a phrase in domains to be a single street name token
            token_position = 0
            while token_position < len(street_name_tokens):
                token = street_name_tokens[token_position]
                if token in self.domain_indexed_by_initial_token:
                    possible_domain_record_list = self.domain_indexed_by_initial_token[token]
                    for possible_domain_record in possible_domain_record_list:
                        number_tokens,input_string = possible_domain_record[0:2]
                        if number_tokens > 1:
                            possible_phrase = ' '.join(street_name_tokens[token_position:token_position+number_tokens])
                            if input_string == possible_phrase:
                                street_name_tokens[token_position:token_position+number_tokens] = [input_string]
                                break
                token_position += 1

    ##            # identify DOT ramp records check this fragment against input = 'RAMP'
    ##            mo = re_ramp.match(street_name)
    ##            if mo:
    ##                bn = mo.group(1)
    ##                if bn:
    ##                	pt = 'RAMP'
    ##                	std = '%s %s' % (pt,bn)
    ##                	parse =  [None, None, pt, bn, None, None, None, '*',std, objectid]  # this was edited to take our full str parse
    ##                	batch_update_recs.append(tuple(parse))
    ##                	continue   # this goes straight into insert list and bails from loop

    ##            # match route names like I-95
    ##    		l = len(street_name_tokens)
    ##    		for i in range(l):
    ##    			if re_route.match(street_name_tokens[i]):
    ##    				a1,a2 = street_name_tokens[i].split(' ')
    ##    				street_name_tokens[i] = a1
    ##    				street_name_tokens.insert(i+1, a2)

    ##            # look for number pairs
    ##            for i in range(len(street_name_tokens)):
    ##                dash_pair = '-'.join(street_name_tokens[i:i+2])
    ##                if dash_pair in num_lookup:
    ##                	street_name_tokens[i:i+2] = [dash_pair]
    ##                	continue

    ##            #standardize numbers
    ##            l = len(street_name_tokens)
    ##            for i in range(l):
    ##            	if num_lookup.has_key(street_name_tokens[i]):
    ##            		street_name_tokens[i] = num_lookup[street_name_tokens[i]]


            #print 'street_name_tokens', street_name_tokens
            # then go through and create a list of domain record candidates for each phrase
            domain_records_by_phrase = []
            for p in street_name_tokens:
                domain_records_this_phrase = []
                if p in self.domain_indexed_by_complete_phrase:
                    for d in self.domain_indexed_by_complete_phrase[p]:
                        domain_records_this_phrase.append(d)
                else:
                    domain_records_this_phrase.append([p,p,'BN',2])
                    domain_records_this_phrase.append([p,p,'SM',0])
                    if re_way.match(p):
                        domain_records_this_phrase.append([p,p,'BT',1])  # single word type contains "-way"
                domain_records_by_phrase.append(domain_records_this_phrase)

            #print 'domain_records_by_phrase', domain_records_by_phrase
            # this section does cartesian product of the above lists of possible interpretations of each token
            # if there's [1A,1B] and [2A,2B,2C] then the result is [1A,2A],[1A,2B],[1A,2C],[1B,2A] etc.
            # each of these sequences then gets checked for validity and scored
            number_phrases = len(domain_records_by_phrase)
            #print 'number_phrases', number_phrases
            dr = domain_records_by_phrase
            if number_phrases == 1:
                candidate_domain_sequences = [[d] for d in dr[0]]
            else:
                candidate_domain_sequences = [ [a,b] for a in dr[0] for b in dr[1] ]
            if number_phrases > 2:
                for domain_set in dr[2:]:
                    candidate_domain_sequences = [ c + [d] for c in candidate_domain_sequences for d in domain_set]

            # the candidate domain sequences get put into an array to simplify multi-dimensional processing
            li = len(candidate_domain_sequences)
            lj = number_phrases
            # cca = candidate array
            cca = np.empty([li,lj,4],dtype='a80')
            for i in range(li):
                for j in range(lj):
                    for k in range(4):
                        #print 'cds insert of %s for i=%d, j=%d, k=%d' %  (candidate_domain_sequences[i][j][k], i, j, k)
                        cca[i,j,k] = candidate_domain_sequences[i][j][k]
            # acl = sequence_of_type_codes
            acl = cca[:,:,2].tolist()  # this extracts list of just sequenceS of codes from combo list
            # pl = allowable_sequences for that number of tokens
            if self.dctdsl.has_key(lj):
                pl = self.dctdsl[lj]
            else:
                pl = []
            # testing and scoring each candidate sequence
            max_scr = 0;
            scr = 0; chc = None
            comments = '*'
            for i in range(len(acl)):
                if acl[i] in pl:
                    # scr = score for this candidate
                    scr = sum([int(i2) for i2 in cca[i,:,3]])
                    if chc == None or scr > max_scr:
                        # chc = accepted candidates
                        chc = cca[i,:,:]
                        max_scr = scr
                        current_allowable_sequence = acl[i]
                    elif scr == max_scr:
                        comments += '%s tied with %s ' % (current_allowable_sequence, acl[i])
                        comments = comments[:200]
                        comments = '2nd round'
            std = None
            if chc is not None:
                for element_value,element_type in chc[:,(1,2)]:
                    # i = element_sequence_number
                    i = element_types[element_type]
                    v = element_value
                    if parse[i-1]:
                        parse[int(i-1)] += (' %s' % unicode(v))
                    else:
                        parse[int(i-1)] = unicode(v)
                std = ' '.join(chc[:,1].tolist())
                std = unicode(std)
                if not std:
                    pass
                else:
                    parse = (tuple(parse))
                    return parse
            else:
                comments += '%s not parsed' % street_name
                comments = comments[:200]

##                skip_flag = True
##            if not skip_flag:
##                parse = (tuple(parse))
##            skip_flag = False

##            return parse

        except:
            print(traceback.format_exc())
            return None

##p = ParseName('Commander Blvd')
##print p.parse()