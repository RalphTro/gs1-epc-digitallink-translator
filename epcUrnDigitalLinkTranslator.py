from re import match
from sys import exit
from gtin import GTIN

print ('Valid input examples: For an EPC URI, a valid input example is "urn:epc:id:sgtin:4012345.011111.987". For an EPC Class URI, a valid input example is "urn:epc:class:lgtin:4012345.012345.Lot987".') ')
urn = input('Enter an EPC or EPC Class URI: ')

# SGTIN EPC URI example: "urn:epc:id:sgtin:4012345.011111.98%22"
if match(r'urn:epc:id:sgtin:(([\d]{6}\.[\d]{7})|([\d]{7}\.[\d]{6})|([\d]{8}\.[\d]{5})|([\d]{9}\.[\d]{4})|([\d]{10}\.[\d]{3})|([\d]{11}\.[\d]{2})|([\d]{12}\.[\d]{1}))\.[\d\w!\'()*+,-.:;=%]{1,20}$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[17:partition]
    itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
    rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
    serial = urn[32:]
    serial = serial.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print('GS1 Element String(s): (01)', str(GTIN(raw=rawGTIN)), '(21)', serial)
    serial = serial.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/01/'+ str(GTIN(raw=rawGTIN)) + '/21/' + serial)

# SSCC EPC URI example: "urn:epc:id:sscc:4012345.3111111111"
elif match(r'urn:epc:id:sscc:(([\d]{6}\.[\d]{11})|([\d]{7}\.[\d]{10})|([\d]{8}\.[\d]{9})|([\d]{9}\.[\d]{8})|([\d]{10}\.[\d]{7})|([\d]{11}\.[\d]{6})|([\d]{12}\.[\d]{5})$)', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    serialref = urn[(partition+1):]
    rawSSCC = urn[(partition+1):(partition+2)] + gs1companyprefix + serialref
    print('GS1 Element String(s): (00)', str(GTIN(raw=rawSSCC)))
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/00/'+ str(GTIN(raw=rawSSCC)))

# SGLN EPC URI example: "urn:epc:id:sgln:4012345.00005.122"
elif match(r'urn:epc:id:sgln:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.))\.[\d\w!\'()*+,-.:;=%]{1,20}$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    locationref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
    rawGLN = gs1companyprefix + locationref
    extension = urn[30:]
    extension = extension.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    # An SGLN EPC URI with extension set to '0' means that a GLN extension is not used     
    if extension == '0':
        print ('GS1 Element String(s): (414)', str(GTIN(raw=rawGLN)))
        print ('Canonical GS1 Digital Link URI: https://id.gs1.org/414/'+ str(GTIN(raw=rawGLN)))
    else:
        print ('GS1 Element String(s): (414)', str(GTIN(raw=rawGLN)),'(254)', extension)         
        extension = extension.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
        print ('Canonical GS1 Digital Link URI: https://id.gs1.org/414/'+ str(GTIN(raw=rawGLN)) + '/254/' + extension)

# GRAI EPC URI example: "urn:epc:id:grai:4012345.00022.334455"
elif match(r'urn:epc:id:grai:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.))\.[\d\w!\'()*+,-.:;=%]{1,16}$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    assetref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
    rawGRAI = '0' + gs1companyprefix + assetref
    serial = urn[30:]
    serial = serial.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print ('GS1 Element String(s): (8003)', str(GTIN(raw=rawGRAI)),serial)
    serial = serial.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/8003/'+ str(GTIN(raw=rawGRAI)) + serial)

# GIAI EPC URI example: "urn:epc:id:giai:4012345.ABC345"
elif match(r'urn:epc:id:giai:(([\d]{6}\.[\d\w!\'()*+,-.:;=%]{1,24}$)|([\d]{7}\.[\d\w!\'()*+,-.:;=%]{1,23}$)|([\d]{8}\.[\d\w!\'()*+,-.:;=%]{1,22}$)|([\d]{9}\.[\d\w!\'()*+,-.:;=%]{1,21}$)|([\d]{10}\.[\d\w!\'()*+,-.:;=%]{1,20$})|([\d]{11}\.[\d\w!\'()*+,-.:;=%]{1,19}$)|([\d]{12}\.[\d\w!\'()*+,-.:;=%]{1,18}))$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    assetref = urn[(partition+1):]
    assetref = assetref.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print('GS1 Element String(s): (8004)', gs1companyprefix + assetref)
    assetref = assetref.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/8004/'+ gs1companyprefix + assetref)

# GSRN EPC URI example: "urn:epc:id:gsrn:4012345.0000006765"
elif match(r'urn:epc:id:gsrn:(([\d]{6}\.[\d]{11}$)|([\d]{7}\.[\d]{10}$)|([\d]{8}\.[\d]{9}$)|([\d]{9}\.[\d]{8}$)|([\d]{10}\.[\d]{7}$)|([\d]{11}\.[\d]{6}$)|([\d]{12}\.[\d]{5}$))', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    serviceref = urn[(partition+1):]
    rawGSRN = gs1companyprefix + serviceref
    print('GS1 Element String(s): (8018)', str(GTIN(raw=rawGSRN)))
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/8018/'+ str(GTIN(raw=rawGSRN)))

# GSRNP EPC URI example: "urn:epc:id:gsrnp:4012345.0000000007"
elif match(r'urn:epc:id:gsrnp:(([\d]{6}\.[\d]{11}$)|([\d]{7}\.[\d]{10}$)|([\d]{8}\.[\d]{9}$)|([\d]{9}\.[\d]{8}$)|([\d]{10}\.[\d]{7}$)|([\d]{11}\.[\d]{6}$)|([\d]{12}\.[\d]{5}$))', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[17:partition]
    serviceref = urn[(partition+1):]
    rawGSRNP = gs1companyprefix + serviceref
    print('GS1 Element String(s): (8017)', str(GTIN(raw=rawGSRNP)))
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/8017/'+ str(GTIN(raw=rawGSRNP)))

# GDTI EPC URI example: "urn:epc:id:gdti:4012345.00009.PO-4711"
elif match(r'urn:epc:id:gdti:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.\.))[\d\w!\'()*+,-.:;=%]{1,20}$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    documenttype = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
    rawGDTI = gs1companyprefix + documenttype
    serial = urn[30:]
    serial = serial.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print ('GS1 Element String(s): (253)', str(GTIN(raw=rawGDTI)), serial)
    serial = serial.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/253/'+ str(GTIN(raw=rawGDTI)) + serial)
 
# CPI EPC URI example: "urn:epc:id:cpi:0614141.11111111111111-A%23%2F.12345"
elif match(r'urn:epc:id:cpi:(([\d]{6}\.[\dA-Z%\-]{1,24})|([\d]{7}\.[\dA-Z%\-]{1,23})|([\d]{8}\.[\dA-Z%\-]{1,22})|([\d]{9}\.[\dA-Z%\-]{1,21})|([\d]{10}\.[\dA-Z%\-]{1,20})|([\d]{11}\.[\dA-Z%\-]{1,19})|([\d]{12}\.[\dA-Z%\-]{1,18}))\.([\d]{1,12}$)', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[15:partition]
    separator = urn.rfind('.')
    cpref = urn[(partition+1):(separator)]
    rawCPI = gs1companyprefix + cpref
    serial = urn[(separator+1):]
    # GS1 Element Strings can contain "/" and "#", while the latter need to be percent-encoded in URIs   
    rawCPI = rawCPI.replace('%2F', '/').replace('%23', '#')
    print('GS1 Element String(s): (8010)', rawCPI, '(8011)', serial)
    rawCPI = rawCPI.replace('/', '%2F').replace('#', '%23')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/8010/'+ rawCPI + '/8011/' + serial)

# SGCN EPC URI example: "urn:epc:id:sgcn:0614141.55555.775533"
elif match(r'urn:epc:id:sgcn:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.))\.[\d\w!\'()*+,-.:;=%]{1,20}$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    couponref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
    rawSGCN = gs1companyprefix + couponref
    serial = urn[30:]
    serial = serial.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print ('GS1 Element String(s): (255)', str(GTIN(raw=rawSGCN)), serial)
    serial = serial.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/255/'+ str(GTIN(raw=rawSGCN)) + serial)

# GINC EPC URI example: "urn:epc:id:ginc:0614141.xyz47%2F11"
elif match(r'urn:epc:id:ginc:(([\d]{6}\.[\d\w!\'()*+,-.:;=%]{1,24}$)|([\d]{7}\.[\d\w!\'()*+,-.:;=%]{1,23}$)|([\d]{8}\.[\d\w!\'()*+,-.:;=%]{1,22}$)|([\d]{9}\.[\d\w!\'()*+,-.:;=%]{1,21}$)|([\d]{10}\.[\d\w!\'()*+,-.:;=%]{1,20$})|([\d]{11}\.[\d\w!\'()*+,-.:;=%]{1,19}$)|([\d]{12}\.[\d\w!\'()*+,-.:;=%]{1,18}$))', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    consignmentref = urn[(partition+1):]
    consignmentref = consignmentref.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print('GS1 Element String(s): (401)', gs1companyprefix + consignmentref)
    consignmentref = consignmentref.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/401/'+ gs1companyprefix + consignmentref)

# GSIN EPC URI example: "urn:epc:id:gsin:4012345.222333444"
elif match(r'urn:epc:id:gsin:(([\d]{6}\.[\d]{10}$)|([\d]{7}\.[\d]{9}$)|([\d]{8}\.[\d]{8}$)|([\d]{9}\.[\d]{7}$)|([\d]{10}\.[\d]{6}$)|([\d]{11}\.[\d]{5}$)|([\d]{12}\.[\d]{4}$))', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    shipperref = urn[(partition+1):]
    rawGSIN = gs1companyprefix + shipperref
    print('GS1 Element String(s): (402)', str(GTIN(raw=rawGSIN)))
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/402/'+ str(GTIN(raw=rawGSIN)))

# ITIP EPC URI example: "urn:epc:id:itip:4012345.011111.01.02.987"
elif match(r'urn:epc:id:itip:(([\d]{6}\.[\d]{7})|([\d]{7}\.[\d]{6})|([\d]{8}\.[\d]{5})|([\d]{9}\.[\d]{4})|([\d]{10}\.[\d]{3})|([\d]{11}\.[\d]{2})|([\d]{12}\.[\d]{1}))\.[\d]{2}\.[\d]{2}\.([\d\w!\'()*+,-.:;=%]{1,20})$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
    rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
    piece = urn[31:33]
    total = urn[34:36]
    serial = urn[37:]
    serial = serial.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print('GS1 Element String(s): (8006)', str(GTIN(raw=rawGTIN)), piece, total, '(21)', serial)
    serial = serial.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/8006/'+ str(GTIN(raw=rawGTIN)) + piece + total + '/21/' + serial)

# UPUI EPC URI example: "urn:epc:id:upui:1234567.098765.51qIgY)%3C%26Jp3*j7'SDB"
elif match(r'urn:epc:id:upui:(([\d]{6}\.[\d]{7})|([\d]{7}\.[\d]{6})|([\d]{8}\.[\d]{5})|([\d]{9}\.[\d]{4})|([\d]{10}\.[\d]{3})|([\d]{11}\.[\d]{2})|([\d]{12}\.[\d]{1}))\.[\d\w!\'()*+,-.:;=%]{1,28}$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
    rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
    serial = urn[31:]
    serial = serial.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print('GS1 Element String(s): (01)', str(GTIN(raw=rawGTIN)), '(235)', serial)
    serial = serial.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/01/'+ str(GTIN(raw=rawGTIN)) + '/235/' + serial)

# PGLN EPC URI example: "urn:epc:id:pgln:4000001.00000" 
elif match(r'urn:epc:id:pgln:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.))$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[16:partition]
    partyref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
    rawGLN = gs1companyprefix + partyref
    print ('GS1 Element String(s): (417)', str(GTIN(raw=rawGLN)))
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/417/'+ str(GTIN(raw=rawGLN)))

# LGTIN EPC Class URI example: "urn:epc:class:lgtin:4012345.012345.Lot987"
elif match(r'urn:epc:class:lgtin:(([\d]{6}\.[\d]{7})|([\d]{7}\.[\d]{6})|([\d]{8}\.[\d]{5})|([\d]{9}\.[\d]{4})|([\d]{10}\.[\d]{3})|([\d]{11}\.[\d]{2})|([\d]{12}\.[\d]{1}))\.[\d\w!\'()*+,-.:;=%]{1,20}$', urn) is not None:
    partition = urn.index('.')
    gs1companyprefix = urn[20:partition]
    itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
    rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
    lot = urn[35:]
    lot = lot.replace('%22','"').replace('%25','%').replace('%26','&').replace('%2F','/').replace('%3C','<').replace('%3E','>').replace('%3F','?')
    print ('GS1 Element String(s): (01)', str(GTIN(raw=rawGTIN)), '(10)', lot)
    lot = lot.replace('"','%22').replace('%','%25').replace('&','%26').replace('/','%2F').replace('<','%3C').replace('>','%3E').replace('?','%3F')
    print ('Canonical GS1 Digital Link URI: https://id.gs1.org/01/'+ str(GTIN(raw=rawGTIN)) + '/10/' + lot)

else:
    print ('This does not seem to be a valid EPC URI/EPC Class URI.')
    exit()
