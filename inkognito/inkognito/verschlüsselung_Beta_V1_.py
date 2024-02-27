import random

def substitutionsalphabet_erstellen(schlüssel):
    normales_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitutions_alphabet = list(normales_alphabet)
    random.seed(schlüssel)
    random.shuffle(substitutions_alphabet)
    return substitutions_alphabet

def text_verschlüsseln(text, substitutions_alphabet):
    verschlüsselter_text = ""
    for char in text:
        if char.isalpha():
            index = ord(char.upper()) - ord('A')
            if char.islower():
                verschlüsselter_text += substitutions_alphabet[index].lower()
            else:
                verschlüsselter_text += substitutions_alphabet[index]
        else:
            verschlüsselter_text += char
    return verschlüsselter_text

def text_entschlüsseln(verschlüsselter_text, substitutions_alphabet):
    normales_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    entschlüsselter_text = ""
    for char in verschlüsselter_text:
        if char.isalpha():
            index = substitutions_alphabet.index(char.upper())
            if char.islower():
                entschlüsselter_text += normales_alphabet[index].lower()
            else:
                entschlüsselter_text += normales_alphabet[index]
        else:
            entschlüsselter_text += char
    return entschlüsselter_text

def text_in_datei_speichern(text, dateiname):
    with open(dateiname, "w") as file:
        file.write(text)

def main():
    schlüssel = input("Bitte geben Sie einen Schlüssel ein: ")
    substitutions_alphabet = substitutionsalphabet_erstellen(schlüssel)
    print("Substitutionsalphabet:", substitutions_alphabet)
    
    modus = input("Möchten Sie den Text verschlüsseln oder entschlüsseln? (v/e): ")
    if modus.lower() == 'v':
        klartext = input("Bitte geben Sie den zu verschlüsselnden Text ein: ")
        verschlüsselter_text = text_verschlüsseln(klartext, substitutions_alphabet)
        dateiname = input("Bitte geben Sie den Dateinamen für den verschlüsselten Text ein: ")
        text_in_datei_speichern(verschlüsselter_text, dateiname)
        print("Verschlüsselter Text wurde in '{}' gespeichert.".format(dateiname))
    elif modus.lower() == 'e':
        verschlüsselter_text = input("Bitte geben Sie den zu entschlüsselnden Text ein: ")
        entschlüsselter_text = text_entschlüsseln(verschlüsselter_text, substitutions_alphabet)
        dateiname = input("Bitte geben Sie den Dateinamen für den entschlüsselten Text ein: ")
        text_in_datei_speichern(entschlüsselter_text, dateiname)
        print("Entschlüsselter Text wurde in '{}' gespeichert.".format(dateiname))
    else:
        print("Ungültige Eingabe. Bitte geben Sie 'v' für Verschlüsseln oder 'e' für Entschlüsseln ein.")

if __name__ == "__main__":
    main()
