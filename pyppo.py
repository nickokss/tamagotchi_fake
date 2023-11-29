import os
import time
import threading 
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pyppo:
    def __init__(self):
        self.hambre = 0
        self.sueño = 0
        self.higiene = 0
        self.aburrimiento = 0
        self.vidas = ["\u2665", "\u2665", "\u2665", "\u2665"]
        self.ultima_actividad = time.time()
        self.tiempo_inicio = time.time()
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
   ( >   < )  />
    '>>-<<' \\__/
~~~~~/ O \\~~~~~
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
        self.hambre += 0.01
        self.sueño += 0.001
        self.higiene += 0.004
        self.aburrimiento += 0.008

    def contar_tiempo(self):
        while len(self.vidas) != 0:  # Continuar hasta que no haya más vidas
            tiempo_transcurrido = 0

            while tiempo_transcurrido <= 600: #600 segundos (10 minutos)
                time.sleep(1)
                tiempo_transcurrido += 1

            if self.hambre >= 1.0:
                self.vidas.pop(0)
                clear_screen()
                self.mostrar_stats()
                print(tamagotchi_art_3)
                print("¡Pyppo está muy hambriento! Aliméntalo. (Pulsa A luego Enter): ")
            if self.sueño >= 1.0:
                self.vidas.pop(0)
                clear_screen()
                self.mostrar_stats()
                print(tamagotchi_art_3)
                print("¡Pyppo está muy cansado! Dale un descanso. (Pulsa S luego Enter): ")
            if self.higiene >= 1.0:
                self.vidas.pop(0)
                clear_screen()
                self.mostrar_stats()
                print(tamagotchi_art_3)
                print("¡Pyppo necesita bañarse! Dale un buen baño. (Pulsa B luego Enter): ")
            if self.aburrimiento >= 1.0:
                self.vidas.pop(0)
                clear_screen()
                self.mostrar_stats()
                print(tamagotchi_art_3)
                print("¡Pyppo está aburrido! Juega con él. (Pulsa J luego Enter): ")
        clear_screen()
        print("PYPPO SE HA MUERTO.")
        print(tamagotchi_art_4) 
        tiempo_transcurrido_total = time.time() - self.tiempo_inicio
        dias, segundos_totales = divmod(tiempo_transcurrido_total, 86400)
        horas, segundos_totales = divmod(segundos_totales, 3600)
        minutos, segundos = divmod(segundos_totales, 60)
        print(f"Lo has cuidado durante {int(dias)} días, {int(horas)} horas y {int(minutos)} minutos.")       
        print("Para salir, pulsa Ctrl+Z (o Ctrl+C en algunos sistemas).")
        
        try:
            # Esperar a que el usuario presione Ctrl+Z
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            sys.exit()            

    def reiniciar_hambre(self):
        accion = input("¡Pyppo está muy hambriento! Aliméntalo. (Pulsa A luego Enter): ")
        while accion.lower() != 'a':
            accion = input("Tecla incorrecta. Pulsa A para darle comida a Pyppo: ")
        clear_screen()
        self.vidas = ["\u2665", "\u2665", "\u2665", "\u2665"]
        self.mostrar_stats()
        self.cambiar_arte('comiendo')
        print(self.arte_actual)
        print("Pyppo está comiendo...")
        time.sleep(6)
        self.hambre = 0
        clear_screen()
        

    def reiniciar_sueño(self):
        accion = input("¡Pyppo está muy cansado! Dale un descanso. (Pulsa S luego Enter): ")
        while accion.lower() != 's':
            accion = input("Tecla incorrecta. Pulsa S para darle un descanso a Pyppo: ")
        clear_screen()
        self.vidas = ["\u2665", "\u2665", "\u2665", "\u2665"]
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
        self.vidas = ["\u2665", "\u2665", "\u2665", "\u2665"]
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
        self.vidas = ["\u2665", "\u2665", "\u2665", "\u2665"]
        pyppo.mostrar_stats()
        self.cambiar_arte('jugando')
        print(self.arte_actual)   
        print("Pyppo está jugando...")
        time.sleep(6)  # Simulación de tiempo de juego
        self.aburrimiento = 0
        clear_screen()

    def mostrar_stats(self):
        print("PYPPO:   ", self.vidas)
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

# Arte ASCII para el Tamagochi
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
tamagotchi_art_4 = '''
     |\_/|  
    / x x \\
   ( > o < )
    '>>-<<'
     / O \\
   
'''
def mostrar_animacion(pyppo):
    while True:
        pyppo.incrementar_estadisticas()
        pyppo.mostrar_arte()

if __name__ == "__main__":
    pyppo = Pyppo()
    # Iniciar hilo para contar tiempo
    hilo_tiempo = threading.Thread(target=pyppo.contar_tiempo)
    hilo_tiempo.start()

    # Mostrar animación en el hilo principal
    mostrar_animacion(pyppo)

    # Esperar a que el hilo de tiempo termine
    hilo_tiempo.join()
