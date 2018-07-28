class PrimeSeq:
    def __init__(self, x):
        self.__primes = []
        self.length = x
        
        
    def __next__(self):     #appends another prime
        if self.length <= len(self.__primes):
            raise StopIteration
        if not self.__primes:
            self.__primes.append(2)
            return 2
        test = self.__primes[-1] + 1
        while 0 in list(map(lambda x: test%x, list(filter(lambda k: k <= test**(.5), self.__primes)))):
            test += 1
        self.__primes.append(test)
        return test

    def __iter__(self):
        return self

def main(): 
    primeseq = PrimeSeq(100)
    for p in primeseq:
        print(p)
    primes_lst = [p for p in PrimeSeq(100)] # uses the new object to get an iterator
    print(primes_lst)

main()

