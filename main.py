class Fibonacci():
    def __init__(self,max):
        self.max = max

    def fibonacci(self):
        a,b=0,1
        while b<self.max:
            yield a
            a,b=b, a+b

    def fibonacci2(self):
        fib=self.fibonacci()
        for f in fib:
            print(f)
if __name__ == '__main__':
    
    try:
        #get ceiling number from user
        max=int(input('enter maximum '))
        fib=Fibonacci(max).fibonacci2()
    except TypeError:
        print('invalid input')


