

def cal(num1,operation):
    """A type of Calculator which Perform
       Calculation like +,-,/ and *"""
    num2=float(input("Enter the Next number: "))
    if(operation=="+"):
        result=num1+num2
    elif(operation=="-"):
        result=num1-num2
    elif(operation=="*"):
        result=num1*num2
    else:
        result=num1/num2
    return result

def calling_calculator(num1):
    print(" + \n - \n / \n *")
    operation=input("Enter Operation you want to choose: ")
    # print(num1,operation)
    result=cal(num1,operation)
    return result

def start_template():    
    print("\nWelcome to Calculator\n")
    num1=float(input("Enter the first number: "))
    answer=calling_calculator(num1)
    opt=1
    while opt==1:
        
        opt=int(input(f"do you want to continue with result {answer} if Yes then 1: "))
        if(opt==1):
            answer=calling_calculator(answer)
        else:
            print("Final result of calculation is: ",answer)
            start_template()
            
start_template()