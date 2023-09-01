from random import choice

from .constants import OTP_LENGTH


def create_random_otp():
    """Uses random.choice() function to create random digits string."""
    digits = '0123456789'
    result = ''
    for _ in range(OTP_LENGTH):
        result += choice(digits)
    return result
