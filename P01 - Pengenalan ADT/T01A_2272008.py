# File: T01A_2272008.py
# Penulis : Elmosius Suli
# ADT Buku dengan tiga buah atribut (judul, penulis, tahun terbit) 
# dan operasi untuk menampilkan informasi dari buku tersebut.

## Definisi Kelas ##
## Definisi Kelas Buku
## Definisi Atribut
# judul1 : atribut untuk menyimpan nilai judul (str)
# penulis1 : atribut untuk menyimpan nilai penulis (str)
# tahun_terbit1 : atribut untuk menyimpan nilai tahun terbit (int)

# judul2 : atribut untuk menyimpan nilai judul (str)
# penulis2 : atribut untuk menyimpan nilai penulis (str)
# tahun_terbit2 : atribut untuk menyimpan nilai tahun terbit (int)

# judul3 : atribut untuk menyimpan nilai judul (str)
# penulis3 : atribut untuk menyimpan nilai penulis (str)
# tahun_terbit3 : atribut untuk menyimpan nilai tahun terbit (int)

class Buku():
    ## Definisi Konstruktor
    def __init__(self):
        # Buku 1
        self.judul1 = "Harry Potter and the Sorcerer's Stone"
        self.penulis1 = "J.K. Rowling"
        self.tahun_terbit1 = 1997 
        
        # Buku 2
        self.judul2 = "To Kill a Mockingbird"
        self.penulis2 = "Harper Lee"
        self.tahun_terbit2 = 1960

        # Buku 3
        self.judul3 = "The Great Gatsby"
        self.penulis3 = "F. Scott Fitzgerald"
        self.tahun_terbit3 = 1925
        return
    
    
    ## Definisi Method tampilkan()
    def tampilkan(self) :
        print(f"{self.judul1} oleh \
{self.penulis1}, Tahun Terbit: {self.tahun_terbit1}")
        print(f"{self.judul2} oleh \
{self.penulis2}, Tahun Terbit: {self.tahun_terbit2}")
        print(f"{self.judul3} oleh \
{self.penulis3}, Tahun Terbit: {self.tahun_terbit3}")
        return
    
## Program utama ##
# Kamus Lokal
# b1 : var penampung objek buku 1 (Buku)
def main():
    b1 = Buku() # buat objek buku 1
    # Output
    print("Informasi Buku:")
    b1.tampilkan()

    return

if __name__ == '__main__':
    main()
