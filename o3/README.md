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

Därför gjordes testet på Daniels Widows dator. Se `screenshot_terminal2.png`. 


## Testresultat (Windows)

Scriptet kördes i en Windows-miljö i PowerShell. Vid körning skapades en EICAR-testfil (`eicar_test.txt`) korrekt.  
Filen förblev kvar efter skapandet under en längre period än väntad. Men den försvann tillslut.

Se `screenshot_terminal1.png` för terminalutskrift som visar körning av scriptet och skapandet
av testfilen.)

## Slutsats
Skriptet fungerar som förväntat genom att korrekt identifiera
operativsystem och avbryta körning i fel miljö.
