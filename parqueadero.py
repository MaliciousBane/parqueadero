import tkinter as tk

class RegistroVehiculos:
    def __init__(self):
        self.vehiculos = []  # Lista para almacenar los vehículos
        self.ventana = tk.Tk()
        self.ventana.title("Registro de Vehículos")

        # Labels y Entry
        tk.Label(self.ventana, text="Placa:").grid(row=0, column=0)
        self.entry_placa = tk.Entry(self.ventana)
        self.entry_placa.grid(row=0, column=1)

        tk.Label(self.ventana, text="Marca:").grid(row=1, column=0)
        self.entry_marca = tk.Entry(self.ventana)
        self.entry_marca.grid(row=1, column=1)

        tk.Label(self.ventana, text="Color:").grid(row=2, column=0)
        self.entry_color = tk.Entry(self.ventana)
        self.entry_color.grid(row=2, column=1)

        tk.Label(self.ventana, text="Tipo:").grid(row=3, column=0)
        self.tipo_var = tk.StringVar(value="Residente")
        tk.Radiobutton(self.ventana, text="Residente", variable=self.tipo_var, value="Residente").grid(row=3, column=1)
        tk.Radiobutton(self.ventana, text="Visitante", variable=self.tipo_var, value="Visitante").grid(row=3, column=2)

        # Mensaje de validación y registros
        self.label_mensaje = tk.Label(self.ventana, text="", fg="red")
        self.label_mensaje.grid(row=4, column=0, columnspan=2)

        self.label_registros = tk.Label(self.ventana, text="", fg="blue", justify="left")
        self.label_registros.grid(row=7, column=0, columnspan=3)

        # Botones
        tk.Button(self.ventana, text="Guardar", command=self.guardar_vehiculo).grid(row=5, column=0)
        tk.Button(self.ventana, text="Limpiar Campos", command=self.limpiar_campos).grid(row=5, column=1)
        tk.Button(self.ventana, text="Mostrar Registros", command=self.mostrar_registros).grid(row=5, column=2)

        self.ventana.mainloop()

    def guardar_vehiculo(self):
        placa = self.entry_placa.get().strip()
        marca = self.entry_marca.get().strip()
        color = self.entry_color.get().strip()
        tipo = self.tipo_var.get()

        if not placa or not marca or not color:
            self.label_mensaje.config(text="Todos los campos son obligatorios.", fg="red")
            return

        vehiculo = {
            "Placa": placa,
            "Marca": marca,
            "Color": color,
            "Tipo": tipo
        }
        self.vehiculos.append(vehiculo)

        self.label_mensaje.config(text="Vehículo registrado exitosamente.", fg="green")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.label_mensaje.config(text="")

    def mostrar_registros(self):
        if not self.vehiculos:
            self.label_registros.config(text="No hay vehículos registrados.")
            return

        texto = ""
        for vehiculo in self.vehiculos:
            texto += f"Placa: {vehiculo['Placa']}, Marca: {vehiculo['Marca']}, Color: {vehiculo['Color']}, Tipo: {vehiculo['Tipo']}\n"

        self.label_registros.config(text=texto)

        print("\n--- Vehículos Registrados ---")
        for vehiculo in self.vehiculos:
            print(vehiculo)

# Ejecutar el programa
RegistroVehiculos()
