import socket 
import MySQLdb
import re
import random


def checkBankSign(moneyOrder, custId):
    #print "Hello"
    order = re.findall('\\d+', moneyOrder)
    iden = re.findall('\\d+', custId)

    query = "Select signBank from MoneyOrder where "
    query += "OrdNum in ('%s')" % (order[0])
    query += " and Id in ('%s');" % (iden[0])

    cursor.execute(query)
    temp = str(cursor.fetchall())
    print temp
    if(temp):
        print "Bank Signature Verified"

        k = random.randrange(0, 1)
        print k 
        if(k == 0):
            string = "left"
        else:
            string = "right"
        
        connection.send(string)
        return True
    else:
        print "Bank Verification Failed"
        return False

def depositMoneyOrder(moneyOrder, custId):
    print "Inside Depositing Function"

    merchantBankSocket.send("Hi I am Merchant Talking")

    string = merchantBankSocket.recv(100)
    print string

    order = re.findall('\\d+', moneyOrder)
    iden = re.findall('\\d+', custId)

    print "Depositing Money Order: %s" %(order[0])

    merchantBankSocket.send(str(order[0]) + ',' + str(iden[0]))


if __name__ == '__main__':

    print "Welcome to Merchant Website, We accept Money Orders"

    sqlDatabase = MySQLdb.connect(host = "localhost", user = "kira", passwd = "123456", db = "CustomerDetails")
    cursor = sqlDatabase.cursor()

    merchantSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    merchantSocket.bind(('localhost', 9500))
    merchantSocket.listen(10)

    merchantBankSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    merchantBankSocket.connect(('localhost', 8000))

    while True:
        connection, fromCustomer = merchantSocket.accept()
        

        receive = connection.recv(100)
       
        print "hi"

        moneyOrder = receive.split(',')[0]
        custId = receive.split(',')[1]
        
        flag = checkBankSign(moneyOrder, custId)

        if(flag):
            depositMoneyOrder(moneyOrder, custId)

        #print receive
