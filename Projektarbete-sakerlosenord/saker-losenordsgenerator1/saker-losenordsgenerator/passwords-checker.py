#!/usr/bin/env python3 
#Gör att scriptet kan köras direkt i Linux med ./passwords-checker.py

MIN_LENGTH = 12
WORDLIST_PATH = "rockyou.txt"

#Feature från William: 
import os
import urllib.request
import subprocess
import gzip
import shutil

ROCKYOU_URL = "https://weakpass.com/wordlists/rockyou.txt.gz"
ROCKYOU_GZ = "rockyou.txt.gz"


def ensure_rockyou(wordlist_path: str = WORDLIST_PATH) -> None:
    """
    Ser till att rockyou.txt finns lokalt.
    Om den saknas: ladda ner rockyou.txt.gz och packa upp.
    """
    if os.path.exists(wordlist_path):
        return  # allt klart

    print(f"{wordlist_path} saknas. Laddar ner {ROCKYOU_GZ}...")

    # Ladda ner .gz
    try:
        urllib.request.urlretrieve(ROCKYOU_URL, ROCKYOU_GZ)
    except Exception as e:
        print("Kunde inte ladda ner rockyou.txt.gz:", e)
        print("Ladda ner filen manuellt och placera den i samma mapp som scriptet.")
        return

    # Försök packa upp med gunzip
    try:
        subprocess.run(["gunzip", "-f", ROCKYOU_GZ], check=True)
        print("Nedladdning & uppackning klar (gunzip).")
        return
    except FileNotFoundError:
        # gunzip finns inte (t.ex. vissa miljöer)
        print("gunzip finns inte i systemet. Packar upp med Python istället...")
    except subprocess.CalledProcessError as e:
        print("gunzip misslyckades:", e)
        print("Försöker packa upp med Python istället...")

    # Fallback: packa upp via Python (funkar överallt)
    try:
        with gzip.open(ROCKYOU_GZ, "rb") as f_in, open(wordlist_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        os.remove(ROCKYOU_GZ)
        print("Nedladdning & uppackning klar (Python).")
    except Exception as e:
        print("Kunde inte packa upp rockyou.txt.gz:", e)
        print("Packa upp manuellt: gunzip rockyou.txt.gz")


def is_in_wordlist(password, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if password.strip() == line.strip():
                    return True
    except FileNotFoundError:
        print("Ordboksfilen hittades inte:", wordlist_path)
    return False

ensure_rockyou()
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