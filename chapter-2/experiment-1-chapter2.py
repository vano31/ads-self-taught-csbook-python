#Print the numbers from 1 to 10 recursively

"""

Requirements for a recursive function:
-function must have a base case
-function must call itself
-function must end when function reaches base case


-The purpose of the base case is to resolve the stack. Recursive functions work via last in, first out?
-The bottom of the stack is the base case. When the base case is reached, base case n equals a number, which
can then be used to resolve all other expressions ascending the stack.
-Since I am ascending from 1 to 10, I need to have the base case b = 1. Once the base case b = 1, the next 
expression in the stack will be b + 1, which I know equal 2. Then I can make b = b + 1 = 2. 
But then, can't I make 10 the base case? Have the incrementation stop once b = 10?
b, the variable in question, goes through recursion in the first place because the computer is continuouly trying
to evaluate b since it is not not expressed. Or maybe that should be the point of num
-We currently have two variables. num and b. num is the number we want the program to stop at once it prints all
the numbers starting at 1. 
-Since the value of num is stated, the value of b should be the variable that is continoulsy being evaluated. 
-Therefore b has to be the variable with a base case. Question is, where should the number stop?
-function numberPrinter is supposed to repeatedly call b until b equals a base case. when 

peerhaps, b acts as the makeshift counter, and when numberPrinter(b) = 1. Every other 

What I don't know:
How am I suppossed to iterate over multiple operations that increasingly increase by one and have it stop 
once the printed value equals the number specified in the parameter?
How does the base case change?
The base case doesn't change. It is the evaluation of the function that changes. And the evaluation 
stack continues to equal a smaller part of the expression over and over until it reaches the base case,
in which the entire expression can be evaluated.

1 - 2 - 3 - 4 - 5 - 6 - 7 - 8

def recurseLooper(num):
    if num == 0:
        recurseLooper(num) = 9
    print(recurseLooper(num - 1))


"""


'''
def numberPrinterLoop (num):
    for x in range(1, num, 1):
        print(x)

numberPrinterLoop(11)

'''

'''

def Looper(num):
    if num == 0:
        return 1
    print(Looper(num - 1))

Looper(10)

'''

def LooperRecurse(n):
    print(n)
    if n > 0:
        LooperRecurse(n - 1)

#LooperRecurse(5)



        




