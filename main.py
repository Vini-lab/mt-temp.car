import tkinter as tk
from tkinter import messagebox
from evaluacion import evaluar_temperatura

# Función para manejar el botón de evaluación
def manejar_evaluacion():
    try:
        # Convertir la temperatura a un número
        temperatura = float(entry_temperatura.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico para la temperatura.")
        return

    tipo_vehiculo = tipo_vehiculo_var.get()
    resultado, sugerencia = evaluar_temperatura(temperatura, tipo_vehiculo)
    
    # Mostrar el resultado en la interfaz
    resultado_var.set(resultado)
    sugerencia_var.set(sugerencia)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Interpretador de Temperaturas para Vehículos")
root.configure(bg="#f0f0f0")  # Fondo de la ventana principal

# Variables de control
tipo_vehiculo_var = tk.StringVar(value="Carro Pequeño")
resultado_var = tk.StringVar(value="")
sugerencia_var = tk.StringVar(value="")

# Etiquetas y campos de entrada
tk.Label(root, text="Temperatura (°C):", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_temperatura = tk.Entry(root, font=("Arial", 12))
entry_temperatura.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Tipo de Vehículo:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tipo_vehiculo_menu = tk.OptionMenu(root, tipo_vehiculo_var, "Carro Pequeño", "Camioneta")
tipo_vehiculo_menu.config(font=("Arial", 12))
tipo_vehiculo_menu.grid(row=1, column=1, padx=10, pady=10)

# Botón de evaluación
boton_evaluar = tk.Button(root, text="Evaluar Temperatura", command=manejar_evaluacion, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
boton_evaluar.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Resultados
tk.Label(root, text="Resultado:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="e")
resultado_label = tk.Label(root, textvariable=resultado_var, font=("Arial", 12), fg="#4CAF50")
resultado_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Sugerencia:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10, sticky="e")
sugerencia_label = tk.Label(root, textvariable=sugerencia_var, font=("Arial", 12), fg="#FF5733", wraplength=250, justify="left")
sugerencia_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Ejecutar la interfaz
root.mainloop()
