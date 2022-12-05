import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk, messagebox
import conexion
import util.generic as utl
from ..trabajador import form_trabajador as ft
from forms import form_login as fl



class trabajador:
    def visualizarPasajeros(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Visualizar Pasajeros')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Visualizar Pasajeros", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        #Imágen
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #Visualizar Total de Pasajeros
        
        visualizarTotalPasajeros = tk.Button(frame_form_access, text="Visualizar Total de Pasajeros", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarAllPasajeros)
        visualizarTotalPasajeros.pack(fill=tk.X, padx=20, pady=20)
        visualizarTotalPasajeros.bind("<Return>", (lambda event: self.abrirVisualizarAllPasajeros()))

        #Buscar Pasajero por Documento
        
        pasajeroPorDocumento = tk.Button(frame_form_access, text="Visualizar Pasajero por Documento", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajeroPorDocumento)
        pasajeroPorDocumento.pack(fill=tk.X, padx=20, pady=20)
        pasajeroPorDocumento.bind("<Return>", (lambda event: self.abrirVisualizarPasajeroPorDocumento()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajeros)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionPasajeros()))
    
        self.ventana.mainloop()
    
    def visualizarAllPasajeros(self):
        db = conexion.get_db()
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Visualizar Pasajeros')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Visualizar Pasajeros", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        #Imágen
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="Documento")
        listado.heading('#1', text="Nombre")
        listado.heading('#2', text="Apellido")
        listado.heading('#3', text="Nacionalidad")
        listado.heading('#4', text="Fecha de Nacimiento")
        listado.heading('#5', text="Genero")
        listado.heading('#6', text="E-mail")
        listado.heading('#7', text="Fono")




        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajeros)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizarPasajeros()))


        pasajeros = db.pasajeros.find({})
        for pasajero in pasajeros:
            listado.insert( "", 
                            tk.END,
                            text=pasajero["_id"],
                            values = (pasajero["nombre"], pasajero["apellido"], pasajero["nacionalidad"], pasajero["fechaNacimiento"], pasajero["genero"], pasajero["email"], pasajero["telefono"])
                            
                            )
    
        self.ventana.mainloop()

    def visualizarPasajeroPorDocumento(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar Pasajeros Por Documento')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Pasajero Según Documento", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DEl codigo del vuelo a consultar
        etiqueta_documentoPax = tk.Label(frame_form_access, text="Inserte el Documento del Pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_documentoPax.pack(fill=tk.X, padx=20, pady=5)

        self.codDocumentoBuscar = ttk.Entry(frame_form_access, font=('Times', 14))
        self.codDocumentoBuscar.pack(fill=tk.BOTH, padx=20, pady=10)
        self.codDocumentoBuscar.insert(0, "formato rut: xxxxxxxx-x")
        self.codDocumentoBuscar.configure(state=tk.DISABLED)
        def on_click(event):
            self.codDocumentoBuscar.configure(state=tk.NORMAL)
            self.codDocumentoBuscar.delete(0, tk.END)
        self.codDocumentoBuscar.bind("<Button-1>", on_click)

        buscarPasajeroDoc =  tk.Button(frame_form_access, text="Buscar Pasajero", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonBuscarPasajeroPorDocumento)
        buscarPasajeroDoc.pack(fill=tk.X, padx=20, pady=20)
        buscarPasajeroDoc.bind("<Return>", (lambda event: self.botonBuscarPasajeroPorDocumento()))

        self.listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
        self.listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listado.heading('#0', text="Documento")
        self.listado.heading('#1', text="Nombre")
        self.listado.heading('#2', text="Apellido")
        self.listado.heading('#3', text="Nacionalidad")
        self.listado.heading('#4', text="Fecha de Nacimiento")
        self.listado.heading('#5', text="Genero")
        self.listado.heading('#6', text="E-mail")
        self.listado.heading('#7', text="Fono")



        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajeros)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizarPasajeros()))

        self.ventana.mainloop()


######################################################################################################################################################################

#MODIFICAR PASAJEROS


    def modificarPasajero(self):
        self.ventana = tk.Tk()                             
        self.ventana.title('Modificar Pasajero')
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
        title = tk.Label(frame_form_top, text= "Modificar Pasajeros", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DE LA ID DEL PASAJERO
        etiqueta_idPax = tk.Label(frame_form_access, text="Inserte el Documento del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_idPax.pack(fill=tk.X, padx=20, pady=5)
        self.idModificarPax = ttk.Entry(frame_form_access, font=('Times', 14,))
        self.idModificarPax.pack(fill=tk.BOTH, padx=20, pady=10)
        self.idModificarPax.insert(0, "formato rut: xxxxxxxx-x")
        self.idModificarPax.configure(state=tk.DISABLED)
        def on_click(event):
            self.idModificarPax.configure(state=tk.NORMAL)
            self.idModificarPax.delete(0, tk.END)
        self.idModificarPax.bind("<Button-1>", on_click)

        #frame separaador para el nombre
        frame_form_label1 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label1.pack(side="top", expand=tk.YES, fill=tk.NONE)

        #String para el textvariable
        self.modNombre = ttk.Entry(frame_form_label1, font=('Times', 14))
        self.modNombre.pack(padx=20, pady=20, side='left')
        self.modNombre.insert(0, "Ingresar Nuevo Nombre")
        self.modNombre.configure(state=tk.DISABLED)
        def on_click(event):
            self.modNombre.configure(state=tk.NORMAL)
            self.modNombre.delete(0, tk.END)
        self.modNombre.bind("<Button-1>", on_click)
        #boton nombre
        modNOmbrePax =  tk.Button(frame_form_label1, text="Modificar Nombre", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModNombre)
        modNOmbrePax.pack(padx=20, pady=20, side='left')
        modNOmbrePax.bind("<Return>", (lambda event: self.botonModNombre()))

        #frame separador para el apellido
        frame_form_label2 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label2.pack(side="top", expand=tk.YES, fill=tk.NONE)

        #String para el textvariable
        self.modApellidoPax = ttk.Entry(frame_form_label2, font=('Times', 14))
        self.modApellidoPax.pack(padx=20, pady=20, side='left')
        self.modApellidoPax.insert(0, "Ingresar Nuevo Apellido")
        self.modApellidoPax.configure(state=tk.DISABLED)
        def on_click(event):
            self.modApellidoPax.configure(state=tk.NORMAL)
            self.modApellidoPax.delete(0, tk.END)
        self.modApellidoPax.bind("<Button-1>", on_click)
        #boton apellido
        modApellidoItin =  tk.Button(frame_form_label2, text="Modificar Apellido", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModApellido)
        modApellidoItin.pack(padx=20, pady=20, side='left')
        modApellidoItin.bind("<Return>", (lambda event: self.botonModApellido()))

        #frame separador para la nacionalidad
        frame_form_label3 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label3.pack(side="top", expand=tk.YES, fill=tk.NONE)

        #String para el textvariable
        self.modNacionalidad = ttk.Entry(frame_form_label3, font=('Times', 14))
        self.modNacionalidad.pack(padx=20, pady=20, side='left')
        self.modNacionalidad.insert(0, "Ingresar Nueva Nacionalidad")
        self.modNacionalidad.configure(state=tk.DISABLED)
        def on_click(event):
            self.modNacionalidad.configure(state=tk.NORMAL)
            self.modNacionalidad.delete(0, tk.END)
        self.modNacionalidad.bind("<Button-1>", on_click)
        #boton fecha itinerario
        modNacionalidadPax =  tk.Button(frame_form_label3, text="Modificar Nacionalidad", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModNacionalidad)
        modNacionalidadPax.pack(padx=20, pady=20, side='left')
        modNacionalidadPax.bind("<Return>", (lambda event: self.botonModNacionalidad()))

        #frame separador para la fecha de nacimiento
        frame_form_label4 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label4.pack(side="top", expand=tk.YES, fill=tk.NONE)

        #String para el textvariable
        self.modNacimiento = ttk.Entry(frame_form_label4, font=('Times', 14))
        self.modNacimiento.pack(padx=20, pady=20, side='left')
        self.modNacimiento.insert(0, "Formato: dd-mm-aaaa")
        self.modNacimiento.configure(state=tk.DISABLED)
        def on_click(event):
            self.modNacimiento.configure(state=tk.NORMAL)
            self.modNacimiento.delete(0, tk.END)
        self.modNacimiento.bind("<Button-1>", on_click)
        #boton nacimiento
        modNacimientoPax =  tk.Button(frame_form_label4, text="Modificar Fecha Nacimiento", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModNacimiento)
        modNacimientoPax.pack(padx=20, pady=20, side='left')
        modNacimientoPax.bind("<Return>", (lambda event: self.botonModNacimiento()))


        #frame separador para el email
        frame_form_label5 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label5.pack(side="top", expand=tk.YES, fill=tk.NONE)

        #String para el textvariable
        self.modEmail = ttk.Entry(frame_form_label5, font=('Times', 14))
        self.modEmail.pack(padx=20, pady=20, side='left')
        self.modEmail.insert(0, "Ingresar nuevo e-mail")
        self.modEmail.configure(state=tk.DISABLED)
        def on_click(event):
            self.modEmail.configure(state=tk.NORMAL)
            self.modEmail.delete(0, tk.END)
        self.modEmail.bind("<Button-1>", on_click)
        #boton email
        modEmailPax =  tk.Button(frame_form_label5, text="Modificar email", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModEmail)
        modEmailPax.pack(padx=20, pady=20, side='left')
        modNacimientoPax.bind("<Return>", (lambda event: self.botonModEmail()))


        #frame separador para el telefono
        frame_form_label6 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label6.pack(side="top", expand=tk.YES, fill=tk.NONE)

        self.modFono = ttk.Entry(frame_form_label6, font=('Times', 14))
        self.modFono.pack(padx=20, pady=20, side='left')
        self.modFono.insert(0, "Ingresar el nuevo teléfono")
        self.modFono.configure(state=tk.DISABLED)
        def on_click(event):
            self.modFono.configure(state=tk.NORMAL)
            self.modFono.delete(0, tk.END)
        self.modFono.bind("<Button-1>", on_click)
        #boton fono
        modFonoPax =  tk.Button(frame_form_label6, text="Modificar Teléfono", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModTelefono)
        modFonoPax.pack(padx=20, pady=20, side='left')
        modNacimientoPax.bind("<Return>", (lambda event: self.botonModTelefono()))

        
        #frame separador del menu anterior
        frame_form_label7 = tk.Frame(frame_form_access, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_label7.pack(side="top", expand=tk.YES, fill=tk.NONE)

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_label7, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajeros)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionPasajeros()))


        self.ventana.mainloop()


######################################################################################################################################################################

#ELIMINAR PASAJEROS

    def eliminarPasajero(self):
        db = conexion.get_db()
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Eliminar Pasajero')
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
        title = tk.Label(frame_form_top, text= "Eliminar Pasajero", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DE LA ID DEL USUARIO A MODIFICAR
        etiqueta_idPax = tk.Label(frame_form_access, text="Inserte número de documento del pasajero a eliminar.", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_idPax.pack(fill=tk.X, padx=20, pady=5)
        self.idEliminarPasajero = ttk.Entry(frame_form_access, font=('Times', 14))
        self.idEliminarPasajero.pack(fill=tk.BOTH, padx=20, pady=10)
        self.idEliminarPasajero.insert(0, "formato rut: xxxxxxxx-x")
        self.idEliminarPasajero.configure(state=tk.DISABLED)
        def on_click(event):
            self.idEliminarPasajero.configure(state=tk.NORMAL)
            self.idEliminarPasajero.delete(0, tk.END)
        self.idEliminarPasajero.bind("<Button-1>", on_click)

        deletePax =  tk.Button(frame_form_access, text="Eliminar Pasajero", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonEliminarPasajero)
        deletePax.pack(fill=tk.X, padx=20, pady=20)
        deletePax.bind("<Return>", (lambda event: self.botonEliminarPasajero()))

        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="Documento")
        listado.heading('#1', text="Nombre")
        listado.heading('#2', text="Apellido")
        listado.heading('#3', text="Nacionalidad")
        listado.heading('#4', text="Fecha de Nacimiento")
        listado.heading('#5', text="Genero")
        listado.heading('#6', text="E-mail")
        listado.heading('#7', text="Fono")

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajeros)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionPasajeros()))

        pasajeros = db.pasajeros.find({})
        for pasajero in pasajeros:
            listado.insert( "", 
                            tk.END,
                            text=pasajero["_id"],
                            values = (pasajero["nombre"], pasajero["apellido"], pasajero["nacionalidad"], pasajero["fechaNacimiento"], pasajero["genero"], pasajero["email"], pasajero["telefono"])
                            
                            )
            

        self.ventana.mainloop()

    #BOTONES DE APERTURA DE MENUS FUNCIONES
    def abrirGestionPasajeros(self):
        self.ventana.destroy()
        ft.TrabajadorMenus().menuPasajeros()

    def menuAnterior(self):
        self.ventana.destroy()
        ft.TrabajadorMenus().menuTrabajador()

    def abrirVisualizarPasajeros(self):
        self.ventana.destroy()
        self.visualizarPasajeros()

    def abrirVisualizarAllPasajeros(self):
        self.ventana.destroy()
        self.visualizarAllPasajeros()

    def abrirVisualizarPasajeroPorDocumento(self):
        self.ventana.destroy()
        self.visualizarPasajeroPorDocumento()

    def abrirModificarPasajero(self):
        self.ventana.destroy()
        self.modificarPasajero()

    def abrirEliminarPasajero(self):
        self.ventana.destroy()
        self.eliminarPasajero()

    def abririniciosesion(self):
        self.ventana.destroy()
        fl.App()



    #VISUALIZAR PASAJEROS POR DOCUMENTO
    def botonBuscarPasajeroPorDocumento(self):
        db = conexion.get_db()
        documento = self.codDocumentoBuscar.get()

        pasajeros = db.pasajeros.find({})
        for pasajero in pasajeros:
            doccod = (str.format(pasajero["_id"]))
            if documento == doccod:
                
                self.listado.insert( "", 
                            tk.END,
                            text=pasajero["_id"],
                            values = (pasajero["nombre"], pasajero["apellido"], pasajero["nacionalidad"], pasajero["fechaNacimiento"], pasajero["genero"], pasajero["email"], pasajero["telefono"])
                            
                            )
                return self.listado
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")


    #BLOQUE MODIFICAR PASAJERO
    

    def botonModNombre(self):
        db = conexion.get_db()
        documento = self.idModificarPax.get()
        nomPax = self.modNombre.get()
        nomPaxm = nomPax.lower()
        nomPaxc = nomPaxm.capitalize()
        itinerarios = db.pasajeros.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if nomPaxc == "" or nomPax == "Ingresar Nuevo Nombre":
                messagebox.showinfo(message="Debe ingresar un nombre.", title="Error")
                return
            if documento == itinid:
                modPasajero = db.pasajeros.update_one(
                    {"_id": {"$regex": documento, "$options": "i"}},
                    {
                        '$set': {
                            "nombre": nomPaxc
                        }
                    }
                )
                messagebox.showinfo(message="Nombre modificado correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                                {"pasajeroId": {"$regex": documento, "$options": "i"}},
                                {
                                    '$set': {
                                        "nombrePax": nomPaxc
                                    }
                                }
                            )

                self.abrirModificarPasajero()
                return modPasajero, pasaje
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")


    def botonModApellido(self):
        db = conexion.get_db()
        documento = self.idModificarPax.get()
        apellido = self.modApellidoPax.get()
        apellidom = apellido.lower()
        apellidoc = apellidom.capitalize()
        itinerarios = db.pasajeros.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if apellidoc == "" or apellido == "Ingresar Nuevo Apellido":
                messagebox.showinfo(message="Debe ingresar un apellido.", title="Error")
                return
            if documento == itinid:
                modPasajero = db.pasajeros.update_one(
                    {"_id": {"$regex": documento, "$options": "i"}},
                    {
                        '$set': {
                            "apellido": apellidoc
                        }
                    }
                )
                messagebox.showinfo(message="Apellido modificado correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                                {"pasajeroId": {"$regex": documento, "$options": "i"}},
                                {
                                    '$set': {
                                        "apellidoPax": apellidoc
                                    }
                                }
                            )
                self.abrirModificarPasajero()
                return modPasajero, pasaje
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")
    
    def botonModNacionalidad(self):
        db = conexion.get_db()
        documento = self.idModificarPax.get()
        nacionalidad = self.modNacionalidad.get()
        itinerarios = db.pasajeros.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if nacionalidad == "" or nacionalidad == "Ingresar Nueva Nacionalidad":
                messagebox.showinfo(message="Debe ingresar una nacionalidad.", title="Error")
                return
            if documento == itinid:
                modPasajero = db.pasajeros.update_one(
                    {"_id": {"$regex": documento, "$options": "i"}},
                    {
                        '$set': {
                            "nacionalidad": nacionalidad
                        }
                    }
                )
                messagebox.showinfo(message="Nacionalidad modificada correctamente", title="Felicidades")
                self.abrirModificarPasajero()
                return modPasajero
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")


    def botonModNacimiento(self):
        db = conexion.get_db()
        documento = self.idModificarPax.get()
        fechaNace = self.modNacimiento.get()
        itinerarios = db.pasajeros.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if fechaNace == "" or fechaNace == "Formato: dd-mm-aaaa":
                messagebox.showinfo(message="Debe ingresar una fecha de nacimiento.", title="Error")
                return
            if documento == itinid:
                modPasajero = db.pasajeros.update_one(
                    {"_id": {"$regex": documento, "$options": "i"}},
                    {
                        '$set': {
                            "fechaNacimiento": fechaNace
                        }
                    }
                )
                messagebox.showinfo(message="Fecha de nacimiento modificada correctamente", title="Felicidades")
                self.abrirModificarPasajero()
                return modPasajero
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")

    def botonModEmail(self):
        db = conexion.get_db()
        documento = self.idModificarPax.get()
        email = self.modEmail.get()
        itinerarios = db.pasajeros.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if email == "" or email == "Ingresar nuevo e-mail":
                messagebox.showinfo(message="Debe ingresar un email.", title="Error")
                return
            if documento == itinid:
                modPasajero = db.pasajeros.update_one(
                    {"_id": {"$regex": documento, "$options": "i"}},
                    {
                        '$set': {
                            "email": email
                        }
                    }
                )
                messagebox.showinfo(message="Email modificado correctamente", title="Felicidades")
                pasaje = db.ventaPasajes.update_many(
                                {"pasajeroId": {"$regex": documento, "$options": "i"}},
                                {
                                    '$set': {
                                        "email": email
                                    }
                                }
                            )
                self.abrirModificarPasajero()
                return modPasajero, pasaje
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")

    def botonModTelefono(self):
        db = conexion.get_db()
        documento = self.idModificarPax.get()
        telefono = self.modFono.get()
        itinerarios = db.pasajeros.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if telefono == "" or telefono == "Ingresar el nuevo teléfono":
                messagebox.showinfo(message="Debe ingresar un teléfono.", title="Error")
                return
            if documento == itinid: 
                modPasajero = db.pasajeros.update_one(
                    {"_id": {"$regex": documento, "$options": "i"}},
                    {
                        '$set': {
                            "telefono": telefono
                        }
                    }
                )
                messagebox.showinfo(message="Telefono modificado correctamente", title="Felicidades")
                self.abrirModificarPasajero()
                return modPasajero
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")

#tambien se ingresa el cancelar o aceptar al eliminar
    def botonEliminarPasajero(self):
        db = conexion.get_db()
        documento = self.idEliminarPasajero.get()
        itinerarios = db.pasajeros.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if documento == itinid: 
                if messagebox.askokcancel(message=f"¿Seguro que quiere eliminar este pasajero {documento}?", title="Título") == True:
                    deletepax = db.pasajeros.delete_one({"_id": {"$regex": documento, "$options": "i"}})
                    messagebox.showinfo(message="Pasajero Eliminado Correctamente.", title="Felicidades")
                    self.abrirEliminarPasajero()
                    return deletepax
                else:
                    self.abrirEliminarPasajero()
        else:
            messagebox.showinfo(message="El id ingresado es incorrecto.", title="Error")