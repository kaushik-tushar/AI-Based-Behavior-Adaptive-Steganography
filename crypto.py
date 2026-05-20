import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 🔐 Fixed secret password
SECRET_KEY = hashlib.sha256(b"default123").digest()


def encrypt_message(message):
    # Create AES cipher in CBC mode
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)

    # Encrypt message
    ciphertext = cipher.encrypt(
        pad(message.encode(), AES.block_size)
    )

    # Combine IV + ciphertext
    encrypted_data = cipher.iv + ciphertext

    # Convert to Base64 string
    return base64.b64encode(encrypted_data).decode()


def decrypt_message(encrypted_message):
    # Decode Base64
    raw_data = base64.b64decode(encrypted_message)

    # Extract IV and ciphertext
    iv = raw_data[:16]
    ciphertext = raw_data[16:]

    # Create cipher for decryption
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv=iv)

    # Decrypt and unpad
    decrypted_data = unpad(
        cipher.decrypt(ciphertext),
        AES.block_size
    )

    return decrypted_data.decode()
