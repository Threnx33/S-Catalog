from erori.exceptii import ValidError

class ValidatorStudent:
    
    def valideaza_stud(self, stud):
        er = ""
        if stud.get_id_stud() < 0:
            er += "Id student invalid!"
        if stud.get_nume_stud() == "":
            er += "Nume student invalid!"
        if len(er) > 0:
            raise ValidError(er)
    
    def valideaza_id(self,id_stud):
        if id_stud < 0:
            raise ValidError("Id invalid!")