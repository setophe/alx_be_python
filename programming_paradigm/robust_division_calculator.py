def safe_divide(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError as e:
        return e