# File: T01B_2272008.py
# Penulis : Elmosius Suli
# ADT kalkulator dengan operasi tambah, kurang, kali, dan bagi.

## Definisi Kelas ##
# Definisi Kelas Kalkulator
# Definisi Atribut
# a1 : atribut untuk menyimpan nilai angka pertama (int)
# a2 : atribut untuk menyimpan nilai angka kedua (int)
# a3 : atribut untuk menyimpan nilai angka pertama (int)
# a4 : atribut untuk menyimpan nilai angka kedua (int)
# a5 : atribut untuk menyimpan nilai angka pertama (int)
# a6 : atribut untuk menyimpan nilai angka kedua (int)
# a7 : atribut untuk menyimpan nilai angka pertama (int)
# a8 : atribut untuk menyimpan nilai angka kedua (int)

# penulis : atribut untuk menyimpan nilai penulis (str)
# tahun_terbit : atribut untuk menyimpan nilai tahun terbit (int)

class Kalkulator():
    
    # Definisi Method tampilkan()
    def tampilkan(self):
        return f"Hasil Penambahan: {self.tambah()}\n\
Hasil Pengurangan: {self.kurang()}\n\
Hasil Perkalian: {self.kali()}\n\
Hasil Pembagian: {self.bagi()}"

    # Definisi Method tambah()
    def tambah(self):
        return (self.a1 + self.a2)

    # Definisi Method kurang()
    def kurang(self):
        return (self.a3 - self.a4)

    # Definisi Method kali()
    def kali(self):
        return (self.a5 * self.a6)

    # Definisi Method bagi()
    def bagi(self):
        return (self.a7 / self.a8)

## Program utama ##
# Kamus Lokal
# k : var penampung objek kalkulator (Kalkulator)
def main():
    k = Kalkulator()  # buat objek angka pertama
    print("Operassi Penambahan")
    k.a1 = int(input("Masukkan angka pertama : "))
    k.a2 = int(input("Masukkan angka kedua : "))
    print()

    print("Operasi Pengurangan")
    k.a3 = int(input("Masukkan angka pertama : "))
    k.a4 = int(input("Masukkan angka kedua : "))
    print()

    print("Operassi Perkalian")
    k.a5 = int(input("Masukkan angka pertama : "))
    k.a6 = int(input("Masukkan angka kedua : "))
    print()

    print("Operassi Pembagian")
    k.a7 = int(input("Masukkan angka pertama : "))
    k.a8 = int(input("Masukkan angka kedua : "))
    print()

    # Output
    print(k.tampilkan())
    return

if __name__ == '__main__':
    main()
