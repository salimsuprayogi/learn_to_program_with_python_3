# Author


def nilai(angka):
    sisa_bagi = angka % 2
    if sisa_bagi == 0:
        return True
    else:
        return False


def result(hasil):
    if nilai(hasil):
        print(hasil, "adalah genap")
    else:
        print(hasil, "adalah ganjil")


result(3)
result(4)

result(float(input("Masukan Angka: ")))
