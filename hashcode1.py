print("////// Hash Code 2020 //////")




class Libreria:
    Id_lib = 0
    numero_libri = 0
    libri = {}
    tempo_registrazione = 0

    def __init__(self, Id_lib, numero_libri, libri):
        self.Id_lib = Id_lib
        self.numero_libri = numero_libri
        self.libri = libri
    def stampa_libreria(self):
        print(f"Libreria_{self.Id_lib} ha {self.numero_libri} libri e i libri sono: ")
        print(self.libri)

class Libro:
    Id_libro = 0

    def __init__(self, Id_libro):
        self.Id_libro = Id_libro