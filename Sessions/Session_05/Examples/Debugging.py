def calculate_factorial(n):
    """
    Calculates the factorial of a number (n!).
    Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    result = 1
    
    # INTENTIONAL BUG: range(n) starts at 0 and ends at n-1.
    # The first value of i will be 0.
    # 1 * 0 is 0, so 'result' becomes 0 and stays 0.
    for i in range(n):
        result = result * i
        
    return result

if __name__ == "__main__":
    number = 5
    print(f"Calculating factorial of {number}...")
    
    # This should print 120, but it will print 0
    fact = calculate_factorial(number)
    
    print(f"The factorial of {number} is {fact}")
