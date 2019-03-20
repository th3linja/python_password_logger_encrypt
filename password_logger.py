import string

encrypted_file = open('encrypted_file', 'r')
encrypted_text = [line.strip() for line in encrypted_file]

letter_up = list(string.ascii_uppercase)
letter_low = list(string.ascii_lowercase)
char_spec = list(string.punctuation)
digit = list(string.digits)

decrypter_file = open('decrypter_file', 'r')
decrypted_text = [line.strip() for line in decrypter_file]

password_to_encrypt = input("Password to be encrypted: ")
encrypted_password = ''

for char in range(len(password_to_encrypt)):
    if password_to_encrypt[char] not in decrypted_text:
        encrypted_password += password_to_encrypt[char]
    else:
        encrypted_password += encrypted_text[decrypted_text.index(password_to_encrypt[char])]


print(encrypted_password)
encrypted_file.close()
