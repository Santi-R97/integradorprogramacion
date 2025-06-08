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
        self.exp_izquierda = exp1
        self.exp_derecha = exp2

    def operador(self):
        raise Exception("Tiene que implementarlo la subclase")

    def calcular_ancho(self):
        return self.exp_izquierda.calcular_ancho() + self.exp_derecha.calcular_ancho()

    def __str__(self):
        ancho_del_arbol = self.calcular_ancho()
        resultado = str(self.evaluar())
        ancho_resultado = len(resultado) // 2
        padding = ancho_del_arbol * 2
        linea_resultado = f"({resultado}) ".rjust(padding + ancho_resultado)
        linea_operador = f"({self.operador()}) ".rjust(padding)
        linea_de_ramas = "/   \\".rjust(padding)

        # Necesitamos dividir las líneas para poder poner la expresion izquierda y derechas
        # en el mismo renglón en la consola
        lineas_expresion_1 = str(self.exp_izquierda).splitlines()
        lineas_expresion_2 = str(self.exp_derecha).splitlines()
        cantidad_de_lineas_de_la_expresion_mas_larga = max(len(lineas_expresion_1), len(lineas_expresion_2))
        todas_las_lineas = []
        for linea in range(cantidad_de_lineas_de_la_expresion_mas_larga):
            # si una línea es más larga que la otra ponemos un string vacío
            linea_exp_izquierda = lineas_expresion_1[linea] if linea < len(lineas_expresion_1) else ""
            linea_exp_derecha = lineas_expresion_2[linea] if linea < len(lineas_expresion_2) else ""
            # si tenemos un valor a la izquierda, agregamos padding mínimo
            # sino el ancho que tenga el árbol
            padding_centro = 3 if linea_exp_derecha.isnumeric()  else ancho_del_arbol
            padding_izquierda = 0 if linea_exp_derecha.isnumeric()  else ancho_del_arbol
            padding_derecha = 0 if linea_exp_izquierda.isnumeric() else ancho_del_arbol
            # ajustamos las lineas con el padding
            linea_exp_izquierda = linea_exp_izquierda.rjust(padding_izquierda)
            linea_exp_derecha = linea_exp_derecha.ljust(padding_derecha)
            todas_las_lineas.append(f"{linea_exp_izquierda}{" " * padding_centro}{linea_exp_derecha}")

        return (f"{linea_resultado}\n"+
                f"{linea_operador}\n"+
                f"{linea_de_ramas}\n"+
                '\n'.join(todas_las_lineas))

class Suma(ExpresionDoble):

    def operador(self):
        return "+"

    def evaluar(self):
        # evaluamos ambas expresiones y sumamos
        return self.exp_izquierda.evaluar() + self.exp_derecha.evaluar()

class Resta(ExpresionDoble):

    def operador(self):
        return "-"

    def evaluar(self):
        # evaluamos ambas expresiones y restamos
        return self.exp_izquierda.evaluar() - self.exp_derecha.evaluar()

class Multiplicacion(ExpresionDoble):

    def operador(self):
        return "*"

    def evaluar(self):
        # evaluamos ambas expresiones y multiplocamos
        return self.exp_izquierda.evaluar() * self.exp_derecha.evaluar()

class Division(ExpresionDoble):

    def operador(self):
        return "/"

    def evaluar(self):
        # evaluamos ambas expresiones y dividimos
        return self.exp_izquierda.evaluar() / self.exp_derecha.evaluar()



multiplicacion = Multiplicacion(
    Suma(
        Valor(3),
        Valor(5)
    ),
    Resta(
        Division(
            Valor(10),
            Valor(5)
        ),
        Valor(1)
    )
)

print(f"El resultado de la multiplicacion es {multiplicacion.evaluar()}")
print(multiplicacion)

suma = Suma(
    Division(
        Valor(-6),
        Valor(-3)
    ),
    Multiplicacion(
        Resta(
            Valor(96),
            Valor(12)
        ),
        Valor(23)
    )
)
print(f"El resultado de la suma es {suma.evaluar()}")
print(suma)