# File: T12_2272008.py
# Penulis : Elmosius Suli
# program yang akan menggunakan ADT 
# BinarySearchTree dimana struktur ADT 
# tersebut dapat dilihat pada tabel terlampir. 
# Program utama akan menampilkan menu untuk 
# memanipulasi elemen dalam queue berdasarkan 
# operasi-operasi yang ada melalui kode angka 
# yang diberikan. Program akan berhenti ketika 
# pengguna memasukkan angka 0

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
    # info : elemen terdepan dri list(int)
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

    # Definisi Method remove(info)
    # Kamus Lokal
    # info : elemen terdepan dri list(int)
    # node : var. sementara root(int) 
    def remove(self, info):
        def _remove(node, info):
            if not node:
                return node
            if info < node.info:
                node.left = _remove(node.left, 
                                    info)
            elif info > node.info:
                node.right = _remove(node.right, 
                                     info)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.info = temp.info
                node.right = _remove(node.right, 
                                     temp.info)
            return node
        self.root = _remove(self.root, info)
    
    
    
    # Definisi Method printProrder()
    def printPreorder(self):
        self._printPreorder(self.root)
        print()
    
    
    # Definisi Method _printPreorder(node)
    # Kamus Lokal
    # node : var. sementara root(BSTNode)
    def _printPreorder(self, node):
        if node is not None:
            print(node.info, end=" ")
            self._printPreorder(node.left)
            self._printPreorder(node.right)
    
    # Definisi Method printPostrder()
    def printPostorder(self):
        self._printPostorder(self.root)
        print()
    
    # Definisi Method _printPostorder(node)
    # Kamus Lokal
    # node : var. sementara root(BSTNode)
    def _printPostorder(self, node):
        if node is not None:
            self._printPostorder(node.left)
            self._printPostorder(node.right)
            print(node.info, end=" ")
            
## Program utama ##
# Kamus Lokal
# bst : var. objek(BinarySearchTree)
# input_pilihan : var. pilihan(int)
# info: var. insert ke method insert(int)
def main():
    bst = BinarySearchTree()
    print("Menu:")
    print("1. Insert")
    print("2. Remove")
    print("3. Lihat Tree (Preorder)")
    print("4. Lihat Tree (Postorder)")
    print("0. Keluar")
    print("-------------")
    

    input_pilihan = int(input("Menu: "))
    while (input_pilihan != 0):
        if (input_pilihan == 1):
            info = int(input("Masukkan angka \
yang ingin ditambahkan: "))
            bst.insert(info)
        elif (input_pilihan == 2):
            info = int(input("Masukkan angka \
yang ingin dihapus: "))
            bst.remove(info)
        elif (input_pilihan == 3):
            print("Preorder:")
            bst.printPreorder()
        elif (input_pilihan == 4):
            print("Postorder:")
            bst.printPostorder()
        else:
            print("Pilihan hanya no 0,1,2,3, dan 4")
        input_pilihan = int(input("Menu: "))

if __name__ == '__main__':
    main()