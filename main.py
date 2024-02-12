import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

class GameInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego de Habilidades Lingüísticas")
        self.configure(bg="#FFCC66")  # Fondo amarillo claro

        # Obteniendo las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Definiendo las dimensiones de la ventana (la mitad del tamaño de la pantalla)
        window_width = screen_width // 2
        window_height = screen_height // 2
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.category_label = tk.Label(self, text="Selecciona una categoría:", bg="#FFCC66", fg="#333333", font=("Arial", 14))
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_var.set("")

        self.button_width = 120  # Ancho fijo para todos los botones
        self.button_height = 120  # Alto fijo para todos los botones

        self.aseo_image_path = os.path.join("images", "aseo_image.png")
        self.aseo_image = Image.open(self.aseo_image_path)
        self.aseo_image.thumbnail((self.button_width - 20, self.button_height - 40))  # Redimensionar la imagen
        self.aseo_image = ImageTk.PhotoImage(self.aseo_image)  # Convertir la imagen a PhotoImage
        self.aseo_button = tk.Button(self, text="Útiles de Aseo", image=self.aseo_image, compound="top", command=lambda: self.select_category("aseo"), bg="#FF9966", fg="white", font=("Arial", 12), width=self.button_width, height=self.button_height)
        self.aseo_button.pack(pady=5)

        self.transport_image_path = os.path.join("images", "transport_image.png")
        self.transport_image = Image.open(self.transport_image_path)
        self.transport_image.thumbnail((self.button_width - 20, self.button_height - 40))  # Redimensionar la imagen
        self.transport_image = ImageTk.PhotoImage(self.transport_image)  # Convertir la imagen a PhotoImage
        self.transport_button = tk.Button(self, text="Medios de\nTransporte", image=self.transport_image, compound="top", command=lambda: self.select_category("transporte"), bg="#6699FF", fg="white", font=("Arial", 12), width=self.button_width, height=self.button_height)
        self.transport_button.pack(pady=5)

        # Calcular el nuevo ancho para el botón de salir
        close_button_width = int(self.button_width * 0.080)

        self.close_button = tk.Button(self, text="Salir", command=self.quit_application, bg="#FF0000", fg="white", font=("Arial", 10), width=close_button_width, height=1)
        self.close_button.pack(pady=5)

    def select_category(self, category):
        self.category_var.set(category)
        selected_category = self.category_var.get()
        if selected_category == "":
            messagebox.showerror("Error", "Por favor, selecciona una categoría antes de continuar.")
        else:
            if selected_category == "aseo":
                self.withdraw()  # Oculta la ventana actual antes de abrir una nueva
                self.difficulty_window = DifficultySelection(selected_category, self)
                self.difficulty_window.grab_set()  # Evita que se interactúe con la ventana principal
                self.difficulty_window.protocol("WM_DELETE_WINDOW", self.show_window)  # Define la acción al cerrar la ventana secundaria
                self.difficulty_window.mainloop()
            else:
                messagebox.showinfo("Info", "Funcionalidad para esta categoría aún no implementada.")

    def show_window(self):
        self.deiconify()  # Muestra la ventana principal nuevamente

    def quit_application(self):
        self.destroy()

class DifficultySelection(tk.Toplevel):
    def __init__(self, category, parent):
        super().__init__()
        self.title("Selección de Dificultad")
        self.configure(bg="#66FF99")  # Fondo verde claro
        self.category = category
        self.parent = parent  # Referencia a la ventana principal

        # Obteniendo las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Definiendo las dimensiones de la ventana (la mitad del tamaño de la pantalla)
        window_width = screen_width // 2
        window_height = screen_height // 2
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.difficulty_label = tk.Label(self, text="Selecciona el nivel de dificultad:", bg="#66FF99", fg="#333333", font=("Arial", 14))
        self.difficulty_label.pack()

        self.easy_button = tk.Button(self, text="Fácil", command=self.start_game_easy, bg="#FF6666", fg="white", font=("Arial", 12))
        self.easy_button.pack(pady=5)

        self.medium_button = tk.Button(self, text="Medio (Bloqueado)", state="disabled", bg="#FF6666", fg="white", font=("Arial", 12))
        self.medium_button.pack(pady=5)

        self.hard_button = tk.Button(self, text="Difícil (Bloqueado)", state="disabled", bg="#FF6666", fg="white", font=("Arial", 12))
        self.hard_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Atrás", command=self.back_to_category_selection, bg="#6699FF", fg="white", font=("Arial", 12))
        self.back_button.pack(pady=5)

    def start_game_easy(self):
        self.withdraw()  # Oculta la ventana actual antes de abrir una nueva
        self.bathroom_window = BathroomScene(self.parent)
        self.bathroom_window.grab_set()  # Evita que se interactúe con la ventana principal
        self.bathroom_window.protocol("WM_DELETE_WINDOW", self.show_window)  # Define la acción al cerrar la ventana secundaria
        self.bathroom_window.mainloop()

    def show_window(self):
        self.deiconify()  # Muestra la ventana principal nuevamente

    def back_to_category_selection(self):
        self.destroy()  # Cierra la ventana secundaria
        self.parent.deiconify()  # Muestra la ventana principal nuevamente

class BathroomScene(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title("Escena del Baño")
        self.configure(bg="white")  # Fondo blanco
        self.parent = parent

        # Obteniendo las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Definiendo las dimensiones de la ventana (la mitad del tamaño de la pantalla)
        window_width = screen_width // 2
        window_height = screen_height // 2
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.bathroom_image_path = os.path.join("images", "bathroom_scene.png")
        self.bathroom_image = Image.open(self.bathroom_image_path)
        self.bathroom_image = ImageTk.PhotoImage(self.bathroom_image)  # Convertir la imagen a PhotoImage

        self.bathroom_label = tk.Label(self, image=self.bathroom_image)
        self.bathroom_label.pack()

        # Útiles de aseo
        self.toothpaste_button = tk.Button(self, text="Crema Dental", bg="#FFFFFF", fg="#000000", font=("Arial", 12), command=lambda: self.select_util("crema_dental"))
        self.toothpaste_button.place(x=50, y=50)

        self.soap_button = tk.Button(self, text="Jabón de Mano", bg="#FFFFFF", fg="#000000", font=("Arial", 12), command=lambda: self.select_util("jabon_mano"))
        self.soap_button.place(x=200, y=200)

        self.towel_button = tk.Button(self, text="Toalla", bg="#FFFFFF", fg="#000000", font=("Arial", 12), command=lambda: self.select_util("toalla"))
        self.towel_button.place(x=350, y=350)

    def select_util(self, util):
        # Simulamos una pregunta aleatoria asociada al útil de aseo seleccionado
        questions = {
            "crema_dental": ["¿Para qué se utiliza este objeto?", "¿Cómo se llama este objeto en inglés?"],
            "jabon_mano": ["¿Cómo se usa este objeto?", "¿Qué olor tiene este objeto?"],
            "toalla": ["¿Para qué se utiliza este objeto?", "¿De qué material está hecho este objeto?"]
        }
        selected_question = random.choice(questions[util])
        messagebox.showinfo("Pregunta", selected_question)
        self.parent.show_window()

if __name__ == "__main__":
    app = GameInterface()
    app.mainloop()