# GS1-EPC-DigitalLink-URI-Translator
Python script that translates EPC URIs and EPC Class URIs into their corresponding canonical GS1 Digital Link URI equivalents 

## Introduction  
The EPC Tag Data Standard defines the **EPC ‘Pure Identity’ URI** that SHOULD be used in **EPCIS**, GS1’s core standard for supply chain visibility. It takes the form of a Uniform Resource Name (URN), which, taking the example of an SGTIN (= Serialised Global Trade Item Number) looks sth. like this: <i>urn:epc:<i>id</i>:sgtin:4012345.011111.987</i>. The EPC is a universal identifier for any physical or digital object, e.g. products, assets, logistics units, parties or locations.

The GS1 Digital Link Standard is another GS1 URI syntax and especially enables web requests through embedding GS1 keys and further attributes into a web-friendly syntax. It SHOULD NOT be used in EPCIS for the purpose of identifying objects, locations, or parties. It takes the form of a Web URI, which, taking the above example, looks like this: ... 


## Supported EPC/EPC Class URIs
+ SGTIN
+ GLN with/without extension


## References
* EPC Tag Data Standard, v. 1.11: https://www.gs1.org/standards/epcrfid-epcis-id-keys/epc-rfid-tds/1-11
* EPCIS Standard, v. 1.2: https://www.gs1.org/standards/epcis
* Core Business Vocabulary (CBV) Standard, v. 1.2.2: https://www.gs1.org/standards/epcis
* GS1 Digital Link Standard, v. 1.1: 
