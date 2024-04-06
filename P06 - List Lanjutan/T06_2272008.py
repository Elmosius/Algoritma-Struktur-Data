# File: T06_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan
# ADT MyList dimana struktur ADT
# tersebut dapat dilihat
# pada table terlampir.

## Definisi Kelas ##
# Definisi Kelas MyList
# Definisi Atribut
# first : menyimpan elemen pertama list(int)
class MyList:
    # Definisi Konstruktor
    # Kamus Lokal
    # first : atribut ref elemen pertama(None)
    def __init__(self):
        self.first = None

    # Definisi Method InsertFirst(a)
    # Kamus Lokal
    # a : parameter nilai yg akn ditmbhkn ke list
    def insertFirst(self, a) -> None:
        a.next = self.first
        self.first = a

    # Definisi Method InsertAfter(prev,a)
    # Kamus Lokal
    # prev : parameter reference elemen sebelum
    # posisi target (MyListElement)
    # a : parameter nilai yang akan ditambahkan
    # pada list MyListElement
    def insertAfter(self, prev, a) -> None:
        a.next = prev.next
        prev.next = a
        return

    # Definisi Method DeleteLast()
    # Kamus Lokal
    # last : elemen terbuang dari list (MyListElement)
    # prevlast : penyimpan reference elemen kedua
    # terakhir (MyListElement)
    def removeLast(self) -> int:
        if (self.first == None):
            return None
        if (self.first.next == None):
            last = self.first
            self.first = None
            return last
        prevlast = None
        last = self.first
        while (last.next != None):
            prevlast = last
            last = last.next
        prevlast.next = None
        return last

    # Definisi Method traversal()
    # Kamus Lokal
    # Iterator : var. nilai isi list(int)
    def traversal(self) -> None:
        Iterator = self.first
        if (Iterator != None):
            print("Linked list:", end=" ")
            while Iterator != None:
                print(f'|{Iterator.info}|', end=" ")
                Iterator = Iterator.next
    # Definisi Method jumlahkan(): int
    # Kamus Lokal
    # Iterator : var. nilai isi list(int)
    # Total : var.total jumlah(int)

    def jumlahkan(self) -> int:
        self.total = 0
        Iterator = self.first
        while Iterator != None:
            self.total += Iterator.info
            Iterator = Iterator.next
        return self.total

## Definisi Kelas ##
# Definisi Kelas MyListElement
# Definisi Atribut
# info : menyimpan nilai elemen (int)


class MyListElement:
    # Definisi Konstruktor
    # Kamus Lokal
    # info : menyimpan nilai elemen (int)
    def __init__(self, info) -> int:
        self.info = info
        self.next = None

## Program utama ##
# Kamus Lokal
# prev : var. input untuk method
# insertAfter(int)
# i : var. input menu (int)
# e : var. input element (int)
# s : var. input insert last(int)
# m : var. penampung objek (MyListElement)
# l : var. penampung objek (MyList)
# de: var. deleted element dari
# method removeLast (int)


def main():
    print("1. Insert First")
    print("2. Insert After")
    print("3. Delete Last")
    print("4. Jumlahkan")
    print("0. Exit")

    l = MyList()
    i = int(input("Menu: "))

    while i != 0:
        # Insert First
        if i == 1:
            e = int(input('Masukkan element\
 value: '))
            m = MyListElement(e)
            l.insertFirst(m)
            l.traversal()
            print()

        # Insert After
        elif i == 2:
            e = int(input('Masukkan element \
value: '))
            s = int(input("Insert setelah?"))
            prev = l.first
            while (prev != None and prev.info != s):
                prev = prev.next
            if (prev != None):
                m = MyListElement(e)
                l.insertAfter(prev, m)
                l.traversal()
                print()
            else:
                print(f'Elemen {s} tidak \
ditemukan.')

        # RemoveLast
        elif i == 3:
            de = l.removeLast()
            if (de):
                print(f'Hapus element \
{de.info}')
                l.traversal()
                print()
            else:
                print('List kosong')

        # Jumlahkan
        elif i == 4:
            if (l.first == None):
                print('List kosong')
            else:
                l.traversal()
                print(f'\nJumlah value \
element: {l.jumlahkan()}')
        else:
            print("Menu yang tersedia: 0, 1, \
2, 3")

        i = int(input("Menu: "))


if __name__ == '__main__':
    main()
