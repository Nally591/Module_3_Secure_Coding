def caesar(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base= ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))
encrypted = caesar(message, shift)

print("Encrypted message:", encrypted)

def caesar_decrypt(text, shift):
    return caesar(text, -shift)

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)

        