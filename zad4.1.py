class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours 
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        if self.hours < 10:
            h = f"0{str(self.hours)}"
        else:
            h = str(self.hours)
        if self.minutes < 10:
            m = "0" + str(self.minutes)
        else:
            m = str(self.minutes)     
        if self.seconds < 10:
            s = "0" + str(self.seconds)
        else:
            s = str(self.seconds)
        
        print(h + ":" + m + ":" + s)
    def update(self,unit,value):
        match unit:
            case 'h':
                self.hours += value
            case 'm':
                self.minutes += value
            case 's':
                self.seconds += value
            case _:
                print('Wrong type!')
        
        self.normalize()

    def normalize(self):
        #sekundy wiekszę np 90 -> 1:30
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.seconds < 0:
            self.seconds += 60
            self.minutes -= 1
        # minuty tak samo
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        while self.minutes < 0:
            self.minutes += 60
            self.hours -= 1
        #godziny 23 -> +2 -> 1
        while self.hours >= 24:
            self.hours -= 24
        while self.hours < 0:
            self.hours += 24

def menu():
    hours = int(input('Podaj godzinę: '))
    minutes = int(input('Podaj minuty: '))
    seconds = int(input('Podaj sekundy: '))
    obj1 = Time(hours, minutes, seconds)
    while True:
        print('Wyświetl godzinę: 1')
        print('Zaktualizuj godzinę 2: ')
        print('Wyjdz 3: ')
        choice = int(input('Wybór: '))
        if choice == 1:
            obj1.display()
        elif choice == 2:
            time_choice = str(input('Co chcesz zaktualizować?(h,m,s)'))
            value_choice = int(input('Wartość: '))
            obj1.update(time_choice, value_choice)
        elif choice == 3:
            return False
        else: 
            print('Error!')

menu()

