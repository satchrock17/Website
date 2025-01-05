
#sys wird verwendet um das Programm zu schließen
import sys

#globaler String text wird erstellt
text = ""

#text, der in einen Hopsitext verändert werden soll, wird hier vom user eingefügt
def textEinfügen():
    global text 
    text = str(input("Text eingeben: \n")).lower()

#alle Sonderzeichen werden entfernt, da diese beim Texthopsen übersprungen werden
def zeichenEntfernen():
    global textEntfernt
    entfernen = [" ",".", ",", ":", ";", "!", "?", "'","\"","'","´","`", "(", ")", "[", "]", "{", "}", "<", ">", "/", "|", 
    "-", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "~", "`", 
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    textEntfernt = text
    for i in entfernen:
        textEntfernt = textEntfernt.replace(i,"")

#hier wird der Buchstabe an der gegebenen Stelle "Eingelesen" um zu bestimmen, wie weit gehopst werden soll
def buchstabenSuche(index):
        anzahlschritte = 0
        if len(textEntfernt) > index:
            Buchstabe = textEntfernt[index]
            match Buchstabe:
                case "a":
                    anzahlschritte = 1
                    index = index + anzahlschritte
                    print("a")
                case "b":
                    anzahlschritte = 2
                    index = index + anzahlschritte
                    print("b")
                case "c":
                    anzahlschritte = 3
                    index = index + anzahlschritte
                    print("c")
                case "d":
                    anzahlschritte = 4
                    index = index + anzahlschritte
                    print("d")
                case "e":
                    anzahlschritte = 5
                    index = index + anzahlschritte
                    print("e")
                case "f":
                    anzahlschritte = 6
                    index = index + anzahlschritte
                    print("f")
                case "g":
                    anzahlschritte = 7
                    index = index + anzahlschritte
                    print("g")
                case "h":
                    anzahlschritte = 8
                    index = index + anzahlschritte
                    print("h")
                case "i":
                    anzahlschritte = 9
                    index = index + anzahlschritte
                    print("i")
                case "j":
                    anzahlschritte = 10
                    index = index + anzahlschritte
                    print("j")
                case "k":
                    anzahlschritte = 11
                    index = index + anzahlschritte
                    print("k")
                case "l":
                    anzahlschritte = 12
                    index = index + anzahlschritte
                    print("l")
                case "m":
                    anzahlschritte = 13
                    index = index + anzahlschritte
                    print("m")
                case "n":
                    anzahlschritte = 14
                    index = index + anzahlschritte
                    print("n")
                case "o":
                    anzahlschritte = 15
                    index = index + anzahlschritte
                    print("o")
                case "p":
                    anzahlschritte = 16
                    index = index + anzahlschritte
                    print("p")
                case "q":
                    anzahlschritte = 17
                    index = index + anzahlschritte
                    print("q")
                case "r":
                    anzahlschritte = 18
                    index = index + anzahlschritte
                    print("r")
                case "s":
                    anzahlschritte = 19
                    index = index + anzahlschritte
                    print("s")
                case "t":
                    anzahlschritte = 20
                    index = index + anzahlschritte
                    print("t")
                case "u":
                    anzahlschritte = 21
                    index = index + anzahlschritte
                    print("u")
                case "v":
                    anzahlschritte = 22
                    index = index + anzahlschritte
                    print("v")
                case "w":
                    anzahlschritte = 23
                    index = index + anzahlschritte
                    print("w")
                case "x":
                    anzahlschritte = 24
                    index = index + anzahlschritte
                    print("x")
                case "y":
                    anzahlschritte = 25
                    index = index + anzahlschritte
                    print("y")
                case "z":
                    anzahlschritte = 26
                    index = index + anzahlschritte
                    print("z")
                case "ä":
                    anzahlschritte = 27
                    index = index + anzahlschritte
                    print("ä")
                case "ö":
                    anzahlschritte = 28
                    index = index + anzahlschritte
                    print("ö")
                case "ü":
                    anzahlschritte = 29
                    index = index + anzahlschritte
                    print("ü")
                case "ß":
                    anzahlschritte = 30
                    index = index + anzahlschritte
                    print("ß")    
                
        return index

#buchstabenSuche wird solange wiederholt, bis die Sprungweite über die Textlänge hinausgeht. Gleichzeitig werden die Sprünge die pro Spieler benögtigt werden gezählt um zu bestimmen, wer gewonnen hat
def Spiel(index = 0):
    sprünge = 0
    while len(textEntfernt) > index:
        index = buchstabenSuche(index)
        sprünge = sprünge + 1
    print(sprünge)
    return sprünge

#um möglichst lange Hopsitexte erstellen zu können, kann am Ende des Textes ein weiterer Satz hinzugefügt werden um ein gleichzeitiges herausspringen zu verhindern.
def satzHinzufügen():
    neuerSatz = input("bitte den hinzuzufügenden Satz eingeben:\n").lower()
    global text 
    text = text + " " + neuerSatz
    print(text)
    main()

#um möglichst lange Hopsitexte erstellen zu können, kann am Anfang des Textes ein weiterer Satz hinzugefügt werden um ein gleichzeitiges herausspringen zu verhindern.
def satzVorneHinzufügen():
    neuerSatz = input("bitte den hinzuzufügenden Satz eingeben:\n").lower()
    global text
    text = neuerSatz + " " + text
    print(text)
    main()

#um möglichst lange Hopsitexte erstellen zu können, können am Ende des Textes beliebig viele Zeichen entfernt werden. Sinnvolle Texte können durch das entfernen ganzer Sätze erstellt werden. 
def buchstabenEntfernen():
    anzahl = int(input("gib die Anzahl der Zeichen an, die entfernt werden soll\n").lower())
    global text
    text = text[:-anzahl]
    print(text)
    main()

#um das erstellen möglichst langer Hopsitexte zu ermöglichen kann der Nutzer bei gleichzeitigem herausspringen eine Methode auswählen den Text zu verändern oder das Programm beenden.
def Bearbeiten():
    eingabe = input("1. Satz am Ende hinzufügen\n2. Satz am Anfang hinzufügen\n3. Zeichen am Ende entfernen\n4. Programm beenden\n").lower()
    if(eingabe == "1"):
        satzHinzufügen()
    elif(eingabe == "2"):
        satzVorneHinzufügen()
    elif(eingabe == "3"):
        buchstabenEntfernen()
    elif(eingabe == "4" or eingabe == "exit"):
        sys.exit()
    else:
        print("bitte 1., 2., 3. oder 4. auswählen")
        Bearbeiten()

#der mainloop des Programmes wird hier durchgeführt. Durch die zwei Methoden aufrufe darunter wird das Programm ursprünglich gestartet. Es werden beide Spiele durchgeführt, dann wird das ergebnis bestimmt und ermöglicht bei bedarf den Text zu verändern.
def main():
    
    zeichenEntfernen()

    ergebnisEins = Spiel(0)

    ergebnisZwei = Spiel(1)

    print("Spieler Eins: " , ergebnisEins)

    print("Spieler Zwei: " , ergebnisZwei)

    if(ergebnisEins > ergebnisZwei):
        print("Spieler Eins gewinnt!")
        weiter = input("1. neuen Text eingeben\n2. Programm beenden\n").lower()
        if weiter == "1":
            textEinfügen()
            main()
        elif weiter == "2":
            sys.exit()
    elif(ergebnisZwei > ergebnisEins):
        print("Spieler Zwei gewinnt!")
        weiter = input("1. neuen Text eingeben\n2. Programm beenden\n").lower()
        if weiter == "1":
            textEinfügen()
            main()
        elif weiter == "2":
            sys.exit()
    elif(ergebnisZwei == ergebnisEins):
        print("unentschieden\n")
        Bearbeiten()

textEinfügen()
main()