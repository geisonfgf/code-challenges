"""Calculate the sum of the first 10 natural numbers
   whose square is divisibe by 5"""

result1 = sum(filter(lambda x: x ** 2 % 5 == 0, xrange(1, 100))[:10])
print "Result1:", result1

def numbers():
    number = 0
    while True:
        yield number
        number += 1

def condition(generator, func=lambda x: True):
    while True:
        value = next(generator)
        if func(value):
            yield value

def take(n, generator):
    for index in xrange(n):
        yield next(generator)

def sum_values(generator):
    s = 0
    for value in generator:
        s += value
    return s

result = sum_values(take(10, condition(numbers(), lambda x: x**2%5==0)))
print "Sum of first 10 natural numbers whose square is divided by 5:", result