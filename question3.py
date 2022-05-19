import os
import requests

#Setting Environment variables
#os.environ['iterations'] = input("Enter the number of iterations: ")
#os.environ['site'] = input("Enter the site url: ")

#This declares the Totaltime variable and sets it to 0
Totaltime = 0
#This converts the environmental variable from a string to an int assigned to t so that a while loop can use a simple int comparison
t = int(os.environ.get('iterations'))
i = 0
#The while loop requests a response from the site variable and records the reponses time and addds it to the Totaltime variable. 
while i < t:
    response = requests.get(os.environ.get('site'))
    Totaltime += response.elapsed.total_seconds()
    i += 1

#In order to check correct operation and display the total time taken as well as teh number of iterations compelted. 
print('It took ', Totaltime, ' seconds to complete ',i,' iterations')
