class Nota:
    
    def __init__(self, id_nota, stud, disc, val_nota):
        self.__id_nota = id_nota
        self.__stud = stud
        self.__disc = disc
        self.__val_nota = val_nota


    def get_id_nota(self):
        return self.__id_nota
    

    def get_stud(self):
        return self.__stud
    

    def get_disc(self):
        return self.__disc
    

    def get_val_nota(self):
        return self.__val_nota
    
    
    def set_stud(self, stud):
        self.__stud = stud


    def set_disc(self, disc):
        self.__disc = disc


    def set_val_nota(self, val_nota):
        self.__val_nota = val_nota
    

    def __eq__(self,other):
        return self.__id_nota == other.get_id_nota()
    
    
    def __str__(self):
        return str(self.__id_nota)+" | "+str(self.__stud)+" | "+str(self.__disc)+" | "+str(self.__val_nota)
    
    
    def get_nota_f(self):
        return (str(self.__id_nota)+","+str(self.__stud.get_id_stud())+","+str(self.__stud.get_nume_stud())+","+str(self.__disc.get_id_disc())+","+
            str(self.__disc.get_nume_disc())+","+str(self.__disc.get_nume_prof())+","+str(self.__val_nota))
    