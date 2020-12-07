from domeniu.entitateStud import Student
from domeniu.entitateUndoRedo import ActiuneUndo
from erori.exceptii import RepoError
import random
import string

class ServiceStud:
    
    def __init__(self, repoStud, validStud):
        self._repoStud = repoStud
        self._validStud = validStud
    
    
    def __len__(self):
        return self._repoStud.__len__()
    
    
    def adauga_stud(self, id_stud, nume_stud):
        """
        metoda care adauga student in lista de studenti | sau eroare daca exista deja
        date de intrare:
            stud-studentul pe care vrem sa il aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Student existent!"
        """
        stud = Student(id_stud,nume_stud)
        self._validStud.valideaza_stud(stud)
        self._repoStud.adauga_stud(stud)
        return stud
        
        
    def adauga_studenti_r(self, nr_studenti):
        letters = string.ascii_lowercase
        for i in range(nr_studenti):
            ok = 0
            while ok == 0:
                try:
                    id_stud = random.randint(1,10000)
                    self._repoStud.cauta_stud(id_stud)
                except RepoError:
                    ok = 1
            nume_stud = ''.join(random.choice(letters) for k in range(15))
            stud = Student(id_stud,nume_stud)
            self._validStud.valideaza_stud(stud)
            self._repoStud.adauga_stud(stud)
    
    
    def modifica_stud(self,id_stud,nume_stud_modif):
        """
        metoda care modifica student in lista de studenti dupa id, id-ul ramanand la fel | sau eroare daca nu il gaseste
        date de intrare:
            stud_modif-inlocuitorul studentului pe care vrem sa-l schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Student inexistent!"
        """
        stud_modif = Student(id_stud,nume_stud_modif)
        self._validStud.valideaza_stud(stud_modif)
        stud_precedent = self._repoStud.modifica_stud(stud_modif)
        return [stud_precedent,stud_modif]
    
    
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
        key_stud = Student(id_stud,"anything")
        self._validStud.valideaza_stud(key_stud)
        return self._repoStud.cauta_stud(id_stud)
    
    
    def get_studenti(self):
        """
        metoda care returneaza toti studentii
        date de intrare:-
        date de iesire:
            self._studenti[:]-copie dupa lista cu studenti
        """
        return self._repoStud.get_studenti()
    
    
    def sterge_stud(self, id_stud):
        """
        metoda care sterge student dupa id in lista de studenti | sau eroare daca nu il gaseste
        date de intrare:
            id_stud-idul studentului
        date de iesire:-
        exceptii:
            RepoError-"Student inexistent!"
        """
        stud = self.cauta_stud(id_stud)
        self._validStud.valideaza_stud(stud)
        self._repoStud.sterge_stud(id_stud)
        return stud
    
    
    def sterge_studenti(self):
        """
        metoda care sterge toti studentii
        """
        self._repoStud.sterge_studenti()
 
 
class ServiceStudUndo(ServiceStud):
     
    def __init__(self, repoStud, validStud, repoUndo):
        ServiceStud.__init__(self, repoStud, validStud)
        self._repoUndo = repoUndo
         
    
    def adauga_stud(self, id_stud, nume_stud):
        stud = ServiceStud.adauga_stud(self,id_stud,nume_stud)
        act_undo = ActiuneUndo(self._repoStud.sterge_stud, self._repoStud.adauga_stud, id_stud, stud)
        self._repoUndo.push(act_undo)
    
    
    def modifica_stud(self, id_stud, nume_stud_modif):
        stud_precedent, stud_modif = ServiceStud.modifica_stud(self, id_stud, nume_stud_modif)
        act_undo = ActiuneUndo(self._repoStud.modifica_stud,self._repoStud.modifica_stud,stud_precedent,stud_modif)
        self._repoUndo.push(act_undo)

    
    def sterge_stud(self, id_stud):
        stud = ServiceStud.sterge_stud(self, id_stud)
        act_undo = ActiuneUndo(self._repoStud.adauga_stud,self._repoStud.sterge_stud,stud,id_stud)
        self._repoUndo.push(act_undo)
 
 
 
