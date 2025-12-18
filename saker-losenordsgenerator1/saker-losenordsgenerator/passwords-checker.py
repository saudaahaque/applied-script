MIN_LENGTH = 12
WORDLIST_PATH = "rockyou.txt"
def is_in_wordlist(password, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if password.strip() == line.strip():
                    return True
    except FileNotFoundError:
        print("Ordboksfilen hittades inte:", wordlist_path)
    return False



password = input("Ange ett lösenord: ")

if not password:
    print("Du måste ange ett lösenord.")
elif len(password) < MIN_LENGTH:
    print("Lösenordet är för kort. Det måste vara minst", MIN_LENGTH, "tecken långt.")
elif not any(char.isupper() for char in password):
    print("Lösenordet måste innehålla minst en stor bokstav.")
elif not any(char.islower() for char in password):
    print("Lösenordet måste innehålla minst en liten bokstav.")
elif not any(char.isdigit() for char in password):
    print("Lösenordet måste innehålla minst en siffra.")
elif not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
    print("Lösenordet måste innehålla minst ett specialtecken.")

elif is_in_wordlist(password, WORDLIST_PATH):
    print("Lösenordet finns i ordboken. Välj ett starkare lösenord.")
else:
    print("Ditt lösenord bedöms som starkt.")