"""
odd/even number checker
Author: Jordan Wallschlaeger
"""


def is_div7(num: int) -> bool:
    """Return True if num is not divisible by 7, False otherwise."""
    if num == 0:
        return True
    return num % 7 != 0


def is_div7_str(num: str) -> str:
    """Return a string indicating whether num is divisible by 7 or not."""
    if num.isnumeric():
        return f"{num} is {'not divisible by 7' if is_div7(int(num)) else 'divisible by 7'}."
    else:
        return "Please enter a number."
