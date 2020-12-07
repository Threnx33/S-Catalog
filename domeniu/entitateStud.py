class Student:

    def __init__(self, id_stud, nume_stud):
        self.__id_stud = id_stud
        self.__nume_stud = nume_stud

    def get_id_stud(self):
        return self.__id_stud

    def get_nume_stud(self):
        return self.__nume_stud

    def set_nume_stud(self, value):
        self.__nume_stud = value
    
    def __str__(self):
        return str(self.__id_stud)+" | "+self.__nume_stud
    
    def __eq__(self,other):
        return self.__id_stud == other.__id_stud

    def get_stud_f(self):
        return str(self.__id_stud)+","+self.__nume_stud