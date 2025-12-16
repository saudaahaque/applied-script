#!/usr/bin/env python3
import os
import time
import platform

print("=== AV/EDR EICAR test ===")

# 1) Kontrollera OS (du har redan gjort detta – men här är en tydlig variant)
system = platform.system()
print(f"Operativsystem: {system}")

# 2) EICAR teststräng (ofarlig teststräng, används för AV-test)
EICAR = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# 3) Skapa fil i nuvarande katalog (o3/o3)
filename = "eicar_test.txt"
filepath = os.path.join(os.getcwd(), filename)

print(f"Skapar testfil: {filepath}")

# 4) Skriv testfil
with open(filepath, "w") as f:
    f.write(EICAR)

print("Testfil skapad.")
print("Väntar 3 sekunder för eventuell AV-reaktion...")
time.sleep(3)

# 5) Kontrollera om filen finns kvar
if os.path.exists(filepath):
    print(" Filen finns kvar.")
    print("Det är normalt på Linux om du inte har AV/EDR som reagerar på EICAR.")
else:
    print(" Filen har tagits bort.")
    print("AV/EDR har reagerat korrekt.")
