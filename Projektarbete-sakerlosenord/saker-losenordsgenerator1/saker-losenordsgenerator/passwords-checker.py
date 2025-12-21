#!/usr/bin/env python3
import subprocess 				                    	# Så att filen kan köra kommandon i CMD.
import os						                        # Så att programet kan arbeta med filvägar och directories.
import urllib.request					                # Så att programet kan ladda ner filer från internet.

script_dir = os.path.dirname(os.path.abspath(__file__)) # Ger mappen som denna python fil ligger i.
filename = "rockyou.txt.gz"				                # Namn på den fil som kommer laddas ner.
url = "https://weakpass.com/download/90/rockyou.txt.gz" # Var filen laddas ner från.
file_path = os.path.join(script_dir, filename)		    # Filvägen som senare kommer letas efter.

if not os.path.exists(file_path):			            # Om rockyou.txt.gz inte finns i mappen som passwords-checker.py ligger i så kommer filen att installeras.
    print("Fil ej hittad. Installerar...")
    urllib.request.urlretrieve(url, file_path)
    print(f"Installation färdig: {file_path}")
else:
    print("Nödvändig fil redan installerad!")
    
print("Extraherar filen")
subprocess.run(["gunzip", "rockyou.txt.gz"], check=True)# Kommando i Linux CMD som extraherar rockyou.txt.gz --> rockyou.txt
print("Filen extraherad!")

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
    

## Förbättring 1: Automatisk installation av rockyou.txt.gz
# Jag gjorde en snutt med kod för att förenkla användandet av programmet. Med denna snutt har koden blivit mer självgående och kräver endast att användaren gör filen körbar. 
# rockyou.txt.gz sätts också i rätt mapp så att passwords-checker.py fortfarande kan fungera.

## Förbättring 2: Automatisk extrahering av rockyou.txt.gz
# Genom importeringen av subprocess kan programmet använda sig av och printa ut linux kommandon i terminalen.
# Tack vare detta kan koden unzipa rockyou.txt.gz helt själv och användaren behöver inte utföra några extra steg för att programmet ska fungera.

# För att summera har både förbättringarna varit så kallade "Quality of Life fixes".
    
