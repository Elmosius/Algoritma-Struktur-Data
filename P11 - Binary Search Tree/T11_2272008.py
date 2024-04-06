# File: T11_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan ADT
# BinarySearchTree dimana struktur ADT
# tersebut dapat dilihat pada tabel
# terlampir. Program utama akan menampilkan
# menu untuk memanipulasi elemen
# berdasarkan operasi-operasi yang
# ada melalui kode angka yang
# diberikan. Program akan berhenti
# etika pengguna memasukkan angka 0.

## Definisi Kelas ##
# Definisi Kelas BSTNode
# Definisi Atribut
# info: menyimpan elemen terdepan dari list (int)
# right: berisi ref. ke anak kanan (BSTNode)
# left: Menyimpan ref. ke anak kiri (BSTNode)
class BSTNode:
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
# root : menyimpan ref. ke node akar(BSTNode)


class BinarySearchTree:
    # Definisi Konstruktor
    # Kamus Lokal
    def __init__(self):
        self.root = None
        return

    # Definisi Method insert(info)
    # Kamus Lokal
    # node : var. sementara root(int)
    def insert(self, info):
        if self.root is None:
            self.root = BSTNode(info)
        else:
            node = self.root
            while node is not None:
                if info < node.info:
                    if node.left is None:
                        node.left = BSTNode(info)
                        return
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = BSTNode(info)
                        return
                    else:
                        node = node.right

    # Definisi Method printInorder()
    # Kamus Lokal
    # node: var. sementara root (BSTNode)
    # Notes :
    # melihat beberapa sumber internet :
    # https://www.enjoyalgorithms.com
    # /blog/insertion-in-binary-search-tree

    def printInorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.printInorder(node.left)
            print(node.info, end=" ")
            if node.right is not None:
                self.printInorder(node.right)
        else:
            print("Tree Kosong", end=" ")

## Program utama ##
# Kamus Lokal
# bst : var. objek(BinarySearchTree)
# input_pilihan : var. pilihan(int)
# info: var. insert ke method insert(int)
def main():
    bst = BinarySearchTree()
    # Menu
    print("Menu:")
    print("1. Insert")
    print("2. Lihat Tree")
    print("0. Keluar")
    print("-------------")

    input_pilihan = int(input("Menu: "))
    while (input_pilihan != 0):
        if (input_pilihan == 1):
            info = int(input("Masukkan angka \
yang ingin ditambahkan: "))
            bst.insert(info)
        elif (input_pilihan == 2):
            print("Tree dlm format inorder:")
            bst.printInorder()
            print()
        else:
            print("Pilihan hanya no 0,1,dan 2")
        input_pilihan = int(input("Menu: "))


if __name__ == '__main__':
    main()
