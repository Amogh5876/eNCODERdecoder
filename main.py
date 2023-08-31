import base64

def decode():
    message = input("Message to be decoded: ")
    message_in_bytes = bytes(message,"utf-8")
    decoded_message = base64.b64decode(message_in_bytes)
    print("Decoded Messege: " , decoded_message)

def encode():
    message = input("Message to be encoded: ")
    message_in_bytes = bytes(message,"utf-8")
    encoded_message= base64.b64encode(message_in_bytes)
    print("Encoded_message: ", encoded_message)

print("Encoder/Decoder")
print("1.Encoder\n2.Decoder")
option = int(input("Choose One Option:1/2"))
if option == 1:
    encode()
elif option == 2:
    decode()
else:
    print("Wrong Choice")
