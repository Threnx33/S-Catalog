from domeniu.entitateDisc import Disciplina
from validare.validareDisc import ValidatorDisciplina
from infrastructura.repositoryDisc import RepositoryDisc,RepositoryDiscFile
from erori.exceptii import ValidError,RepoError

class TesteDisc:

    def test_domeniuDisc(self):
        id_disc = 1
        nume_disc = "Analiza"
        nume_prof = "Berinde Stefan"
        disc = Disciplina(id_disc,nume_disc,nume_prof)
        assert disc.get_id_disc() == id_disc
        assert disc.get_nume_disc() == nume_disc
        assert disc.get_nume_prof() == nume_prof
        assert str(disc) == "1 | Analiza | Berinde Stefan"
        disc2 = Disciplina(id_disc,"Logica","Pop")
        assert disc == disc2
    
    
    def test_validareDisc(self):
        validDisc = ValidatorDisciplina()
        id_disc = 1
        nume_disc = "Analiza"
        nume_prof = "Berinde Stefan"
        disc = Disciplina(id_disc,nume_disc,nume_prof)
        validDisc.valideaza_disc(disc)
        disc_gresit = Disciplina(-1,"","")
        try:
            validDisc.valideaza_disc(disc_gresit)
            assert False
        except ValidError as ve:
            assert str(ve) == "Id disciplina invalid!Nume disciplina invalid!Nume profesor invalid!"
        
    def test_repoDisc(self,repoDisc,lung_init):
        assert len(repoDisc) == 0+lung_init
        id_disc = 0
        nume_disc = "Analiza"
        nume_prof = "Berinde Stefan"
        disc = Disciplina(id_disc,nume_disc,nume_prof)
        repoDisc.adauga_disc(disc)
        assert len(repoDisc) == 1+lung_init
        try:
            repoDisc.adauga_disc(disc)
            assert False
        except RepoError as re:
            assert str(re) == "Disciplina existenta!"
        disc_modif = Disciplina(id_disc,"Algebra","Modoi")
        repoDisc.modifica_disc(disc_modif)
        assert disc_modif.get_nume_disc() == "Algebra"
        assert disc_modif.get_nume_prof() == "Modoi"
        disc_modif_gresit = Disciplina(id_disc+99,"Logica","Pop")
        try:
            repoDisc.modifica_disc(disc_modif_gresit)
            assert False
        except RepoError as re:
            assert str(re) == "Disciplina inexistenta!"
        gasit = repoDisc.cauta_disc(id_disc)
        assert gasit == disc_modif
        try:
            repoDisc.cauta_disc(id_disc+99)
            assert False
        except RepoError as re:
            assert str(re) == "Disciplina inexistenta!"
        discipline = repoDisc.get_discipline()
        assert len(discipline) == 1+lung_init
        repoDisc.sterge_disc(id_disc)
        assert len(repoDisc) == 0+lung_init
        try:
            repoDisc.sterge_disc(id_disc)
            assert False
        except RepoError as re:
            assert str(re) == "Disciplina inexistenta!"
            
            
    def test_repoDiscFile(self,repoDiscF):
        lung_init = len(repoDiscF)
        assert lung_init == 3
        self.test_repoDisc(repoDiscF,lung_init)
        id_disc = 1
        disc = Disciplina(id_disc,"a","a")
        try:
            repoDiscF.adauga_disc(disc)
            assert False
        except RepoError as re:
            assert str(re) == "Disciplina existenta!"
            
        
        
        
        
        