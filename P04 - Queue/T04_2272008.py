# File: T04_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan ADT Queue
# array alternatif 2 dimana struktur ADT
# tersebut dapat dilihat pada tabel terlampir

## Definisi Kelas ##
# Definisi Kelas
# Definisi Atribut
# data : menyimpan array data (int)
# Nmax : menyimpan kapasitas maks array (int)
# head : menyimpan posisi head Queue (int)
# tail : menyimpan posisi tail,Queue (int)
class Queue:
    # Definisi Konstruktor
    # Kamus Lokal
    # ukuran : ukuran queue (int)
    def __init__(self, ukuran):
        self.head = -1
        self.tail = -1
        self.Nmax = ukuran
        self.data = ["_"]*(ukuran+1)

    # Definisi Method insert(X)
    # Kamus Lokal
    # X : nilai yang akan ditambahkan (int)
    def insert(self, X):
        if (self.tail == self.Nmax):
            for i in range(0, self.Nmax, 1):
                if (i <= self.tail - self.head):
                    self.data[i] = (
                        self.data[self.head+i-1])
                elif (i == self.tail
                      - self.head + 1):
                    self.data[i] = X
                else:
                    self.data[i] = "_"
            self.tail = self.tail - self.head + 2
            self.head = 1
        else:
            if (self.isEmpty()):
                self.head = 1
                self.tail = 0
            self.data[self.tail] = X
            self.tail += 1

    # Definisi Method delete()
    # Kamus Lokal
    # X : nilai yang akan dibuang (integer)
    def delete(self):
        X = self.data[self.head-1]
        self.data[self.head-1] = "_"
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head += 1
        return (f'Delete: {X}')

    # Definisi Method isEmpty()
    # Kamus Lokal

    def isEmpty(self):
        return (self.head == -1 and
                self.tail == -1)

    # Definisi Method isFull()
    # Kamus Lokal
    def isFull(self):
        return (self.head == 1 and
                self.tail == self.Nmax)

    # Definisi Method countElm()
    # Kamus Lokal
    def countElm(self):
        if (self.isEmpty()):
            return "Stack Kosong"
        else:
            print('Jumlah element: ', end="")
            if (self.tail >= self.head):
                return (self.tail -
                        self.head + 1)
            else:
                return (self.Nmax +
                        self.tail - self.head)

    # Definisi Method cetakQueue()
    # Kamus Lokal
    def cetakQueue(self):
        if (self.isEmpty()):
            print(f'Stack Kosong')
        else:
            for i in range(0, self.Nmax, 1):
                print(f'{self.data[i]}',
                      end=' ')
            print()
        return

## Program utama ##
# Kamus Lokal
# u : ukuran array (int)
# m : var. input menu(int)
# b : var. input insert(int)


def main():
    u = Queue(int(input("N:")))
    print("=== ADT Stack ===")
    print('1. Insert\n2. Delete')
    print('3. Info Jumlah Element')
    print('0. Exit')
    print('----------------')

    m = int(input('menu: '))
    while (m != 0):
        if (m == 1):
            if (u.isFull() == False):
                b = int(input("Bilangan "
                              "yg akan "
                              "di-insert:"))
                u.insert(b)
                print(f'Head: {u.head}', end="")
                print(f' Tail: {u.tail}')
                u.cetakQueue()
            else:
                print('Stack penuh')
        elif (m == 2):
            if (u.isEmpty()):
                print('Stock kosong')
            else:
                print(f'{u.delete()}')
                print(f'Head: {u.head}', end="")
                print(f' Tail: {u.tail}')
                u.cetakQueue()
        elif (m == 3):
            print(u.countElm())
        m = int(input('menu: '))


if __name__ == '__main__':
    main()
