class personagem():
    def __init__(self, nome,idade,classe):
        self._nome=nome
        self._idade=idade
        self._classe=classe 
        self._vida=30
        self._ataque=10
        self._defesa=5


    def classes(self):
           
            if(self.classe==1):
                self.vida-10
                self.ataque+5
                self.defesa-2
                n_classe="Mago"
                return n_classe,self.vida,self.ataque,self.defesa
            else:
            
                self.vida+10
                self.defesa+1
                n_classe="Guerreiro"
                return n_classe,self.vida,self.ataque,self.defesa




        
    
    