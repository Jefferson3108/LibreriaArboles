from abc import ABC, abstractmethod
class Componente(ABC):
    @abstractmethod
    def insertar(self, valor):
        pass

    @abstractmethod
    def eliminar(self, valor):
        pass

    @abstractmethod
    def buscar(self, valor):
        pass

    @abstractmethod
    def recorrer(self):
        pass
    @abstractmethod
    def obtener_altura(self):
        pass
    @abstractmethod
    def mostrar_arbol(self):
        pass

class Hoja(Componente):
    def __init__(self, valor):
        self.valor = valor

    def insertar(self, componente):
        raise NotImplementedError("No se pueden insertar valores en una hoja")

    def eliminar(self, componente):
        raise NotImplementedError("No se pueden eliminar valores de una hoja")

    def buscar(self, valor):
        return self.valor == valor

    def recorrer(self):
        return [self.valor]
    
    def obtener_altura(self):
        return 1
    
    def mostrar_arbol(self, nivel=0):
        print(" " * (nivel * 4) + str(self.valor))

class Rama(Componente):
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def insertar(self, componente):
        self.hijos.append(componente)

    def buscar(self, valor):
         if self.valor == valor:
             return True

         for hijo in self.hijos:
             if hijo.buscar(valor):
              return True

         return False


    def eliminar(self, valor):
         for hijo in self.hijos:
             if hijo.valor == valor:
                 self.hijos.remove(hijo)
                 return True

             if isinstance(hijo, Rama):
                 if hijo.eliminar(valor):
                     return True
         return False
        
    def recorrer(self):
        resultado = [self.valor]
        for hijo in self.hijos:
            resultado.extend(hijo.recorrer())
        return resultado
    
    def obtener_altura(self):
        if not self.hijos:
            return 1
        else:
            alturas = [hijo.obtener_altura() for hijo in self.hijos]
            return 1 + max(alturas)
    
    def mostrar_arbol(self, nivel=0):
        print(" " * (nivel * 4) + str(self.valor))
        for hijo in self.hijos:
            hijo.mostrar_arbol(nivel + 1)

# Ejemplo de uso
raiz = Rama("A")
rama1 = Rama("B")
rama2 = Rama("C")
hoja1 = Hoja("D")
hoja2 = Hoja("E")
rama1.insertar(hoja1)
rama1.insertar(hoja2)
raiz.insertar(rama1)
raiz.insertar(rama2)
print("Recorrido del árbol:", raiz.recorrer())
print("Altura del árbol:", raiz.obtener_altura())
print("Árbol completo:")
raiz.mostrar_arbol()
raiz.eliminar("D")
print("Recorrido del árbol después de eliminar B:", raiz.recorrer())
print("Altura del árbol después de eliminar B:", raiz.obtener_altura())
print("Árbol completo después de eliminar B:")
raiz.mostrar_arbol()