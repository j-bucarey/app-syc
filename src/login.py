import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from src.objects import Producto

class Login:
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu == "root" and password == "1234") :
            self.ventana.destroy()
            Producto()
        else:
            messagebox.showerror(message="La credenciales ingresadas son incorrectas",title="Mensaje")

    def __init__(self,root):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
       

        logo =utl.leer_imagen("./images/3d-truck.jpg",(320,320))


        #frame logo

        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#fcfcfc')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='#fcfcfc')
        label.place(x=0,relwidth=1, relheight=1)
        #final frame logo

        #frame_form

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #final frame form
        
        #Frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg = 'black')
        frame_form_top.pack(side='top',fill=tk.X)
        title = tk.Label(frame_form_top, text='Inicio de sesion',font=('Times', 30),fg = "#666a88",bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #final frame form top

        #Frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES,fill=tk.BOTH)
        #Label Usuario
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg='#666a88',bg='#fcfcfc',anchor='w')
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5 )
        self.usuario = ttk.Entry(frame_form_fill, font=('Times',14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)
        #Label Contraseña
        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg='#666a88',bg='#fcfcfc',anchor='w')
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5 )
        self.password = ttk.Entry(frame_form_fill, font=('Times',14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        #Boton Ingresar
        inicio = tk.Button(frame_form_fill,text = "Iniciar Sesion" , font=('Times', 15,BOLD), bg='#3a7ff6',bd =0,fg='#fff',command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))

        self.ventana.mainloop()