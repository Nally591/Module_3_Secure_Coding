import hashlib
message = input("Enter a message: ")
hash_object = hashlib.sha256(message.encode())
print("SHA-256 Hash:")
print(hash_object.hexdigest())

check_message = input ("\nEnter the message again to verify ")
check_hash = hashlib.sha256(check_message.encode())

if hash_object.hexdigest() == check_hash.hexdigest():
    print("The message has not changed")

else:
    print("The message has been changed")




        
    