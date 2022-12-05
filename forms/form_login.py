import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.admin.form_admin import AdminMenus
from forms.trabajador.form_trabajador import TrabajadorMenus
import conexion
import bcrypt

class App:   
    def verificar(self):
        db = conexion.get_db() 
        usu = self.usuario.get()
        usum = usu.lower()
        password = self.password.get()

        listuser = []
        users = db.adminUser.find({"nombreUsuario":usum},{"nombreUsuario": 1, "_id": 0})

        for user in users:
            nombreu = (str.format(user["nombreUsuario"]))
            listuser.append(user)
            if usum == nombreu:
                contra = db.adminUser.find({},{"contraseña": 1, "_id": 0})
                for contras in contra:
                    contrasena = (str.format(contras["contraseña"]))
                    if password == contrasena:
                        self.ventana.destroy()
                        AdminMenus().menuAdmin()
                    else:
                        messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")
                            
        tusers = db.trabajadorUsers.find({"nombreUsuario":usum},{"nombreUsuario": 1, "_id": 0})
        for tuser in tusers:
            tnombreu = (str.format(tuser["nombreUsuario"]))
            listuser.append(tuser)
            if usum == tnombreu:
                password= password.encode()
                tcontra = db.trabajadorUsers.find({"nombreUsuario":usum})
                for tcontras in tcontra:
                    tcontrasena = (tcontras["password"])
                    if bcrypt.checkpw(password, tcontrasena):
                        self.ventana.destroy()
                        TrabajadorMenus().menuTrabajador()
                    else:
                        messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")
        if len(listuser) == 0:
            messagebox.showerror(message="El usuario ingresado no existe.",title="Error")
        
            

    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,500)
        
        logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#3a7ff6')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='#3a7ff6' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))
        #end frame_form_fill
        self.ventana.mainloop()
        
if __name__ == "__main__":
   App()