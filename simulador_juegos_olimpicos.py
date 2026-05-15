"""
* EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
"""



import random


# =============================================================================
# CLASE: Participant
# Representa a un atleta con nombre y país.
# =============================================================================
class Participant:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        """
        Permite comparar dos participantes con el operador ==.
        Dos participantes son iguales si tienen el mismo nombre Y país.
        Esto se usa en: `if participant in self.participants[event]`
        """
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False

    def __hash__(self) -> int:
        """
        Necesario cuando se define __eq__: permite usar el objeto
        en sets o como clave de diccionario.

        BUG ORIGINAL: hash(self.name, self.country) → hash() solo acepta UN argumento.
        CORRECCIÓN:   hash((self.name, self.country)) → se pasa una TUPLA.
        """
        return hash((self.name, self.country))


# =============================================================================
# CLASE: Olympics
# Núcleo del simulador. Gestiona eventos, participantes, resultados y medallero.
# =============================================================================
class Olympics:

    def __init__(self):
        # Lista con los nombres de los eventos registrados. Ej: ["100m lisos", "Natación"]
        self.events = []

        # Diccionario que mapea cada evento a su lista de participantes.
        # Estructura: { "100m lisos": [Participant, Participant, ...], ... }
        self.participants = {}

        # Diccionario que guarda los ganadores de cada evento simulado.
        # Estructura: { "100m lisos": [oro, plata, bronce], ... }
        # Cada valor es una lista de 3 objetos Participant.
        self.event_results = {}

        # Diccionario que acumula el medallero por país.
        # Estructura: { "España": {"gold": 2, "silver": 1, "bronze": 0}, ... }
        self.country_results = {}

    # -------------------------------------------------------------------------
    # Método: register_event
    # Pide un nombre de evento y lo añade a la lista si no existe ya.
    # -------------------------------------------------------------------------
    def register_event(self):
        event = input("Introduce el nombre del evento deportivo: ").strip()

        # Comprobación de duplicados: no se permite registrar el mismo evento dos veces.
        if event in self.events:
            print(f"El evento {event} ya está registrado.")
        else:
            self.events.append(event)
            print(f"Evento {event} registrado correctamente.")

    # -------------------------------------------------------------------------
    # Método: register_participant
    # Pide datos del participante, muestra los eventos disponibles y lo asigna
    # al evento elegido por el usuario.
    # -------------------------------------------------------------------------
    def register_participant(self):

        if not self.events:
            print("No hay eventos registrados. Por favor, registra uno primero.")
            return

        name = input("Introduce el nombre del participante: ").strip()
        country = input("Introduce el país del participante: ").strip()

        # Creamos el objeto Participant con los datos introducidos.
        participant = Participant(name, country)

        # Mostramos el listado numerado de eventos para que el usuario elija.
        print("Eventos deportivos disponibles:")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")

        # Restamos 1 al input para convertir el número visible (1, 2, 3...)
        # en un índice de lista (0, 1, 2...).
        event_choice = int(
            input("Selecciona el número del evento para asignar al participante: ")) - 1

        # Validamos que el índice esté dentro del rango de la lista.
        if 0 <= event_choice < len(self.events):

            event = self.events[event_choice]

            # Comprobamos si el participante ya está inscrito en ese evento.
            # Funciona gracias a __eq__: compara nombre y país.
            if event in self.participants and participant in self.participants[event]:
                print(
                    f"El participante {name} de {country} ya está registrado en el evento deportivo {event}.")
            else:
                # Si el evento aún no tiene ningún participante, inicializamos su lista.
                if event not in self.participants:
                    self.participants[event] = []

                self.participants[event].append(participant)
                print(
                    f"El participante {name} de {country} se ha registrado en el evento deportivo {event}.")
        else:
            print(
                "Selección de evento deportivo inválido. El participante no se ha registrado.")

    # -------------------------------------------------------------------------
    # Método: simulate_events
    # Recorre todos los eventos registrados y simula el resultado de cada uno
    # eligiendo 3 participantes al azar y asignándoles medallas.
    # -------------------------------------------------------------------------
    def simulate_events(self):

        if not self.events:
            print("No hay eventos registrados. Por favor, registra uno primero.")
            return

        for event in self.events:

            # BUG ORIGINAL: self.participants[event] lanzaba KeyError si el evento
            # no tenía participantes inscritos.
            # CORRECCIÓN: usamos .get() que devuelve [] por defecto si no existe la clave.
            event_participants = self.participants.get(event, [])

            # El requisito exige mínimo 3 participantes para poder simular.
            if len(event_participants) < 3:
                print(
                    f"No hay participantes suficientes para simular el evento {event} (mínimo 3).")
                continue

            # random.sample(lista, 3) → elige 3 elementos sin repetición al azar.
            # random.shuffle(lista)   → baraja los 3 elegidos (añade otra capa de aleatoriedad).
            selected = random.sample(event_participants, 3)
            random.shuffle(selected)

            # Desempaquetado directo: el primer elemento es oro, el segundo plata, el tercero bronce.
            gold, silver, bronze = selected

            # Guardamos los resultados del evento en el diccionario.
            self.event_results[event] = [gold, silver, bronze]

            # Actualizamos el medallero global de países.
            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"\nResultados simulación del evento: {event}")
            print(f"  Oro:    {gold.name} ({gold.country})")
            print(f"  Plata:  {silver.name} ({silver.country})")
            print(f"  Bronce: {bronze.name} ({bronze.country})")

    # -------------------------------------------------------------------------
    # Método: update_country_results
    # Incrementa en 1 el contador de la medalla indicada para el país dado.
    # Se llama desde simulate_events tras conocer los ganadores.
    # -------------------------------------------------------------------------
    def update_country_results(self, country, medal):
        # Si el país no aparece aún en el medallero, lo inicializamos a cero en las tres medallas.
        if country not in self.country_results:
            self.country_results[country] = {"gold": 0, "silver": 0, "bronze": 0}

        # Incrementamos la medalla correspondiente.
        self.country_results[country][medal] += 1

    # -------------------------------------------------------------------------
    # Método: show_report
    # Muestra dos informes: resultados por evento y ranking de países.
    # -------------------------------------------------------------------------
    def show_report(self):

        print("\n===== Informe Juegos Olímpicos =====")

        # --- Informe por evento ---
        if self.event_results:
            print("\n📋 Informe por evento:")
            for event, winners in self.event_results.items():
                print(f"\n  Evento: {event}")
                print(f"    🥇 Oro:    {winners[0].name} ({winners[0].country})")
                print(f"    🥈 Plata:  {winners[1].name} ({winners[1].country})")
                print(f"    🥉 Bronce: {winners[2].name} ({winners[2].country})")
        else:
            print("No hay resultados registrados.")

        print()

        # --- Ranking de países ---
        if self.country_results:
            print("🌍 Ranking por país:")

            # sorted() ordena el diccionario por una clave compuesta (lambda).
            # La lambda devuelve una tupla (oros, platas, bronces) de cada país.
            # reverse=True → de mayor a menor (el más medallado primero).
            # Python compara tuplas elemento a elemento, por lo que el orden de prioridad es:
            #   1º oros → 2º platas → 3º bronces.
            ranking = sorted(
                self.country_results.items(),
                key=lambda x: (x[1]["gold"], x[1]["silver"], x[1]["bronze"]),
                reverse=True
            )

            for position, (country, medals) in enumerate(ranking, start=1):
                print(
                    f"  {position}. {country}: "
                    f"🥇 {medals['gold']}  "
                    f"🥈 {medals['silver']}  "
                    f"🥉 {medals['bronze']}"
                )
        else:
            print("No hay medallas por país registradas.")


# =============================================================================
# PROGRAMA PRINCIPAL
# Crea la instancia de Olympics y lanza el bucle interactivo.
# =============================================================================
olympics = Olympics()

print("🏅 Simulador de Juegos Olímpicos París 2024")

# Bucle infinito que solo termina cuando el usuario elige la opción 5.
while True:

    print("\n--- Menú ---")
    print("1. Registro de eventos")
    print("2. Registro de participantes")
    print("3. Simulación de eventos")
    print("4. Creación de informes")
    print("5. Salir")

    option = input("Selecciona una acción: ")

    # match/case: disponible desde Python 3.10.
    # Equivalente al switch de otros lenguajes.
    # El caso _ es el "default": captura cualquier opción no listada.
    match option:
        case "1":
            olympics.register_event()
        case "2":
            olympics.register_participant()
        case "3":
            olympics.simulate_events()
        case "4":
            olympics.show_report()
        case "5":
            print("Saliendo del simulador... ¡Hasta los próximos JJOO!")
            break
        case _:
            print("Opción inválida. Por favor, selecciona una nueva.")