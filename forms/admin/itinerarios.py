
import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk, messagebox
import conexion
import util.generic as utl
from ..admin import form_admin as fa
from ..admin import usuarios as u
from forms import form_login as fl


#  ITINERARIOS
class itinera:
    def allItinerarios(self):
        db = conexion.get_db()

        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Total de Itinerarios')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Total de Itinerarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="Código de Vuelo")
        listado.heading('#1', text="Origen")
        listado.heading('#2', text="Destino")
        listado.heading('#3', text="Fecha de Ida")
        listado.heading('#4', text="Duración")
        listado.heading('#5', text="Hora de Vuelo")
        listado.heading('#6', text="Valor del Pasaje")
        listado.heading('#7', text="Asientos Disponibles")
        listado.heading('#8', text="Estado")

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizacionItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizacionItinerarios()))

        itinerarios = db.itinerarios.find({})
        for itinerario in itinerarios:
            listado.insert( "", 
                            tk.END,
                            text=itinerario["_id"],
                            values = (itinerario["origen"], itinerario["destino"], itinerario["fechaIda"], itinerario["duracion"], itinerario["horaIda"], itinerario["valorTramo"], itinerario["disponibilidad"], itinerario["estadoVuelo"])
                            
                            )
            

        self.ventana.mainloop()

    def itinerarioPorCodigo(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar Itinerarios por Código')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Itinerario según código", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DEl codigo del vuelo a consultar
        etiqueta_codigoVuelo = tk.Label(frame_form_access, text="Inserte el código del vuelo a buscar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_codigoVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.codVueloBuscar = ttk.Entry(frame_form_access, font=('Times', 14))
        self.codVueloBuscar.pack(fill=tk.BOTH, padx=20, pady=10)

        buscarCodigoVuelo =  tk.Button(frame_form_access, text="Buscar Vuelo", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonBuscarCodigoVuelo)
        buscarCodigoVuelo.pack(fill=tk.X, padx=20, pady=20)
        buscarCodigoVuelo.bind("<Return>", (lambda event: self.botonBuscarCodigoVuelo()))

        self.listadoCod = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.listadoCod.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listadoCod.heading('#0', text="Código de Vuelo")
        self.listadoCod.heading('#1', text="Origen")
        self.listadoCod.heading('#2', text="Destino")
        self.listadoCod.heading('#3', text="Fecha de Ida")
        self.listadoCod.heading('#4', text="Duración")
        self.listadoCod.heading('#5', text="Hora de Vuelo")
        self.listadoCod.heading('#6', text="Valor del Pasaje")
        self.listadoCod.heading('#7', text="Asientos Disponibles")
        self.listadoCod.heading('#8', text="Estado")         

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizacionItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizacionItinerarios()))

        self.ventana.mainloop()

    def itinerarioPorFecha(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar Itinerarios por Fecha')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Itinerario según Fecha", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DEl codigo del vuelo a consultar
        etiqueta_fechaVuelo = tk.Label(frame_form_access, text="Inserte la fecha del vuelo a buscar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_fechaVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.fechaVueloBuscar = ttk.Entry(frame_form_access, font=('Times', 14))
        self.fechaVueloBuscar.pack(fill=tk.BOTH, padx=20, pady=10)
        self.fechaVueloBuscar.insert(0, "Formato de fecha: DD-MM-AAA")
        self.fechaVueloBuscar.configure(state=tk.DISABLED)
        def on_click(event):
            self.fechaVueloBuscar.configure(state=tk.NORMAL)
            self.fechaVueloBuscar.delete(0, tk.END)
        self.fechaVueloBuscar.bind("<Button-1>", on_click)

        buscarFechaVuelo =  tk.Button(frame_form_access, text="Buscar Vuelo", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonBuscarFechaVuelo)
        buscarFechaVuelo.pack(fill=tk.X, padx=20, pady=20)
        buscarFechaVuelo.bind("<Return>", (lambda event: self.botonBuscarFechaVuelo()))

        self.listadoFecha = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.listadoFecha.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listadoFecha.heading('#0', text="Código de Vuelo")
        self.listadoFecha.heading('#1', text="Origen")
        self.listadoFecha.heading('#2', text="Destino")
        self.listadoFecha.heading('#3', text="Fecha de Ida")
        self.listadoFecha.heading('#4', text="Duración")
        self.listadoFecha.heading('#5', text="Hora de Vuelo")
        self.listadoFecha.heading('#6', text="Valor del Pasaje")
        self.listadoFecha.heading('#7', text="Asientos Disponibles")
        self.listadoFecha.heading('#8', text="Estado")         

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizacionItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizacionItinerarios()))

        self.ventana.mainloop()
    def addItinerario(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Agregar Itinerario de Vuelo')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto de título
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Agregar Itinerario de Vuelo", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        
        #Inserción del origen del vuelo, con un Entry para escribir
        etiqueta_origenVuelo = tk.Label(frame_form_access, text="Inserte Origen del Vuelo", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_origenVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.origenVuelo = ttk.Entry(frame_form_access, font=('Times', 14))
        self.origenVuelo.pack(fill=tk.BOTH, padx=20, pady=10)

        #Inserción de destino del vuelo, con un Entry para escribir
        etiqueta_destinoVuelo = tk.Label(frame_form_access, text="Inserte Destino del Vuelo", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_destinoVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.destinoVuelo = ttk.Entry(frame_form_access, font=('Times', 14))
        self.destinoVuelo.pack(fill=tk.BOTH, padx=20, pady=10)

        #Inserción de fecha de Ida, con un Entry para ser capturado en la función mas adelante.
        etiqueta_fechaIda = tk.Label(frame_form_access, text="Inserte la Fecha de Ida del vuelo, formato MM-DD-AAAA", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_fechaIda.pack(fill=tk.X, padx=20, pady=5)
        self.fechaIda = ttk.Entry(frame_form_access, font=('Times', 14))
        self.fechaIda.pack(fill=tk.BOTH, padx=20, pady=10)

        #inserción de la hora de Ida del vuelo, con un Entry.
        etiqueta_horaVuelo = tk.Label(frame_form_access, text="Inserte la Hora del Vuelo, formato HH:MM", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_horaVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.horaVuelo = ttk.Entry(frame_form_access, font=('Times', 14))
        self.horaVuelo.pack(fill=tk.BOTH, padx=20, pady=10)

        

        agregar = tk.Button(frame_form_access, text="Agregar Itinerario", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonAgregarItinerario)
        agregar.pack(fill=tk.X, padx=20, pady=20)
        agregar.bind("<Return>", (lambda event: self.botonAgregarItinerario()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionItinerarios()))

        self.ventana.mainloop()


    def modificarItinerario(self):
        self.ventana = tk.Tk()                             
        self.ventana.title('Modificar Usuario Trabajador')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto de título
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Modificar Itinerarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DE LA ID DEL ITINERARIO
        etiqueta_idItin = tk.Label(frame_form_access, text="Inserte ID del itinerario a modificar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_idItin.pack(fill=tk.X, padx=20, pady=5)
        self.idModificarItin = ttk.Entry(frame_form_access, font=('Times', 14))
        self.idModificarItin.pack(fill=tk.BOTH, padx=20, pady=10)

        #frame separaador para el origen
        frame_form_label1 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label1.pack(side="top", expand=tk.YES, fill=tk.NONE)

        
        self.modOrigen = ttk.Entry(frame_form_label1, font=('Times', 14))
        self.modOrigen.pack(padx=20, pady=20, side='left')
        self.modOrigen.insert(0, "Ingresar nuevo origen")
        self.modOrigen.configure(state=tk.DISABLED)
        def on_click(event):
            self.modOrigen.configure(state=tk.NORMAL)
            self.modOrigen.delete(0, tk.END)
        self.modOrigen.bind("<Button-1>", on_click)
        #boton origen itinerario
        modOrigenItin =  tk.Button(frame_form_label1, text="Modificar Origen", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModOrigen)
        modOrigenItin.pack(padx=20, pady=20, side='left')
        modOrigenItin.bind("<Return>", (lambda event: self.botonModOrigen()))

        #frame separador para el destino
        frame_form_label2 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label2.pack(side="top", expand=tk.YES, fill=tk.NONE)

        
        self.modDestinoItinerario = ttk.Entry(frame_form_label2, font=('Times', 14))
        self.modDestinoItinerario.pack(padx=20, pady=20, side='left')
        self.modDestinoItinerario.insert(0, "Ingresar nuevo destino")
        self.modDestinoItinerario.configure(state=tk.DISABLED)
        def on_click(event):
            self.modDestinoItinerario.configure(state=tk.NORMAL)
            self.modDestinoItinerario.delete(0, tk.END)
        self.modDestinoItinerario.bind("<Button-1>", on_click)
        #boton destino itinerario
        modDestinoItin =  tk.Button(frame_form_label2, text="Modificar Destino", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModDestino)
        modDestinoItin.pack(padx=20, pady=20, side='left')
        modDestinoItin.bind("<Return>", (lambda event: self.botonModDestino()))

        #frame separador para la fecha
        frame_form_label3 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label3.pack(side="top", expand=tk.YES, fill=tk.NONE)

        
        self.modFechaIda = ttk.Entry(frame_form_label3, font=('Times', 14))
        self.modFechaIda.pack(padx=20, pady=20, side='left')
        self.modFechaIda.insert(0, "Ingresar nueva fecha")
        self.modFechaIda.configure(state=tk.DISABLED)
        def on_click(event):
            self.modFechaIda.configure(state=tk.NORMAL)
            self.modFechaIda.delete(0, tk.END)
        self.modFechaIda.bind("<Button-1>", on_click)
        #boton fecha itinerario
        modfechaIdaItin =  tk.Button(frame_form_label3, text="Modificar Fecha", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModFecha)
        modfechaIdaItin.pack(padx=20, pady=20, side='left')
        modfechaIdaItin.bind("<Return>", (lambda event: self.botonModFecha()))

        #frame separador para el valor
        frame_form_label4 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label4.pack(side="top", expand=tk.YES, fill=tk.NONE)

        
        self.modValor = ttk.Entry(frame_form_label4, font=('Times', 14))
        self.modValor.pack(padx=20, pady=20, side='left')
        self.modValor.insert(0, "ej: 30.000")
        self.modValor.configure(state=tk.DISABLED)
        def on_click(event):
            self.modValor.configure(state=tk.NORMAL)
            self.modValor.delete(0, tk.END)
        self.modValor.bind("<Button-1>", on_click)
        #boton fecha itinerario
        modValorItin =  tk.Button(frame_form_label4, text="Modificar Valor", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModValor)
        modValorItin.pack(padx=20, pady=20, side='left')
        modValorItin.bind("<Return>", (lambda event: self.botonModValor()))

        #frame separador para la la hora
        frame_form_label5 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label5.pack(side="top", expand=tk.YES, fill=tk.NONE)

        
        self.modHoraIdaItin = ttk.Entry(frame_form_label5, font=('Times', 14))
        self.modHoraIdaItin.pack(padx=20, pady=20, side='left')
        self.modHoraIdaItin.insert(0, "Ingresar nueva hora")
        self.modHoraIdaItin.configure(state=tk.DISABLED)
        def on_click(event):
            self.modHoraIdaItin.configure(state=tk.NORMAL)
            self.modHoraIdaItin.delete(0, tk.END)
        self.modHoraIdaItin.bind("<Button-1>", on_click)
        #boton hora itinerario
        modHoraIdaItin =  tk.Button(frame_form_label5, text="Modificar Hora", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModHora)
        modHoraIdaItin.pack(padx=20, pady=20, side='left')
        modHoraIdaItin.bind("<Return>", (lambda event: self.botonModHora()))

        #frame separador para el menu anterior
        frame_form_label6 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label6.pack(side="top", expand=tk.YES, fill=tk.NONE)

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_label6, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionItinerarios()))


        self.ventana.mainloop()





    def deleteItinerario(self):
        db = conexion.get_db()
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Cancelar Itinerario')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto de título
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Cancelar Itinerario", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DE LA ID DEL USUARIO A MODIFICAR
        etiqueta_idItin = tk.Label(frame_form_access, text="Inserte ID de Vuelo a Cancelar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_idItin.pack(fill=tk.X, padx=20, pady=5)
        self.idEliminarItinerario = ttk.Entry(frame_form_access, font=('Times', 14))
        self.idEliminarItinerario.pack(fill=tk.BOTH, padx=20, pady=10)

        deleteItin =  tk.Button(frame_form_access, text="Cancelar Itinerario", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonEliminarItinerario)
        deleteItin.pack(fill=tk.X, padx=20, pady=20)
        deleteItin.bind("<Return>", (lambda event: self.botonEliminarItinerario()))

        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="Código de Vuelo")
        listado.heading('#1', text="Origen")
        listado.heading('#2', text="Destino")
        listado.heading('#3', text="Fecha de Ida")
        listado.heading('#4', text="Duración")
        listado.heading('#5', text="Hora de Vuelo")
        listado.heading('#6', text="Valor del Pasaje")
        listado.heading('#7', text="Asientos Disponibles")
        listado.heading('#8', text="Estado")

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionItinerarios()))

        itinerarios = db.itinerarios.find({})
        for itinerario in itinerarios:
            listado.insert( "", 
                            tk.END,
                            text=itinerario["_id"],
                            values = (itinerario["origen"], itinerario["destino"], itinerario["fechaIda"], itinerario["duracion"], itinerario["horaIda"], itinerario["valorTramo"], itinerario["disponibilidad"], itinerario["estadoVuelo"])
                            
                            )
            

        self.ventana.mainloop()

    #FUNCIONES DE BOTONES
    def menuAnterior(self):
        self.ventana.destroy()
        fa.AdminMenus().menuAdmin()

    def abrirGestionUsuarios(self):
        self.ventana.destroy()
        fa.AdminMenus().menuUsuariosAdm()

    def abrirGestionItinerarios(self):
        self.ventana.destroy()
        fa.AdminMenus().menuItinerariosAdm()

    def abrirVisualizacionItinerarios(self):
        self.ventana.destroy()
        fa.AdminMenus().menuItinerariosFiltros()

    def abrirAllItinerarios(self):
        self.ventana.destroy()
        self.allItinerarios()

    def abrirAllUsuarios(self):
        self.ventana.destroy()
        u.User().allUsers(self)

    def abrirAgregarUsuario(self):
        self.ventana.destroy()
        u.User().addUsuarioTrabajador()

    def abrirModificarUsuario(self):
        self.ventana.destroy()
        u.User.modificarUsuario(self)

    def abrirEliminarUsuario(self):
        self.ventana.destroy()
        u.User.eliminarUsuario(self)

    #itinerarios

    def abrirBuscarItinCodigo(self):
        self.ventana.destroy()
        self.itinerarioPorCodigo()

    def abrirBuscarItinFecha(self):
        self.ventana.destroy()
        self.itinerarioPorFecha()

    def abrirAddItinerario(self):
        self.ventana.destroy()
        self.addItinerario()

    def abrirEliminarItinerario(self):
        self.ventana.destroy()
        self.deleteItinerario()

    def abrirModificarItinerario(self):
        self.ventana.destroy()
        self.modificarItinerario()
    
    def abririniciosesion(self):
        self.ventana.destroy()
        fl.App()

    #FUNCIONES ITINERARIOS

    def botonBuscarCodigoVuelo(self):
        db = conexion.get_db()
        codVuelo = self.codVueloBuscar.get()
        ucodVuelo = codVuelo.upper()
        itinerarios = db.itinerarios.find({"_id": {"$regex": ucodVuelo, "$options": "i"}})
        for itin in itinerarios:
            itincod = (str.format(itin["_id"]))
            if ucodVuelo == itincod:
                
                self.listadoCod.insert( "", 
                            tk.END,
                            text=itin["_id"],
                            values = (itin["origen"], itin["destino"], itin["fechaIda"], itin["duracion"], itin["horaIda"], itin["valorTramo"], itin["disponibilidad"], itin["estadoVuelo"])
                                
                            )
                return itinerarios
        else:
            messagebox.showinfo(message="El codigo de vuelo no coincide", title="Error")

        

    def botonBuscarFechaVuelo(self):
        db = conexion.get_db()
        fechaVuelo = self.fechaVueloBuscar.get()
        listiti = []
        itinerarios = db.itinerarios.find({"fechaIda": fechaVuelo})
        for itin in itinerarios:
            listiti.append(itin)
            itinfecha = (str.format(itin["fechaIda"]))
            if fechaVuelo == itinfecha:
                self.listadoFecha.insert( "", 
                            tk.END,
                            text=itin["_id"],
                            values = (itin["origen"], itin["destino"], itin["fechaIda"], itin["duracion"], itin["horaIda"], itin["valorTramo"], itin["disponibilidad"], itin["estadoVuelo"])
                                
                            )
        if len(listiti) == 0:      
            messagebox.showerror(message="la fecha ingresada no cuenta con vuelos programados.", title="Error")
            return

#id automatico
    def botonAgregarItinerario(self):
        db = conexion.get_db()

        origen = self.origenVuelo.get()
        origenm = origen.lower()
        origenc = origenm.capitalize()
        destino = self.destinoVuelo.get()
        destinom = destino.lower()
        destinoc = destinom.capitalize()
        fechaVuelo = self.fechaIda.get()
        hora = self.horaVuelo.get()
    

        itinerarios = db.itinerarios.find({}, {"origen": 1, "fechaIda": 1})

        Idlist = []
        for itin in itinerarios:
            itinID = (itin["_id"])
            Idlist.append(itinID)

        listiti = []

        itinerarios = db.itinerarios.find({}, {"origen": 1, "fechaIda": 1, "_id":0})
        for itin in itinerarios:
            listiti.append(itin)
            itinfecha = (str.format(itin["fechaIda"]))
            itinOrigen = (str.format(itin["origen"]))

            if origenc == itinOrigen and fechaVuelo == itinfecha:
                    messagebox.showerror(message="Ya existe un vuelo en el origen y fecha ingresado.", title="Error")
                    return itinerarios
            else:
                    idVuelo = len(Idlist)+1
                    idVuelo = (f"DAP{idVuelo}")
                    if origenc == "" or destinoc == "" or fechaVuelo == "" or hora == "":
                        messagebox.showerror(message="No se pueden insertar valores vacíos", title="Error")
                        return itinerarios
                    else:
                        insertarItin = db.itinerarios.insert_one(
                            {
                                "_id": idVuelo,
                                "origen": origenc,
                                "destino": destinoc,
                                "fechaIda": fechaVuelo,
                                "duracion": "15 minutos",
                                "horaIda": hora,
                                "valorTramo": "40.000",
                                "disponibilidad": 8,
                                "estadoVuelo": "Activo"
                            })
                        messagebox.showinfo(message="Itinerario Agregado Correctamente", title="Felicidades")
                            
                        self.abrirAllItinerarios()
                        return insertarItin
        if len(listiti) == 0:
            idVuelo = len(Idlist)+1
            idVuelo = (f"DAP{idVuelo}")
            if origenc == "" or destinoc == "" or fechaVuelo == "" or hora == "":
                messagebox.showerror(message="No se pueden insertar valores vacíos", title="Error")
                return itinerarios
            else:
                insertarItin = db.itinerarios.insert_one(
                    {
                        "_id": idVuelo,
                        "origen": origenc,
                        "destino": destinoc,
                        "fechaIda": fechaVuelo,
                        "duracion": "15 minutos",
                        "horaIda": hora,
                        "valorTramo": "40.000",
                        "disponibilidad": 8,
                        "estadoVuelo": "Activo"
                    })
                messagebox.showinfo(message="Itinerario Agregado Correctamente", title="Felicidades")
                            
                self.abrirAllItinerarios()
                return insertarItin



    def botonModOrigen(self):
        db = conexion.get_db()
        idVuelo = self.idModificarItin.get()
        uidVuelo = idVuelo.upper()
        origen = self.modOrigen.get()
        origenm = origen.lower()
        origenc = origenm.capitalize()
        itinerarios = db.itinerarios.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if origen == "" or origen == "Ingresar nuevo origen":
                messagebox.showinfo(message="No se puede insertar un origen vacío", title="Error")
                return
            if uidVuelo == itinid: 
                moditin = db.itinerarios.update_one(
                    {"_id": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "origen": origenc
                        }
                    }
                )
                messagebox.showinfo(message="Origen Modificado Correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                    {"codVuelo": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "origen": origenc
                        }
                    }
                )
                self.abrirModificarItinerario()
                return moditin, pasaje
        else:
            messagebox.showinfo(message="El ID ingresado no existe", title="Error")

    def botonModDestino(self):
        db = conexion.get_db()
        idVuelo = self.idModificarItin.get()
        uidVuelo = idVuelo.upper()
        destino = self.modDestinoItinerario.get()
        destinom = destino.lower()
        destinoc = destinom.capitalize()
        itinerarios = db.itinerarios.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if destinoc == "" or destino == "Ingresar nuevo destino":
                messagebox.showinfo(message="No se puede insertar un destino vacío", title="Error")
                return
            if uidVuelo == itinid: 
                moditin = db.itinerarios.update_one(
                    {"_id": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "destino": destinoc
                        }
                    }
                )
                messagebox.showinfo(message="Destino Modificado Correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                    {"codVuelo": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "destino": destinoc
                        }
                    }
                )
                self.abrirModificarItinerario()
                return moditin, pasaje
        else:
            messagebox.showinfo(message="El ID inrgesado no existe", title="Felicidades")

    def botonModFecha(self):
        db = conexion.get_db()
        idVuelo = self.idModificarItin.get()
        uidVuelo = idVuelo.upper()
        fecha = self.modFechaIda.get()
        itinerarios = db.itinerarios.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if fecha == "" or fecha == "Ingresar nueva fecha":
                messagebox.showinfo(message="Debe insertar una fecha", title="Error")
                return
            if uidVuelo == itinid: 
                moditin = db.itinerarios.update_one(
                    {"_id": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "fechaIda": fecha
                        }
                    }
                )
                messagebox.showinfo(message="Fecha Modificada Correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                    {"codVuelo": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "fechaVuelo": fecha
                        }
                    }
                )
                self.abrirModificarItinerario()
                return moditin, pasaje
        else:
            messagebox.showinfo(message="El ID inrgesado no existe", title="Felicidades")

    def botonModValor(self):
        db = conexion.get_db()
        idVuelo = self.idModificarItin.get()
        uidVuelo = idVuelo.upper()
        valor = self.modValor.get()
        itinerarios = db.itinerarios.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if valor == "" or valor == "ej: 30.000":
                messagebox.showinfo(message="Debe insertar un valor", title="Error")
                return
            if uidVuelo == itinid: 
                moditin = db.itinerarios.update_one(
                    {"_id": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "ValorTramo": valor
                        }
                    }
                )
                messagebox.showinfo(message="Valor Modificada Correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                    {"codVuelo": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "valorTramo": valor
                        }
                    }
                )
                self.abrirModificarItinerario()
                return moditin, pasaje
        else:
            messagebox.showinfo(message="El ID ingresado no existe", title="Felicidades")

    def botonModHora(self):
        db = conexion.get_db()
        idVuelo = self.idModificarItin.get()
        uidVuelo = idVuelo.upper()
        hora = self.modHoraIdaItin.get()
        itinerarios = db.itinerarios.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if hora == "" or hora == "Ingresar nueva hora":
                messagebox.showinfo(message="Debe insertar una hora de vuelo", title="Error")
                return
            if uidVuelo == itinid: 
                moditin = db.itinerarios.update_one(
                    {"_id": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "horaIda": hora
                        }
                    }
                )
                messagebox.showinfo(message="Hora Modificada Correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                    {"codVuelo": {"$regex": uidVuelo, "$options": "i"}},
                    {
                        '$set': {
                            "horaVuelo": hora
                        }
                    }
                )
                self.abrirModificarItinerario()
                return moditin, pasaje
        else:
            messagebox.showinfo(message="El ID ingresado no existe", title="Felicidades")






#aca se eliminar el itinerario mas los pasajes de dicho itinerario
#tambien se ingresa el cancelar o aceptar al eliminar
    def botonEliminarItinerario(self):
        db = conexion.get_db()
        idVuelo = self.idEliminarItinerario.get()
        uidVuelo = idVuelo.upper()
        itinerarios = db.itinerarios.find({})
        pasajeros = db.ventaPasajes.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if uidVuelo == itinid:
                vendidos = 8-itin["disponibilidad"]
                nocuenta = "Este itinerario no cuenta con pasajes asociados, por lo que su cancelación no afectaría a ningún pasajero."
                sicuenta = f"Este itinerario cuenta con {vendidos} pasajes asociados, su cancelación deberá ser notificada a los pasajeros."
                decide = ""
                if itin["disponibilidad"] < 8:
                    decide = sicuenta
                    if messagebox.askokcancel(message=f"¿Seguro que quiere cancelar el itinerario {idVuelo}?\n{decide}", title="Título") == True:
                        moditin = db.itinerarios.update_one(
                            {"_id": {"$regex": uidVuelo, "$options": "i"}},
                            {
                                '$set': {
                                    "estadoVuelo": "Cancelado"
                                }
                            }
                        )
                        
                        for pasa in pasajeros:
                            pasajerosI = (pasa["pasajeroId"])
                            codvuelo = (pasa["codVuelo"])
                            if uidVuelo == codvuelo:
                                anularPasaje = db.ventaPasajes.update_one(
                                    {"pasajeroId": {"$regex": pasajerosI, "$options": "i"}},
                                    {
                                        '$set': {
                                            "estadoPasaje": 'Anulado'
                                        }
                                    }
                                )
                        messagebox.showinfo(message="Itinerario cancelado correctamente.", title="Felicidades")
                        self.abrirEliminarItinerario()
                        return
                    else:
                        self.abrirEliminarItinerario()
                        return
                if itin["disponibilidad"] == 8:
                    decide = nocuenta
                    if messagebox.askokcancel(message=f"¿Seguro que quiere cancelar el itinerario {idVuelo}?\n{decide}", title="Título") == True:
                        moditin = db.itinerarios.update_one(
                            {"_id": {"$regex": uidVuelo, "$options": "i"}},
                            {
                                '$set': {
                                    "estadoVuelo": "Cancelado"
                                }
                            }
                        )
                        
                        # for pasa in pasajeros:
                        #     pasajerosI = (pasa["_id"])
                        #     codvuelo = (pasa["codVuelo"])
                        #     if idVuelo == codvuelo:
                        #         deleteitinerario = db.ventaPasajes.delete_one({"_id": pasajerosI})
                        messagebox.showinfo(message="Itinerario cancelado correctamente.", title="Felicidades")
                        self.abrirEliminarItinerario()
                        return
                    else:
                        self.abrirEliminarItinerario()
                        return
        else:
            messagebox.showinfo(message="Error en el id del itinerario.", title="Error")