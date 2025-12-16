
class Osoba:

    def __init__(self,imie, nazwisko, data_urodzenia, numer_dowodu):
        self.imie = imie
        self.naziwsko = nazwisko 
        self.data_urodzenia = data_urodzenia
        self.numer_dowodu = numer_dowodu

    def __str__(self):
        return (
            f'Imie: {self.imie}\n'
            f'Nazwisko: {self.naziwsko}\n'
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
                  rok_studiow):
        super().__init__(imie,nazwisko,data_urodzenia,numer_dowodu)
        self.rok_rozpoczecia = rok_rozpoczecia
        self.rok_zakonczenia = rok_zakonczenia
        self.aktywny = aktywny
        self.kierunek = kierunek
        self.rok_studiow = rok_studiow

    def __str__(self):
        return (
            super().__str__() + 
            f'Rok rozpoczęcia: {self.rok_rozpoczecia}\n'
            f'Rok zakonczenia: {self.rok_zakonczenia}\n'
            f'Aktywny: {self.aktywny}\n'
            f'Kierunek: {self.kierunek}\n'
            f'Rok studiów: {self.rok_studiow}\n'
        )
    def pokaz_dane_studenta(self):
        return str(self)

class Pracownik(Osoba):

    def __init__(self,
                  imie,
                  nazwisko,
                  data_urodzenia,
                  numer_dowodu,
                  start_zatrudnienia,
                  staz_pracy,
                  stanowisko,
                  zwolnienie_lekarskie):
        super().__init__(imie, nazwisko, data_urodzenia, numer_dowodu)
        self.start_zatrudnienia = start_zatrudnienia
        self.staz_pracy = staz_pracy
        self.stanowisko = stanowisko
        self.zwolnienie_lekarskie = zwolnienie_lekarskie
    
    def __str__(self):
        return (
            super().__str__() +
            f'Start zatrudnienia: {self.start_zatrudnienia}\n'
            f'Staż pracy: {self.staz_pracy}\n'
            f'Stanowisko: {self.stanowisko}\n'
            f'Zwolnienie lekarskie: {self.zwolnienie_lekarskie}\n'
        )
    
    def pokaz_dane_pracownika(self):
        return str(self)
    
class Manager(Pracownik):

    def __init__(self,
                 imie,
                 nazwisko,
                 data_urodzenia,
                 numer_dowodu, 
                 start_zatrudnienia, 
                 staz_pracy, 
                 stanowisko, 
                 zwolnienie_lekarskie, 
                 dzial, 
                 liczba_pracownikow):
        super().__init__(imie, nazwisko, data_urodzenia, numer_dowodu, start_zatrudnienia, staz_pracy, stanowisko, zwolnienie_lekarskie)
        self.dzial = dzial
        self.liczba_pracownikow = liczba_pracownikow

    def __str__(self):
        return (
            super().__str__() +
            f'Dział: {self.dzial}\n'
            f'Liczba pracowników: {self.liczba_pracownikow}\n'
        )
    
    def pokaz_dane_managera(self):
        return str(self)

osoba = Osoba('osoba', 'osoba', 'osoba', 'osoba')
student = Student('student','student','student','student','student','student','student','student','student')
pracownik = Pracownik('Pracownik','Pracownik','Pracownik','Pracownik','Pracownik','Pracownik','Pracownik','Pracownik')
manager = Manager('manager','manager','manager','manager','manager','manager','manager','manager','manager','manager')
print(osoba.pokaz_dane_osoby())
print(student.pokaz_dane_studenta())
print(pracownik.pokaz_dane_pracownika())
print(manager.pokaz_dane_managera())