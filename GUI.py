from Tkinter import *
import neo

class Application(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

        
    def create_widgets(self):
        Label(self, text="Seleccione sus generos favoritos!").grid(row=1,column=2)

        self.deporte = BooleanVar()
        self.aventura = BooleanVar()
        self.rpg = BooleanVar()
        self.pelea = BooleanVar()
        self.shooter = BooleanVar()
        
        Checkbutton(self, text="Deporte", variable = self.deporte, command=self.update_text).grid(row = 2, column=1,sticky = W)
        Checkbutton(self, text="Aventura", variable = self.aventura, command=self.update_text).grid(row = 2, column=2,sticky = W)
        Checkbutton(self, text="RPG", variable = self.rpg, command=self.update_text).grid(row = 2, column=3,sticky = W)
        Checkbutton(self, text="Pelea", variable = self.pelea, command=self.update_text).grid(row = 3, column=1,sticky = W)
        Checkbutton(self, text="Shooter", variable = self.shooter, command=self.update_text).grid(row = 3, column=2,sticky = W)
        
        self.result=Text(self,width=40,height=5,wrap=WORD)
        self.result.grid(row=5,column=0,columnspan=3)
        

    def update_text(self):
        ## Condiciones para checkbox
        
        if self.deporte.get():
            buscar="Fifa 17"
            quiero="Tipo"
            res = neo.__neo4j__(buscar,quiero) ## Llamamos a neo 
            print(res)
            
        else:
            genero = "--"

        self.result.delete(0.0,END)
        self.result.insert(0.0,genero)
        

neo._crearBD_()       
root =Tk()
root.title("Gamming")
root.geometry("500x500")
app = Application(root)
#neo._delDb_()
root.mainloop()
