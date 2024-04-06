# File: T14_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan ADT
# Heap dengan array dimana struktur ADT
# tersebut dapat dilihat pada tabel terlampir.
# Program utama akan meminta N bilangan.
# Untuk setiap bilangan, program perlu menampilakn
# kondisi heap setelah selesai proses penambahan.

## Definisi Kelas ##
# Definisi Kelas myHeap
# Definisi Atribut
# data : menyimpan array data (array int)
# Nmax : menyimpan kapasitas array data (int)
# N : menyimpan banyaknya elemen di array data (int)

class MyHeap:
    # Definisi Konstruktor(ukuran:int)
    # Kamus Lokal
    # ukuran : var. parameter (int)
    def __init__(self, ukuran: int):
        self.Nmax = ukuran
        self.data = [None] * self.Nmax
        self.N = 0
        return

    # Definisi Method print
    # Kamus Lokal
    # i : var. parameter for (int)
    def print(self):
        if (self.N == 0):
            print("Heap masih kosong")
        else:
            for i in range(self.N):
                print(self.data[i], end=' ')
            print()

    # Definisi Method addElmt(X: int)
    # Kamus Lokal
    # X : var. parameter (int)
    def addElmt(self, X: int):
        self.data[self.N] = X
        self.N += 1
        self.addElmt_(self.N - 1)

    # Definisi Method addElmt_(i : int)
    # Kamus Lokal
    # i : var. parameter dari method addElmt (int)
    # parent : var. parent pada tree (int)
    # temp : var. sementara (int)
    def addElmt_(self, i):
        parent = ((i - 1) // 2)
        if (i > 0 and self.data[i] > self.data[parent]):
            temp = self.data[i]
            self.data[i] = self.data[parent]
            self.data[parent] = temp
            self.addElmt_(parent)

## Program utama ##
# Kamus Lokal
# mh : var. objek(MyHeap)
# input_pilihan : var. pilihan(int)
# u : var. ukuran input array(int)
# info: var. insert ke method insert(int)


def main():
    u = int(input("Ukuran heap: "))
    mh = MyHeap(u)
    print("Menu:")
    print("1. Insert")
    print("2. Print")
    print("0. Keluar")
    print("-------------")

    input_pilihan = int(input("Menu: "))
    while (input_pilihan != 0):
        if (input_pilihan == 1):
            if (mh.N >= mh.Nmax):
                print("Heap sudah penuh")
            else:
                info = int(input("Masukkan angka yang \
ingin ditambahkan: "))
                mh.addElmt(info)
                mh.print()
                print()
        elif (input_pilihan == 2):
            print("Print Heap:")
            mh.print()
            print()
        else:
            print("Pilihan hanya no 0,1, dan 2")
        input_pilihan = int(input("Menu: "))


if __name__ == '__main__':
    main()
