import string

encrypted_file = open('encrypted_file', 'r')
password_log = open('password_log', 'a')
decrypter_file = open('decrypter_file', 'r')

encrypted_text = [line.strip() for line in encrypted_file]
decrypted_text = [line.strip() for line in decrypter_file]

letter_up = list(string.ascii_uppercase)
letter_low = list(string.ascii_lowercase)
char_spec = list(string.punctuation)
digit = list(string.digits)

password_for = input("Password for: ")
password_to_encrypt = input("Password to be encrypted: ")
encrypted_password = ''

for char in range(len(password_to_encrypt)):
    if password_to_encrypt[char] not in decrypted_text:
        encrypted_password += password_to_encrypt[char]
    else:
        encrypted_password += encrypted_text[decrypted_text.index(password_to_encrypt[char])]

password_log.write(password_for.strip() + ": " + encrypted_password + '\n')

print(encrypted_password)

encrypted_file.close()
password_log.close()
decrypter_file.close()
