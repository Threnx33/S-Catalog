from erori.exceptii import RepoError
from domeniu.entitateStud import Student
from domeniu.entitateDisc import Disciplina
from domeniu.entitateNota import Nota

class RepositoryNota:
    
    def __init__(self):
        self._note = []
    
    
    def adauga_nota(self, nota):
        """
        metoda care adauga nota | sau eroare daca exista deja
        date de intrare:
            nota-nota pe care vrem sa o aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Nota existenta!"
        """
        if nota in self._note:
            raise RepoError("Nota existenta!")
        self._note.append(nota)
        
    
    def modifica_nota(self, nota_modif):
        """
        metoda care modifica nota in lista de note dupa id, id-ul ramanand la fel | sau eroare daca nu o gaseste
        date de intrare:
            nota_modif-noua nota pe care vrem sa o schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        for i in range(len(self._note)):
            if self._note[i] == nota_modif:
                nota_precedenta = self._note[i]
                self._note[i] = nota_modif
                return nota_precedenta
        raise RepoError("Nota inexistenta!")
    
    
    def cauta_nota(self, id_nota):
        """
        metoda care returneaza o nota dupa id in lista de note | sau eroare daca nu o gaseste
        date de intrare:
            id_nota-idul notei pe care o cautam
        date de iesire:
            el-nota pe care o cautam
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        for el in self._note:
            if el.get_id_nota() == id_nota:
                return el
        raise RepoError("Nota inexistenta!")
    
    
    def sterge_nota(self, id_nota):
        """
        metoda care sterge nota dupa id | sau eroare daca nu o gaseste
        date de intrare:
            id_nota-idul notei
        date de iesire:-
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        for i in range(len(self._note)):
            if self._note[i].get_id_nota() == id_nota:
                del self._note[i]
                return 
        raise RepoError("Nota inexistenta!")
    
    
    def sterge_note(self):
        """
        metoda care sterge toate notele
        """
        self._note = []
    
    
    def get_note(self):
        return self._note[:]
    
    
    def __len__(self):
        return len(self._note)
    

    def get_note_by_disc(self,disc):
        """
        metoda care returneaza o lista de studenti si notele lor la o anumita materie
        date de intrare:
            disc-disciplina
        date de iesire:
            rez-lista de studenti si notele lor la disciplina 
        exceptii:-
        """
        rez = []
        for i in range(len(self._note)):
            if self._note[i].get_disc() == disc:
                nume_stud = self._note[i].get_stud().get_nume_stud()
                val_nota = self._note[i].get_val_nota()
                rez.append([nume_stud,val_nota])
        return rez
    
    
    def modifica_stud_note(self,stud):
        """
        metoda care modifica toate notele care contin studentul respectiv
        """
        for i in range(len(self._note)):
            if self._note[i].get_stud() == stud:
                self._note[i].set_stud(stud)
    
    
    def modifica_disc_note(self,disc):
        """
        metoda care modifica toate notele care contin disciplina respectiva
        """
        for i in range(len(self._note)):
            if self._note[i].get_disc() == disc:
                self._note[i].set_disc(disc)
    
    
    def sterge_note_stud(self,id_stud):
        """
        metoda care sterge student si notele care contin studentul dupa id_stud | sau eroare daca nu o gaseste
        date de intrare:
            id_stud-idul studentului
        date de iesire:-
        date de exceptie:-
        """
        l = len(self._note)
        i = 0
        while i < l:
            if self._note[i].get_stud().get_id_stud() == id_stud:
                del self._note[i]
                l -= 1
            else:
                i += 1
                
    
    def sterge_note_disc(self,id_disc):
        """
        metoda care sterge disciplina si notele care contin disciplina dupa id_disc | sau eroare daca nu o gaseste
        date de intrare:
            id_disc-idul disciplinei
        date de iesire:-
        date de exceptie:-
        """
        l = len(self._note)
        i = 0
        while i < l:
            if self._note[i].get_disc().get_id_disc() == id_disc:
                del self._note[i]
                l -= 1
            else:
                i += 1
                
                
    def set_note(self, note):
        """
        metoda care seteaza toti studentii
        date de intrare:
            note-lista de note cu care vrem sa setam lista noastra
        """
        self._note = note
                

class RepositoryNotaFile(RepositoryNota):
    
    def __init__(self,file):
        RepositoryNota.__init__(self)
        self.__file = file
        self.__load_note()
        
    
    def __load_note(self):
        """
        metoda care incarca toate notele din fisier
        date de intrare:-
        date de iesire:-
        exceptii:-
        """
        with open(self.__file,"r") as fn:
            for line in fn:
                atr_nota = line.split(",")
                for i in range(len(atr_nota)):
                    atr_nota[i] = atr_nota[i].strip()
                atr_nota[0] = int(atr_nota[0])
                atr_nota[1] = int(atr_nota[1])
                atr_nota[3] = int(atr_nota[3])
                atr_nota[6] = float(atr_nota[6])
                nota = Nota(atr_nota[0],Student(atr_nota[1],atr_nota[2]),Disciplina(atr_nota[3],atr_nota[4],atr_nota[5]),atr_nota[6])
                self._note.append(nota)
    
    
    def append_nota(self,nota):
        """
        metoda care appenduieste nota in fisier
        """
        with open(self.__file,"a") as fn:
            fn.write(nota.get_nota_f()+"\n")
            
    
    def store_note(self):
        """
        metoda care uploadeaza notele in fisier
        date de intrare:-
        date de iesire:-
        exceptii:-
        """
        with open(self.__file,"w") as fn:
            for nota in self._note:
                fn.write(nota.get_nota_f()+"\n")
    
    
    def adauga_nota(self, nota):
        """
        metoda care adauga nota in lista si in fisier | sau eroare daca exista deja
        date de intrare:
            nota-nota pe care vrem sa o aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Nota existenta!"
        """
        RepositoryNota.adauga_nota(self,nota)
        self.append_nota(nota)
        
    
    def modifica_nota(self, nota_modif):
        """
        metoda care modifica nota in lista si in fisier dupa id, id-ul ramanand la fel | sau eroare daca nu o gaseste
        date de intrare:
            nota_modif-noua nota pe care vrem sa o schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        RepositoryNota.modifica_nota(self,nota_modif)
        self.store_note()
    
    
    def sterge_nota(self, id_nota):
        """
        metoda care sterge nota dupa id, in lista si in fisier  | sau eroare daca nu o gaseste
        date de intrare:
            id_nota-idul notei
        date de iesire:-
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        RepositoryNota.sterge_nota(self,id_nota)
        self.store_note()
    
    
    def sterge_note(self):
        """
        metoda care sterge toate notele
        """
        RepositoryNota.sterge_note(self)
        self.store_note()
    
    
    def sterge_note_stud(self,id_stud):
        """
        metoda care sterge student si notele care contin studentul dupa id_stud, in lista si in fisier | sau eroare daca nu o gaseste
        date de intrare:
            id_stud-idul studentului
        date de iesire:-
        date de exceptie:-
        """
        RepositoryNota.sterge_note_stud(self, id_stud)
        self.store_note()
                
    
    def sterge_note_disc(self,id_disc):
        """
        metoda care sterge disciplina si notele care contin disciplina dupa id_disc, in lista si in fisier | sau eroare daca nu o gaseste
        date de intrare:
            id_disc-idul disciplinei
        date de iesire:-
        date de exceptie:-
        """
        RepositoryNota.sterge_note_disc(self, id_disc)
        self.store_note()
        
    
    def set_note(self, note):
        """
        metoda care seteaza toti studentii
        date de intrare:
            note-lista de note cu care vrem sa setam lista noastra
        """
        RepositoryNota.set_note(self, note)
        self.store_note()



    