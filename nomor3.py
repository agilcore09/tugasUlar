# import libary random
from random import *

# penampungan nilai sementara
jar = []

# mencetak 10 angka acak
def summonAngka():
    for i in range(10):
        bil = randint(0, 100)
        print("Angka acak yang ter summon : ",bil)
        jar.insert(1, bil)

# mencari angka terkecil dari nilai array 
def cariMinMax():
    print("nilai terkecil dari angka random : ", min(jar))
    print("nilai terbesar dari angka random : ", max(jar))

def averages() :
    nilaiRata = sum(jar) / len(jar)
    print("nilai rata - rata : ", nilaiRata)

summonAngka()
cariMinMax()
averages()