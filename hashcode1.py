print("////// Hash Code 2020 //////")



def ordinaLibrerie(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].tempo_registrazione > arr[j+1].tempo_registrazione :
                temp = arr[j]
                arr[j] = arr[j+1] 
                arr[j+1] = temp
    return arr
    
def checkDuplicati(arr_lib):

    n = len(arr_lib)
    print("ARRAY" +str(n))
    for x in range(n):
        for y in range(n-1):
            if x == y:
                arr_lib.pop(x)
                print("CANCELLATO..." + "X: " +str(x) + "Y: " + str)
    
        
class Libreria:
    Id_lib = 0
    numero_libri = 0
    libri = []
    tempo_registrazione = 0


    def __init__(self, Id_lib, numero_libri, libri, tempo_registrazione):
        self.Id_lib = Id_lib
        self.numero_libri = numero_libri
        self.libri = libri
        self.tempo_registrazione = tempo_registrazione


    def stampa_libreria(self):
        print(f"Libreria_{self.Id_lib} ha {self.numero_libri} libri e i libri sono: ")
        print("Tempo: " +str(self.tempo_registrazione))
        print(self.libri)

class Libro:
    Id_libro = 0

    def __init__(self, Id_libro):
        self.Id_libro = Id_libro

libro1 = Libro(0)
libro1b = Libro(0)
libro2 = Libro(1)
libro3 = Libro(2)

lib1 =Libreria(0,4,[libro1,libro1b,libro2,libro3], 12)
lib2 =Libreria(1,2,[], 3)
lib3 =Libreria(2,4,[], 6)
lib4 =Libreria(3,5,[], 2)

array = [lib1,lib2,lib3,lib4]

array = ordinaLibrerie(array)

checkDuplicati([libro1,libro1b,libro2,libro3])


for lib in array:
    print(lib.stampa_libreria())