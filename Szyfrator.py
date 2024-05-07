
# Importing functions used in the program.
# Importowanie funkcji wykorzystywanych w programie.

import subprocess
import sqlite3
import random
import os
import textwrap

# Key library.
# Biblioteka kluczy.

conn = sqlite3.connect('KEYS')
cur = conn.cursor()

# A list containing a cipher.
# Lista zawierająca szyfr.
Cipher = []

while True:

# Main menu.
# Menu główne.

    print(  "       Enter a number.""\n"
            "       Wpisz cyfrę""\n"
            "       [0]     -       EXIT""\n"
            "       [1]     -       INFO""\n"
            "       [2]     -       ENCRYPT / ZASZYFRUJ""\n"
            "       [3]     -       DECRYPT / ODSZYFRUJ")

    SZ1 = input("   :")

# Exit the program.
# Wyjście z programu.

    if SZ1 == "0":
        exit()

# Function that displays information about Szyfrator 1.0.
# Funkcja wyświetlająca informacje o Szyfrator 1.0.

    elif SZ1 == "1":
        SZ3 = 0

# Language selection.
# Wybór języka.

        while SZ3 == 0:
            print(  "     [1]     -       English""\n"
                    "     [2]     -       Polski")


            SZ2 = input("   :")

# English language.
# Język angieslki.

            if SZ2 == "1":
                SZ3 = 1


                print(  "Szyfrator 1.0 to program do szyfrowanie i odszyfrowywania tekstu.""\n"
                        "............................................................................................")
                print(  "Encrypt - Notepad will open. Enter the text to be encrypted, save it and close the notebook.""\n"
                        "The encrypted text will be opened in Notepad.""\n"
                        "It is possible to export the encrypted text to Notepad.""\n"
                        "\n"
                        "Szyfrator 1.0 recognizes signs""\n"
                        "a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s t u v w x y z ź ż""\n"
                        "A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P Q R S T U V W X Y Z Ź Ż""\n"
                        "0 1 2 3 4 5 6 7 8 9""\n"
                        "! \ # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^  ` { } | ~""\n"
                        "Sign outside the list will not be encrypted and may cause a program error""\n"                    
                        "............................................................................................")
                print(  "Decrypt - Notepad will open. Enter the code to decrypt, save it and close the notebook.""\n"
                        "The decrypted text will be displayed""\n"
                        "It is possible to export the decrypted text to Notepad.""\n"
                        "\n"
                        "Szyfrator 1.0 can only decrypt its own code""\n"
                        "............................................................................................")

# Polish language.
# Język polski.

            elif SZ2 == "2":
                SZ3 = 1
                print(  "Szyfrator 1.0 to program do szyfrowanie i odszyfrowywania tekstu.""\n"
                        "............................................................................................")
                print(  "Zaszyfruj - otwarty zostanie Notatnik. Wpisz tekst do zaszyfrowania, zapisz go i zamknij notatnik.""\n"
                        "Zaszyfrowany tekst zostanie wyświetlony.""\n"
                        "Istnieje możliwość wyeksportowania zaszyfrowanego tekstu do Notatnika."
                        "\n"
                        "Szyfrator 1.0 rozpoznaje następujące znaki:""\n"
                        "a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s t u v w x y z ź ż""\n"
                        "A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P Q R S T U V W X Y Z Ź Ż""\n"
                        "0 1 2 3 4 5 6 7 8 9""\n"
                        "! \ # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^  ` { } | ~""\n"
                        "Znaki spoza listy nie zostaną zaszyfrowane i mogą wywołać błąd programu""\n"
                        "............................................................................................")
                print(  "Odszyfruj - otwarty zostanie Notatnik. Wpisz kod do odszyfrowania, zapisz go i zamknij notatnik.""\n"
                        "Odszyfrowany tekst zostanie wyświetlony""\n"
                        "Istnieje możliwość wyeksportowania odszyfrowanego tekstu do Notatnika""\n"
                        "\n"
                        "Szyfrator 1.0 może odszyfrować jedynie własny kod""\n"
                        "............................................................................................")

# Information after entering an incorrect value.
# Informacja po wprowadzeniu błędnej wartości.

            else:
                print("INVALID VALUE / NIEPOPRAWNA WARTOŚĆ")

# Return to main menu.
# Powrót do menu głównego.

        print(" [ENTER]     -       BACK TO / COFNIJ")
        SZ3 = input("   :")

# Encryption function.
# Funkcja szyfrująca.

    elif SZ1 == "2":

# Designating the path to the Text.txt file.
# Wyznaczanie ścieżki do pliku Text.txt.

        current_file_path = os.path.realpath(__file__)
        Text_file_path = current_file_path.replace("Szyfrator.py", "Text.txt")

# Entering text to be encrypted.
# Wprowadzanie tekstu do zaszyfrowania.

        with open(Text_file_path, 'w') as TEXT_W:
            TEXT_W.write("Enter the text to be encrypted. Save the file and close Notepad.""\n""Wpisz tekst do zaszyfrowania. Zapisz plik i zamknij Notatnik.")
        subprocess.run(['notepad', Text_file_path])
        Text = open(Text_file_path, 'r', encoding='utf-8').read()

# Replacement in the text to encrypt whitespace with _.
# Podmiana w tekście do zaszyfrowania znaków białych na _.

        Text_ = Text.replace(" ", "_").replace("\n", "_").replace("\t", "_")

# A loop that loops through individual characters of text.
# Pętla przechodząca po poszczególnych znakach tekstu.

        for sing in Text_:

# A list containing a single, encrypted character.
# Lista zawierająca pojedynczy, zaszyfrowany znak.

            SingC = []

# Random key id.
# Losowanie id klucza.
            x = random.randint(1, 253)
            SingC.append(x)

# Retrieving the key from the database.
# Pobieranie klucza z bazy danych.
            cur.execute('SELECT id, keys FROM Keys WHERE id LIKE ?', (str(x),))
            for row in cur:
                id, keys = row

# Get the sign indexes in the key.
# Pobranie indeksy znaku w kluczu.
            for q in keys:
                if q == sing:
                    SingC.append(keys.index(q))

# Randomize a false value.
# Losowanie fałszywej wartości.
            x = random.randint(1, 9)
            SingC.append(x)
            Cipher.append(SingC)

# Display encoded text.
# Wyświetlenie zakodowanego tekstu.

        Cipher_str = "".join(str(Cipher))
        Cipher_str_wrap = textwrap.fill(Cipher_str, width=100)
        print("Encrypted text.")
        print("Zaszyfrowany tekst.")
        print(Cipher_str_wrap)

# Export encoded text to Notepad.
# Eksport zakodowanego tekstu do Notatnika.

        SZ5 = 0
        while SZ5 == 0:
            print("Should I export text to Notepad?. [YES / NO]")
            print("Czy wyeksportować text do Notatnika? [TAK / NIE]")
            SZ4 = input("   :").upper()
            if SZ4 == "YES" or SZ4 == "TAK":
                Text_file_path_2 = current_file_path.replace("Szyfrator.py", "Cipher.txt")
                with open(Text_file_path_2, 'w') as TEXT_W:
                    TEXT_W.write(Cipher_str_wrap)
                subprocess.run(['notepad', Text_file_path_2])
                SZ5 = 7

            elif SZ4 == "NO" or SZ4 == "NIE":
                SZ5 = 5

            else:
                print("Invalid value entered")
                print("Wprowadzono niepoprawną wartość")

# Decryption function.
# Funkcja deszyfrująca.

    elif SZ1 == "3":
        Text_dc = ""
# Designating the path to the Text.txt file.
# Wyznaczanie ścieżki do pliku Text.txt.

        current_file_path = os.path.realpath(__file__)
        Text_file_path_3 = current_file_path.replace("Szyfrator.py", "Cipher_2.txt")

# Entering text to be decrypted.
# Wprowadzanie tekstu do odszyfrowania.

        with open(Text_file_path_3, 'w') as Cript_W:
            Cript_W.write("Enter the text to be decrypted. Save the file and close Notepad.""\n""Wpisz tekst do odszyfrowania. Zapisz plik i zamknij Notatnik.")
        subprocess.run(['notepad', Text_file_path_3])
        Text = open(Text_file_path_3, 'r', encoding='utf-8').read()


# Transform string into a list.
# Transformacja tekstu na listę.

        Text_L = eval(Text)

# Loop through the elements of the Text_L list
# Pętla przechodząca po elementach listy Text_L

        for C in Text_L:

# Retrieving the key from the database.
# Pobranie klucza z bazy danych.

            cur.execute('SELECT id, keys FROM Keys WHERE id LIKE ?', (str(C[0]),))
            for row in cur:
                id, keys = row

# Retrieving an encrypted sign from the key.
# Pobranie z klucza zaszyfowanego znaku.

            sign = keys[C[1]]

# Adding the downloaded character to the decrypted text.
# Dodawanie pobranego znaku do odszyfrowanego tekstu.

            Text_dc +=sign

# Replace _ with a space.
# Zamiana _ na spację.

        Text_dc_2 = Text_dc.replace("_", " ")

# Display the decrypted text.
# Wyświetlenie odszyfrowanego tekstu.
        Text_dc_2_wrap = textwrap.fill(Text_dc_2, width=100)
        print(Text_dc_2_wrap)


# Eksport odszyfrowanego tekstu do notatnika.

        SZ7 = 0
        while SZ7 == 0:
            print("Should I export text to Notepad?. [YES / NO]")
            print("Czy wyeksportować text do Notatnika? [TAK / NIE]")
            SZ8 = input("   :").upper()
            if SZ8 == "YES" or SZ8 == "TAK":
                Text_file_path_3 = current_file_path.replace("Szyfrator.py", "Text_2.txt")
                with open(Text_file_path_3, 'w') as TEXT_W:
                    TEXT_W.write(Text_dc_2_wrap)
                subprocess.run(['notepad', Text_file_path_3])
                SZ7 = 7

            elif SZ8 == "NO" or SZ8 == "NIE":
                SZ7 = 5

            else:
                print("Invalid value entered")
                print("Wprowadzono niepoprawną wartość")