class Character:

    def __init__(self,hp,name,type,pos):
        self.hp = hp
        self.name = name
        self.type = type
        self.pos = pos

    def move(self, values):
        self.pos[0] += values[0]
        self.pos[1] += values[1]

    def show_character(self):
        print(type(self.pos))
        #v = [self.hp, self.name, self.type, self.pos]
        #for elem in v:
            #print(elem)
        print("Name:", self.name)
        print("HP:", self.hp)
        print("Type:", self.type)
        print(f"Position: x={self.pos[0]} y={self.pos[1]}")
        print("\n------------------")

    def interaction(self):
        print("Interaction type:", self.type)
        if self.type == "Enemy":
            print(f"{self.name} Attack!")
        elif self.type == "Friend":
            print(f"{self.name} Help.")
        else:
            print(f"{self.name} Do nothing.")

def menu():
    print('Stwórz postać')
    name = str(input('Nazwa postaci: '))
    hp = int(input('Ilość życia: '))
    type = str(input('Typ postaci(Enemy,Friend): '))
    pos = str(input('Podaj współrzędne np 1 1: '))
    pos = pos.split()
    pos_list = [int(x) for x in pos]   #zamiana str -> int
    obj1 = Character(name, hp, type, pos_list)
    while True:
        print("\n------------------\n")
        print('Wyświetl postać: 1')
        print('Przesuń postać: 2')
        print('Interakcja: 3')
        print('Wyjdz: 4')
        print("\n------------------")
        choice = int(input('Wybór: '))
        if choice == 1:
            obj1.show_character()
        elif choice == 2:
            pos = str(input('Podaj współrzędne np 1 1: '))
            pos_list = pos.split()
            pos_list = [int(x) for x in pos_list]   #zamiana str -> int
            obj1.move(pos_list)
        elif choice == 3:
            obj1.interaction()
        elif choice == 4:
            return False
        else: 
            print('Error!')

menu()