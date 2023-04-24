listArray = []

# memasukkan nilai array yang panjangnya max hanya 10
def inputArrays() :

    # memasukkan nilai sampai 10
    for i in range(10):
       inputValues = int(input("masukkan nilai sampai 10 nilai : "))
       listArray.insert(1, inputValues)

    # mengembalikan nilai array
    return listArray
print("isi array yang sudah di masukkan : ", inputArrays())

# menjumlahkan semua nilai yang ada di dalam array 
def summary() : 
    jumlah = sum(listArray)
    return jumlah
print("total dari panjang array : ", summary())

# mencari nilai rata - rata dari semua nilai yang ada di array

def averages() :
    nilaiRata = summary() / len(listArray)
    return nilaiRata

print("Total nilai rata - rata : ", averages())

# mencipatakan data yang tidak ada duplikasi
def cekDuplikat(): 
    arrayBaru = list(dict.fromkeys(listArray))
    result = arrayBaru
    listArray.clear()
    # mengubah menjadi tipe data tuple
    listArray.insert(1, tuple(result))
    return listArray

print("Nilai Array yang baru : ", cekDuplikat())

