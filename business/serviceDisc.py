from domeniu.entitateDisc import Disciplina
from domeniu.entitateUndoRedo import ActiuneUndo

class ServiceDisc:
    
    def __init__(self, repoDisc, validDisc):
        self._repoDisc = repoDisc
        self._validDisc = validDisc
        
    def __len__(self):
        return len(self._repoDisc)
    
    def adauga_disc(self,id_disc,nume_disc,nume_prof):
        """
        metoda care adauga disciplina | sau eroare daca exista deja
        date de intrare:
            disc-disciplina pe care vrem sa o aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina existenta!"
        """
        disc = Disciplina(id_disc,nume_disc,nume_prof)
        self._validDisc.valideaza_disc(disc)
        self._repoDisc.adauga_disc(disc)
        return disc
    
    def modifica_disc(self,id_disc,nume_disc,nume_prof):
        """
        metoda care modifica disciplina dupa id, id-ul ramanand la fel | sau eroare daca nu o gaseste
        date de intrare:
            disc_modif-inlocuitorul disciplinei pe care vrem s-o schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        disc_modif = Disciplina(id_disc,nume_disc,nume_prof)
        self._validDisc.valideaza_disc(disc_modif)
        disc_precedent = self._repoDisc.modifica_disc(disc_modif)
        return [disc_precedent,disc_modif]
    
    
    def cauta_disc(self,id_disc):
        """
        metoda care returneaza o disciplina dupa id | sau eroare daca nu o gaseste
        date de intrare:
            id_disc-idul disciplinei pe care o cautam
        date de iesire:
            self._discipline[i]-disciplina pe care o cautam
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        key_disc = Disciplina(id_disc,"anything","anything")
        self._validDisc.valideaza_disc(key_disc)
        return self._repoDisc.cauta_disc(id_disc)
    
    
    def get_discipline(self):
        """
        metoda care returneaza toate disciplinele
        date de intrare:-
        date de iesire:
            self._discipline[:]-copie dupa lista cu discipline
        """
        return self._repoDisc.get_discipline()
    
    
    def sterge_disc(self,id_disc):
        """
        metoda care sterge disciplina dupa id | sau eroare daca nu o gaseste
        date de intrare:
            id_disc-idul disciplinei
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        disc = self._repoDisc.cauta_disc(id_disc)
        self._validDisc.valideaza_disc(disc)
        self._repoDisc.sterge_disc(id_disc)
        return disc
    
    def sterge_discipline(self):
        """
        metoda care sterge toate disciplinele
        """
        self._repoDisc.sterge_discipline()
        

class ServiceDiscUndo(ServiceDisc):
    
    def __init__(self, repoDisc, validDisc, repoUndo):
        ServiceDisc.__init__(self, repoDisc, validDisc)
        self._repoUndo = repoUndo
        
        
    def adauga_disc(self, id_disc, nume_disc, nume_prof):
        disc = ServiceDisc.adauga_disc(self, id_disc, nume_disc, nume_prof)
        act_undo = ActiuneUndo(self._repoDisc.sterge_disc,self._repoDisc.adauga_disc,id_disc,disc)
        self._repoUndo.push(act_undo)
    
    
    def modifica_disc(self, id_disc, nume_disc, nume_prof):
        disc_precedent,disc = ServiceDisc.modifica_disc(self, id_disc, nume_disc, nume_prof) 
        act_undo = ActiuneUndo(self._repoDisc.modifica_disc,self._repoDisc.modifica_disc,disc_precedent,disc)
        self._repoUndo.push(act_undo)
        
        
    def sterge_disc(self, id_disc):
        disc = ServiceDisc.sterge_disc(self, id_disc)
        act_undo = ActiuneUndo(self._repoDisc.adauga_disc,self._repoDisc.sterge_disc,disc,id_disc)
        self._repoUndo.push(act_undo)






