def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result is: {result}"
    
    except ZeroDivisionError:
        return f"Error: Divison by zero is not allowed"
    
    except ValueError:
        return "Error: Non-numeric input provided."

