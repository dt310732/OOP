class Osoba:

    def __init__(self,imie, nazwisko, data_urodzenia, numer_dowodu):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.data_urodzenia = data_urodzenia
        self.numer_dowodu = numer_dowodu

    def __str__(self):
        return (
            f'Imie: {self.imie}\n'
            f'Nazwisko: {self.nazwisko}\n'
            f'Data urodzenia: {self.data_urodzenia}\n'
            f'Numer dowodu: {self.numer_dowodu}\n'
        )

    def pokaz_dane_osoby(self):
        return str(self)

class Student(Osoba):

    def __init__(self,
                  imie,
                  nazwisko,
                  data_urodzenia,
                  numer_dowodu,
                  rok_rozpoczecia,
                  rok_zakonczenia,
                  aktywny,
                  kierunek,
                  rok_studiow,
                  lista_ocen=None):
        super().__init__(imie,nazwisko,data_urodzenia,numer_dowodu)
        self.rok_rozpoczecia = rok_rozpoczecia
        self.rok_zakonczenia = rok_zakonczenia
        self.aktywny = aktywny
        self.kierunek = kierunek
        self.rok_studiow = rok_studiow
        if lista_ocen is None:
            self.lista_ocen = 'Brak Ocen'
        else:
            self.lista_ocen = lista_ocen
    def __str__(self):
        return (
            super().__str__() + 
            f'Rok rozpoczęcia: {self.rok_rozpoczecia}\n'
            f'Rok zakonczenia: {self.rok_zakonczenia}\n'
            f'Aktywny: {self.aktywny}\n'
            f'Kierunek: {self.kierunek}\n'
            f'Rok studiów: {self.rok_studiow}\n'
            f'Oceny: {self.lista_ocen}\n'
        )
    def pokaz_dane_studenta(self):
        return str(self)


class ListaOcen(dict):

    def dodaj_przedmiot(self, przedmiot, ocena):
        if przedmiot not in self:
            if (2 <= ocena <= 5):
                self[przedmiot.strip()] = ocena
            else:
                print('Ocena musi byc w zakresie 2-5')
        else:
            print('Taki przedmiot juz istnieje')

    def usun_przedmiot(self, przedmiot):
        if not isinstance(przedmiot, str) or not przedmiot.strip():
            raise ValueError('Nazwa przedmiotu musi być niepustym stringiem.')
        przedmiot = przedmiot.strip()

        if przedmiot in self:
            print(f'Przedmiot {przedmiot} zostal usuniety')
            del self[przedmiot]
            return True
        return False
        
    def szukaj_przedmiotu(self, przedmiot):
        if not isinstance(przedmiot, str) or not przedmiot.strip():
            raise ValueError('Nazwa przedmiotu musi być niepustym stringiem.')
        for _ in self:
            if _ == przedmiot:
                print('Przedmiot znaleziony')
                return True
        print('Przedmiot nie znaleziony')   
        return False         

    def wyswietl_oceny(self):
        if not self:
            print('Brak ocen')
            return       
        print('Oceny')
        print('--------')
        for przedmiot, oceny in self.items():
            print(f'{przedmiot}: {oceny}')

class Lista_studentow(dict):

    def dodaj_studenta(self, index,student):
        self[index] = student

    def usun_studenta(self, index):
        if index in self.keys():
            print(f'Usunięto studenta o indexie {index}')
            del self[index]
            return True
        else:
            print('Nie ma takiego studenta')
            return False
    def znajdz_studenta(self, index):
        for _ in self:
            if _ == index:
                print(f'Student o indeksie {index} istnieje')
                print(self[index]) 
                return
        print(f'Student o indeksie {index} nie istnieje')
    
    def lista_studentow(self):
        for index, student in self.items():
            print(f'Indeks: {index}') 
            print(student)

    def pokaz_oceny_studenta(self, index):
            student = self[index]
            print(f"Oceny studenta {student.imie} {student.nazwisko}:")
            for przedmiot, ocena in student.lista_ocen.items():
                print(f"{przedmiot}: {ocena}")
oceny = ListaOcen()
oceny.dodaj_przedmiot('Matematyka', 5)
oceny.dodaj_przedmiot('Polski', 3.5)
osoba = Osoba('Jan', 'Nowak', '1999-01-01', 'ABC123')
student = Student('Jan', 'Nowak', '1999-01-01', 'ABC123', '2020-01-01', '2025-01-01', 'Tak', 'Informatyka', 2, oceny)
lista_studentow = Lista_studentow()
lista_studentow.dodaj_studenta(12345, student)
print(osoba.pokaz_dane_osoby())
print(student.pokaz_dane_studenta())
lista_studentow.pokaz_oceny_studenta(12345)
oceny.wyswietl_oceny()
lista_studentow.lista_studentow()
