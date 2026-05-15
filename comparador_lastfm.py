"""
🎵 Ejercicio: El Comparador Musical Pro
Contexto
Cuatro artistas de estilos muy diferentes (LP, Thy Art is Murder, Bad Bunny y Swallow the Sun) han anunciado que salen de gira. Tu misión es determinar quién es el más popular utilizando datos reales para ayudar a un promotor de conciertos a decidir a quién darle el escenario principal.

Requisitos Técnicos
Registro de Desarrollador: Crea una cuenta en Last.fm API y obtén tu API_KEY.

Conexión: Utiliza la librería requests de Python para conectarte al endpoint artist.getinfo.

Gestión de Errores: El programa debe ser capaz de gestionar nombres con espacios y evitar cerrarse si un artista no es encontrado o si la API devuelve un error.

Acciones del Programa
Recuperación de Datos: Para cada artista, debes obtener al menos 3 tipos de datos distintos:

Número total de oyentes (listeners).

Número total de reproducciones (playcount).

Género musical principal (tags).

Procesamiento:

Convierte los datos numéricos (que vienen como texto) a números enteros (int) para poder operar con ellos.

Limpia la respuesta para quedarte solo con la información útil.

Visualización: Muestra por consola los resultados de forma elegante, usando separadores de miles para que los números sean legibles.

El Veredicto:

Establece un criterio de victoria (por ejemplo, mayor número de oyentes únicos).

Haz que Python compare automáticamente los resultados y proclame a un ganador.
"""

import requests

# --- CONFIGURACIÓN ---
API_KEY = "2e41833aff35ef3ac7e5382d4fa010af"
ARTISTAS = ["LP", "Thy Art is Murder", "Bad Bunny", "Swallow the Sun"]

def obtener_datos_lastfm(nombre_artista):
    url = "http://ws.audioscrobbler.com/2.0/"
    # Usar 'params' es la clave para evitar el KeyError
    parametros = {
        'method': 'artist.getinfo',
        'artist': nombre_artista,
        'api_key': API_KEY,
        'format': 'json'
    }

    try:
        respuesta = requests.get(url, params=parametros)
        datos = respuesta.json()
        
        # Si la API responde pero con un error (ej: artista no encontrado)
        if 'error' in datos:
            print(f"⚠️ Last.fm dice: {datos['message']} ({nombre_artista})")
            return None
            
        info = datos['artist']
        return {
            "nombre": info['name'],
            "oyentes": int(info['stats']['listeners']),
            "plays": int(info['stats']['playcount']),
            "genero": info['tags']['tag'][0]['name'] if info['tags']['tag'] else "Sin género"
        }
    except Exception as e:
        print(f"❌ Error inesperado con {nombre_artista}: {e}")


# --- EJECUCIÓN ---
print("--- 📊 COMPARATIVA DE POPULARIDAD ---")
resultados = []

for a in ARTISTAS:
    dato = obtener_datos_lastfm(a)
    if dato:
        resultados.append(dato)
        print(f"✅ {dato['nombre']} recuperado.")

if resultados:
    print("\n--- RESULTADOS FINALES ---")
    for art in resultados:
        print(f"⭐ {art['nombre']} [{art['genero'].upper()}]")
        print(f"   👥 Oyentes: {art['oyentes']:,} | 🎧 Plays: {art['plays']:,}\n")

    ganador = max(resultados, key=lambda x: x['oyentes'])
    print(f"🏆 GANADOR: {ganador['nombre']} con {ganador['oyentes']:,} oyentes.")
else:
    print("❌ No se pudo obtener información de ningún artista.")

