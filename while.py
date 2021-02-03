#You won't need to import any modules
#A while loop is like an if statement and a for loop combined. 
#Here is the while loop

#We could run an infinite loop by doing while True:

while True:
  print("hi")
  #This would print hi forever, since it is always true. But a while loop can stop...
 
 
import random
 
running = True
 
while running:
  print("hi!")
  if random.randint(1, 10) == random.randint(1, 1):
    running = False
    #The while loop would stop here because running now equals False

#Like I said before, a while loop is like an if statement

a = 10

while a == 10:
  print("hi!")
  a = a + 1
#This would print out one hi, since after a = a + 1, a is NOT (!=) equal to 10.
