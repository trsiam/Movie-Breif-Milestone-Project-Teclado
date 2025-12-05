# import ast
# user_input = input("Enter a dictionary: ")
# d = ast.literal_eval(user_input)
# print(d)
import json
import os
keys = ['Movie Name','Year','Quality']
filename = "data.json"
D = {}
def function_one():
    global D
    if os.path.exists(filename):
        with open(filename,'r') as f:
            D = json.load(f)
    what()

def function_two():
    global D
    for i in keys:
        value = input(f' Enter {i}-')
        D[i] = value
    what()

def function_three():
    global D
    with open(filename,'w') as f:
        json.dump(D,f,indent=4)
    print('data Saved')
    what()

def function_four():
    global D
    print(D)
    what()

def what():
    wh = int(input('What to Do'))
    if wh == 1:
        function_one()
    elif wh == 2:
        function_two()
    elif wh == 3:
        function_three()
    elif wh == 4:
        function_four()


what()





