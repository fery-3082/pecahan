def mobil_sedan():
    class Mobil_Sedan:
        def __init__(self, Pemilik, Merk, Warna):
            self.Pemilik = Pemilik
            self.Merk = Merk
            self.Warna = Warna

        @property
        def warna(self):
            pass

        @property
        def pemilik(self):
            pass

        @warna.getter
        def warna(self):
            return self.Warna

        @warna.setter
        def warna(self, input):
            self.Warna = input

        @pemilik.getter
        def pemilik(self):
            return self.Pemilik

        @pemilik.setter
        def pemilik(self, inputName):
            self.Pemilik = inputName

    sedan = Mobil_Sedan(input("Pemilik: "), input("Merk: "), input("Warna: "))
    print(sedan.__dict__)

    print(" ")
    print("Apakah Anda ingin mengubah warna mobil Anda?")
    print("Yes/No")
    pilihan = input()
    if pilihan == "Yes":
        sedan.warna = input("Silakan ubah warna sedan Anda: ")
        print("Warna berhasil diubah menjadi " + sedan.warna)
        print(sedan.__dict__)
    else:
        print(sedan.__dict__)

    print(" ")
    print("Apakah Anda ingin menjual mobil Anda?")
    print("Yes/No")
    pilihan2 = input()
    if pilihan2 == "Yes":
        sedan.pemilik = input("Silakan jual mobil sedan Anda kepada: ")
        print("Anda telah menjual mobil sedan kepada " + sedan.pemilik)
        print(sedan.__dict__)
    else:
        print(sedan.__dict__)
    return 

def ikan():
    class Ikan():
        def __init__(self, Ikan, Pemilik):
            self.Ikan = Ikan
            self.Pemilik = Pemilik

        @property
        def pemilik(self):
            pass

        @pemilik.getter
        def pemilik(self):
            return self.Pemilik

        @pemilik.setter
        def pemilik(self, input):
            self.Pemilik = input

    ikan1 = Ikan(input("Jenis ikan: "), input("Pemilik: "))
    print(ikan1.__dict__)

    print(" ")
    print("Apakah Anda ingin menjual ikan?")
    print("Yes/No")
    pilihan = input()
    if pilihan == "Yes":
        ikan1.pemilik = input("Silakan jual ikan kepada: ")
        print("Anda telah menjual ikan kepada " + ikan1.pemilik)
        print(ikan1.__dict__)
    else:
        print(ikan1.__dict__)
    return

def burung():
    class Burung():
        def __init__(self, jenis_burung, pemilik):
            self.Burung = jenis_burung
            self.Pemilik = pemilik

        @property
        def pemilik(self):
            pass

        @pemilik.setter
        def pemilik(self):
            return self.Pemilik

        @pemilik.getter
        def pemilik(self, input):
            self.Pemilik = input

    burung1 = Burung(input("Jenis Burung: "), input("Pemilik: "))
    print(burung1.__dict__)

    print(" ")
    print("Apakah Anda ingin menjual burung Anda?")
    print("Yes/No")
    pilihan = input()
    if pilihan == "Yes":
        burung1.Pemilik = input("Silakan jual burung kepada: ")
        print("Anda telah menjual burung kepada: ")
        print(burung1.__dict__)
    else:
        print(burung1.__dict__)
    return

def komputer():
    class Komputer:
        def __init__(self, pemilik, ram, sistem_operasi):
            self.Pemilik = pemilik
            self.RAM = ram
            self.Sistem_Operasi = sistem_operasi

        @property
        def pemilik(self):
            pass
    
        @property
        def ram(self):
            pass

        @property
        def sistem_operasi(self):
            pass

        @pemilik.getter
        def pemilik(self):
            return self.Pemilik
    
        @pemilik.setter
        def pemilik(self, input1):
            self.Pemilik = input1

        @ram.getter
        def ram(self):
            return self.RAM

        @ram.setter
        def ram(self, input2):
            self.RAM = input2

        @sistem_operasi.getter
        def sistem_operasi(self):
            return self.Sistem_Operasi
    
        @sistem_operasi.setter
        def sistem_operasi(self, input3):
            self.Sistem_Operasi = input3

    komputer = Komputer(input("Pemilik: "), input("RAM: "), input("Sistem Operasi: "))
    print(komputer.__dict__)

    print(" ")
    print("Apakah Anda ingin mengganti sistem operasi pada komputer Anda?")
    print("Yes/No")
    pilihan1 = input()
    if pilihan1 == "Yes":
        komputer.sistem_operasi = input("Silakan pilih sistem operasi baru: ")
        print("Anda berhasil mengganti sistem operasi menjadi "+komputer.Sistem_Operasi)
        print(komputer.__dict__)
    else:
        print(komputer.__dict__)

    print(" ")
    print("Apakah Anda ingin mengganti RAM?")
    print("Yes/No")
    pilihan2 = input()
    if pilihan2 == "Yes":
        komputer.ram = input("Silakan pilih RAM yang baru: ")
        print("Anda telah berhasil mengganti RAM menjadi "+ komputer.ram)
        print(komputer.__dict__)
    else:
        print(komputer.__dict__)

    print(" ")
    print("Apakah Anda ingin menjual komputer Anda?")
    print("Yes/No")
    pilihan3 = input()
    if pilihan3 == "Yes":
        komputer.pemilik = input("Anda akan menjual komputer kepada: ")
        print("Anda telah menjual komputer Anda kepada " + komputer.pemilik)
        print(komputer.__dict__)
    else:
        print(komputer.__dict__)
    return

print("Pilih salah satu: \n 1. Mobil Sedan \n 2. Ikan \n 3. Burung \n 4. Komputer")
n = input()
if n == "1":
    mobil_sedan()
elif n == "2":
    ikan()
elif n == "3":
    burung()
elif n == "4":
    komputer()
else:
    print("Program Error")