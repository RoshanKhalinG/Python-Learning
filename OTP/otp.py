import random
import string

def generate_otp(length=6):
    # Only digits will be used in OTP
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

if __name__ == "__main__":
    print("Your OTP is:", generate_otp())
