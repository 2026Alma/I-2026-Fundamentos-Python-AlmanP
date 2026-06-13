class Seleccion:
    def __init__(self, pais, confederacion):
        self.confederacion = confederacion
        self.jugadores = []
        self.pais = pais
    def agregrar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def eliminar_jugador(self, jugador):
        for jugador_en_lista in self.jugadores:
            if jugador_en_lista == jugador:
                self.jugadores.remove(jugador_en_lista)
                break

