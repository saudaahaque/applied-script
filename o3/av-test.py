#!/usr/bin/env python3
import platform
import time
import os

# 1) Kontrollera OS
system = platform.system()

if system == "Windows":
    print("Windows upptäckt. Scriptet fortsätter..")
elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    exit()
elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    exit()
else:
    print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
    exit()

# 2) EICAR-signaturen (måste vara exakt)
eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# 3) Välj var filen ska skapas (ex: skrivbordet)
# På Windows brukar Desktop ligga här:
filnamn = os.path.join(os.path.expanduser("~"), "Desktop", "AV-TEST-NOT-DANGEROUS.txt")

# Skapa filen och skriv signaturen
try:
    with open(filnamn, "w") as f:
        f.write(eicar_str)
    print(f"[+++] Fil skapad: {filnamn}")
except Exception as e:
    print("[!!!] Kunde inte skapa filen. Testa en annan mapp (t.ex. Hämtade filer).")
    print(e)
    exit()

# Vänta så AV/EDR hinner reagera
time.sleep(3)

# Kontrollera om filen finns kvar och kan läsas
try:
    if os.path.exists(filnamn):
        with open(filnamn, "r") as f:
            fil_innehall = f.read()

        if fil_innehall == eicar_str:
            print("[???] Filen finns kvar och matchar EICAR. AV/EDR kanske inte har reagerat än.")
        else:
            print("[???] Filen finns kvar men innehållet skiljer sig.")
    else:
        print("[!!!] Filen finns inte kvar (troligen borttagen/karantänad av AV/EDR).")
        print("[---] Din AV/EDR-lösning är helt fungerande och skyddar mot kända virus-signaturer.")
except Exception as e:
    print("[!!!] Filen kunde inte läsas!")
    print("[!!!] AV har tagit bort/karantänat filen.")
    print("[---] Din AV/EDR-lösning är helt fungerande och skyddar mot kända virus-signaturer.")
#!/usr/bin/env python3
