class Mat():
    def __init__(self):
        pass

    def fibonacci(self,n):
        def fib(n):
            if n <= 1:
                return n
            else:
                return fib(n - 1) + fib(n - 2)
        return fib(n)

    def fatorial(self,n):
        def fat(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * fat( n-1 )
        return fat(n)
    
    def fibonarial(self,n):
        x=self.fibonacci(n)
        y=self.fatorial(x)
        return y

    def primo(self,n):
        if n%2==1:
            return"primo"
        else:
            return"não primo"
