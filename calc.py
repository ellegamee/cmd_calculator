#imports
import time

while True:
    total = input("Write a math question.")

    #Different lists
    lista = total.split()
    forsta_tal = lista[0] 
    andra = lista[1]
    tredjedwuohwdlpowa = lista[2]

    #functions
    if (andra == "+"):
        print("Answer: " + str( int(forsta_tal) + int(tredjedwuohwdlpowa)))
    elif(andra == "-"):
        print("Answer: " + str( int(forsta_tal) - int(tredjedwuohwdlpowa)))
    elif(andra == "/"):
        print("Answer: " + str( int(forsta_tal) / int(tredjedwuohwdlpowa)))
    elif(andra == "*"):
        print("Answer: " + str( int(forsta_tal) * int(tredjedwuohwdlpowa)))
    else:
        print("Error, try again")