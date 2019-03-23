def selection():
    user_input = input("Encrypt(1) or Decrypt(2): ")
    while user_input != '1' and user_input != '2':
        user_input = input("Please enter: 1 for encryption or 2 for decryption: ")

    if(user_input == '1'):
        encrypt()
    if(user_input == '2'):
        decrypt()

def encrypt():
    password_for = input("Password for: ")
    password_to_encrypt = input("Password to be encrypted: ")
    encrypted_password = ''

    for char in range(len(password_to_encrypt)):
        if password_to_encrypt[char] not in decrypted_text:
            encrypted_password += password_to_encrypt[char]
        else:
            encrypted_password += encrypted_text[decrypted_text.index(password_to_encrypt[char])]

    password_log_write.write(password_for.strip() + ": " + encrypted_password + '\n')

    print(encrypted_password)

def decrypt():
    pass_for = []
    pass_word = []
    for colon in range(len(password_text)):
        pass_for.append(password_text[colon][:password_text[colon].index(':')])
        pass_word.append(password_text[colon][password_text[colon].index(':') + 2:])

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


encrypted_file = open('encrypted_file', 'r')
password_log_write = open('password_log', 'a')
decrypter_file = open('decrypter_file', 'r')
password_log = open('password_log', 'r')

encrypted_text = [line.strip() for line in encrypted_file]
decrypted_text = [line.strip() for line in decrypter_file]
password_text = [line.strip() for line in password_log]

selection()

encrypted_file.close()
password_log.close()
password_log_write.close()
decrypter_file.close()
