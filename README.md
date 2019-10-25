# GS1 EPC URI - Digital Link URI Translator

## Introduction  
The **EPC Pure Identity URI** (or simply EPC URI) is a universal identifier for any physical or digital object such as products, assets, logistics units, documents, or locations. It is the preferred way within information systems to denote arbitrary business objects. Applications based on **EPCIS**, GS1’s core standard for supply chain visibility, SHOULD use this syntax. It takes the form of a Uniform Resource Name (URN), which, taking the example of an SGTIN (= Serialised Global Trade Item Number) looks sth. like this: <i>urn:epc:<i>id</i>:sgtin:4012345.011111.987</i>. 

A **GS1 Digital Link URI** is another GS1 URI, introduced especially to enable web applications through embedding GS1 keys and descriptive attributes into a web-friendly syntax. It SHOULD NOT be used in EPCIS for the purpose of identifying objects or locations. It takes the form of a Web URI, which, taking the above example, looks like this: <i><i>https</i>://id.gs1.org/01/04012345111118/21/987</i> or <i><i>https</i>://example.com/01/04012345111118/21/987?15=211231</i>. 

In case organisation wish to combine the powerful features of both supply chain visibility and accessibility to object-related information in the web (e.g. product description page or patient information leaflet), they need to translate EPC URIs into GS1 Digital Link URIs. As GS1 Digital Link URIs can also be constructed with company-specific domain names, this script can easily be adapted to also support custom domain names (e.g "example.com"). 

## Supported EPC/EPC Class URIs
+ SGTIN:  Serialised Global Trade Item Number
+ SSCC:   Serial Shipping Container Code
+ SGLN:   Global Location Number with or without extension 
+ GRAI:   Global Returnable Asset Identifier
+ GIAI:   Global Individual Asset Identifier
+ GSRN:   Global Service Relation Number - Recipient
+ GSRNP:  Global Service Relation Number – Provider
+ GDTI:   Global Document Type Identifier 
+ CPI:    Component / Part Identifier
+ SGCN:   Serialised Global Coupon Number
+ GINC:   Global Identification Number for Consignment
+ GSIN:   Global Shipment Identification Number
+ ITIP:   Individual Trade Item Piece  
+ UPUI:   Unit Pack Identifier
+ PGLN:   Global Location Number of Party 
+ LGTIN:  GTIN + Batch/Lot

Note that the remaining EPC schemes as defined in the EPC Tag Data Standard, namely GID, USDOD, ADI, and BIC, are not supported as they lack a GS1 Company Prefix, thus cannot be translated into GS1 Element Strings/GS1 Digital Link URIs. 

## Installation
pip install epcdltranslator (see https://pypi.org/project/epcdltranslator/1.0.0/)

## Usage/Short test script 
Once installed, enter the following code into the Python shell:
<i>>>></i> import epcdltranslator as edt
<i>>>></i> edt.epcDLTranslator('<i>urn:epc:<i>id:</i>sgtin:4012345.011111.987</i>')
It then should return:
'https://id.gs1.org/01/04012345111118/21/987'

## References
* EPC Tag Data Standard, v. 1.12: https://www.gs1.org/standards/epcrfid-epcis-id-keys/epc-rfid-tds/
* EPCIS Standard, v. 1.2: https://www.gs1.org/standards/epcis
* Core Business Vocabulary (CBV) Standard, v. 1.2.2: https://www.gs1.org/standards/epcis
* GS1 Digital Link Standard, v. 1.1: https://www.gs1.org/standards/gs1-digital-link
