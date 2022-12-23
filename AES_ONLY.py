from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


"""
data="hello world"
key1 = get_random_bytes(16)
key2 = get_random_bytes(16)
key3 = get_random_bytes(16)


cipher = AES.new(key1, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data.encode('ASCII'))

cipher = AES.new(key1, AES.MODE_EAX, cipher.nonce)
data_d = cipher.decrypt_and_verify(ciphertext, tag)

print("hello")
print(ciphertext)
print(f"tag is : {tag}")
print(f"my real text is {data_d}")


a="hello"
b=" world"
print(a+b)
st="Hello world"

binary_st=' '.join(format(ord(x), 'b') for x in st)

print(f"binary is {binary_st}")

key2 = get_random_bytes(16)
print(f"key is {key2}")
"""


destination_port_number=""


encrypted_message3= "i like pineapple pizza"+destination_port_number
print("This is the message to be encrypted ",encrypted_message3)

key3 = b'\xceO\xdd"\xef\x1fV.\x1c\x835\xbcD\x87\xf5\xad'
# text file for node 3

cipher3 = AES.new(key3, AES.MODE_EAX)
ciphertext3, tag3 = cipher3.encrypt_and_digest(encrypted_message3.encode('ASCII'))
f = open("tag_node_3.txt", "wb")
f.write(tag3)
f.close()
print("This is the encrypted message ",ciphertext3)

f = open("tag_node_3.txt", "wb")
writing=tag3
f.write(writing)
f.close()


f= open("tag_node_3.txt", "rb")
tag3_read=f.read();

cipher3.nonce=' '.join(map(str,list(cipher3.nonce)))

cipher3.nonce=bytes(map(int,cipher3.nonce.split(' ')))
              
cipher3 = AES.new(key3, AES.MODE_EAX, cipher3.nonce)
decrypt1=cipher3.decrypt_and_verify(ciphertext3, tag3_read)
print("This is the decrypted message ",decrypt1)



