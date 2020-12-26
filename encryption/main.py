# import base64
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#
# password_provided = "password"  # This is input in the form of a string
# password = password_provided.encode()  # Convert to type bytes
# salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=100000,
#     backend=default_backend()
# )
# key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
#
# print(password_provided.encode())
# print(password)

from cryptography.fernet import Fernet
message = "password".encode()
key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)
print(encrypted)
print(decrypted)
if message == decrypted:
    print(True)

#
# from cryptography.fernet import Fernet, InvalidToken
# encrypted = b"...encrypted bytes..."
#
# f = Fernet(key)  # An example of providing the incorrect key
# try:
#     decrypted = f.decrypt(encrypted)
#     print("Valid Key - Successfully decrypted")
# except InvalidToken as e:  # Catch any InvalidToken exceptions if the correct key was not provided
#     print("Invalid Key - Unsuccessfully decrypted")