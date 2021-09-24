def function1():
    print("This is ENG1003's first Tuturial Programing Task \nEnter the fuction to be excute:")
    print("YAN\nHim\nIan\nWalton\nRonald")
    

def function2():
    print('This text represent the content of function 2')  #To be edited by member 2, Replace this line with your actual function code


def function3():
    print('This text represent the content of function 3')  #To be edited by member 3, Replace this line with your actual function code


def function4():
    x = 6 
    y = 4
    'Comparison；x>y = 6>4'
    print(x>y)
    print('Therefore, x is larger than y')  #To be edited by member 4, Replace this line with your actual function code


#The Main function edited by Group leader
print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')   #Ask for an integer

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
else:
    print('There is no function', inp)
