from time import time

data = int(input("Enter the number that you want to loop the execution for input * 3 to check performance :- "))

def performance_check(value):

    def wrapper(*ar, **kwr):
        time1 = time()
        result = value(*ar, **kwr)
        time2 = time()
        print(f'The total execution time is {time2 - time1} seconds ')
        return result
    return wrapper


@performance_check
def execution():
    for i in range(data):
        i * 3

execution()