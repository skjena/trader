# Contains methods for important display configurations

import os
from binance.client import Client

def welcomeMenu():
    print("\n                                 Welcome to Trader.                                    ")
    print("==========================================\n")
    print("================Main=Menu==================\n")
    print("Which trader would you like to employ? \n")
    print("1. Noob Buyer")
    print("2. Noob Seller")
    print("\n0. Exit")

    return

def orderConfirmation(coinpair, price, qty, orderType):
    print("======================================")
    print("Type  :  " + orderType)
    print("@ Price  :  " + price)
    print("Amount  :  %d" %(qty))
    print("Of Pair  :  " + coinpair)
    print("======================================\n")

    answer = raw_input("Confirm? [ y / n ] ")

    if (answer == "y"):
        return True
    else:
        return False

    return

def showFunds(coin, balance, locked):
    
    print("========== Funds ===========");
    print("Coin: %s \n Available: %s \n Locked: %s \n" %(coin, balance, locked));

    return

def showPrice():
    
    return
