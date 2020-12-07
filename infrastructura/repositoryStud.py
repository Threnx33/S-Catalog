from erori.exceptii import RepoError
from domeniu.entitateStud import Student

class RepositoryStud:
    
    def __init__(self):
        self._studenti = []
    
    
    def adauga_stud(self,stud):
        """
        metoda care adauga student in lista de studenti | sau eroare daca exista deja
        date de intrare:
            stud-studentul pe care vrem sa il aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Student existent!"
        """
        if stud in self._studenti:
            raise RepoError("Student existent!")
        self._studenti.append(stud)
    
    
    def modifica_stud(self, stud_modif):
        """
        metoda care modifica student in lista de studenti dupa id, id-ul ramanand la fel | sau eroare daca nu il gaseste
        date de intrare:
            stud_modif-inlocuitorul studentului pe care vrem sa-l schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Student inexistent!"
        """
        for i in range(len(self._studenti)):
            if self._studenti[i] == stud_modif:
                stud_precedent = self._studenti[i]
                self._studenti[i] = stud_modif
                return stud_precedent
        raise RepoError("Student inexistent!")
    

    def cauta_stud(self, id_stud):
        """
        metoda care returneaza un student dupa id in lista de studenti | sau eroare daca nu il gaseste
        date de intrare:
            id_stud-idul studentului pe care il cautam
        date de iesire:
            el-studentul pe care il cautam
        date de exceptie:
            RepoError-"Student inexistent!"
        """
        for el in self._studenti:
            if el.get_id_stud() == id_stud:
                return el
        raise RepoError("Student inexistent!")
    
        
    def get_studenti(self):
        """
        metoda care returneaza toti studentii
        date de intrare:-
        date de iesire:
            self.__studenti[:]-copie dupa lista cu studenti
        """
        return self._studenti[:]
    
    
    def sterge_stud(self, id_stud):
        """
        metoda care sterge student dupa id in lista de studenti | sau eroare daca nu il gaseste
        date de intrare:
            id_stud-idul studentului
        date de iesire:-
        exceptii:
            RepoError-"Student inexistent!"
        """
        for i in range(len(self._studenti)):
            if self._studenti[i].get_id_stud() == id_stud:
                del self._studenti[i]
                return
        raise RepoError("Student inexistent!")
        
        
    def __len__(self):
        return len(self._studenti)
    
    
    def sterge_studenti(self):
        """
        Metoda care sterge toti studentii
        """
        self._studenti = []
    

    
    
    
class RepositoryStudFile(RepositoryStud):
    
    def __init__(self, file):
        RepositoryStud.__init__(self)
        self.__file = file
        self.__load_studenti()
    
    
    def __load_studenti(self):
        """
        metoda care incarca toti studentii din fisier
        date de intrare:-
        date de iesire:-
        exceptii:-
        """
        with open(self.__file,"r") as fs:
            for line in fs:
                atr_stud = line.split(",")
                for i in range(len(atr_stud)):
                    atr_stud[i] = atr_stud[i].strip()
                atr_stud[0] = int(atr_stud[0])
                stud = Student(atr_stud[0],atr_stud[1])
                self._studenti.append(stud)
    
    
    def __store_studenti(self):
        """
        metoda care uploadeaza studentii in fisier
        date de intrare:-
        date de iesire:-
        exceptii:-
        """
        with open(self.__file,"w") as fs:
            for stud in self._studenti:
                fs.write(stud.get_stud_f()+"\n")
    
    
    def __append_student(self,stud):
        """
        metoda care appenduieste student in fisier
        """
        with open(self.__file,"a") as fs:
            fs.write(stud.get_stud_f()+"\n")
    
    
    def adauga_stud(self,stud):
        """
        metoda care adauga student in lista de studenti si fisier | sau eroare daca exista deja
        date de intrare:
            stud-studentul pe care vrem sa il aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Student existent!"
        """
        RepositoryStud.adauga_stud(self, stud)
        self.__append_student(stud)
    
    
    def modifica_stud(self, stud_modif):
        """
        metoda care modifica student in lista de studenti si fisier dupa id, id-ul ramanand la fel | sau eroare daca nu il gaseste
        date de intrare:
            stud_modif-inlocuitorul studentului pe care vrem sa-l schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Student inexistent!"
        """
        RepositoryStud.modifica_stud(self, stud_modif)
        self.__store_studenti()
    
    
    def sterge_stud(self, id_stud):
        """
        metoda care sterge student dupa id in lista de studenti si fisier | sau eroare daca nu il gaseste
        date de intrare:
            id_stud-idul studentului
        date de iesire:-
        exceptii:
            RepoError-"Student inexistent!"
        """
        RepositoryStud.sterge_stud(self, id_stud)
        self.__store_studenti()
        
    
    def sterge_studenti(self):
        """
        Metoda care sterge toti studentii si updateaza in fisier
        """
        RepositoryStud.sterge_studenti(self)
        self.__store_studenti()



