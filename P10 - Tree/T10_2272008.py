# File: T10_2272008.py
# Penulis : Elmosius Suli
#  program yang akan menyimpan data dalam
# representasi tree.
# Data bersifat bebas namun harus
# menghasilkan minimal tujuh element tree dan
# tiga level. Struktur elemen tree terlampir

## Definisi Kelas ##
# Definisi Kelas TreeElmt
# Definisi Atribut
# value : menyimpan nilai dri elemen (str)
# children : menyimpan anak2 dari elmnt
# (arrat of TreeElmt)
class TreeElmt:
    # Definisi Konstruktor
    # Kamus Lokal
    # nilai : simpan nilai element (str)
    # ukuran : parameter untuk ukr chil (int)
    def __init__(self, nilai: str, ukuran: int):
        self.childrenCount = ukuran
        self.children = [None] * self.childrenCount
        self.value = nilai

        return

    def display(self, lvl=0):
        print("  " * lvl + self.value)
        for child in self.children:
            if (child is not None):
                child.display(lvl + 1)
    
    

## Program utama ##
# Kamus Lokal
# root : var. objek TreeElemt


def main():
    # Buat objek 2 children
    root = TreeElmt("A", 2)
    root.children[0] = TreeElmt("B", 1)
    root.children[1] = TreeElmt("C", 1)

    # Level pertama
    root.children[0].children[0] = TreeElmt("D", 1)
    root.children[1].children[0] = TreeElmt("E", 1)

    # Level kedua
    root.children[0].children[0].children[0] = TreeElmt("F", 2)
    root.children[1].children[0].children[0] = TreeElmt("G", 2)

    # Level ketiga
    root.children[0].children[0].children[0].children[0] = TreeElmt("H", 0)
    root.children[0].children[0].children[0].children[1] = TreeElmt("I", 0)
    root.children[1].children[0].children[0].children[0] = TreeElmt("J", 0)
    root.children[1].children[0].children[0].children[1] = TreeElmt("K", 0)

    root.display()


if __name__ == '__main__':
    main()
