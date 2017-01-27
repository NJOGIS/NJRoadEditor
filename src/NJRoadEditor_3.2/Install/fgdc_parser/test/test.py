import sys, os
from fgdc_parser import fgdc_parser
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

p = fgdc_parser.ParseName.ParseName('Commander Blvd')

print p.parse()