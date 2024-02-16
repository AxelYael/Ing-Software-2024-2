"""
Este script deberá de emular el comportamiento de un marcador de un partido de tenis
"""
class MarcadorTenis:
    def __init__(self, sets_a_ganar, nombres_jugadores):
        self.sets_a_ganar = sets_a_ganar
        self.nombres_jugadores = nombres_jugadores
        self.marcador_sets = [0, 0]  # [Jugador 1, Jugador 2]
        self.marcador_juegos = [0, 0]  # [Jugador 1, Jugador 2]
        self.jugador_con_ventaja = None
        self.saque_jugador = 0  
        self.total_juegos = 0 

    def punto_para_jugador(self, jugador):
        otro_jugador = 1 - jugador
        if self.jugador_con_ventaja is not None:
            # Si un jugador tiene ventaja, y el otro hace punto, se iguala
            if jugador == self.jugador_con_ventaja:
                self.jugador_con_ventaja = None
            else:
                self.marcador_juegos[otro_jugador] -= 1
        else:
            # Si están empatados en 40, el que hace punto tiene ventaja
            if self.marcador_juegos[jugador] == 3 and self.marcador_juegos[otro_jugador] == 3:
                self.jugador_con_ventaja = jugador

        # Hacer el punto
        self.marcador_juegos[jugador] += 1
        self.total_juegos += 1

        # Verificar si se ha ganado un juego
        if self.marcador_juegos[jugador] >= 4 and self.marcador_juegos[jugador] - self.marcador_juegos[otro_jugador] >= 2:
            self.marcador_juegos = [0, 0]  
            self.marcador_sets[jugador] += 1  
            self.saque_jugador = otro_jugador  
            self.total_juegos = 0  
            print(f"¡{self.nombres_jugadores[jugador]} gana el set {sum(self.marcador_sets)}!")
            print()
         

        # Verificar si se ha ganado un set
        if max(self.marcador_sets) == self.sets_a_ganar:
            print("¡Partido terminado!")
            print(f"Marcador final: {self.nombres_jugadores[0]} vs {self.nombres_jugadores[1]} => {self.marcador_sets[0]} sets - {self.marcador_sets[1]} sets")
            return True  # El partido ha terminado

        # Verificar si se debe realizar cambio de cancha
        if self.total_juegos % 2 != 0:
            print("CAMBIO DE CANCHA.")

        return False  # El partido aún no ha terminado

    def obtener_marcador(self):
        if self.jugador_con_ventaja is not None:
            marcador_jugador_con_ventaja = "Adv."
            marcador_otro_jugador = "40"
        else:
            marcador_jugador_con_ventaja = "40" if self.marcador_juegos[0] == 3 else str(self.marcador_juegos[0] * 15)
            marcador_otro_jugador = "40" if self.marcador_juegos[1] == 3 else str(self.marcador_juegos[1] * 15)

        return f"{self.nombres_jugadores[0]}: {marcador_jugador_con_ventaja} - {marcador_otro_jugador} :{self.nombres_jugadores[1]}, Saque: {self.nombres_jugadores[self.saque_jugador]}"


while True:
    try:
        sets_a_ganar = int(input("Ingresa el número impar de sets a jugar: "))
        if sets_a_ganar % 2 != 1:
            raise ValueError("El número de sets debe ser impar.")
        break
    except ValueError as ve:
        print(f"Error: {ve}")

nombres_jugadores = []
for i in range(2):
    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    nombres_jugadores.append(nombre)



# Main
partido = MarcadorTenis(sets_a_ganar, nombres_jugadores)
print(f"Empieza el set 1 de {sets_a_ganar}")

while True:
    try:
        print("Marcador actual:", partido.obtener_marcador())
        ganador = int(input("¿Quién gana el punto? (1 para el primer jugador, 2 para el segundo jugador): ")) - 1
        if partido.punto_para_jugador(ganador):
            break
    except KeyboardInterrupt:
        print("\n¡Partida interrumpida!")
        break
    except Exception as e:
        print(f"Error: {e}. Por favor, intenta de nuevo.")
