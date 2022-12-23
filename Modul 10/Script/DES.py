from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

data = "Data ini akan dienkripsi"

# Enkripsi
key = b'InIkunCI'

BLOCK_SIZE = 32

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)

print ("Enkripsi Teks : ", data)
print ("Hasil Enkripsi Teks : ", encrypted_text)

# Dekripsi
key = b'InIkunCI'

des = DES.new(key, DES.MODE_ECB)
decrypted_text = des.decrypt(encrypted_text)

print ("Hasil Dekripsi Teks : ", decrypted_text.decode())