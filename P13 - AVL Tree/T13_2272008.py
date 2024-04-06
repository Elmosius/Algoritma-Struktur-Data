# File: T13_2272008.py
# Penulis : Elmosius Suli
# Program yang akan menggunakan 
# ADT AVLTree dimana struktur ADT 
# tersebut dapat dilihat pada tabel terlampir. 
# Program utama akan menampilkan menu untuk 
# memanipulasi elemen dalam queue berdasarkan 
# operasi-operasi yang ada melalui kode angka 
# yang diberikan. Program akan 
# berhenti ketika pengguna memasukkan angka 0.

## Definisi Kelas ##
# Definisi Kelas AVLNode
# Definisi Atribut
# info: menyimpan elemen terdepan dari list (int)
# right: berisi ref. ke anak kanan (AVLNode)
# left: Menyimpan ref. ke anak kiri (AVLNode)
class AVLNode:
    # Definisi Konstruktor
    # Kamus Lokal
    def __init__(self, info: int):
        self.info = info
        self.right = None
        self.left = None
        return

## Definisi Kelas ##
# Definisi Kelas BinarySearchTree
# Definisi Atribut
# root : menyimpan ref. ke node akar(AVLNode)
class BinarySearchTree:
    # Definisi Konstruktor
    # Kamus Lokal
    def __init__(self):
        self.root = None
        return

    # Definisi Method insert(info)
    # Kamus Lokal
    # info : elemen terdepan dri list(int)
    # node : var. sementara root(int)
    def insert(self, info):
        if self.root is None:
            self.root = AVLNode(info)
        else:
            node = self.root
            while node is not None:
                if info < node.info:
                    if node.left is None:
                        node.left = AVLNode(info)
                        return
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = AVLNode(info)
                        return
                    else:
                        node = node.right
                            
    # Definisi Method printInOrder()
    # Kamus Lokal
    # node : var. sementara root(AVLNode)
    def _printInorder(self, node):
        if (node is not None):
            self._printInorder(node.left)
            print(node.info, end=' ')
            self._printInorder(node.right)
    
    # Definisi Method printInorder()
    def printInorder(self):
        self._printInorder(self.root)
        print()
            
## Program utama ##
# Kamus Lokal
# bst : var. objek(BinarySearchTree)
# input_pilihan : var. pilihan(int)
# info: var. insert ke method insert(int)
def main():
    bst = BinarySearchTree()
    print("Menu:")
    print("1. Insert")
    print("2. Lihat Tree (Inorder)")
    print("0. Keluar")
    print("-------------")
    
    input_pilihan = int(input("Menu: "))
    while (input_pilihan != 0):
        if (input_pilihan == 1):
            info = int(input("Masukkan angka \
yang ingin ditambahkan: "))
            bst.insert(info)
        elif (input_pilihan == 2):
            print("Inorder:")
            bst.printInorder()
        else:
            print("Pilihan hanya no 0,1, dan 2")
        input_pilihan = int(input("Menu: "))

if __name__ == '__main__':
    main()
