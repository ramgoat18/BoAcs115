'''
Title:
- 2020 Spring Capstone Project 

Collaborator(s):
- CS 115 Discussion Group 
- TAs (Michael and Bharddwaj)
- Olorundamilola Kazeem
- lambert
- Stack Overflow 

Date(s):
- 2020 May 14

Filename: 
- advrelationship.py

Description:
- This module defines the AdvRelationship class
'''
from account import Account

class AdvRelationship(Account):
    ACC_TYPE = "Adv.Relationship"
    OVER_TYPE = "Accept"
    OVER_FEE = 35
    MONTHLY_MIN = 10000
    MONTHLY_FEE = 25
    FREE_WITHDRAWS = "Unlimited"
    MAX_WITHDRAW_FEE = None
    AVOID_WITHDRAW_FEE = None
    WITHDRAW_LIMIT = None  
    INT_RATE = 0 
    WITHDRAW_FEE_COUNT = 0
    WITHDRAW_COUNT = 0 

    def __init__(self, rewards_member, student, name, pin, balance):
        super().__init__(rewards_member, student, name, pin, balance)
       
    def withdraw(self, amount):
        '''withdraws the given amount from the account balance'''
        super().withdraw(amount)

    def deposit(self, amount):
        '''deposits the given amount into the account'''
        super().deposit(amount)

    def transfer(self, amount, acc):
        '''Transfers the given amount from the account given to the account that the method is used in and returns none if successful. Returns error message if it fails'''
        super().transfer(amount, acc)

    def resetCount(self):
        '''resets counters'''
        super().resetCount()

    def computeInterest(self):
        '''computes and automatically deposits money into the account'''
        super().computeInterest
    
    def oneMonthForward(self):
        '''This function when used represents the start of a new month which results in interest being deposited into accounts and withdraw limits being reset'''
        super().oneMonthForward

    def getBalance(self):
        '''returns the balance of the savings account'''
        super().getBalance()
       
    def getName(self):
        '''returns the name'''
        super().getName()

    def getPin(self):
        '''returns the pin'''
        super().getPin()
    
    def getStudent(self):
        '''returns true if the account holder is a student under the age of 24'''
        super().getStudent()

    def getWithdrawCount(self):
        '''returns the withdraw count'''
        super().getWithdrawCount()

    def getRewardstatus(self):
        '''Returns true if the account holder is a Preferred Rewards Program Member'''
        super().getRewardstatus
        



