from array import array
# definisikan array
isiArray = [10, 20, 30, 10, 40, 30, 20, 20, 50, 10]
def cacah(x):
    cacah = 0
    for i in isiArray :
        if(i == x):
            cacah += i
            print("nilai yang sama : ", cacah)

cacah(20)
cacah(10)
cacah(30)
cacah(50)
# kalau tidak ada 
cacah(51)