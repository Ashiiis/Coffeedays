# Import required modules
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import hashlib

# Function to generate checksum
def generate_checksum(params):
    # Concatenate all parameters to form a string
    params_string = "&".join(f"{key}={value}" for key, value in sorted(params.items()))

    # Add your merchant key to the end of the string
    params_string += "&" + "your_merchant_key"

    # Hash the string using SHA-256
    hash_object = hashlib.sha256(params_string.encode("utf-8"))
    hash_hex = hash_object.hexdigest()

    # Use the first 32 characters of the hash as the checksum
    checksum = hash_hex[:32]

    # Encrypt the checksum using AES
    cipher = AES.new("your_encryption_key".encode("utf-8"), AES.MODE_ECB)
    encrypted_checksum = base64.b64encode(cipher.encrypt(pad(checksum.encode("utf-8"), AES.block_size))).decode("utf-8")

    return encrypted_checksum
