#!/usr/bin/env python
# coding: utf-8

# In[27]:


# set to 1 to allow extra debug info
debug_mode=1

#imports
import random
import math

#Accurcy setting
n=input("Enter the number of trials you wish to use: ")
while True:
    if n.isdigit():
        n=int(n)
        if n>0 and n<=10**6:
            break
        else:
            print("Invlaid number")
    else:
        print("Invlaid input")
    
    n=input("Enter the number of trials you wish to use:")
    
if debug_mode==1:
    print("Number of trials: "+str(n))
       
    
#avg val calculator by rolling one dice
def avg_val_one(sides, n):
    total=0
    dice=[i for i in range(1, sides+1)]
    for i in range(n):
        total+=random.choice(dice)
        
    avg=total/n
    
    avg=float(f'{avg:.3f}')
    
    print(avg)
    
#avg val cal by c one dice
def avg_val_one_p(sides):
    total=0
    dice=[i for i in range(1, sides+1)]
    for i in range(sides):
        total+=dice[i]*(1/sides)
        
    avg=float(f'{total:.3f}')
    
    print(avg)
    
#avg val by rolling two dice pick best
def avg_val_two_p1(sides, n):
    total=0
    dice=[i for i in range(1, sides+1)]
    for i in range(n):
        best=max(random.choice(dice),random.choice(dice))
        total+=best
        
    avg=total/n
    
    avg=float(f'{avg:.3f}')
    
    print(avg)
    
#avg val by cal two dice pick best
def avg_val_two_p1_p(sides):
    total=0
    for i in range(1, sides+1):
        for e in range(1, sides+1):
            total+=max(i,e)
        
    avg=total/(sides*sides)
    
    avg=float(f'{avg:.3f}')
    
    print(avg)
    
#avg val by rolling three dice pick best
def avg_val_three_p1(sides, n):
    total=0
    dice=[i for i in range(1, sides+1)]
    for i in range(n):
        best=max(random.choice(dice),random.choice(dice),random.choice(dice))
        total+=best
        
    avg=total/n
    
    avg=float(f'{avg:.3f}')
    
    print(avg)
    
#avg val by cal three dice pick best
def avg_val_three_p1_p(sides):
    total=0
    for i in range(1, sides+1):
        for e in range(1, sides+1):
            for j in range(1, sides+1):
                total+=max(i,e,j)
        
    avg=total/(sides*sides*sides)
    
    avg=float(f'{avg:.3f}')
    
    print(avg)
            
    
    
    
#select number of sides
sides=input("Enter the number of sides you wish the dice to have: ")
while True:
    if sides.isdigit():
        sides=int(sides)
        if sides>1 and sides<=100:
            break
        else:
            print("Invlaid number")
    else:
        print("Invlaid input")
    
    sides=input("Enter the number of trials you wish to use:")
    
if debug_mode==1:
    print("Number of sides: "+str(sides))
    
#main section
print("One dice rolling:")
avg_val_one(sides, n)
print("One dice prob:")
avg_val_one_p(sides)
print("two dice rolling:")
avg_val_two_p1(sides, n)
print("two dice prob:")
avg_val_two_p1_p(sides)
print("three dice rolling:")
avg_val_three_p1(sides, n)
print("three dice prob:")
avg_val_three_p1_p(sides)

        


# In[ ]:




