'''
Title:
- 2020 Spring Capstone Project 

Collaborator(s):
- CS 115 Discussion Group 
- TAs (Michael and Bharddwaj)
- Olorundamilola Kazeem
- Stack Overflow 

Date(s):
- 2020 May 14

Filename: 
- bank.py 

Description:
- This module defines the Bank class
'''

import pickle
import random
from account import Account 
from savings import Savings
from advrelationship import AdvRelationship
from safebalance import SafeBalance
from advplus import AdvPlus


class Bank():
    '''This Bank class represents a collection of different accounts.'''
    def __init__(self, fileName = None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts."""
        self.accounts = {}
        #the key is name and pin string and the value is a list of accounts associated with that 
    
    def __str__(self):
        """Returns the string representation of the bank."""
        return "\n".join([str(v) for (k, v) in
                          sorted(self.accounts.items(),
                                 key=lambda cv: cv[1].getName())])

    def createAccount(self, ACC_TYPE):
        if ACC_TYPE == "Savings":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            savings = Savings(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                self.accounts[key].append(savings)
            else:
                # key is not already in dictionary so dictionary needs to intialized and then appeneded with the key
                self.accounts[key] = []
                self.accounts[key].append(savings)
        elif ACC_TYPE == "Adv.Relationship":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            advrelationship = AdvRelationship(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                self.accounts[key].append(advrelationship)
            else:
                # key is not already in dictionary so dictionary needs to intialized and then appeneded with the key
                self.accounts[key] = []
                self.accounts[key].append(advrelationship)
        elif ACC_TYPE == "SafeBalance":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            safebalance = SafeBalance(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                self.accounts[key].append(safebalance)
            else:
                # key is not already in dictionary so dictionary needs to intialized and then appeneded with the key
                self.accounts[key] = []
                self.accounts[key].append(safebalance)
        elif ACC_TYPE == "Adv.Plus":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            advplus = AdvPlus(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                self.accounts[key].append(advplus)
            else:
                # key is not already in dictionary so dictionary needs to intialized and then appeneded with the key
                self.accounts[key] = []
                self.accounts[key].append(advplus)
        else:
            return "Please enter a valid account type"

    def makeKey(self, name, pin):
        """Returns a key for the account.  A key is composed of a name and a pin"""
        return name + "/" + pin
        

    def remove(self, ACC_TYPE):
        """Removes the account from the bank and
        and returns it, or None if the account does
        not exist."""
        if ACC_TYPE == "Savings":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            savings = Savings(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                getDeleted = False 
                for i in self.accounts[key]:
                    if isinstance(i, Savings):
                        self.accounts[key].remove(i)
                        getDeleted = True 
                        # this for loop searches through the dictionary and if it exist it is removed from the dictionary and getDeleted becomes true
                if getDeleted == False:
                    return "Account not found"
                else:
                    return "Account deleted"
            else:
               return "Error: User not a customer" 
        elif ACC_TYPE == "Adv.Relationship":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            advrelationship = AdvRelationship(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                getDeleted = False 
                for i in self.accounts[key]:
                    if isinstance(i, AdvRelationship):
                        self.accounts[key].remove(i)
                        getDeleted = True 
                if getDeleted == False:
                    return "Account not found"
                else:
                    return "Account deleted"
            else:
               return "Error: User not a customer" 
        elif ACC_TYPE == "SafeBalance":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            safebalance = SafeBalance(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                getDeleted = False 
                for i in self.accounts[key]:
                    if isinstance(i, SafeBalance):
                        self.accounts[key].remove(i)
                        getDeleted = True 
                if getDeleted == False:
                    return "Account not found"
                else:
                    return "Account deleted"
            else:
               return "Error: User not a customer" 
        elif ACC_TYPE == "Adv.Plus":
            rewards_member = bool(input("Please enter true if you are a rewards_member: "))
            name = str(input("Please enter your first name: "))
            pin = str(input("Please enter four digit pin: "))
            balance = float(input("Please enter the starting balance of your account: "))
            student = bool(input("Please enter true if you are a student of some sort under the age of 24: "))
            advplus = AdvPlus(rewards_member, student, name, pin, balance)
            key = self.makeKey(name, pin)
            if key in self.accounts:
                # checks to see if the user already has an account because if their key is already in the dictionary it means they have an account 
                getDeleted = False 
                for i in self.accounts[key]:
                    if isinstance(i, AdvPlus):
                        self.accounts[key].remove(i)
                        getDeleted = True 
                if getDeleted == False:
                    return "Account not found"
                else:
                    return "Account deleted"
            else:
               return "Error: User not a customer" 
        else:
            return "Please enter a valid account type"
        

    def getAccounts(self, name, pin):
        '''returns the value associated with the key from the dictionary'''
        return self.accounts[self.makeKey(name, pin)]

# Functions for testing


def testAccount():
    """Test function for savings account."""
    account = Account(True, True, "Ken", "1000", 500.00)
    print(account)
    print("Amount deposited: ", account.deposit(100))
    print("Expect 600:", account.getBalance())
    print("Amount deposited: ", account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print("Withdrawed amount is: ", account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print("Withdrawed amount is: ", account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print("Withdrawed amount is: ", account.withdraw(100000))
    print("Expect 500:", account.getBalance())
    #For the mvp a limit on the amount that can be overdrawn is not included in the mvp




if __name__ == "__main__":
    
    #testAccount()
    
    #print(createBank())
    #main()

    t = Bank()
    # t.createAccount("Savings")
    # print(t.getAccounts("Jack", "1222"))
    # t.createAccount("Savings")
    # print(t.getAccounts("Jack", "1222"))
    t.__str__()

