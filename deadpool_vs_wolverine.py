"""
/*
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */
"""
import random
import time

# === FUNCIÓN PARA PEDIR VIDA ===
def pedir_vida(personaje):
    while True:
        try:
            vida = int(input(f"Introduce la vida inicial de {personaje}"))
            if vida > 0:
                return vida
            else:
                print("❌ La vida debe ser mayor que 0.")
        except ValueError:
            print("❌ Error: Solo se permiten números enteros positivos.")

# === FUNCIÓN DE ATAQUE (reutilizable) ===
def realizar_ataque(atacante, defensor, vida_defensor, min_dano, max_dano, prob_evasion, regeneracion_atacante, regeneracion_defensor):
    """
    Realiza un ataque y devuelve la vida actualizada del defensor.
    También actualiza las banderas de regeneración.
    """
    if regeneracion_atacante[0]:  # regeneracion_atacante es una lista para modificar por referencia
        print(f"🛠️ {atacante} se está regenerando y no puede atacar este turno")
        regeneracion_atacante[0] = False
        return vida_defensor
    
    dano = random.randint(min_dano, max_dano)

    # Intento de evasión
    if random.random() < prob_evasion:
        print(f"🛡️ ¡{defensor} esquivó el ataque de {atacante}!")
        return vida_defensor
    else:
        vida_defensor -= dano
        print(f"⚔️ {atacante} ataca con {dano} de daño.")
        
        if vida_defensor < 0:
            print(f"💀 {defensor} ha sido derrotado")
            return vida_defensor
        print(f"❤️ Vida restante de {defensor}: {vida_defensor}")

        # Daño máximo → regeneración del defensor el próximo turno
        if dano == max_dano:
            print(f"¡Golpe crítico de {atacante} a {defensor}! {defensor} debe regenerarse el próximo turno.")
            regeneracion_defensor[0] = True
        return vida_defensor
    
# === INICIO DEL PROGRAMA ===
print("¡Deadpool vs Wolverine - Batalla Épica! ⚔️\n")

vida_deadpool = pedir_vida("Deadpool")
vida_wolverine = pedir_vida("Wolverine")

turno = 1

# Uso listas para poder modificar las banderas dentro de la función
regeneracion_deadpool = [False]
regeneracion_wolverine = [False]

print("\n¡Que comienze la batalla!\n")

while vida_deadpool > 0 and vida_wolverine > 0:
    print(f"\n=== TURNO {turno} ===")

    # Deadpool ataca
    vida_wolverine = realizar_ataque(
        atacante="Deadpool",
        defensor="Wolverine",
        vida_defensor=vida_wolverine,
        min_dano=10,
        max_dano=100,
        prob_evasion=0.20,  # 20% probabilidad de evasión
        regeneracion_defensor=regeneracion_wolverine,
        regeneracion_atacante=regeneracion_deadpool
    )

    if vida_wolverine <= 0:
        break

    # Wolverine ataca
    vida_deadpool = realizar_ataque(
        atacante="Wolverine",
        defensor="Deadpool",
        vida_defensor=vida_deadpool,
        min_dano=10,
        max_dano=120,
        prob_evasion=0.25,  # 25% probabilidad de evasión
        regeneracion_defensor=regeneracion_deadpool,
        regeneracion_atacante=regeneracion_wolverine
    )

    time.sleep(1)
    turno += 1

# === RESULTADO FINAL ===
print("\n" + "="*50)
if vida_deadpool > 0:
    print(f"🏆 ¡DEADPOOL GANA LA BATALLA! 🏆")
    print(f"Vida restante: {vida_deadpool}")
else:
    print(f"🏆 ¡WOLVERINE GANA LA BATALLA! 🏆")
    print(f"Vida restante: {vida_wolverine}")
print("="*50)

