from operaciones import Componente


class NodoBST():
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    # ---------------- INSERTAR ----------------
    def insertar(self, valor):
        if valor < self.valor:
            if self.izq is None:
                self.izq = NodoBST(valor)
            else:
                self.izq.insertar(valor)
        else:
            if self.der is None:
                self.der = NodoBST(valor)
            else:
                self.der.insertar(valor)

    # ---------------- BUSCAR ----------------
    def buscar(self, valor):
     if self.valor == valor:
         return f" Valor {valor} encontrado en el árbol"

     if valor < self.valor:
         if self.izq:
             return self.izq.buscar(valor)
         return f" Valor {valor} no encontrado"

     else:
        if self.der:
         return self.der.buscar(valor)
        return f" Valor {valor} no encontrado"

    # ---------------- RECORRIDO INORDEN ----------------
    def recorrer(self):
        resultado = []

        if self.izq:
            resultado += self.izq.recorrer()

        resultado.append(self.valor)

        if self.der:
            resultado += self.der.recorrer()

        return resultado

    # ---------------- ALTURA ----------------
    def obtener_altura(self):
        izq = self.izq.obtener_altura() if self.izq else 0
        der = self.der.obtener_altura() if self.der else 0
        return 1 + max(izq, der)

    # ---------------- MOSTRAR ----------------
    def mostrar_arbol(self, nivel=0):
        if self.der:
            self.der.mostrar_arbol(nivel + 1)

        print(" " * (nivel * 4) + str(self.valor))

        if self.izq:
            self.izq.mostrar_arbol(nivel + 1)

    # ---------------- ELIMINAR ----------------
    def eliminar(self, valor):
        if valor < self.valor:
            if self.izq:
                self.izq = self.izq.eliminar(valor)

        elif valor > self.valor:
            if self.der:
                self.der = self.der.eliminar(valor)

        else:
            # caso 0 hijos
            if self.izq is None and self.der is None:
                return None

            # caso 1 hijo
            if self.izq is None:
                return self.der
            if self.der is None:
                return self.izq

            # caso 2 hijos (sucesor inorden)
            sucesor = self.der
            while sucesor.izq:
                sucesor = sucesor.izq

            self.valor = sucesor.valor
            self.der = self.der.eliminar(sucesor.valor)

        return self


class ArbolBinarioBusqueda(Componente):
    def __init__(self):
        self.raiz = None

    # ---------------- INSERTAR ----------------
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoBST(valor)
        else:
            self.raiz.insertar(valor)

    # ---------------- BUSCAR ----------------
    def buscar(self, valor):
        
     if self.raiz is None:
         return " Árbol vacío"
     return self.raiz.buscar(valor)

        

    # ---------------- RECORRER ----------------
    def recorrer(self):
        return self.raiz.recorrer() if self.raiz else []

    # ---------------- ALTURA ----------------
    def obtener_altura(self):
        return self.raiz.obtener_altura() if self.raiz else 0

    # ---------------- MOSTRAR ----------------
    def mostrar_arbol(self):
        if self.raiz:
            self.raiz.mostrar_arbol()

    # ---------------- ELIMINAR ----------------
    def eliminar(self, valor):
        if self.raiz:
            self.raiz = self.raiz.eliminar(valor)

    # ---------------- NIVEL REAL (IMPORTANTE) ----------------
    def obtener_nivel(self, valor):
        return self._nivel_rec(self.raiz, valor, 1)

    def _nivel_rec(self, nodo, valor, nivel):
        if nodo is None:
            return -1  # no encontrado

        if nodo.valor == valor:
            return nivel

        if valor < nodo.valor:
            return self._nivel_rec(nodo.izq, valor, nivel + 1)

        return self._nivel_rec(nodo.der, valor, nivel + 1)

arbol = ArbolBinarioBusqueda()

for v in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(v)
print(arbol.buscar(40))  
print(arbol.buscar(99)) 
print(arbol.buscar(20))  
print(arbol.buscar(10))  

print("Inorden:", arbol.recorrer())
print("Altura:", arbol.obtener_altura())

print("Nivel 50:", arbol.obtener_nivel(50))
print("Nivel 20:", arbol.obtener_nivel(20))
print("Nivel 80:", arbol.obtener_nivel(80))

arbol.mostrar_arbol()

arbol.eliminar(30)

print("Después de eliminar 30:")
arbol.mostrar_arbol()


           

        
    
    

   