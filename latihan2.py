angka = []
def mengurut(angka):
    a =int(input("Masukan Bilangan 1 :"))
    angka.append(a)
    b =int(input("Masukan Bilangan 2 :"))
    angka.append(b)
    c =int(input("Masukan Bilangan 3 :"))
    angka.append(c)
    tukar = True
    while tukar:
        tukar=False
        for n in range(len(angka)-1):
            if angka[n] > angka[n+1]:
                angka[n], angka[n+1] = angka[n+1], angka[n]
                tukar = True
    return angka
print(mengurut(angka))
