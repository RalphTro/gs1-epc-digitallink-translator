import re
import sys
from gtin import GTIN

urn = input('Enter an EPC URI, e.g. "urn:epc:id:sgtin:4012345.011111.987": ')

# SGTIN EPC URI example: "urn:epc:id:sgtin:4012345.011111.987"
if re.match(r'urn:epc:id:sgtin:([0-9]{6,12})\.([0-9]{1,7})\.([!%-?A-Z_a-z\x22]{1,20})', urn) is not None:
    print ('Identified scheme: SGTIN EPC URI')
    partition = urn.index('.')
    gs1companyprefix = urn[17:partition]
    itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
    rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
    print('GTIN: ', str(GTIN(raw=rawGTIN)))
    serial = urn[32:]
    print ('Serial: ', serial)
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/01/'+ str(GTIN(raw=rawGTIN)) + '/21/' + serial)
    
else:
    print ('This does not seem to be a valid EPC URI.')
    sys.exit()
