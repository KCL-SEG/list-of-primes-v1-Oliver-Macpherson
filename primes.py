"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count=0
    while count<number_of_primes:
        for num in range(2,100000000000000):
            prime = True
            for i in range(2,num):
                if num%i==0:
                    prime = False
            if prime:
                list.append(num)
                count+=1
                if count>=number_of_primes:
                    break
    return list

#print(primes(10))
