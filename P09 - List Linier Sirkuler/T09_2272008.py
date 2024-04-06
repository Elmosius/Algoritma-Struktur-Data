# File: T09_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan ADT SList
# dimana struktur ADT tersebut dapat
# ilihat pada table terlampir
# Keterangan : Beberapa code ambil dari modul ppt

## Definisi Kelas ##
# Definisi Kelas Slist
# Definisi Atribut
# head : menyimpan elemen pertama
# list(MyListElement)
class Slist:
    # Definisi Konstruktor
    # Kamus Lokal
    # head : atribut ref elemen pertama
    # (MyListElement)
    def __init__(self):
        self.head = None
        return

    # Definisi Method insertFirst(p)
    # Kamus Lokal
    # p : node yg akan ditambahkan
    # (MyListElement)
    # Last : penanda node terakhir
    # (MyListElement)
    def insertFirst(self, p):
        if self.isEmpty():
            p.next = p
            self.head = p
        else:
            Last = self.head
            while (Last.next != self.head):
                Last = Last.next
            Last.next = p
            p.next = self.head
            self.head = p
        return

    # Definisi Method insertLast(p)
    # Kamus Lokal
    # p : node yang akan ditambahkan
    # (MyListElement)
    def insertLast(self, p):
        if self.isEmpty():
            self.head = p
            p.next = p
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = p
            p.next = self.head
        return

   # Definisi Method deleteFirst()
    # Kamus Lokal
    # p : node terbuang (MyListElement)
    # Last : node terakhir (MyListElement)
    def removeFirst(self):
        p = self.head
        if (self.head.next == self.head):
            p.next = None
            self.head = None
        else:
            Last = self.head
            while (Last.next != self.head):
                Last = Last.next
            self.head = self.head.next
            Last.next = self.head
        return p

    # Definisi Method deleteLast()
    # Kamus Lokal
    # p : node yg dibuang (MyListElement)
    # prevLast : mode sebelum node
    # terbuang (MyListElement)
    def removeLast(self):
        p = self.head
        if (self.head.next == self.head):
            self.head = None
        else:
            prevLast = self.head
            while (prevLast.next.next != self.head):
                prevLast = prevLast.next
            p = prevLast.next
            prevLast.next = self.head
        return p

    # Definisi Method traversal()
    # Kamus Lokal
    # p : iterator node (MyListElement)
    # c : count total list (int)
    def traversal(self):
        if (self.isEmpty()):
            print('List kosong')
        else:
            p = self.head
            while (p.next != self.head):
                print(p.info, end=" ")
                p = p.next
            print(p.info)
            return

    # Definisi Method isEmpty()
    # Kamus Lokal
    def isEmpty(self):
        return (self.head == None)

## Definisi Kelas ##
# Definisi Kelas MyListElement
# Definisi Atribut
# info : menyimpan nilai elemen (int)
# next : menyimpan alamat elemen berikutnya (int)
# prev : menyimpan alamat elemen sebelumnya (int)


class MyListElement:
    # Definisi Konstruktor
    # Kamus Lokal
    # info : simpan nilai elemen (int)
    # next : simpan elemen berikutnya (int)
    # prev : simpan elemen sebelumnya (int)
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None
        return

## Program utama ##
# Kamus Lokal
# m : var. penampung objek (MyListElement)
# sl : var. penampung objek (Slist)
# input_pilihan : var.input pilihan(int)


def main():

    sl = Slist()
    # kondisi
    print("===========")
    print("kondisi list:")
    sl.traversal()

    # Menu
    print("menu:")
    print("1. Insert first")
    print("2. Insert last")
    print("3. Delete first")
    print("4. Delete last")
    print("0. Keluar")
    print("-------------")

    input_pilihan = int(input("Menu: "))
    while (input_pilihan != 0):

        # Pilihan 1
        if (input_pilihan == 1):
            m = MyListElement(
                str(input("Masukkan nama: ")))
            sl.insertFirst(m)

        # Pilihan 2
        elif (input_pilihan == 2):
            m = MyListElement(
                str(input("Masukkan nama: ")))
            sl.insertLast(m)

        # Pilihan 3
        elif (input_pilihan == 3):
            if (sl.isEmpty()):
                pass
            else:
                print(sl.removeFirst().info,
                      "terhapus")

        # Pilihan 4
        elif (input_pilihan == 4):
            if (sl.isEmpty()):
                pass
            else:
                print(sl.removeLast().info,
                      "terhapus")

        else:
            print("Menu yg tersedia: 0 <= x <= 4")

        # kondisi
        print("===========")
        print("kondisi list:")
        sl.traversal()

       # Menu
        print("menu:")
        print("1. Insert first")
        print("2. Insert last")
        print("3. Delete first")
        print("4. Delete last")
        print("0. Keluar")
        print("-------------")
        input_pilihan = int(input
                            ("Pilihan Anda: "))


if __name__ == '__main__':
    main()
