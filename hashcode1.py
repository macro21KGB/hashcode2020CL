print("////// Hash Code 2020 //////")



def ordinaLibrerie(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].tempo_registrazione > arr[j+1].tempo_registrazione :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

class Libreria:
    Id_lib = 0
    numero_libri = 0
    libri = {}
    tempo_registrazione = 0


    def __init__(self, Id_lib, numero_libri, libri, tempo_registrazione):
        self.Id_lib = Id_lib
        self.numero_libri = numero_libri
        self.libri = libri
        self.tempo_registrazione = tempo_registrazione
    def stampa_libreria(self):
        print(f"Libreria_{self.Id_lib} ha {self.numero_libri} libri e i libri sono: ")
        print(self.libri)

class Libro:
    Id_libro = 0

    def __init__(self, Id_libro):
        self.Id_libro = Id_libro

lib1 =Libreria(0,4,{}, 12)
lib2 =Libreria(1,2,{}, 3)
lib3 =Libreria(2,4,{}, 6)
lib4 =Libreria(3,5,{}, 2)

array = [lib1,lib2,lib3,lib4]

array = ordinaLibrerie(array)

for lib in array:
    print(lib.tempo_registrazione)