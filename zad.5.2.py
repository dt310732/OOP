
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


class ListaOcen(dict):


    def dodaj_przedmiot(self, przedmiot, ocena):
        self[przedmiot.strip()] = ocena

oceny = ListaOcen()
oceny.dodaj_przedmiot('Matematyka', 4)
print(oceny)