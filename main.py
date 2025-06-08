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
        padding_izquierda = self.exp1.calcular_nivel()
        padding_derecha = self.exp2.calcular_nivel()
        padding_total = (padding_izquierda + padding_derecha) * 5
        expresion_1 = str(self.exp1)
        expresion_2 = str(self.exp2)
        lineas_expresion_1 = expresion_1.splitlines()
        lineas_expresion_2 = expresion_2.splitlines()
        maximo_de_lineas = max(len(lineas_expresion_1), len(lineas_expresion_2))
        lineas_unidas = []
        operador = f"{" " * ((padding_total // 2)-1)} ({self.operador()})\n"
        ramas = f"/ {" " * padding_total} \\\n"

        numero_expresion_1 = 1
        numero_expresion_2 = 1
        for linea in range(maximo_de_lineas):
            if linea < len(lineas_expresion_1):
                numero_expresion_1 += 1
                linea1 = lineas_expresion_1[linea]
            else:
                linea1 = ""
            if linea < len(lineas_expresion_2):
                numero_expresion_2 += 1
                linea2= lineas_expresion_2[linea]
            else:
                linea2 = ""

            lineas_unidas.append(f"{linea1}{"  "}{linea2}")

        return operador + ramas +  "\n".join(lineas_unidas)

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



multiplicacion = Multiplicacion(
    Suma(
        Valor(1),
        Valor(2)
    ),
    Resta(
        Valor(9),
        Valor(9)
    )
)
print(multiplicacion)
