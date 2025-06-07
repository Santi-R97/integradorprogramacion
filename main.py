class Expresion:
    def evaluar(self):
        raise Exception("Tiene que implementarlo la subclase")

    def calcular_nivel(self):
        return 0

class Valor(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self):
        return self.valor

    def __str__(self):
        return str(self.valor)

class ExpresionDoble(Expresion):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def operador(self):
        raise Exception("Tiene que implementarlo la subclase")

    def calcular_nivel(self):
        return 1 + max(self.exp1.calcular_nivel(), self.exp2.calcular_nivel())

    def __str__(self):
        padding = self.calcular_nivel() * 5
        operador = f"({self.operador()})".center(int(padding * 2)) + "\n"
        ramas = "/".center(padding) + "\\".center(padding)
        expresiones = str(self.exp1).center(padding) + str(self.exp2).center(padding)
        return operador + ramas + expresiones

class Suma(ExpresionDoble):

    def operador(self):
        return "+"

    def evaluar(self):
        # evaluamos ambas expresiones y sumamos
        return self.exp1.evaluar() + self.exp2.evaluar()

class Resta(ExpresionDoble):

    def operador(self):
        return "-"

    def evaluar(self):
        # evaluamos ambas expresiones y restamos
        return self.exp1.evaluar() - self.exp2.evaluar()

class Multiplicacion(ExpresionDoble):

    def operador(self):
        return "*"

    def evaluar(self):
        # evaluamos ambas expresiones y multiplocamos
        return self.exp1.evaluar() * self.exp2.evaluar()

class Division(ExpresionDoble):

    def operador(self):
        return "/"

    def evaluar(self):
        # evaluamos ambas expresiones y dividimos
        return self.exp1.evaluar() / self.exp2.evaluar()


suma = Suma(Valor(3), Valor(5))
resta = Resta(Valor(2), Valor(1))
multiplicacion = Multiplicacion(suma, resta)
print(multiplicacion)
