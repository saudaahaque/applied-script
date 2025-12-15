import random
import hashlib

def generate_password(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Lösenordslängder som ska testas
lengths = [3, 4, 5, 6, 7]

print("Genererar lösenord i olika längder och deras MD5-hashar:\n")

for length in lengths:
    password = generate_password(length)
    hash_value = md5_hash(password)
    print(f"Längd: {length} | Lösenord: {password} | Hash: {hash_value}")
