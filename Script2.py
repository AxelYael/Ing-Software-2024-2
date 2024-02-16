"""  
Ejercicio 1: Contar valles
"""
def contar_valles(recorrido):
    if not recorrido:
        return 0
    
    if not all(paso in ['D', 'U'] for paso in recorrido):
        raise ValueError("El recorrido solo debe contener las letras 'D' o 'U'")
    
    nivel_del_mar = 0
    cantidad_valles = 0
    en_valle = False
    
    for paso in recorrido:
        if paso == 'U':
            nivel_del_mar += 1
        elif paso == 'D':
            nivel_del_mar -= 1
        
        if nivel_del_mar < 0 and not en_valle:
            en_valle = True
        
        if nivel_del_mar == 0 and en_valle:
            cantidad_valles += 1
            en_valle = False
    
    return cantidad_valles

"""  
Ejercicio 2: Árbol binario de búsqueda
"""
class NodoArbolBinario:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        nuevo_nodo = NodoArbolBinario(clave)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            actual = self.raiz
            while actual:
                padre = actual
                if clave <= actual.clave:
                    actual = actual.izquierda
                else:
                    actual = actual.derecha
            if clave <= padre.clave:
                padre.izquierda = nuevo_nodo
            else:
                padre.derecha = nuevo_nodo
            nuevo_nodo.padre = padre

    def recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.clave, end=" ")
            self.recorrido_preorden(nodo.izquierda)
            self.recorrido_preorden(nodo.derecha)

    def recorrido_en_orden(self, nodo):
        if nodo:
            self.recorrido_en_orden(nodo.izquierda)
            print(nodo.clave, end=" ")
            self.recorrido_en_orden(nodo.derecha)

    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izquierda)
            self.recorrido_postorden(nodo.derecha)
            print(nodo.clave, end=" ")


# Main
recorrido = "UDUUDDDUUDDDUUDDUU"
print("Número de valles:", contar_valles(recorrido))

arbol = ArbolBinarioBusqueda()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("Recorrido en preorden:")
arbol.recorrido_preorden(arbol.raiz)
print("\nRecorrido en orden:")
arbol.recorrido_en_orden(arbol.raiz)
print("\nRecorrido en postorden:")
arbol.recorrido_postorden(arbol.raiz)
