class CuentaCorriente:
    
    def __init__(self, dni, saldo):
        self.dni = dni
        self.nombre = ""
        self.saldo = saldo

    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo
    
    def ingresarDinero(self, saldo):
        self.saldo = self.saldo + saldo

    def sacarDinero(self, saldo):
        available = True
        if self.saldo > 0:
            self.saldo = self.saldo - saldo
        else:
            available = False
        return available
    
    def __str__(self) -> str:
        return "DNI: " + str(self.dni) + " Name: " + self.nombre + " Balance: " + str(self.saldo) + "\n"
    
    def __eq__(self, obj) -> bool:
        equal = False
        if self.dni == obj.dni:
            equal = True
        return equal
    
    def __lt__ (self, obj) -> bool:
        menor = False
        if self.saldo < obj.saldo:
            menor = True
        return menor