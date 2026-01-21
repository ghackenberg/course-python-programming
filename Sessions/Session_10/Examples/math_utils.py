def is_even(number: int) -> bool:
    """
    Checks if a number is even.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        bool: True if even, False if odd.
    """
    return number % 2 == 0

def calculate_average(numbers: list[float]) -> float:
    """
    Calculates the arithmetic mean of a list of numbers.
    
    Args:
        numbers (list[float]): A list of numbers.
        
    Returns:
        float: The average value, or 0.0 if the list is empty.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u) in a string.
    The check is case-insensitive.
    
    Args:
        text (str): The input string.
        
    Returns:
        int: The number of vowels found.
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
