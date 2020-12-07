from erori.exceptii import ValidError

class ValidatorDisciplina:
    
    def valideaza_disc(self,disc):
        er = ""
        if disc.get_id_disc() < 0:
            er += "Id disciplina invalid!"
        if disc.get_nume_disc() == "":
            er += "Nume disciplina invalid!"
        if disc.get_nume_prof() == "":
            er += "Nume profesor invalid!"
        if len(er) > 0:
            raise ValidError(er)