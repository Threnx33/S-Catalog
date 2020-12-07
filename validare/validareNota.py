from erori.exceptii import ValidError

class ValidatorNota:
    
    def valideaza_nota(self, nota):
        """
        metoda care valideaza o nota
        date de intrare: nota
        date de iesire:-
        exceptii: ValidError
        "Id nota invalid"-daca n<0
        "val nota invalid"-val_nota nu apartine [1,10]
        """
        er = ""
        if nota.get_id_nota() < 0:
            er += "Id nota invalid! "
        if nota.get_val_nota() < 1 or nota.get_val_nota() > 10:
            er += "Valoare nota invalida! "
        if len(er) > 0:
            er = er[:-1]
            raise ValidError(er)
    