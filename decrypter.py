
encrypted_file = open('encrypted_file', 'r')
password_log = open('password_log', 'r')
decrypter_file = open('decrypter_file', 'r')


encrypted_text = [line.strip() for line in encrypted_file]
decrypted_text = [line.strip() for line in decrypter_file]
password_text = [line.strip() for line in password_log]

pass_for = []
pass_word = []

for colon in range(len(password_text)):
    pass_for.append(password_text[colon][:password_text[colon].index(':')])
    pass_word.append(password_text[colon][password_text[colon].index(':')+2:])


password_for = input("Password for: ")

if password_for not in pass_for:
    print("You do not have a password saved for: " + password_for)

password_to_decrypt = pass_word[pass_for.index(password_for)]

password = ''
build_block = ''

for code in range(len(password_to_decrypt)):
    build_block += password_to_decrypt[code]
    if build_block in encrypted_text:
        password += decrypted_text[encrypted_text.index(build_block)]
        build_block = ''


print(password)

encrypted_file.close()
password_log.close()
decrypter_file.close()