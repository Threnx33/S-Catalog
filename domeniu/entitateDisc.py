class Disciplina:

    def __init__(self, id_disc, nume_disc, nume_prof):
        self.__id_disc = id_disc
        self.__nume_disc = nume_disc
        self.__nume_prof = nume_prof

    def get_id_disc(self):
        return self.__id_disc

    def get_nume_disc(self):
        return self.__nume_disc

    def get_nume_prof(self):
        return self.__nume_prof

    def set_nume_disc(self, value):
        self.__nume_disc = value

    def set_nume_prof(self, value):
        self.__nume_prof = value
    
    def __str__(self):
        return str(self.__id_disc)+" | "+self.__nume_disc+" | "+self.__nume_prof
    
    def __eq__(self,other):
        return self.get_id_disc() == other.get_id_disc()    
    
    def get_disc_f(self):
        return str(self.__id_disc)+","+self.__nume_disc+","+self.__nume_prof