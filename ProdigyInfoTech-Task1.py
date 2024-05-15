def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26
            if decrypt:
                shifted = (26 + shifted) % 26  
            result += chr(base + shifted)
        else:
            result += char
    return result

def main():
    print("*********************************************************************************")
    print(" ")
    print("  Welcome to the Cybersecurity Caesar Cipher Encryption and Decryption Tool!")
    print(" ")
    print("*********************************************************************************")
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()

        if choice == 'q':
            print(" ")
            print(" Exiting the Cybersecurity Caesar Cipher Tool. Stay secure! ")
            print(" ")
            break

        elif choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the secret shift value for encryption: "))
            encrypted_message = caesar_cipher(message, shift)

            print(" Encryption successful! Transmitting secure message: ")
            print("****************************************************")
            print(" ")
            print(encrypted_message)
            print(" ")
            print("****************************************************")

        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the secret shift value for decryption: "))
            decrypted_message = caesar_cipher(message, shift, decrypt=True)

            print(" Decryption complete! Revealing confidential message: ")
            print("****************************************************")
            print(" ")
            print(decrypted_message)
            print(" ")
            print("****************************************************")
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()

