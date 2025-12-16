# Övning 3 – AV/EDR malware test (EICAR)

## Syfte
Syftet med denna övning är att testa hur en AV/EDR-lösning reagerar
på en känd virus-signatur (EICAR) samt verifiera detektionen via loggar.

## Miljö
- Värddator: macOS
- Virtuell miljö: Linux (Oracle VirtualBox)
- Programmeringsspråk: Python 3

## Genomförande
Ett Python-skript skapades enligt instruktionerna i dokumentet.
Skriptet kontrollerar först vilket operativsystem som används.

Eftersom testet enligt dokumentationen är avsett för Windows
(avsett att testas mot Windows Defender och Event Viewer),
avbryter skriptet automatiskt körningen om operativsystemet
inte är Windows.

Vid körning i Linux avslutas skriptet korrekt med ett
informationsmeddelande, vilket verifierar att OS-kontrollen
fungerar som tänkt.

## Varför EICAR inte testades i denna miljö
Linux-miljön saknar Windows Defender och Event Viewer,
vilket krävs för att genomföra och verifiera testet enligt
uppgiftens instruktioner.

Att köra EICAR-testet i Linux eller macOS skulle därför
inte uppfylla övningens krav.

## Testresultat (Linux)

Scriptet kördes i en Linux-miljö. Vid körning skapades en EICAR-testfil (`eicar_test.txt`) korrekt.  
Filen förblev kvar efter skapandet, vilket är förväntat beteende i denna miljö då ingen
antivirus- eller EDR-lösning är aktiv som reagerar på EICAR-signaturen.

Se `screenshot_terminal1.png` för terminalutskrift som visar körning av scriptet och skapandet
av testfilen.

## Hur testet hade genomförts i Windows
Om en Windows-miljö hade använts skulle skriptet:
1. Skapa en fil innehållande EICAR-signaturen
2. Vänta några sekunder
3. Kontrollera om filen tagits bort eller karantänats
4. Verifiera detektionen via Windows Defender Event Viewer
   (Event ID 1116 / 1117)

## Slutsats
Skriptet fungerar som förväntat genom att korrekt identifiera
operativsystem och avbryta körning i fel miljö.
