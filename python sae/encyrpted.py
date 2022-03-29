# Fungsi Enkripsi
def encryption(unencrypt_string):
     global output_trnslt
     # translate = []
     encrypt_trnslt = ''
     for i in unencrypt_string:
          chip = ord(i)-96
          # print(chip)
          if chip % 3 != 0:
              encrypt_trnslt += str(chip)
          if chip % 3 == 0:
               encrypt_trnslt += i
               # for n in translate :
                    # encrypt_trnslt += n
                    # print(encrypt_trnslt)
     print(f'Pesan yang sudah di enkripsi : {encrypt_trnslt}')

# YANG FUNGSI DECRYPT MASIH ADA BUG NYA 
def decrypt(encrypt_string):
     unencrypt_trnslt = ''
     for i in encrypt_string:
          # convert_int = int(i)
          if i.isnumeric():
               convert_int = int(i)
               decrypt_chip = chr(convert_int+96)
               unencrypt_trnslt += decrypt_chip
     print(unencrypt_trnslt)

               

print('''
Option :
1. Encrypt 
2. Decrypt
''')
option = input('Pilih : ')
if option == '1':
     word = input("Masukan Kata/Kalimat yang ingin di enkripsi : ")
     encryption(word)

elif option == '2':
     word = input("Masukan Kata/Kalimat yang ingin di dekripsi : ")
     decrypt(word)

else :
     print('Opsi tidak tersedia')


print('Copyright : Jegi 2022')
