import socket 
import MySQLdb
import re
import random

def callCheck(moneyOrder, custId):

    print "Inside callCheck"

    order = re.findall('\\d+', moneyOrder)
    iden = re.findall('\\d+', custId)

    query = "Select Ind from MoneyOrder where "
    query += "OrdNum in ('%s') "% (order[0])
    query += " and Ind = 0 "
    query += " and Id in ('%s');" %(iden[0])
    cursor.execute(query)

    temp = cursor.fetchall()

    if (len(temp) > 0 ):
        print "The Money Order is Valid, Depositing Money to your Account"

        query = "Update MoneyOrder  "
        query += "set Ind = 1"
        query += " where OrdNum in ('%s') "% (order[0])
        query += " and Ind = 0 "
        query += " and Id in ('%s');" %(iden[0])

        cursor.execute(query)
        sqlDatabase.commit()
    else:
        print "Merchant has already deposited this Money Order."


if __name__ == '__main__':
    print "Bank Merchant Server Website"

    
    sqlDatabase = MySQLdb.connect(host = "localhost", user = "kira", passwd = "123456", db = "CustomerDetails")
    cursor = sqlDatabase.cursor()

    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.bind(('localhost', 8000))
    listenSocket.listen(10)  ## Number of connections 

    while True:
        connection, fromMerchant = listenSocket.accept()
        receive = connection.recv(100)

        print receive

        connection.send("Hello, Greetings from Bank")
        
        string = connection.recv(100)
        print string
        moneyOrder = string.split(',')[0]
        custId = string.split(',')[1]

        callCheck(moneyOrder, custId)
