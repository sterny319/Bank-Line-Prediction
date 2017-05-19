#Based off of lecture 

import random

def chance(p):
    return random.random() < p
secondsPerMinute = 60
secondsPerHour = 60 * secondsPerMinute
secondsPerWorkDay = 8 * secondsPerHour

arrivalProb = 20/secondsPerHour

class Customer:
    def __init__(self):
        self.transactionTime = int((1+random.random()*4)*secondsPerMinute)
class Bank:
    def __init__(self):
        self.line = []
        self.time = 0
        self.servingCustomer = False
    def lineLength(self):
        if len(self.line)<2:
            return 0
        else:
            return len(self.line)-1
    def doOneSecond(self):
        self.time +=1
        if chance(arrivalProb):
            self.line.append(Customer())
        self.finishCustomer()
        self.startCustomer()
    def finishCustomer(self):
        if self.servingCustomer and self.time == self.line[0].endTime:
            self.line = self.line[1:]
            self.servingCustomer = False
    def startCustomer(self):
        if self.servingCustomer:
            return False
        elif len(self.line)>0:
            self.servingCustomer = True
            #endTime is an object of the Customer Class
            self.line[0].endTime = self.time + self.line[0].transactionTime

pattern = 'Average line length {0:4.1f}'
for simulation in range(10):
    theBank = Bank()
    total = 0
    while theBank.time < secondsPerWorkDay:
        theBank.doOneSecond()
        total+=theBank.lineLength()
    print(pattern.format(total/secondsPerWorkDay))





























            
