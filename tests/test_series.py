import pytest 
from math_series.math_script import lucas, fibonacci, sum_series
# testing fibonacci function 
def test_one_fibo():
    actual=fibonacci(1)
    excepted=1
    assert actual==excepted

def test_two_fibo():
    actual=fibonacci(2)
    excepted=1
    assert actual==excepted

def test_five_fibo():
    actual=fibonacci(5)
    excepted=5
    assert actual==excepted

def test_seven_fibo():
    actual=fibonacci(7)
    excepted=13
    assert actual==excepted

def test_negative_fibo():
    actual=fibonacci(-2)
    excepted="please enter a positive value"
    assert actual==excepted

def test_string_fibo():
    actual=fibonacci("f")
    excepted="please enter only numbers"
    assert actual==excepted


# testing lucas function 

def test_negative_lucas():
    actual=lucas(-2)
    excepted="please enter a positive value"
    assert actual==excepted

def test_string_lucas():
    actual=lucas("f")
    excepted="please enter only numbers"
    assert actual==excepted

def test_zero_lucas():
    actual=lucas(0)
    excepted=2
    assert actual==excepted
    
def test_one_lucas():
    actual=lucas(1)
    excepted=1
    assert actual==excepted

def test_two_lucas():
    actual=lucas(2)
    excepted=3
    assert actual==excepted

def test_five_lucas():
    actual=lucas(5)
    excepted=11
    assert actual==excepted
    
# testing sum_series function 

def test_negative_sum():
    actual=sum_series(-2)
    excepted="please enter a positive value"
    assert actual==excepted

def test_string_sum():
    actual=sum_series("f")
    excepted="please enter only numbers"
    assert actual==excepted

def test_zero_sum():
    actual=sum_series(0)
    excepted=0
    assert actual==excepted

def test_first_base_value_sum():
    actual=sum_series(0,3,4)
    excepted=3
    assert actual==excepted

def test_second_base_value_sum():
    actual=sum_series(1,3,4)
    excepted=4
    assert actual==excepted

def test_three_sum():
    actual=sum_series(3)
    excepted=2
    assert actual==excepted

def test_six_sum():
    actual=sum_series(6)
    excepted=8
    assert actual==excepted

def test_seven_diff_bases_sum():
    actual=sum_series(7,2,1)
    excepted=29
    assert actual==excepted