import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Adivina el núnmero - Modo Humillante")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Variables del juego
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 10

        # Mensajes humillantes al perder 
        self.humiliating_messages = [
            "¡Vaya! Ni en 10 intentos... ¿Quieres que te dé las instrucciones en dibujos?",
            "10 intentos y sigues sin acertar. ¿Estás jugando con los ojos cerrados?",
            "El número era obvio y aun así fallaste. Mi abuela lo habría adivinado antes.",
            "¡Impresionante! Has conseguido fallar 10 veces seguidas. Nuevo récord personal.",
            "Felicidades... por nada. El número era más fácil que contar con los dedos.",
            "10 intentos desperdiciados. ¿Quieres que llame a un amigo para que te ayude?",
            "Hasta un niño de 5 años lo habría hecho mejor. ¿Quieres intentarlo de nuevo o rendirte ya?",
            "¡Qué talento para fallar! Deberías dedicarte a otra cosa, amigo.",
            "El ordenador se está riendo de ti ahora mismo. Yo también.",
            "10 intentos y cero aciertos. ¿Estás seguro de que sabes leer números?",
            "Perdiste contra una máquina que solo sabe elegir un número al azar. Reflexiona.",
            "¡Boom! 10 intentos y nada. ¿Quieres que te dé una pista? Demasiado tarde."
        ]

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # Título
        title = tk.Label(self.root, text = "🎲 Adivina el Número 🎲", font = ("Helvetica", 22, "bold"), bg="#f0f0f0", fg="#1e3a8a")
        title.pack(pady=20)
        instruction = tk.Label(self.root, 
                        text="El número secreto está entre 1 y 100.\nTienes máximo 10 intentos.",
                        font=("Helvetica", 12), bg="#f0f0f0", fg="#444", justify="center")
        instruction.pack(pady=10)

        # Campo de entrada
        self.entry = tk.Entry(self.root, font=("Helvetica", 20), justify="center", width=10)
        self.entry.pack(pady=15)
        self.entry.focus()

        # Botón de adivinar
        guess_btn = tk.Button(self.root, text="¡Adivinar!", font=("Helvetica", 14, "bold"),
                             bg="#4CAF50", fg="white", padx=30, pady=12,
                             command=self.check_guess)
        guess_btn.pack(pady=10)

        # Etiqueta de resultado
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"),
                                    bg="#f0f0f0", height=4, width=48, wraplength=450)
        self.result_label.pack(pady=15)

        # Contador de intentos
        self.attempts_label = tk.Label(self.root, text=f"Intentos: 0 / {self.max_attempts}", 
                                      font=("Helvetica", 13, "bold"), bg="#f0f0f0", fg="#333")
        self.attempts_label.pack(pady=8)

        # Barra visual de intentos
        self.progress = tk.Label(self.root, text="██████████", font=("Courier", 16), 
                                bg="#f0f0f0", fg="#4CAF50")
        self.progress.pack(pady=5)

        # Botón Nuevo Juego
        new_game_btn = tk.Button(self.root, text="Nuevo Juego", font=("Helvetica", 12),
                                bg="#2196F3", fg="white", padx=25, pady=10,
                                command=self.new_game)
        new_game_btn.pack(pady=25)

        self.root.bind("<Return>", lambda event: self.check_guess())

    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="¡Nuevo juego iniciado!\n¡Tienes 10 intentos!", fg="#1e3a8a")
        self.attempts_label.config(text=f"Intentos: 0 / {self.max_attempts}", fg="#333")
        self.progress.config(text="██████████", fg="#4CAF50")
        self.entry.focus()

    def update_progress(self):
        remaining = self.max_attempts - self.attempts
        bars = ' ' * remaining + ' ' * (self.max_attempts - remaining)
        color = "#4CAF50" if remaining > 6 else "#FF9800" if remaining > 3 else "#f44336"
        self.progress.config(text=bars, fg=color)

    def get_random_humiliating_messages(self):
        return random.choice(self.humiliating_messages)
    
    def check_guess(self):
        if self.attempts >= self.max_attempts:
            return
        try:
            guess = int(self.entry.get().strip())
            if guess < 1 or guess > 100:
                messagebox.showwarning("Rango incorrecto", "Por favor, ingresa un número entre 1 y 100.")
                self.entry.delete(0, tk.END)
                return
            self.attempts += 1
            self.attempts_label.config(text=f"Intentos: {self.attempts} / {self.max_attempts}")
            self.update_progress()

            if guess == self.secret_number:
                self.result_label.config(text=f"¡🎉 FELICIDADES! 🎉\nAdivinaste el número {self.secret_number}\nen {self.attempts} intentos!", fg="#4CAF50")
                messagebox.showinfo("¡Victoria!", 
                                  f"¡Correcto! El número era {self.secret_number}.\nLo lograste en {self.attempts} intentos.")
                if messagebox.askyesno("Nuevo Juego", "¿Quieres jugar otra vez"):
                    self.new_game()
                else:
                    self.root.quit()
                return

            if guess < self.secret_number:
                hint = "📈 Demasiado bajo\nIntenta con un número más alto"
            else:
                hint = "📉 Demasiado alto\nIntenta con un número más bajo"
            self.result_label.config(text=hint, fg="#FF9800")

            # Si se acabaron los intentos, mensaje humillante
            if self.attempts >= self.max_attempts:
                humiliating_msg = self.get_random_humiliating_messages()
                self.result_label.config(text=f"¡Se acabaron los 10 intentos! 😢\nEl número secreto era {self.secret_number}.", fg="#f44336")
                messagebox.showinfo("¡Derrota Total!", 
                                  f"{humiliating_msg}\n\nEl número secreto era: {self.secret_number}")
                if messagebox.askyesno("Nuevo Juego", "¿Quieres intentarlo de nuevo o prefieres rendirte?"):
                    self.new_game()
                else:
                    self.root.quit()
            self.entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero válido.")
            self.entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

# ========================
# Iniciar el juego
# ========================
if __name__ == "__main__":
    game = NumberGuessingGame();
    game.run()