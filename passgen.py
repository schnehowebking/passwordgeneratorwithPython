import random

lowerr_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "~!@#$%^&*()<>/\?"

use_for = lowerr_case + upper_case + number + symbols
length_for_pass = 16

password ="".join(random.sample(use_for, length_for_pass))
print(password)
