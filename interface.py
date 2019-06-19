from tkinter import filedialog 
from tkinter import*
  


treinoimg = " "
testeimg = " "
def load_directory():
    dirLocal = filedialog.askdirectory()
    return dirLocal
def load_file():
    fileLocal = filedialog.askopenfilename()
    return fileLocal    
class Janela:
    def __init__(self, master=None):
        
       
        self.fontePadrao = ("Arial", "20")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()
        
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()
        
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Classificador de imagens")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()
  
        self.autenticar = Button(self.segundoContainer)
        self.autenticar["text"] = "Imagens teste"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 20
        self.autenticar["command"] = self.importtest
        self.autenticar.pack()
        
        self.autenticar = Button(self.terceiroContainer)
        self.autenticar["text"] = "Imagens treino"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 20
        self.autenticar["command"] = self.importtreino
        self.autenticar.pack()
       
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Classificar"
        self.autenticar["font"] = ("Calibri", "20")
        self.autenticar["width"] = 50
        self.autenticar["command"] = self.classificar
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
    
    def importtreino(self):
       global treinoimg
       treinoimg= load_directory()
 
    def importtest(self):
        global testeimg
        testeimg = load_directory()
    def classificar(self):
        global treinoimg
        global testeimg
        gatocachorro.training(treinoimg,testeimg)
        
  
root = Tk()
Janela(root)
root.mainloop()
