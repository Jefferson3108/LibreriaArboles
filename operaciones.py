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

    @abstractmethod
    def obtener_nivel(self):
        pass