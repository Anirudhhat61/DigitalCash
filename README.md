# DigitalCash

Digital Cash Implementation Authors - Anirudhha Tiwari

Submitted for class project, Network security, SJSU Instructed by Dr. Gokay Saldamli.

The Code Invloves the Protocols such as Secret Splitting Bit Commitment RSA Encryption Blind Signature Protocol

Language: Python2.7 (3.x compatible with minor changes)

Dependencies: BitVector, random, pycrypto, socket, hashlib

Pre requistes:-
Ubuntu 16.04-> Install mysql,bitvector. 
Using : apt-get install python-mysqldb, pip install BitVector without this there would be import error.

Steps to run:
Then run python Bank.py first then python customer.py following with bankMerchant.py and last Merchant.py.

After everthing runs the transaction starts from Customer.py to enter the order ID from the testdatabase we have from Query.data .

Once Transaction is about to be done Merchant.py Bank Signature is verified and money deposited.
