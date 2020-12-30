#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included). The numbers obtained should be printed in a comma - separated sequence on a single line.

# In[24]:


print(*(i for i in range(2000,3200) if i%7 == 0 if i%5 !=0), sep = ',') # using concepts of generators and list comprehension


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the reverse order with a space between first name and last name.

# In[32]:


fname = input("Please enter first name:")
lname = input("Please enter last name:")
print(lname + ' ' + fname) # Using concept of Concatenation 


# 3. Write a python program to find the volume of a sphere with diameter 12 cm. 

# In[33]:


import math # imported math library to get the pi value (3.14)
pi = math.pi
r = float(12/2) # radius formula (r = diameter/2)
v = float((4/3)*pi*pow(r,3)) # Volume of a sphere formula (V= 4/3*pi*r^3) also using the concept of power function (r^3 = pow(r,3))
print("Volume of a sphere with diameter 12 cm is",v)

