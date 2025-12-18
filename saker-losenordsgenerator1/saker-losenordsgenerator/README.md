# Projektidé 2 – Säker lösenordsgenerator

## Projektbeskrivning

Detta projekt är en säker lösenordskontroller skriven i Python.  
Programmet analyserar ett lösenord som användaren anger och avgör om det är svagt eller starkt baserat på flera säkerhetskrav samt en jämförelse mot en känd lösenordsordlista.

Projektet är genomfört enligt **Projektidé 2: Säker lösenordsgenerator**.


## Funktionalitet

Programmet:
- tar emot ett lösenord från användaren
- ger tydlig återkoppling vid första felet
- avgör om lösenordet är starkt eller svagt


## Säkerhetskontroller

Lösenordet måste:
- vara minst **12 tecken långt**
- innehålla minst:
  - en **stor bokstav**
  - en **liten bokstav**
  - en **siffra**
  - ett **specialtecken**
- inte förekomma i en känd lösenordsordlista (`rockyou.txt`)


## Säkerhetstänk & designval

Programmet använder en lokal ordlista (`rockyou.txt`)  
för att identifiera vanliga och läckta lösenord.

Kontrollerna körs i logisk ordning:
1. Grundläggande krav (längd och teckentyper)
2. Därefter ordlistekontroll

Programmet stoppar vid första felet för att ge tydlig och pedagogisk återkoppling till användaren.

Online-kontroll mot externa tjänster har valts bort, då detta angavs som ett valfritt tillägg i projektbeskrivningen.


## Teknik & verktyg

- **Programmeringsspråk:** Python 3
- **Utvecklingsmiljö:** Visual Studio Code
- **Operativsystem:** macOS
- **Körs via:** Terminal


## Projektstruktur

```text
saker-losenordsgenerator/
├── passwords-checker.py
├── README.md
└── rockyou.txt   (ingår ej i GitHub-repot)

## Ordlista (rockyou.txt)

Projektet använder den välkända ordlistan **rockyou.txt**, som innehåller vanliga lösenord från tidigare dataläckor.

Filen ingår **inte** i GitHub-repot på grund av storlek och licens.

### Så laddar du ner ordlistan

1. Besök:  
   https://weakpass.com/wordlists/rockyou.txt
2. Ladda ner filen
3. Om filen är komprimerad (`.gz`), packa upp den:
   ```bash
   gunzip rockyou.txt.gz
4. Placera rockyou.txt i samma mapp som passwords-checker.py

## Körinstruktioner

Öppna terminalen i projektmappen och kör:

```bash
python3 passwords-checker.py

När programmet körs ombeds användaren att ange ett lösenord.

## Exempel på körning

**Svagt lösenord (finns i ordlistan):**
```text
Lösenordet finns i ordboken. Välj ett starkare lösenord.
 **Starkt lösenord:
Ditt lösenord bedöms som starkt.

## Vidareutveckling

Möjliga framtida förbättringar:
- Online-kontroll mot kända dataläckor
- Automatisk generering av säkra lösenord
- Visning av flera fel samtidigt


## Författare: Sauda Haque**

