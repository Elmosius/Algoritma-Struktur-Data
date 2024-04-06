# File: T07_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan ADT QueueList
# dimana struktur ADT tersebut dapat dilihat
# pada table terlampir. Program utama bebas
# namun harus dapat memvalidasi kebenaran
# setiap method pada ADT QueueList

## Definisi Kelas ##
# Definisi Kelas QueueList
# Definisi Atribut
# first : menyimpan elemen pertama list(int)
class QueueList:
    # Definisi Konstruktor
    # Kamus Lokal
    # head : simpan elemen terdepan (MyListElement)
    # tail : simpan elemen terbelakang (MyListElement)
    def __init__(self):
        self.head = None
        self.tail = None
        return

    # Definisi Method enqueue(x)
    # Kamus Lokal
    # x : elemen yang ditambahkan (int)
    # m : node x (MyListElement)
    def enqueue(self, x):
        m = MyListElement(x)
        if (self.isEmpty()):
            self.head = m
            self.tail = m
        else:
            self.tail.next = m
            self.tail = m
        return

    # Definisi Method dequeue()
    # Kamus Lokal
    # m : node terbuang (MyListElement)
    def dequeue(self):
        m = self.head
        if (self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return m.info

    # Definisi Method traversal()
    # Kamus Lokal
    # a : var. nilai isi list(int)
    def traversal(self) -> None:
        a = self.head
        while (a != None):
            print(f'{a.info}', end=" ")
            a = a.next

    # Definisi Method isEmpty()
    # Kamus Lokal
    def isEmpty(self):
        return (self.head == None)

## Definisi Kelas ##
# Definisi Kelas MyListElement
# Definisi Atribut
# info : menyimpan nilai elemen (int)


class MyListElement:
    # Definisi Konstruktor
    # Kamus Lokal
    # info : menyimpan nilai elemen (int)
    # next : ref elemen berikutnya (int)
    def __init__(self, info) -> int:
        self.info = info
        self.next = None

## Program utama ##
# Kamus Lokal
# i : var. input menu (int)
# q : var. penampung objek (QueueList)
# b : var. input bilangan(int)
def main():
    print("1. Enqueue")
    print("2. Dequeue")
    print("0. Exit")
    print("-------------")

    q = QueueList()
    i = int(input("Menu: "))

    while (i != 0):
        # Enqueue
        if i == 1:
            b = int(input('Bilangan:'))
            q.enqueue(b)
            q.traversal()
            print()

        # Dequeue
        elif i == 2:
            if (q.isEmpty()):
                print('Antrian Kosong')
            else:
                q.dequeue()
                q.traversal()
                print()
        else:
            print("Menu yg tersedia: 0, 1, 3")

        i = int(input("Menu: "))


if __name__ == '__main__':
    main()
