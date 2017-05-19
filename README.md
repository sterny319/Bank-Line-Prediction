# Bank-Line-Prediction
 A bank is open from 9 a.m. to 5 p.m. There is one teller.  Customers arrive at random times, averaging 20 per hour.  Each needs a random amount of time with the teller,  ranging from one to five minutes.  When one customer is with the teller, others wait on a line.  Write a simulation program to find out, on average, how long the line at the   bank will be.
Then rerun the simulation with an average of 25 customers arriving per hour.  
You may find the following function useful. It returns ​True​ with probability ​p​:    
   def chance(p):      
     return random.random()<p    
Suppose, for example, that we pass in .3. The ​random.random​ function picks a number at random between 0 and 1. There is a 30 percent chance that this number will happen to be lower than .3, so there is a 30 percent chance that the ​chance  function will return ​True​.    
We use the function this way:    
 if chance(.3):
   something
 
 In this case, there is a 30 percent chance that the ‘something’ in the body of the ​if  statement will happen. 
