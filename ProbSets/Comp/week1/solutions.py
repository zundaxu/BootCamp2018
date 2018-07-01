# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math

# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
# def operator(a, b, oper):
#     if type(oper) != str:
#         raise ValueError("Oper should be a string")
#     if len(oper) != 1:
#         raise ValueError("Oper should be one character")
#     if oper == "+":
#         return a + b
#     if oper == "/":
#         if b == 0:
#             raise ValueError("You can't divide by zero!")
#         return a/float(b)
#     if oper == "-":
#         return a-b
#     if oper == "*":
#         return a*b
#     else:
#         raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# The following code of problem 2 is the same as the code in the notebook.
def operator(a, b, oper):
    if type(oper) is not str:
        raise TypeError("Oper should be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
             raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))

# Problem 5: Write code for the Set game here
def count_sets(cards):
    '''
    Return the number of sets in the provided Set hand.
    Parameters:
    cards (list(str)) a list of twelve cards as 4-bit integers in
    base 3 as strings, such as ["1022", "1122", ..., "1020"].
    Returns:
    (int) The number of sets in the hand.
    Raises:
    ValueError: if the list does not contain a valid Set hand, meaning
    - there are not exactly 12 cards,
    - the cards are not all unique,
    - one or more cards does not have exactly 4 digits, or
    - one or more cards has a character other than 0, 1, or 2.
    '''
    results = []
    combs = list(itertools.combinations(cards,3))
    if len(cards)!=12:
        raise ValueError("there are not exactly 12 cards")
    elif len(set(cards))!=len(cards):
        raise ValueError("the cards are not all unique")
    elif sum([1 if len(i)!=4 else 0 for i in cards])!=0:
        raise ValueError("one or more cards does not have exactly 4 digits")
    else:
        for comb in combs:
            a,b,c = comb
            if is_set(a,b,c) :
                results.append(1)
        return int(sum(results))

def is_set(a, b, c):
    '''
    Determine if the cards a, b, and c constitute a set.
    Parameters:
    a, b, c (str): string representations of 4-bit integers in base 3.
    For example, "1022", "1122", and "1020" (which is not a set).
    Returns:
    True if a, b, and c form a set, meaning the ith digit of a, b,
    and c are either the same or all different for i=1,2,3,4.
    False if a, b, and c do not form a set.
    '''
    counter = 0
    try:
        a = [int(i) for i in list(a)]
        b = [int(i) for i in list(b)]
        c = [int(i) for i in list(c)]
    except ValueError:
        raise ValueError("one or more cards has a character other than 0, 1, or 2")
    temp = a.copy()
    temp.extend(b)
    temp.extend(c)
    print (temp)
    if sum([1 if (int(i)>=3) else 0 for i in temp])!=0:
        raise ValueError("one or more cards has a character other than 0, 1, or 2")
    for i in range(3):
        if (a[i]==b[i] & b[i]==c[i]):
            counter += 1
        elif (a[i] !=b[i]&b[i]!=c[i]&a[i]!=c[i]):
            counter += 1
    return counter==3

cards_1 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0210", "2110", "1020"]
cards_2 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0510", "2110", "1020"]
