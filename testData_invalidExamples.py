import epcdltranslator as edt

print (edt.epcDLTranslator('urn:epc:id:sgtin:4012345.011111.999999999999999999999')) # serial reference too long 
print (edt.epcDLTranslator('urn:epc:id:sscc:401234.3111111111')) # GCP too short
print (edt.epcDLTranslator('urn:epc:id:sgln:4012345.00005.')) # lacks GLN extension component
print (edt.epcDLTranslator('urn:epc:id:grai:4012345.0002.334455')) # asset type too short
print (edt.epcDLTranslator('urn:epc:id:giai:4012345.ABC345§')) # includes an invalid character (§)
print (edt.epcDLTranslator('urn:epc:id:gsrn:4012345.6')) # service reference too short
print (edt.epcDLTranslator('urn:epc:id:gsrnp:4012345.00000000078')) # service reference too long
print (edt.epcDLTranslator('urn:epc:id:gdti:ABC.00009.PO-4711')) # GCP must only contain digits
print (edt.epcDLTranslator('urn:epc:id:cpi:0614141.123%24.12345')) # includes invalid escaped charater (%24)
print (edt.epcDLTranslator('urn:epc:id:cpi:0614141.abc.12345')) # cp ref with lowercase letters
print (edt.epcDLTranslator('urn:epc:id:cpi:0614141.12345.abf')) # cp serial must only contain digits
print (edt.epcDLTranslator('urn:epc:id:sgcn:0614141.55555.7755339999999')) # serial up to 12 digits
print (edt.epcDLTranslator('urn:epc:id:sgcn:0614141.55555.12ab')) # gcn serial must only contain digits
print (edt.epcDLTranslator('urn:epc:ginc:0614141.xyz47%2F11')) # incorrect urn notation
print (edt.epcDLTranslator('(402)40123452223334442')) # GS1 Element String instead of URN notation
print (edt.epcDLTranslator('urn:epc:id:itip:4012345.011111.1.2.987')) # only one digit to express piece and total
print (edt.epcDLTranslator('urn:epc:id:upui:1234567.098765.51qIgY)%3C%26Jp3*j7\'SDB><')) # contains non-escaped characters (><)
print (edt.epcDLTranslator('urn:epc:id:pgln:4000001.00000.0')) # contains invalid serial reference
print (edt.epcDLTranslator('urn:epc:class:lgtin:4012345.012345.Lot987/')) # contains non-escaped characters (/)