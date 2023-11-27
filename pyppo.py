import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pyppo:
    def __init__(self):
        self.hambre = 0
        self.sueño = 0
        self.higiene = 0
        self.aburrimiento = 0
        
        self.tamagotchi_art = {
            'comiendo': '''
     |\_/| 
    / G G \\
   ( >   < )
    '>>-<<'    ,,
     / O \\    -__-
            ''',
            'descansando': '''
     |\_/| 
    / - - \\ zzZZ
   ( >   < )
    '>>-<<'
     / O \\
            ''',
            'bañandose': '''
     |\_/| 
    / ~ ~ \\
   ( >   < )
    '>>-<<'
     / O \\
            ''',
            'jugando': '''
     |\_/| 
    / 0 0 \\
   ( >   < ) O
    '>>-<<'  O
     / O \\   |
            '''
        }

        self.arte_actual = None

    def incrementar_estadisticas(self):
        # Ajusta las tasas de incremento según tus preferencias
        self.hambre += 0.02
        self.sueño += 0.001
        self.higiene += 0.006
        self.aburrimiento += 0.008

       
    def reiniciar_hambre(self):
        accion = input("¡Pyppo está muy hambriento! Aliméntalo. (Pulsa A luego Enter): ")
        while accion.lower() != 'a':
            accion = input("Tecla incorrecta. Pulsa A para alimentar a Pyppo: ")   
        clear_screen()
        pyppo.mostrar_stats()
        self.cambiar_arte('comiendo')
        print(self.arte_actual)   
        print("Pyppo está comiendo...")
        time.sleep(6)  # Simulación de tiempo de alimentación
        self.hambre = 0
        clear_screen()

    def reiniciar_sueño(self):
        accion = input("¡Pyppo está muy cansado! Dale un descanso. (Pulsa S luego Enter): ")
        while accion.lower() != 's':
            accion = input("Tecla incorrecta. Pulsa S para darle un descanso a Pyppo: ")
        clear_screen()
        pyppo.mostrar_stats()
        self.cambiar_arte('descansando')
        print(self.arte_actual)    
        print("Pyppo está descansando...")
        time.sleep(17)  # Simulación de tiempo de descanso
        self.sueño = 0
        clear_screen()

    def reiniciar_higiene(self):
        accion = input("¡Pyppo necesita bañarse! Dale un buen baño. (Pulsa B luego Enter): ")
        while accion.lower() != 'b':
            accion = input("Tecla incorrecta. Pulsa B para bañar a Pyppo: ")
        clear_screen()
        pyppo.mostrar_stats()
        self.cambiar_arte('bañandose')
        print(self.arte_actual)   
        print("Pyppo está tomando un baño...")
        time.sleep(8)  # Simulación de tiempo de baño
        self.higiene = 0
        clear_screen()

    def reiniciar_aburrimiento(self):
        accion = input("¡Pyppo está aburrido! Juega con él. (Pulsa J luego Enter): ")
        while accion.lower() != 'j':
            accion = input("Tecla incorrecta. Pulsa J para jugar con Pyppo: ")
        clear_screen()
        pyppo.mostrar_stats()
        self.cambiar_arte('jugando')
        print(self.arte_actual)   
        print("Pyppo está jugando...")
        time.sleep(6)  # Simulación de tiempo de juego
        self.aburrimiento = 0
        clear_screen()

    def mostrar_stats(self):
        print("----- PYPPO -----")
        print("Hambre:  ", self.get_bar(self.hambre))
        print("Sueño :  ", self.get_bar(self.sueño))
        print("Higiene: ", self.get_bar(self.higiene))
        print("Jugar:   ", self.get_bar(self.aburrimiento))
        
    def mostrar_arte(self):
        if self.hambre >= 1.0:
            pyppo.mostrar_stats()
            print(tamagotchi_art_3)
            self.reiniciar_hambre()
        elif self.sueño >= 1.0:
            pyppo.mostrar_stats()
            print(tamagotchi_art_3)
            self.reiniciar_sueño()
        elif self.higiene >= 1.0:
            pyppo.mostrar_stats()
            print(tamagotchi_art_3)
            self.reiniciar_higiene()
        elif self.aburrimiento >= 1.0:
            pyppo.mostrar_stats()
            print(tamagotchi_art_3)
            self.reiniciar_aburrimiento()
        else:
            pyppo.mostrar_stats()
            print(tamagotchi_art_1)
            time.sleep(0.5)
            clear_screen()
            pyppo.mostrar_stats()
            print(tamagotchi_art_2)
            time.sleep(0.5)
            clear_screen()

    def cambiar_arte(self, accion):
        self.arte_actual = self.tamagotchi_art.get(accion, None)
        
    def get_bar(self, value):
        bar_length = 20
        bar_fill = int(bar_length * value)
        return "[" + "=" * bar_fill + " " * (bar_length - bar_fill) + "]"

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
tamagotchi_art_3 = '''
     |\_/|  ????
    / _ _ \\
   ( >   < )
    '>>-<<'
     / O \\
   
'''
def mostrar_animacion(pyppo):
    while True:
        pyppo.incrementar_estadisticas()
        pyppo.mostrar_arte()

if __name__ == "__main__":
    pyppo = Pyppo()
    mostrar_animacion(pyppo)
