# import modul
from cryptography.fernet import Fernet


# key generation
key = Fernet.generate_key()
 
# read string kunci
with open('filekunci.key', 'wb') as filekey:
   filekey.write(key)


# pakai kunci
fernet = Fernet(key)
 
# buka file csv
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/file_csv.csv', 'rb') as file:
    original = file.read()
     
# enkripsi csv
encrypted = fernet.encrypt(original)
 
# simpan file enkripsi
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/enkrip.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


#DEKRIPSI
    
# pakai kunci yang tadi
fernet = Fernet(key)

# buka file hasil enkrpisi
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/enkrip.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# langsung di dekripsi 
decrypted = fernet.decrypt(encrypted)

# cek hasil dekripsi cocok apa tidak ??
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/deskrip.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
