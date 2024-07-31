import string
import random
def OTP(len):
    id = "".join(random.choice(string.digits) for _ in range(len))
    return id