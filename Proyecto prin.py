import tkinter as tk
from pyqrcode import QRCode as qrcode 
from customtkinter import  CTk, CTkFrame


c_blanco= "#ffffff"
c_negro= "#000000"
c_amarillo= "#d1ca10"
c_rojo= "#f50000"
c_morado= "#ff00ea"
c_rosa= "#f0adad"


class Ventana1:
    def __init__(self, master):
        self.master = master
        self.master.title("Ingreso de Datos")
        self.master.geometry("400x400")
        self.master.config(bg= c_negro)
        #self.master.iconbitmap("C:/Users//Windows 10/Desktop/Proyecto Python/imagenes/logo.png")

        # Creamos los campos de entrada para los datos
        tk.Label(self.master, text= "Ingreso de datos", font=("calibri", 14), bg= c_negro, fg= c_blanco) .grid(row=0, column=1, padx=10, pady=10)

        #Nombre
        tk.Label(self.master, text="Nombre", bg= c_negro, fg= c_blanco).grid(row=1, column=0, padx=10, pady=10)
        self.nombre = tk.Entry(self.master)
        self.nombre.grid(row=1, column=1, padx=10, pady=10)
        self.nombre.config(bg= c_negro, fg= c_blanco)

        #Cedula
        tk.Label(self.master, text="Número de CI", bg= c_negro, fg= c_blanco).grid(row=2, column=0, padx=10, pady=10)
        self.ci = tk.Entry(self.master)
        self.ci.grid(row=2, column=1, padx=10, pady=10)
        self.ci.config(bg= c_negro, fg= c_blanco)

        tk.Label(self.master, text="Hora de entrada", bg= c_negro, fg= c_blanco).grid(row=3, column=0, padx=10, pady=10)
        self.hora = tk.Entry(self.master)
        self.hora.grid(row=3, column=1, padx=10, pady=10)
        self.hora.config(bg= c_negro, fg= c_blanco)

        tk.Label(self.master, text="Hora de salida", bg= c_negro, fg= c_blanco).grid(row=4, column=0, padx=10, pady=10)
        self.hora_s = tk.Entry(self.master)
        self.hora_s.grid(row=4, column=1, padx=10, pady=10)
        self.hora_s.config(bg= c_negro, fg= c_blanco)

        tk.Label(self.master, text="Fecha:", bg= c_negro, fg= c_blanco).grid(row=5, column=0, padx=10, pady=10)
        self.fecha = tk.Entry(self.master)
        self.fecha.grid(row=5, column=1, padx=10, pady=10)
        self.fecha.config(bg= c_negro, fg= c_blanco)

        tk.Label(self.master, text="Número de Vehículo:", bg= c_negro, fg= c_blanco).grid(row=6, column=0, padx=10, pady=10)
        self.vehiculo = tk.Entry(self.master)
        self.vehiculo.grid(row=6, column=1, padx=10, pady=10)
        self.vehiculo.config(bg= c_negro, fg= c_blanco)

        # Creamos el botón para avanzar a la siguiente ventana
        tk.Button(self.master, text="Siguiente", command=self.abrir_ventana2, bg= c_negro, fg= c_blanco, bd= 3, highlightthickness= 3  , highlightbackground= "red").grid(row=7, column=1, padx=10, pady=10)

    def abrir_ventana2(self):
        
        # Creamos la ventana 2
        self.ventana2 = tk.Toplevel(self.master)
        self.ventana2.title("Seleccionar Asiento")
        self.ventana2.geometry("250x600")
        self.ventana2.config(bg= c_negro)
        # tk.Label(self.ventana2, text= "Seleccione la posicion!!", font=("calibri", 14), bg= c_negro, fg= c_blanco,).grid(row=0, column=1, padx=10, pady=10)

        # Creamos los asientos
        
        self.puestos = []
        for i in range(60):
            self.puestos.append(tk.Button(self.ventana2, text=str(i+1), command=lambda j=i: self.seleccionar_asiento(j)))
            self.puestos[i].grid(row=(i//5)+1, column=i%5, padx=10, pady=10)
            self.puestos[i].config(bg= c_negro, fg= c_blanco)

    def seleccionar_asiento(self, num_puesto):
        # Guardamos el número de asiento seleccionado
        self.num_puesto = num_puesto+1

        # Cerramos la ventana 2
        self.ventana2.destroy()

        # Abrimos la ventana 3
        self.abrir_ventana3()

    def abrir_ventana3(self):
        # Creamos la ventana 3
        self.ventana3 = tk.Toplevel(self.master)
        self.ventana3.title("Datos Generales")
        self.ventana3.geometry("600x300")
        self.ventana3.config(bg= c_blanco)

        # Mostramos los datos ingresados en la ventana 1
        tk.Label(self.ventana3, text="Nombre "+self.nombre.get(), bg= c_negro, fg= c_blanco).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.ventana3, text="Número de CI "+self.ci.get(), bg= c_negro, fg= c_blanco).grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.ventana3, text="Hora de entrada"+self.hora.get(), bg= c_negro, fg= c_blanco).grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.ventana3, text="Hora de salida"+self.hora_s.get(), bg= c_negro, fg= c_blanco).grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.ventana3, text="Fecha "+self.fecha.get(), bg= c_negro, fg= c_blanco).grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.ventana3, text="Número de Vehículo "+self.vehiculo.get(), bg= c_negro, fg= c_blanco).grid(row=5, column=0, padx=10, pady=10)

        # Mostramos el número de asiento seleccionado
        tk.Label(self.ventana3, text="Asiento seleccionado: "+str(self.num_puesto), bg= c_negro, fg= c_blanco).grid(row=6, column=0, padx=10, pady=10)

        # Generamos codigo QR con la informacion del usuario
        user_info = f"Nombre: {self.nombre.get()}\nNúmero de CI: {self.ci.get()}\nHora: {self.hora.get()}\nFecha: {self.fecha.get()}\nNúmero de Vehículo: {self.vehiculo.get()}"
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(user_info)
        qr.make(fit=True)

        # Creamos la imagen desde el codigo QR
        qr_image = qr.make_image(fill_color=c_blanco, back_color= c_negro)

        # Convertimos la imagen a un objeto PhotoImage de Tkinter
        imagen_tk = ImageTk.PhotoImage(qr_image)

        # Creamos una etiqueta para mostrar la imagen del código QR
        imagen_qr = tk.Label(self.ventana3, image=imagen_tk)
        imagen_qr.grid(row=7, column=0, padx=10, pady=10)

        # Mostramos la ventana 3
        self.ventana3.mainloop()

# Creamos la ventana principal
root = tk.Tk()

# Creamos la interfaz
app = Ventana1(root)

# Iniciamos el bucle principal de la aplicación

root.mainloop()

