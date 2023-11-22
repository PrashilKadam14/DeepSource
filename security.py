# example.py

import os

def execute_command(user_input):
    os.system(f"echo {user_input}")

user_input = input("Enter something: ")
execute_command(user_input)
