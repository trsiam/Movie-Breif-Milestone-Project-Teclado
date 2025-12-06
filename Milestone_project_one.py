import json
import os
from termcolor import colored

filename = "data.json"
T = []

def function_one():
    global D,T
    if os.path.exists(filename):
        try:
            with open(filename,'r') as f:
                T = json.load(f)
        except json.JSONDecodeError:
            print('')
            
def function_two():
    keys = ['Movie Name','Year','Director']
    global T
    D = {}
    for i in keys:
        value = input(f' Enter {i}-')
        D[i] = value
    T.append(D)
    function_four()
    what()

def function_three():
    global T
    if T == []:
        print("There is nothing in the database")
    else:
        for i in T:
            print(i,"\n")
    print("\n")
    what()
   

def function_four():
    global D,T
    with open(filename,'w') as f:
        json.dump(T,f,indent=4)
    print("\n")
    print('data Saved')
    print("\n")
    what()

def function_five():
    global T
    temp_v =str(input('Enter Movie Attributes--'))
    for i in T:
        for key in i:
            if temp_v == i[key]:
                print('\n')
                print(i)
    what()            
            


def what():
    print("\n")
    print(" 1 . Show all Movies")
    print(" 2 . Add Movie")
    print(" 3 . Find Movie")
    print("\n")
    try:
        wh = int(input('What to Do- '))
        if wh == 1:
            print("\n")
            function_three()
        elif wh == 2:
            print("\n")
            function_two()
        elif wh == 3:
            print("\n")
            function_five()
    except:
        print(colored("<------Enter which numbered task you want to do---->",'red'))
    what()
function_one()
what()




