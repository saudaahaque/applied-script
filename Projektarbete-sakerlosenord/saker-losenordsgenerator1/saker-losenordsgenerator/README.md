Projektidé 2 - Säker lösenordsgenerator
Projektbeskrivning

Detta projekt är en säker lösenordskontroller skriven i Python. Syftet är att analysera ett användarvalt lösenord och avgöra om det är svagt eller starkt baserat på flera säkerhetskrav samt jämförelse mot en känd lösenordsordlista.

Programmet hanterar automatiskt nedladdning och upppackning av lösenordslistan "rockyou.txt" vid behov. 

Projektet är genomfört enligt Projektidé 2: Säker lösenordsgenerator.

Uppfyllda krav (kopplat till bedömning):
Funktionalitet
Programmet:
- tar emot ett lösenord från användaren
- validerar lösenordet stegvis
- ger tydlig återkoppling vid första felet
- avgör om lösenordet är starkt eller svagt


Säkerhetskontroller:
Lösenordet måste:
- vara minst 12 tecken långt
- innehålla minst:
   - en stor bokstav
   - en liten bokstav
   - en siffra
   - ett specialtecken
- inte förekomma i en känd lösenordsordlista (rockyou.txt)



Säkerhetstänk & designval:
- Programmet använder en lokal ordlista (rockyou.txt) för att identifiera vanliga och läckta lösenord.
- Kontrollerna körs i logisk ordning:
   1. grundläggande krav (längd, teckentyper)
   2. därefter ordlistekontroll
- Programmet stoppar vid första felet, vilket gör återkopplingen tydlig och pedagogisk.
- Online-kontroll mot externa API:er har valts bort medvetet, då detta angavs som ett valfritt tillägg i projektbeskrivningen.


Teknik & verktyg:
- Språk: Python 3
- Utvecklingsmiljö: Visual Studio Code
- Operativsystem: macOS
- Körs via: Terminal



Projektstruktur:
saker-losenordsgenerator/
├── passwords-checker.py
├── README.md
└── rockyou.txt (laddas ner automatiskt vid körning)


Ordlista (rockyou.txt):
Projektet använder den välkända ordlistan rockyou.txt, som innehåller vanliga lösenord från tidigare dataläckor.
Filen ingår inte i GitHub-repot på grund av storlek och licens.
Programmet laddar autoamtikst ner och packar upp "rockyou.txt.gz" vid första körning om filen saknas. Ingen manuell nedladdning krävs. 


Körinstruktioner:
chmod +x passwords-checker.py
./passwords-checker.py
När programmet körs ombeds användaren att ange ett lösenord.

Exempel på körning:
Svagt lösenord (finns i ordlista):
"Lösenordet finns i ordboken. Välj ett starkare lösenord."

Starkt lösenord:
"Ditt lösenord bedöms som starkt."

Feedback & förbättringar från programmeringspartner: 
Efter feedback från William har programmet förbättrats genom att automatisera hanteringen av lösendordslistan "rockyou.txt". Programmet laddar nu själv ner och packar upp ordlistan vid behov, vilket gör lösningen mer användarvänlig och robust.
Dessutom har ett Linux-kompatibelt shebang (#!/usr/bin/env python3) lagts till så att skriptet kan köras direkt som ett program. 

Vidareutveckling:
Möjliga framtida förbättringar:
- Online-kontroll mot kända dataläckor
- Automatisk generering av säkra lösenord
- Visning av flera fel samtidigt


Författare: Sauda Haque

