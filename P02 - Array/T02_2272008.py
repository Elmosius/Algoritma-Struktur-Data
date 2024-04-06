# File: T02_2272008.py
# Penulis : Elmosius Suli
# ADT array untuk menginput data, menampilkan isi array, 
# menampilkan rata-rata dan minimum, mencari nilai

## Definisi Kelas ##
## Definisi Kelas Array
## Definisi Atribut

# data : menyimpan array data (Int)
# Nmax : menyimpan kapasitas maksimum array (int)
# N : menyimpan banyak elemen array yang terisi (int)

class Array():
    ## Definisi Konstruktor
    def __init__(self, ukuran:int):
        # menyalin ukuran ke atribut Nmax
        self.Nmax = ukuran
        # deklarasi array sebanyak Nmax
        self.data = [None] * self.Nmax
        # isi nilai N dengan 0
        self.N = 0
        return

    # Definisi Method isEmpty()
    def isEmpty(self):
        return self.N == 0

    # Definisi Method IsiArray()
    # Kamus Lokal
    # NN : var input (int)
    # i : var iterator (int)
    def IsiArray(self):
        # input banyaknya elemen array
        NN = int(input("Nilai N : "))
        # validasi NN
        while (NN <= 0 or NN > self.Nmax):
            print("Nilai N harus > 0 dan < Nmax")
            NN = int(input("Nilai N : "))
        # input data, simpan ke elemen array
        for i in range (0, NN, 1):
            self.data[i] = int(input("Nilai x : "))
        # update N
        self.N = NN
        return

    # Definisi Method PrintArray()
    # Kamus Lokal
    # i : var iterator (int)
    def PrintArray(self):
        # Jika array masih kosong
        if (self.isEmpty()):
            print("Tabel masih kosong")
        else:
            # Menampilkan tiap elemen 
            for i in range (0, self.N, 1):
                print(f"A[ {i} ] = {self.data[i]}")
        return

    # Definisi Method Search()
    # Kamus Lokal
    # i : var iterator (int)
    def Search(self, X:int):
        # Memeriksa apakah nilai X ada dalam array
        if X in self.data:
            # mengembalikan posisi indeks X
            return self.data.index(X)
        else:
            return -1
        
    # Definisi Method RataRata()
    # Kamus Lokal
    # jml : var menyimpan jumlah data (int)
    # i : var iterator (int)
    def RataRata(self):
        jml = 0
        for i in range (0, self.N, 1):
            jml += self.data[i]
        return jml / self.N

    # Definisi Method NilaiMin()
    # Kamus Lokal
    # min : var menyimpan nilai terkecil (int)
    # i : var iterator (int)
    def NilaiMin(self):
        min = self.data[0]
        for i in range (1, self.N, 1):
            if (self.data[i] < min):
                min = self.data[i]
        return min

## Program utama ##
# Kamus Lokal
# A : var penampung objek array (Array)
def main():
    A = Array(10)
    A.IsiArray()

    print("Tampilkan Isi Array")
    A.PrintArray()
    print()

    print(f"Nilai rata-rata: {A.RataRata()}")
    print(f"Nilai minimum: {A.NilaiMin()}")
    X = int(input("Input nilai yg akan dicari : "))

    if (A.Search(X) == -1):
        print(f"Nilai {X} tidak ditemukan")
    else:
        print(f"Nilai {X} ada di index ke {A.Search(X)}")

if __name__ == '__main__':
    main()