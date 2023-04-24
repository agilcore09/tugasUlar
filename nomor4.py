class Matriks:
    def __init__(self, baris, kolom):
        self.baris = baris
        self.kolom = kolom
        self.data = [[0 for j in range(kolom)] for i in range(baris)]

    def isiMatriks(self):
        for i in range(self.baris):
            for j in range(self.kolom):
                self.data[i][j] = int(input(f"Masukkan data baris {i+1}, kolom {j+1}: "))

    def dispMatriks(self):
        for i in range(self.baris):
            print(self.data[i])

    def Hapus(self, brs, kol, x):
        if x in self.data[brs-1]:
            idx = self.data[brs-1].index(x)
            self.data[brs-1][idx] = ''
            print(f"Data ada di baris: {brs}, kolom: {idx+1}")
        else:
            print("Data itu tidak ada dalam Matriks")

def Main():
    A = Matriks(3, 3)
    A.isiMatriks()
    print("Matriks sebelum dihapus:")
    A.dispMatriks()
    x = int(input("Masukkan data yang ingin dihapus: "))
    A.Hapus(2, 1, x)
    print("Setelah dihapus:")
    A.dispMatriks()
    y = int(input("Masukkan data yang ingin dihapus: "))
    A.Hapus(3, 2, y)
    print("Setelah dihapus:")
    A.dispMatriks()

Main()