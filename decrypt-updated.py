import os
from cryptography.fernet import Fernet
from colorama import Fore, Style

# Initialize colorama
Fore.GREEN, Style.RESET_ALL

# Get the path of the encrypted file from the user
encrypted_file_path = input("Enter the path of the encrypted file: ")

# Check if the file exists
if not os.path.exists(encrypted_file_path):
    print(f"{Fore.RED}File '{encrypted_file_path}' not found.{Style.RESET_ALL}")
    exit()

# Get the path of the file to save the decrypted contents to
decrypted_file_path = input("Enter the path of the file to save the decrypted contents to: ")

# Read the contents of the encrypted file
with open(encrypted_file_path, "rb") as f:
    encrypted_contents = f.read()

# Get the Fernet key from the user
key = input("Enter the Fernet key: ")

# Create a Fernet object with the key
fernet = Fernet(key)

try:
    # Decrypt the contents of the file
    decrypted_contents = fernet.decrypt(encrypted_contents)

    # Write the decrypted contents to a new file
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_contents)

    # Print the success message
    print(Fore.GREEN + "Decryption process complete.")
    print(f" - Encrypted file: '{encrypted_file_path}'")
    print(f" - Decrypted file: '{decrypted_file_path}'")
    print("Decryption process completed successfully." + Style.RESET_ALL)
except:
    # Print the error message
    print(Fore.RED + "Decryption process failed. Please check your inputs." + Style.RESET_ALL)
