

class telefonia():

    company = "TELCEL"
    
    def __init__(self, usuario):
        self.usuario = usuario


n1 = telefonia("NESTOR")
n2 = telefonia("OSCAR")
n3 = telefonia("ENRIQUE")
print(n1.company)
print(n2.company)
print(n3.company)

n2.company="CLARO"
print(n2.company)

telefonia.company="MOVISTAR"
print(n1.company)
print(n2.company)
print(n3.company)