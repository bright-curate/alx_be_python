# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling non-numeric input and division by zero.
    Returns a string with the result or an error message.
    """
    try:
        # Convert both inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try dividing
        try:
            result = num / den
            return f"The result of dividing {num} by {den} is {result:.2f}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
