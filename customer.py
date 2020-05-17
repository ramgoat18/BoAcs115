
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
- customer.py

Description:
- This module defines the Customer class
'''
class Customer():

    def __init__(self, pin, name, student, rewards_member):
         self.rewards_member = rewards_member
         self.pin = pin
         self.student = student
         self.name = name 
    def cus(self, pin, name, student, rewards_member):
        self.pin = str(input("Enter your four digit pin"))
        self.name = str(input("Please enter your name"))
        self.student = bool(input("Enter True if you are a student under the age of 24"))
        self.rewards_member = bool(input("Enter True if you are a member of the preferred rewards program"))
    




# init for the customer would be instance varoables for the customer. pass in customer object 
