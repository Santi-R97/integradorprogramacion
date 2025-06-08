class Expresion:
    def evaluar(self):
        raise Exception("Tiene que implementarlo la subclase")

    def calcular_ancho(self):
        raise Exception("Tiene que implementarlo la subclase")

class Valor(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def calcular_ancho(self):
        return 1

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

    def calcular_ancho(self):
        return self.exp1.calcular_ancho() + self.exp2.calcular_ancho()

    def __str__(self):
        expresion_1 = str(self.exp1)
        expresion_2 = str(self.exp2)
        lineas_expresion_1 = expresion_1.splitlines()
        lineas_expresion_2 = expresion_2.splitlines()
        ancho_del_arbol = self.calcular_ancho()
        linea_operador = f"({self.operador()}) ".rjust(ancho_del_arbol*2)
        linea_de_ramas = "/   \\".rjust(ancho_del_arbol*2)

        cantidad_de_lineas_de_la_expresion_mas_larga = max(len(lineas_expresion_1), len(lineas_expresion_2))
        todas_las_lineas = []
        for linea in range(cantidad_de_lineas_de_la_expresion_mas_larga):
            linea_exp_1 = lineas_expresion_1[linea] if linea < len(lineas_expresion_1) else ""
            linea_exp_2 = lineas_expresion_2[linea] if linea < len(lineas_expresion_2) else ""
            padding_centro = 3 if linea_exp_2.isnumeric()  else 0
            padding_izquierda = 0 if linea_exp_2.isnumeric()  else ancho_del_arbol
            padding_derecha = 0 if linea_exp_1.isnumeric() else ancho_del_arbol
            linea_exp_1 = linea_exp_1.rjust(padding_izquierda)
            linea_exp_2 = linea_exp_2.ljust(padding_derecha)
            todas_las_lineas.append(f"{linea_exp_1}{" " * padding_centro}{linea_exp_2}")

        return (f"{linea_operador}\n"+
                f"{linea_de_ramas}\n"+
                '\n'.join(todas_las_lineas))

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
        Valor(2),
        Valor(1)
    ),
    Resta(
        Division(
            Suma(
                Resta(
                    Division(
                        Suma(
                            Resta(
                                Division(
                                    Suma(
                                        Valor(2),
                                        Valor(1)
                                    ),
                                    Valor(1)
                                ),
                                Valor(1)
                            ),
                            Valor(1)
                        ),
                        Valor(1)
                    ),
                    Valor(1)
                ),
                Valor(1)
            ),
            Valor(1)
        ),
        Valor(1)
    )
)
print(f"El resultado de la multiplicación es {multiplicacion.evaluar()}")
print(multiplicacion)