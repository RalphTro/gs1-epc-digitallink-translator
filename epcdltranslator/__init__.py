from re import match
from gtin import GTIN

# Version 1.0.0
# Last update: 2020-06-01

# Function 'epcDLTranslator' expects an EPC/EPC Class URI and returns the corresponding GS1 Digital Link URI.
# For an EPC URI, a valid input example is "urn:epc:id:sgtin:4012345.011111.987".
# For an EPC Class URI, a valid input example is "urn:epc:class:lgtin:4012345.012345.Lot987".

def epcDLTranslator(urn):
    if match(r'^urn:epc:id:sgtin:((\d{6}\.\d{7})|(\d{7}\.\d{6})|(\d{8}\.\d{5})|(\d{9}\.\d{4})|(\d{10}\.\d{3})|(\d{11}\.\d{2})|(\d{12}\.\d{1}))\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,20}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[17:partition]
        itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
        rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
        serial = urn[32:]
        return ('https://id.gs1.org/01/'+ str(GTIN(raw=rawGTIN)) + '/21/' + serial)
    elif match(r'^urn:epc:id:sscc:((\d{6}\.\d{11}$)|(\d{7}\.\d{10}$)|(\d{8}\.\d{9}$)|(\d{9}\.\d{8}$)|(\d{10}\.\d{7}$)|(\d{11}\.\d{6}$)|(\d{12}\.\d{5}$))', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        serialref = urn[(partition+1):]
        rawSSCC = urn[(partition+1):(partition+2)] + gs1companyprefix + serialref
        return ('https://id.gs1.org/00/'+ str(GTIN(raw=rawSSCC)))
    elif match(r'^urn:epc:id:sgln:((\d{6}\.\d{6})|(\d{7}\.\d{5})|(\d{8}\.\d{4})|(\d{9}\.\d{3})|(\d{10}\.\d{2})|(\d{11}\.\d{1})|(\d{12}\.))\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,20}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        locationref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
        rawGLN = gs1companyprefix + locationref
        extension = urn[30:]
        if extension == '0':
            return ('https://id.gs1.org/414/'+ str(GTIN(raw=rawGLN)))
        else:
            return ('https://id.gs1.org/414/'+ str(GTIN(raw=rawGLN)) + '/254/' + extension)
    elif match(r'^urn:epc:id:grai:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.))\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,16}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        assetref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
        rawGRAI = '0' + gs1companyprefix + assetref
        serial = urn[30:]
        return ('https://id.gs1.org/8003/'+ str(GTIN(raw=rawGRAI)) + serial)
    elif match(r'^urn:epc:id:giai:(([\d]{6}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,24})|([\d]{7}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,23})|([\d]{8}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,22})|([\d]{9}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,21})|([\d]{10}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,20})|([\d]{11}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,19})|([\d]{12}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,18}))$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        assetref = urn[(partition+1):]
        return ('https://id.gs1.org/8004/'+ gs1companyprefix + assetref)
    elif match(r'^urn:epc:id:gsrn:(([\d]{6}\.[\d]{11}$)|([\d]{7}\.[\d]{10}$)|([\d]{8}\.[\d]{9}$)|([\d]{9}\.[\d]{8}$)|([\d]{10}\.[\d]{7}$)|([\d]{11}\.[\d]{6}$)|([\d]{12}\.[\d]{5}$))', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        serviceref = urn[(partition+1):]
        rawGSRN = gs1companyprefix + serviceref
        return ('https://id.gs1.org/8018/'+ str(GTIN(raw=rawGSRN)))
    elif match(r'^urn:epc:id:gsrnp:(([\d]{6}\.[\d]{11}$)|([\d]{7}\.[\d]{10}$)|([\d]{8}\.[\d]{9}$)|([\d]{9}\.[\d]{8}$)|([\d]{10}\.[\d]{7}$)|([\d]{11}\.[\d]{6}$)|([\d]{12}\.[\d]{5}$))', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[17:partition]
        serviceref = urn[(partition+1):]
        rawGSRNP = gs1companyprefix + serviceref
        return ('https://id.gs1.org/8017/'+ str(GTIN(raw=rawGSRNP)))
    elif match(r'^urn:epc:id:gdti:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.\.))(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,20}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        documenttype = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
        rawGDTI = gs1companyprefix + documenttype
        serial = urn[30:]
        return ('https://id.gs1.org/253/'+ str(GTIN(raw=rawGDTI)) + serial)
    elif match(r'^urn:epc:id:cpi:((\d{6}\.(\%2[3dfDF]|\%3[0-9]|\%4[1-9A-Fa-f]|\%5[0-9Aa]|[0-9A-Z-]){1,24})|(\d{7}\.(\%2[3dfDF]|\%3[0-9]|\%4[1-9A-Fa-f]|\%5[0-9Aa]|[0-9A-Z-]){1,23})|(\d{8}\.(\%2[3dfDF]|\%3[0-9]|\%4[1-9A-Fa-f]|\%5[0-9Aa]|[0-9A-Z-]){1,22})|(\d{9}\.(\%2[3dfDF]|\%3[0-9]|\%4[1-9A-Fa-f]|\%5[0-9Aa]|[0-9A-Z-]){1,21})|(\d{10}\.(\%2[3dfDF]|\%3[0-9]|\%4[1-9A-Fa-f]|\%5[0-9Aa]|[0-9A-Z-]){1,20})|(\d{11}\.(\%2[3dfDF]|\%3[0-9]|\%4[1-9A-Fa-f]|\%5[0-9Aa]|[0-9A-Z-]){1,19})|(\d{12}\.(\%2[3dfDF]|\%3[0-9]|\%4[1-9A-Fa-f]|\%5[0-9Aa]|[0-9A-Z-]){1,18}))\.[\d]{1,12}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[15:partition]
        separator = urn.rfind('.')
        cpref = urn[(partition+1):(separator)]
        rawCPI = gs1companyprefix + cpref
        serial = urn[(separator+1):]
        return ('https://id.gs1.org/8010/'+ rawCPI + '/8011/' + serial)
    elif match(r'^urn:epc:id:sgcn:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.))\.[\d]{1,12}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        couponref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
        rawSGCN = gs1companyprefix + couponref
        serial = urn[30:]
        return ('https://id.gs1.org/255/'+ str(GTIN(raw=rawSGCN)) + serial)
    elif match(r'^urn:epc:id:ginc:([\d]{6}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,24}|[\d]{7}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,23}|[\d]{8}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,22}|[\d]{9}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,21}|[\d]{10}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,20}|[\d]{11}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,19}|[\d]{12}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,18})$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        consignmentref = urn[(partition+1):]
        return ('https://id.gs1.org/401/'+ gs1companyprefix + consignmentref)
    elif match(r'^urn:epc:id:gsin:(([\d]{6}\.[\d]{10}$)|([\d]{7}\.[\d]{9}$)|([\d]{8}\.[\d]{8}$)|([\d]{9}\.[\d]{7}$)|([\d]{10}\.[\d]{6}$)|([\d]{11}\.[\d]{5}$)|([\d]{12}\.[\d]{4}$))', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        shipperref = urn[(partition+1):]
        rawGSIN = gs1companyprefix + shipperref
        return ('https://id.gs1.org/402/'+ str(GTIN(raw=rawGSIN)))
    elif match(r'^urn:epc:id:itip:(([\d]{6}\.[\d]{7})|([\d]{7}\.[\d]{6})|([\d]{8}\.[\d]{5})|([\d]{9}\.[\d]{4})|([\d]{10}\.[\d]{3})|([\d]{11}\.[\d]{2})|([\d]{12}\.[\d]{1}))\.[\d]{2}\.[\d]{2}\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,20}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
        rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
        piece = urn[31:33]
        total = urn[34:36]
        serial = urn[37:]
        return ('https://id.gs1.org/8006/'+ str(GTIN(raw=rawGTIN)) + piece + total + '/21/' + serial)
    elif match(r'^urn:epc:id:upui:((\d{6}\.\d{7})|(\d{7}\.\d{6})|(\d{8}\.\d{5})|(\d{9}\.\d{4})|(\d{10}\.\d{3})|(\d{11}\.\d{2})|(\d{12}\.\d{1}))\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,28}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
        rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
        serial = urn[31:]
        return ('https://id.gs1.org/01/'+ str(GTIN(raw=rawGTIN)) + '/235/' + serial)
    elif match(r'^urn:epc:id:pgln:(([\d]{6}\.[\d]{6})|([\d]{7}\.[\d]{5})|([\d]{8}\.[\d]{4})|([\d]{9}\.[\d]{3})|([\d]{10}\.[\d]{2})|([\d]{11}\.[\d]{1})|([\d]{12}\.))$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[16:partition]
        partyref = urn[(partition+1):(partition+1+(12-len(gs1companyprefix)))]
        rawGLN = gs1companyprefix + partyref
        return ('https://id.gs1.org/417/'+ str(GTIN(raw=rawGLN)))
    elif match(r'^urn:epc:class:lgtin:(([\d]{6}\.[\d]{7})|([\d]{7}\.[\d]{6})|([\d]{8}\.[\d]{5})|([\d]{9}\.[\d]{4})|([\d]{10}\.[\d]{3})|([\d]{11}\.[\d]{2})|([\d]{12}\.[\d]{1}))\.(\%2[125-9A-Fa-f]|\%3[0-9A-Fa-f]|\%4[1-9A-Fa-f]|\%5[0-9AaFf]|\%6[1-9A-Fa-f]|\%7[0-9Aa]|[!\')(*+,.0-9:;=A-Za-z_-]){1,20}$', urn) is not None:
        partition = urn.index('.')
        gs1companyprefix = urn[20:partition]
        itemref = urn[(partition+1):(partition+1+(13-len(gs1companyprefix)))]
        rawGTIN = itemref[0:1] + gs1companyprefix + itemref[1:]
        lot = urn[35:]
        return ('https://id.gs1.org/01/'+ str(GTIN(raw=rawGTIN)) + '/10/' + lot)
    else:
        return ('This does not seem to be a valid EPC URI/EPC Class URI.')
