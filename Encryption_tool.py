from cryptography.fernet import Fernet

KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)
    print("Encryption key generated and saved.")


def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    print("Encrypted message:")
    print(encrypted.decode())


def decrypt_message(encrypted_message):
    key = load_key()
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message.encode())
    print("Decrypted message:")
    print(decrypted.decode())


while True:
    print("\n---Encryption / Decryption Tool---")
    print("1. Generate Key")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        msg = input("Enter message to encrypt: ")
        encrypt_message(msg)

    elif choice == "3":
        encrypted_msg = input("Enter encrypted message: ")
        decrypt_message(encrypted_msg)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
