from erori.exceptii import RepoError
from domeniu.entitateDisc import Disciplina

class RepositoryDisc:
    
    def __init__(self):
        self._discipline = []
    
    def __len__(self):
        return len(self._discipline)
    
    def adauga_disc(self, disc):
        """
        metoda care adauga disciplina | sau eroare daca exista deja
        date de intrare:
            disc-disciplina pe care vrem sa o aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina existenta!"
        """
        if disc in self._discipline:
            raise RepoError("Disciplina existenta!")
        self._discipline.append(disc)
    
    def modifica_disc(self, disc_modif):
        """
        metoda care modifica disciplina dupa id, id-ul ramanand la fel | sau eroare daca nu o gaseste
        date de intrare:
            disc_modif-inlocuitorul disciplinei pe care vrem s-o schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        for i in range(len(self._discipline)):
            if self._discipline[i] == disc_modif:
                disc_precedent = self._discipline[i]
                self._discipline[i] = disc_modif
                return disc_precedent
        raise RepoError("Disciplina inexistenta!")
    
    def cauta_disc(self, id_disc):
        """
        metoda care returneaza o disciplina dupa id | sau eroare daca nu o gaseste
        date de intrare:
            id_disc-idul disciplinei pe care o cautam
        date de iesire:
            self.__discipline[i]-disciplina pe care o cautam
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        for i in range(len(self._discipline)):
            if self._discipline[i].get_id_disc() == id_disc:
                return self._discipline[i]
        raise RepoError("Disciplina inexistenta!")

    
    def get_discipline(self):
        """
        metoda care returneaza toate disciplinele
        date de intrare:-
        date de iesire:
            self.__discipline[:]-copie dupa lista cu discipline
        """
        return self._discipline[:]

    
    def sterge_disc(self, id_disc):
        """
        metoda care sterge disciplina dupa id | sau eroare daca nu o gaseste
        date de intrare:
            id_disc-idul disciplinei
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        for i in range(len(self._discipline)):
            if self._discipline[i].get_id_disc() == id_disc:
                del self._discipline[i]
                return 
        raise RepoError("Disciplina inexistenta!")
    
    def sterge_discipline(self):
        """
        metoda care sterge toate disciplinele
        """
        self._discipline = []
    
class RepositoryDiscFile(RepositoryDisc):
    
    def __init__(self, file):
        RepositoryDisc.__init__(self)
        self.__file = file
        self.__load_discipline()
        
        
    def __load_discipline(self):
        """
        metoda care incarca toate disciplinele din fisier
        date de intrare:-
        date de iesire:-
        exceptii:-
        """
        with open(self.__file,"r") as fd:
            for line in fd:
                atr_disc = line.split(",")
                for i in range(len(atr_disc)):
                    atr_disc[i] = atr_disc[i].strip()
                atr_disc[0] = int(atr_disc[0])
                disc = Disciplina(atr_disc[0],atr_disc[1],atr_disc[2])
                self._discipline.append(disc)
        
    
    def __store_discipline(self):
        """
        metoda care uploadeaza disciplinele in fisier
        date de intrare:-
        date de iesire:-
        exceptii:-
        """
        with open(self.__file,"w") as fd:
            for disc in self._discipline:
                fd.write(disc.get_disc_f()+"\n")
    
    
    def __append_disc(self,disc):
        """
        metoda care da append la disciplina in fisier
        """
        with open(self.__file,"a") as fd:
            fd.write(disc.get_disc_f()+"\n")
        
    
    def adauga_disc(self, disc):
        """
        metoda care adauga disciplina in lista de studenti si in fisier | sau eroare daca exista deja
        date de intrare:
            disc-disciplina pe care vrem sa o aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina existenta!"
        """
        RepositoryDisc.adauga_disc(self, disc)
        self.__append_disc(disc)
            
            
    def modifica_disc(self, disc_modif):
        """
        metoda care modifica disciplina in lista de studenti si in fisier dupa id, id-ul ramanand la fel | sau eroare daca nu o gaseste
        date de intrare:
            disc_modif-inlocuitorul disciplinei pe care vrem s-o schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        RepositoryDisc.modifica_disc(self, disc_modif)
        self.__store_discipline()

    
    def sterge_disc(self, id_disc):
        """
        metoda care sterge disciplina in lista de studenti si in fisier dupa id | sau eroare daca nu il gaseste
        date de intrare:
            id_disc-idul disciplinei
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        RepositoryDisc.sterge_disc(self, id_disc)
        self.__store_discipline()
    
    def sterge_discipline(self):
        RepositoryDisc.sterge_discipline(self)
        self.__store_discipline()
        
        
        
        
        
        
        
        
        