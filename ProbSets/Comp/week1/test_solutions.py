# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(1,2) == 3, "Failed for adding"

def test_smallest_factor():
    assert soln.smallest_factor(1) == 1, "Failed for 1"
    assert soln.smallest_factor(2)==2, "Failed for 2"
    assert soln.smallest_factor(6)==2, "Failed for composite number"
    assert soln.smallest_factor(7)==7, "Failed for prime number"
    assert soln.smallest_factor(9) == 3, "Failed for squared number"

# Problem 2: Test the operator function from solutions.py
def test_operator():
    with pytest.raises(TypeError) as excinfo:
        soln.operator(4, 0, 0)
    assert excinfo.value.args[0] == "Oper should be a string"
    with pytest.raises(ValueError) as excinfo:
        soln.operator(4, 0, ")")
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
    assert soln.operator(1, 2, "+")==3, "Failed for adding"
    assert soln.operator(1, 2, "-") == -1, "Failed for minusing"
    assert soln.operator(1, 2, "*") == 2, "Failed for multiplying"
    assert soln.operator(2, 1, "/") == 2, "Failed for dividing"
    with pytest.raises(ZeroDivisionError) as excinfo:
        soln.operator(4, 0, "/")
    assert excinfo.value.args[0] == "division by zero is undefined"

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_subtraction(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
    assert number_1 - number_3 == soln.ComplexNumber(-1, -7)
    assert number_2 - number_3 == soln.ComplexNumber(3, -4)
    assert number_3 - number_3 == soln.ComplexNumber(0, 0)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_division(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 / number_2 == soln.ComplexNumber(0.3, 0.1)
    with pytest.raises(ValueError) as excinfo:
        temp2 =soln.ComplexNumber(0,0)
        number_1.__truediv__(temp2)
    assert excinfo.value.args[0] == "Cannot divide by zero"

def test_complex_str(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert str(number_1) == "1+2i", "Not printing correctly"

def test_complex_eq(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    temp =  soln.ComplexNumber(1,2)
    assert number_1 == temp, "failed for equal"

def test_complex_init(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.real == 1 , "Real part not setting up correctly"
    assert number_1.imag == 2, "Imaginary part not setting up correctly"

def test_complex_conjugate(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.conjugate() == soln.ComplexNumber(1, -2)

def test_complex_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.norm() == math.sqrt(5)

def test_month():
    assert soln.month_length("April")==30, "failed for 30-day months"
    assert soln.month_length("January") == 31, "failed for 31-day months"
    assert soln.month_length("February") == 28, "failed for non-leap feb"
    assert soln.month_length("February", True) == 29, "failed for non-leap feb"
    assert soln.month_length("asd") == None, "failed for jibberish"


# Problem 4: Write test cases for the Set game.

@pytest.fixture
def set_up_cards():
    cards_1 = ["1022", "1122", "1020"]
    cards_2 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0)10", "2110", "1020"]
    cards_3 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "010", "2110", "1020"]
    cards_4 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0210", "2111", "1020"]
    cards_5 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0510", "2110", "1020"]
    cards_6 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0210", "2110", "1020"]
    return cards_1, cards_2, cards_3, cards_4, cards_5, cards_6

def test_set(set_up_cards):
    cards_1, cards_2, cards_3, cards_4, cards_5, cards_6 = set_up_cards
    assert soln.count_sets(cards_6) == 6, "Not counting cards correctly"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_1)
    assert excinfo.value.args[0] == "there are not exactly 12 cards"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_2)
    assert excinfo.value.args[0] == "one or more cards has a character other than 0, 1, or 2"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_3)
    assert excinfo.value.args[0] == "one or more cards does not have exactly 4 digits"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_4)
    assert excinfo.value.args[0] == "the cards are not all unique"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_5)
    assert excinfo.value.args[0] == "one or more cards has a character other than 0, 1, or 2"
