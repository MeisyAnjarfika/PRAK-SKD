from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
data_to_encrypt = input('Masukan Teks : ')
data = data_to_encrypt.encode('utf-8')

# Enkripsi
cipher_encrypt = AES.new(key, AES.MODE_CFB)
ciphered_bytes = cipher_encrypt.encrypt(data)

iv = cipher_encrypt.iv
ciphered_data = ciphered_bytes

# Dekripsi
cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
deciphered_bytes = cipher_decrypt.decrypt(ciphered_data)

decrypted_data = deciphered_bytes.decode('utf-8')

# Hasil
print("Hasil Enkripsi : ", ciphered_data)
print("Hasil Dekripsi : ", decrypted_data)