import pytest
from math_utils import is_even, calculate_average, count_vowels

def test_is_even():
    # Happy path
    assert is_even(2) is True
    assert is_even(7) is False
    # Edge case
    assert is_even(0) is True

def test_calculate_average_normal():
    assert calculate_average([1, 2, 3]) == 2.0
    assert calculate_average([10, 20]) == 15.0

def test_calculate_average_empty():
    # Testing an edge case (empty list)
    assert calculate_average([]) == 0.0

def test_calculate_average_single_item():
    assert calculate_average([5.5]) == 5.5

def test_count_vowels_basic():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1

def test_count_vowels_case_insensitive():
    assert count_vowels("AEIOU") == 5

def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0

def test_count_vowels_empty():
    assert count_vowels("") == 0
