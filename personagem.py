class personagem():
    def __init__(self, nome,idade,classe):
        self._nome=nome
        self._idade=idade
        self._classe=classe 
        self._vida=30
        self._ataque=10
        self._defesa=5


    def classes(self):
           
            if(self._classe==1):
                self._vida-10
                self._ataque+5
                self._defesa-2
                n_classe="Mago"
                return n_classe,self._vida,self._ataque,self._defesa
            else:
            
                self._vida+10
                self._defesa+1
                n_classe="Guerreiro"
                return n_classe,self._vida,self._ataque,self._defesa




        
    
    