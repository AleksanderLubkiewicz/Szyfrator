# IMPORT
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QScrollArea
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
import sqlite3
import random
import os
#....................................................................................................................

# Designating the path to files.
# Wyznaczanie ścieżki dla plików
current_file_path = os.path.realpath(__file__)
file_path = current_file_path.replace("Szyfrator.py", "")

# Key library.
# Biblioteka kluczy.
conn = sqlite3.connect(file_path + "KEYS")
cur = conn.cursor()


#...................................................................................................................
# Variables
# Zmienne

# Text in the result window.
# Tekst w oknie z wynikiem.
TEXT = ''

# Information text in Polish.
# Tekst informacyjny w języku polskim.
TEXT_INFO_PL =  'Szyfrator to program do szyfrowanie i odszyfrowywania tekstu. ''\n' \
                'Szyfrator rozpoznaje następujące znaki: ''\n' \
                'a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s t u v w x y z ź ż ''\n' \
                'A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P Q R S T U V W X Y Z Ź Ż ''\n' \
                '0 1 2 3 4 5 6 7 8 9''\n' \
                '! \ # $ % & " ( ) * + , - . / : ; < = > ? @ [ ] ^  ` { } | ~ ''\n' \
                'Znaki spoza listy nie zostaną zaszyfrowane i mogą wywołać błąd programu ''\n' \
                'Szyfrator może odszyfrować jedynie własny kod'

# Information text in English.
# Tekst informacyjny w języku angielskim.
TEXT_INFO_GB = 'Szyfrator is a program for encrypting and decrypting text. ''\n' \
                'Szyfrator recognizes signs: ''\n' \
                'a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s t u v w x y z ź ż ''\n' \
                'A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P Q R S T U V W X Y Z Ź Ż ''\n' \
                '0 1 2 3 4 5 6 7 8 9''\n' \
                '! \ # $ % & " ( ) * + , - . / : ; < = > ? @ [ ] ^  ` { } | ~ ''\n' \
                'Sign outside the list will not be encrypted and may cause a program error ''\n' \
                'Szyfrator can only decrypt its own code'

#.....................................................................................................................
# Main application window
# Główne okno aplikacji
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('SZYFRATOR_2')
        self.setGeometry(100, 100, 800, 800)

        #............................................................................................................
        # Elements
        # Elementy.
        # Polish language selection button.
        # Przycisk wyboru języka polskiego.
        self.button_PL = QPushButton('PL')
        self.button_PL.setFixedSize(QSize(75, 40))
        self.button_PL.setIcon(QIcon(file_path + 'B_PL.png'))
        self.button_PL.setStyleSheet('background-color: lightblue;')
        self.button_PL.clicked.connect(self.B_PL_C)

        # English language selection button
        # Przycisk wyboru języka angielskiego
        self.button_GB = QPushButton('GB')
        self.button_GB.setFixedSize(QSize(75, 40))
        self.button_GB.setIcon(QIcon(file_path + 'B_GB.png'))
        self.button_GB.setStyleSheet('background-color: lightblue;')
        self.button_GB.clicked.connect(self.B_GB_C)

        # Information button
        # Przycisk informacji
        self.button_INFO = QPushButton('INFO')
        self.button_INFO.setCheckable(True)
        self.button_INFO.setFixedSize(QSize(75, 40))
        self.button_INFO.setIcon(QIcon(file_path + 'B_INFO.png'))
        self.button_INFO.setStyleSheet('background-color: yellow;')
        self.button_INFO.clicked.connect(self.B_INFO_C)

        # Exit button
        # Przycisk exit
        self.button_EXIT = QPushButton('EXIT')
        self.button_EXIT.setFixedSize(QSize(75, 40))
        self.button_EXIT.setIcon(QIcon(file_path + 'B_EXIT.png'))
        self.button_EXIT.setStyleSheet('background-color: yellow;')
        self.button_EXIT.clicked.connect(self.B_EXIT_C)

        # Encrypt button
        # Przycisk szyfruj
        self.button_ENC = QPushButton('SZYFRUJ')
        self.button_ENC.setFixedSize(QSize(75, 40))
        self.button_ENC.setStyleSheet('background-color: lightgray;')
        self.button_ENC.clicked.connect(self.B_Szyfruj_C)

        # Decrypt button
        # Przycisk deszyfruj
        self.button_DEC = QPushButton('DESZYFRUJ')
        self.button_DEC.setFixedSize(QSize(75, 40))
        self.button_DEC.setStyleSheet('background-color: lightgray;')
        self.button_DEC.clicked.connect(self.B_Odszyfruj_C)

        # Text edit box
        # Pole edycji tekstu
        self.text_edit = QTextEdit(self)
        self.text_edit.setFixedSize(800,300)
        self.opis_te = QLabel('Wprowadź tekst do zaszyfrowania / odszyfrowania')

        # Encoded/decoded text display field
        # Pole wyświetlania tekstu zakodowanego / odkodowanego
        self.label = QLabel(TEXT)
        self.label.setWordWrap(True)

        # Information text display field
        # Pole wyświetlenia tekstu informacyjnego
        self.label_INFO = QLabel(TEXT_INFO_PL)
        self.label_INFO.setWordWrap(True)
        self.label_INFO.setVisible(False)

        # Scroll
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setWidgetResizable(True)

        # ..........................................................................................................
        # Placement of elements
        # Umiejscowienie elementów
        layout = QVBoxLayout()

        # Language + information + exit buttons
        # Przyciski wyboru języka + informacyjny + exit
        layout_1 = QHBoxLayout()
        layout_1.addStretch()
        layout_1.addWidget(self.button_PL)
        layout_1.addWidget(self.button_GB)
        layout_1.addWidget(self.button_INFO)
        layout_1.addWidget(self.button_EXIT)

        # Information triggered by the INFO button.
        # Informacja wyzwalana przez przycisk INFO.
        layout_2 = QVBoxLayout()
        layout_2.addWidget(self.label_INFO)

        # Pole edycji tekstu
        layout_3 = QVBoxLayout()
        layout_3.addWidget(self.opis_te)
        layout_3.addWidget(self.text_edit)

        # Text edit box
        # Przyciski szyfruj i odszyfruj
        layout_4 = QHBoxLayout()
        layout_4.addStretch()
        layout_4.addWidget(self.button_ENC)
        layout_4.addStretch()
        layout_4.addWidget(self.button_DEC)
        layout_4.addStretch()

        # Field with encrypted/decrypted text
        # Pole z tekstem zaszyfrowanym / odszyfrowanym
        layout_5 = QHBoxLayout()
        layout_5.addWidget(self.scroll_area)


        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout.addLayout(layout_3)
        layout.addLayout(layout_4)
        layout.addLayout(layout_5)

        self.setLayout(layout)


        # Show the window
        # Pokarz okno
        self.show()
    #...............................................................................................................
    # Funkcje.
    # Exit button
    # Przycisk Exit
    def B_EXIT_C(self):
        sys.exit()

    # INFO button
    # Przycisk INFO

    def B_INFO_C(self):
        if self.label_INFO.isVisible():
            self.label_INFO.setVisible(False)
            #self.adjustSize()
        else:
            self.label_INFO.setVisible(True)
            #self.adjustSize()

    # GB button
    # Przycisk GB
    def B_GB_C(self):
        self.button_ENC.setText('ENCRIPT')
        self.button_ENC.update()
        self.button_DEC.setText('DECRIPT')
        self.button_DEC.update()
        self.opis_te.setText('Enter the text to be encrypted / decrypted')
        self.opis_te.update()
        self.label_INFO.setText(TEXT_INFO_GB)
        self.label_INFO.update()

    # PL button
    # Przycisk PL
    def B_PL_C(self):
        self.button_ENC.setText('SZYFRUJ')
        self.button_ENC.update()
        self.button_DEC.setText('ODSZYFRUJ')
        self.button_DEC.update()
        self.opis_te.setText('Wprowadź tekst do zaszyfrowania / odszyfrowania')
        self.opis_te.update()
        self.label_INFO.setText(TEXT_INFO_PL)
        self.label_INFO.update()

    # Encrypt button
    # Przycisk Szyfruj
    def B_Szyfruj_C(self):

        Cipher = []
        TEXT_C = self.text_edit.toPlainText()

        # Replacement in the text to encrypt whitespace with _.
        # Podmiana w tekście do zaszyfrowania znaków białych na _.
        TEXT_C = TEXT_C.replace(" ", "_").replace("\n", "_").replace("\t", "_")

        # A loop that loops through individual characters of text.
        # Pętla przechodząca po poszczególnych znakach tekstu.
        for sing in TEXT_C:

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
        # Pobranie indeksy znaku w kluczu
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
        self.label.setText(Cipher_str)
        self.label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse | Qt.TextInteractionFlag.TextSelectableByKeyboard)
        self.label.update()

    # Decrypt button
    # Przycisk Odszyfruj

    def B_Odszyfruj_C(self):
        TEXT_DC = ''
        TEXT = self.text_edit.toPlainText()
        # Transform string into a list.
        # Transformacja tekstu na listę.

        TEXT = eval(TEXT)

        # Loop through the elements of the Text_L list
        # Pętla przechodząca po elementach listy Text_L

        for C in TEXT:

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

            TEXT_DC += sign

        # Replace _ with a space.
        # Zamiana _ na spację.

        TEXT_DC_2 = TEXT_DC.replace("_", " ")

        # Display encoded text.
        # Wyświetlenie zakodowanego tekstu.

        self.label.setText(TEXT_DC_2)
        self.label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse | Qt.TextInteractionFlag.TextSelectableByKeyboard)
        self.label.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec())