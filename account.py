'''
Title:
- 2020 Spring Capstone Project 

Collaborator(s):
- CS 115 Discussion Group 
- TAs (Michael and Bharddwaj)
- Olorundamilola Kazeem
- Lambert
- Stack Overflow 

Date(s):
- 2020 May 14

Filename: 
- account.py

Description:
- This module defines the Account class
'''
from customer import Customer
class Account():
    ACC_TYPE = "Decline"
    OVER_TYPE = "Base"
    OVER_FEE = 0
    MONTHLY_MIN = 0
    MONTHLY_FEE = 0
    WITHDRAW_FEE = 0 
    FREE_WITHDRAWLS = 0
    MAX_WITHDRAW_FEE = 0
    AVOID_WITHDRAW_FEE = 0
    WITHDRAW_LIMIT = 0
    INT_RATE = 0
    WITHDRAW_FEE_COUNT = 0 
    WITHDRAW_COUNT = 0 

    def __init__(self, rewards_member, student, name, pin, balance):
        '''rewards_member is a boolean that is true if the account holder is a member of the Preferred Rewards Program and false if not. student is also
        a boolean that is true if the account holder is a student and false if not. name is a string and it is the first name of the account holder. pin is
        an integer and it acts as the password to the account and balance is a float and it represents the value of the account. withdraw_count is an
        int and it acts as the counter for withdraws.'''
        self.rewards_member = rewards_member
        self.student = student 
        self.name = name 
        self.pin = pin 
        self.balance = balance
        # self.rewards_member = c.getRewards 
        #intialize c 
        
    
    def __str__(self):
        '''Returns string of name, account owned, and balance of the account'''
        s = "Account Holder: " + self.name + "\n" 
        s += "Account Type: " + self.ACC_TYPE + "\n"
        s += "Balance: " +str(self.balance)
        return s

    def deposit(self, amount):
        '''Deposits the given amount and returns none'''
        if amount > 0:
            self.balance += amount
            return amount 
        else:
            return "No amount deposited. Deposit amount must be > 0"

    def withdraw(self, amount): 
        '''Evalautes the amount given to see if it is appropriate to withdraw. Depending on certain conditions it will evaluate if an overdraft fee is needed or a withdraw fee. 
        Returns none if there was a problem with the withdrawed amount'''
        if amount < 0:
            return "No amount withdrawed. Please enter a valid amount to withdraw"
        elif amount > self.balance and self.OVER_TYPE == "Accept":
            if self.WITHDRAW_LIMIT != None:
                if self.WITHDRAW_COUNT < 7:
                   self.WITHDRAW_COUNT += 1 
                   self.balance -= amount   
                   self.balance -= self.OVER_FEE
                   return amount 
                elif self.WITHDRAW_FEE_COUNT < 7:
                    if self.rewards_member == True or self.balance > 20000:
                        self.WITHDRAW_FEE_COUNT += 1
                        self.balance -= amount   
                        self.balance -= self.OVER_FEE
                        return amount 
                    else:
                        self.WITHDRAW_FEE_COUNT += 1
                        self.balance -= amount   
                        self.balance -= self.OVER_FEE
                        self.balance -= 10
                        return amount  
                else:
                    return "No amount withdrawed. You have done the max amount of withdraws on this account for the month"
            else:
                self.balance -= amount   
                self.balance -= self.OVER_FEE
                return amount 
        elif self.balance > amount:
            if self.WITHDRAW_LIMIT == None:
                self.balance -= amount 
                return amount
            else:
                if self.WITHDRAW_COUNT < 7:
                    self.WITHDRAW_COUNT += 1 
                    self.balance -= amount 
                    return amount
                elif self.WITHDRAW_FEE_COUNT < 7:
                    if self.rewards_member == True or self.balance > 20000:
                        self.WITHDRAW_FEE_COUNT += 1
                        self.balance -= amount
                        return amount   
                    else:
                        self.WITHDRAW_FEE_COUNT += 1
                        self.balance -= amount   
                        self.balance -= 10
                        return amount
                else:
                    return "No amount withdrawed. You have done the max amount of withdraws on this account for the month"
        elif amount > self.balance and self.OVER_TYPE == "Decline":
            return "No amount withdrawed. This transaction will not be completed to avoid an overdraft fee" 
        else:
            self.balance -= amount 
            return amount
             

    def transfer(self, amount, acc):
        '''Transfers the given amount from the account given to the account that the method is used in and returns none if successful. Returns error message if it fails'''
        amtWith = acc.withdraw(amount)
        if amtWith == amount:
            return "There has been an error in your transfer please try again"
        else:
            self.deposit(amtWith)

    def computeInterest(self):
        ''' computes and deposits interest into account'''
        """Computes, deposits, and returns the interest."""
        interest = self.balance * self.INT_RATE
        self.deposit(interest)
        return interest

    def resetCount(self):
        '''resets counters'''
        self.WITHDRAW_FEE_COUNT == 0
        self.WITHDRAW_COUNT == 0

    def oneMonthForward(self):
        '''This function when used represents the start of a new month which results in interest being deposited into accounts and withdraw limits being reset'''
        self.computeInterest()
        self.resetCount()

    def getBalance(self):
        '''returns the balance'''
        return self.balance

    def getName(self):
        '''returns the name'''
        return self.name
    
    def getStudent(self):
        '''returns true if the account holder is a student under the age of 24'''
        return self.student

    def getPin(self):
        '''returns the pin'''
        return self.pin

    def getWithdrawCount(self):
        '''returns the withdraw count'''
        self.WITHDRAW_COUNT
        self.WITHDRAW_FEE_COUNT

    def getRewardstatus(self):
        '''Returns true if the account holder is a Preferred Rewards Program Member'''
        return self.rewards_member
