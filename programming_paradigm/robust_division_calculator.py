def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling non-numeric input and division by zero.
    Returns a string with the result or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result:.1f}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
