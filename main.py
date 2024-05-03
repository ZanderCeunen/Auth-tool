#!/usr/bin/env python3
import pyotp
import hashlib
import base64
import getpass


def generate_totp(secret_key):
    totp = pyotp.TOTP(secret_key, interval=900)  # Set interval to 900 seconds (15 minutes)
    return totp.now()


if __name__ == "__main__":
    print("""     ___      __    __  .___________. __    __         .___________.  ______     ______    __      
    /   \    |  |  |  | |           ||  |  |  |        |           | /  __  \   /  __  \  |  |     
   /  ^  \   |  |  |  | `---|  |----`|  |__|  |  ______`---|  |----`|  |  |  | |  |  |  | |  |     
  /  /_\  \  |  |  |  |     |  |     |   __   | |______|   |  |     |  |  |  | |  |  |  | |  |     
 /  _____  \ |  `--'  |     |  |     |  |  |  |            |  |     |  `--'  | |  `--'  | |  `----.
/__/     \__\ \______/      |__|     |__|  |__|            |__|      \______/   \______/  |_______|
                                                                                                   """)
    print("\nWelcome to the Communication Authenticator!")

    #Get information
    print("1: Host a secure chat | 2: Connect to a secure chat")
    number = input("Number:")
    if number == "1":
        print("Please enter your official email to start.")
    elif number == "2":
        print("Please enter the host's official email to start.")
    email = input("E-mail:")
    print("Please enter your official password to start.")
    password = getpass.getpass("Password:")

    #Calculate codes
    pass_hash = hashlib.sha256((email + password).encode()).hexdigest()
    totp_code = generate_totp(base64.b32encode(pass_hash.encode()))

    #print generated code
    print(f"Validate yourself with : {totp_code[:3]}")
    print(f"Code of other person is: {totp_code[3:]}")
