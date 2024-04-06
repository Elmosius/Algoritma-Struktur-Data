# File: T03_2272008.py
# Penulis : Elmosius Suli
# Aprogram yang akan menggunakan ADT Stack dengan
# array dimana struktur ADT tersebut
# dapat dilihat pada tabel terlampir

## Definisi Kelas ##
# Definisi Kelas Stack
# Definisi Atribut
# data : menyimpan array data (int)
# Nmax : menyimpan kapasitas maksimum array (int)
# top : menyimpan posisi top dari Stack (int)

class Stack():
    # Definisi Konstruktor
    def __init__(self, ukuran: int):
        self.Nmax = ukuran
        self.data = (self.Nmax+1)*[None]
        self.top = -1
        return

    # Definisi Method isEmpty()
    # Kamus Lokal
    def isEmpty(self):
        return self.top == -1

    # Definisi Method isFull()
    # Kamus Lokal
    def isFull(self):
        return self.top == self.Nmax-1

    # Definisi Method infoTop()
    # Kamus Lokal
    def infoTop(self):
        return self.data[self.top]

    # Definisi Method push(X)
    # Kamus Lokal
    # X : nilai yang akan dimasukkan (integer)
    def push(self, X):
        self.top += 1
        self.data[self.top] = X
        return

    # Definisi Method pop()
    # Kamus Lokal
    # X : nilai yang akan dikembalikan (integer)
    def pop(self):
        X = self.data[self.top]
        self.top -= 1
        return X

    # Definisi Method countElm()
    # Kamus Lokal
    def countElm(self):
        if (self.isEmpty()):
            print(f'Stack kosong')
        else:
            return self.top+1
       

    # Definisi Method printStack()
    # Kamus Lokal
    def printStack(self):
        if (self.isEmpty()):
            print(f'Stack kosong')
        else:
            print(f'Isi stack: ', end="")
            for i in range(0, self.top+1, 1):
                print(f'{self.data[i]}', end=' ')
            print()
        return

## Program utama ##
# Kamus Lokal
# u : ukuran array (int)
# s : instansiasi stack (Stack)
# m : var. input menu(int)
# b : var. input insert(int)
def main():
    u = int(input("N:")) 
    s =  Stack(u)
    
    print(f"=== ADT Stack ===")
    print(f'1. Push\n2. Pop')
    print(f'3. Info Jumlah Element')
    print(f'4. Info Element Top\n0. Exit')
    print(f'----------------')

    m = int(input(f'menu: '))
    while (m != 0):
        if (m == 1):
            if(s.isFull() == False):
                b = int(input(f"Bilangan "
                "yg akan "
                "di-insert:"))
                s.push(b)
                s.printStack()
            else:
                print(f'Stack penuh')
        elif (m == 2):
            print(f'Pop: {s.pop()}')
            s.printStack()
        elif (m == 3):
            print(f'Jumlah element: {s.countElm()}')
        else:
            print(f'Element teratas: {s.infoTop()}')
        m = int(input(f'menu: '))

if __name__ == '__main__':
    main()
