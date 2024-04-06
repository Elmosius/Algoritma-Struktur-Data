# File: T05_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan ADT MyList 
# dimana struktur ADT tersebut dapat dilihat 
# pada table terlampir

## Definisi Kelas ##
# Definisi Kelas MyList
# Definisi Atribut
# first : menyimpan elemen pertama list(int)
class MyList:
    # Definisi Konstruktor
    # Kamus Lokal
    # first : atribut ref elemen pertama
    def __init__(self):
        self.first = None

    # Definisi Method InsertFirst(a)
    # Kamus Lokal
    # a : parameter nilai yg akn ditmbhkn ke list
    def InsertFirst(self, a):
        a.next = self.first
        self.first = a
 
    # Definisi Method InsertLast(a)
    # Kamus Lokal
    # a : parameter nilai yg akn ditmbhkn ke list
    def InsertLast(self, a):
        if self.first == None:
            self.InsertFirst(a)
        else:
            last = self.first
            while last.next != None:
                last = last.next
            last.next = a
    
    # Definisi Method DeleteFirst()
    # Kamus Lokal
    # a : elemen terbuang dari list 
    def DeleteFirst(self):
        if self.first:
            a = self.first
            self.first = self.first.next
            a.next = None
            return a
        else:
            return None
    
    # Definisi Method traversal()
    # Kamus Lokal
    # Iterator : var. 
    def traversal(self):
        Iterator = self.first
        print("Linked list:", end=" ")
        while Iterator != None:
            print(f'|{Iterator.info}|', end=" ")
            Iterator = Iterator.next
        
## Definisi Kelas ##
# Definisi Kelas MyListElement
# Definisi Atribut
# info : menyimpan nilai elemen (int)
class MyListElement:
    # Definisi Konstruktor
    # Kamus Lokal
    # value : var yang menyimpan nilai (int)
    def __init__(self, info):
        self.info = info
        self.next = None
    
## Program utama ##
# Kamus Lokal
# i : var. input menu (int)
# e : var. input element (int)
# m : var. penampung objek (MyListElement)
# l : var. penampung objek (MyList)
def main():
    print("1. Insert First")
    print("2. Insert Last")
    print("3. Delete First")
    print("0. Exit")
    
    l = MyList()
    i = int(input("Menu: "))
    
    while i != 0:
        if i == 1:
            e = int(input('Masukkan element \
 value: '))
            m = MyListElement(e)
            l.InsertFirst(m)
            l.traversal()
            print()
        elif i == 2:
            e = int(input('Masukkan element \
value: '))
            m = MyListElement(e)
            l.InsertLast(m)
            l.traversal()
            print()
        elif i == 3:
            deleted_element = l.DeleteFirst()
            if deleted_element:
                print(f'Hapus element \
{deleted_element.info}')
                l.traversal()
                print()
            else:
                print('List kosong')
        else:
            print("Menu yang tersedia: 0, 1, \
2, 3")
            
        i = int(input("Menu: "))

if __name__ == '__main__':
    main()
