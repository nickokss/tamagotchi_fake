import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Hipopotamo:
    def __init__(self):
        self.hambre = 0
        self.sueño = 0
        self.higiene = 0
        self.aburrimiento = 0

    def incrementar_estadisticas(self):
        # Ajusta las tasas de incremento según tus preferencias
        self.hambre += 0.05
        self.sueño += 0.02
        self.higiene += 0.03
        self.aburrimiento += 0.04

        # Verifica si alguna estadística ha alcanzado su máximo
        if self.hambre >= 1.0:
            accion = input("¡El hipopótamo está muy hambriento! Aliméntalo.(Pulsa A luego Enter):")
            self.hambre = 1.0
            if accion == 'a':
                hipopotamo.reiniciar_hambre()       

        if self.sueño >= 1.0:
            accion = input("¡El hipopótamo está muy cansado! Dale un descanso.(Pulsa S luego Enter):")
            self.sueño = 1.0
            if accion == 's':
                hipopotamo.reiniciar_sueño()   

        if self.higiene >= 1.0:
            accion = input("¡El hipopótamo necesita bañarse! Dale un buen baño.(Pulsa B luego Enter):")
            self.higiene = 1.0
            if accion == 'b':
                hipopotamo.reiniciar_higiene()  

        if self.aburrimiento >= 1.0:
            accion = input("¡El hipopótamo está aburrido! Juega con él.(Pulsa J luego Enter):")
            self.aburrimiento = 1.0
            if accion == 'j':
                hipopotamo.reiniciar_aburrimiento()  

    def reiniciar_hambre(self):
        print("El hipopótamo está comiendo...")
        time.sleep(3)  # Simulación de tiempo de alimentación
        self.hambre = 0

    def reiniciar_sueño(self):
        print("El hipopótamo está descansando...")
        time.sleep(3)  # Simulación de tiempo de descanso
        self.sueño = 0

    def reiniciar_higiene(self):
        print("El hipopótamo está tomando un baño...")
        time.sleep(3)  # Simulación de tiempo de baño
        self.higiene = 0

    def reiniciar_aburrimiento(self):
        print("El hipopótamo está jugando...")
        time.sleep(3)  # Simulación de tiempo de juego
        self.aburrimiento = 0

    def mostrar_stats(self):
        print(f"Hambre: {self.hambre:.2f}")
        print(f"Sueño: {self.sueño:.2f}")
        print(f"Higiene: {self.higiene:.2f}")
        print(f"Aburrimiento: {self.aburrimiento:.2f}")

# Arte ASCII para el Tamagotchi con forma de hipopótamo
tamagotchi_art_1 = '''
     |\_/| 
    / ^ ^ \\
   ( >   < )
    '>>-<<'
     / O \\
   
'''
tamagotchi_art_2 = '''
     |\_/| 
    / O O \\
   ( >   < )
    '>>-<<'
     / O \\
   
'''

def mostrar_animacion(hipopotamo):
    while True:
        hipopotamo.incrementar_estadisticas()
        clear_screen()
        hipopotamo.mostrar_stats()
        print(tamagotchi_art_1)
        time.sleep(0.5)

        hipopotamo.incrementar_estadisticas()
        clear_screen()
        hipopotamo.mostrar_stats()
        print(tamagotchi_art_2)
        time.sleep(0.5)       
        

if __name__ == "__main__":
    hipopotamo = Hipopotamo()
    mostrar_animacion(hipopotamo)
