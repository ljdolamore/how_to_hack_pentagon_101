alphabet = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
key = " m'8c>xFBE}52<)XQ[N-J&e@Yk#\"y!aDg]IA?*/P(,tn$p=SRu6fbWz3_GjTZ.i0qK+`:lM~vUV4r;o%7|{9^swHdLh\\CO1"

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "$$$ Pangram.Hack_The_Pentagon $$$"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
