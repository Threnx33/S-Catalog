from domeniu.entitateStud import Student
from domeniu.entitateDisc import Disciplina
from domeniu.entitateNota import Nota
from validare.validareNota import ValidatorNota
from validare.validareDisc import ValidatorDisciplina
from validare.validareStud import ValidatorStudent
from infrastructura.repositoryNota import RepositoryNota, RepositoryNotaFile
from infrastructura.repositoryStud import RepositoryStud
from infrastructura.repositoryDisc import RepositoryDisc
from business.serviceNota import ServiceNota
from erori.exceptii import ValidError,RepoError

class TesteNota:

    def test_domeniuNota(self):
        id_nota = 0
        id_stud = 3
        nume_stud = "Mircea Augustin"
        stud = Student(id_stud,nume_stud)
        id_disc = 2
        nume_disc = "Analiza"
        nume_prof = "Berinde Stefan"
        disc = Disciplina(id_disc,nume_disc,nume_prof)
        val_nota = 9.5
        nota = Nota(id_nota,stud,disc,val_nota)
        assert nota.get_id_nota() == id_nota
        assert nota.get_stud() == stud
        assert nota.get_disc() == disc
        assert abs(nota.get_val_nota() - val_nota) < 0.0001
        nota2 = Nota(id_nota,Student(0,"a"),Disciplina(0,"a","a"),5.4)
        assert nota == nota2
        
    
    def test_validareNota(self):
        validNota = ValidatorNota()
        id_nota = 0
        stud = Student(3,"Mircea Augustin")
        disc = Disciplina(2,"Analiza","Berinde Stefan")
        val_nota = 9.5
        nota = Nota(id_nota,stud,disc,val_nota)
        validNota.valideaza_nota(nota)
        nota_gresita = Nota(-1,stud,disc,10.3)
        try:
            validNota.valideaza_nota(nota_gresita)
            assert False
        except ValidError as ve:
            assert str(ve) == ("Id nota invalid! Valoare nota invalida!")
            
            
    def __ex_valori_note(self,repoNota):
        id_disc = 1
        disc = Disciplina(id_disc,"Analiza","Berinde")
        disc2 = Disciplina(3,"ASC","Vancea")
        disc3 = Disciplina(4,"LC","Pop")
        repoNota.adauga_nota(Nota(1,Student(1,"nutu"),disc,5))
        repoNota.adauga_nota(Nota(10,Student(7,"bologneze"),disc2,9))
        repoNota.adauga_nota(Nota(2,Student(2,"andrei"),disc,10))
        repoNota.adauga_nota(Nota(5,Student(4,"aandrei"),disc,4.5))
        repoNota.adauga_nota(Nota(8,Student(2,"andrei"),disc2,8.6))
        repoNota.adauga_nota(Nota(3,Student(2,"andrei"),disc3,1))
        repoNota.adauga_nota(Nota(9,Student(1,"nutu"),disc,7))
    
    
    def test_repoNota(self):
        repoNota = RepositoryNota()
        id_nota = 0
        stud = Student(3,"Mircea Augustin")
        disc = Disciplina(2,"Analiza","Berinde Stefan")
        val_nota = 9.5
        nota = Nota(id_nota,stud,disc,val_nota)
        repoNota.adauga_nota(nota)
        assert len(repoNota) == 1
        try:
            repoNota.adauga_nota(nota)
            assert False
        except RepoError as re:
            assert str(re) == "Nota existenta!"
        assert len(repoNota) == 1
        stud2 = Student(2,"Andrei George")
        nota_modif = Nota(id_nota,stud2,disc,10)
        repoNota.modifica_nota(nota_modif)
        nota_modif_gr = Nota(id_nota+5,stud2,disc,4)
        try:
            repoNota.modifica_nota(nota_modif_gr)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
        gasit = repoNota.cauta_nota(id_nota)
        assert gasit == nota_modif
        try:
            repoNota.cauta_nota(id_nota+5)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
        tot = repoNota.get_note()
        assert len(tot) == 1
        try:
            repoNota.sterge_nota(id_nota+5)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
        repoNota.sterge_nota(id_nota)
        assert len(repoNota) == 0
        try:
            repoNota.sterge_nota(id_nota)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
            
            
        """
        test get toate notele de la o disciplina
        """      
        self.__ex_valori_note(repoNota)
        disc = Disciplina(1,"Analiza","Berinde")
        note_disc = repoNota.get_note_by_disc(disc)
        assert note_disc == [["nutu",5],["andrei",10],["aandrei",4.5],["nutu",7]]
        disc2 = Disciplina(5,"Sport","HabarNam")
        note_disc2 = repoNota.get_note_by_disc(disc2)
        assert note_disc2 == []
        
        """
        test modifica note de la stud
        """
        stud_modif = Student(2,"andrei")
        repoNota.modifica_stud_note(stud_modif)
        tot_note = repoNota.get_note()
        assert tot_note[2].get_stud() == stud_modif
        assert tot_note[4].get_stud() == stud_modif
        assert tot_note[5].get_stud() == stud_modif
        
        
        """
        test modifica note de la disc
        """
        disc_modif = Disciplina(3,"TIC","Amanoae")
        repoNota.modifica_disc_note(disc_modif)
        tot_note = repoNota.get_note()
        assert tot_note[1].get_disc() == disc_modif
        assert tot_note[4].get_disc() == disc_modif
        
        
        """
        test sterge note de la stud
        """
        id_stud = 2
        repoNota.sterge_note_stud(id_stud)
        assert len(repoNota) == 4
        id_stud2 = 7
        repoNota.sterge_note_stud(id_stud2)
        assert len(repoNota) == 3
        id_stud3 = 99
        repoNota.sterge_note_stud(id_stud3)
        assert len(repoNota) == 3
        
        
        """
        test sterge note de la stud
        """
        repoNota.sterge_note()
        self.__ex_valori_note(repoNota)
        assert len(repoNota) == 7
        id_disc = 1
        repoNota.sterge_note_disc(id_disc)
        assert len(repoNota) == 3
        id_disc2 = 10
        repoNota.sterge_note_disc(id_disc2)
        assert len(repoNota) == 3
        id_disc3 = 3
        repoNota.sterge_note_disc(id_disc3)
        assert len(repoNota) == 1
        id_disc4 = 4
        repoNota.sterge_note_disc(id_disc4)
        assert len(repoNota) == 0
    
    
    def test_srvNota(self):
        repoNota = RepositoryNota()
        repoDisc = RepositoryDisc()
        repoDisc.adauga_disc(Disciplina(1,"Analiza","Berinde"))
        srvNota = ServiceNota(repoNota,ValidatorNota(),RepositoryStud(),ValidatorStudent(),repoDisc,ValidatorDisciplina())
        
        """
        test sotare by nume
        """
        id_disc = 1
        self.__ex_valori_note(repoNota)
        sorted_note_disc3,nume_disc = srvNota.get_sorted_note_disc_by_nume_sau_nota(id_disc,0)
        assert sorted_note_disc3 == [["aandrei",4.5],["andrei",10],["nutu",7],["nutu",5]]
        assert nume_disc == "Analiza"
        
        
        
    
    def test_repoNotaFile(self,file,file2):
        repoNotaF = RepositoryNotaFile(file)
        repoNotaF2 = RepositoryNotaFile(file2)
        note = repoNotaF2.get_note()
        assert abs(note[0].get_val_nota()-9.95) < 0.001
        repoNotaF.set_note(note)
        #daca pun cele 5 valori din fisierul "valori" ca sa verific load
        assert len(repoNotaF) == 6
        id_nota = 1
        nota_cautata = repoNotaF.cauta_nota(id_nota)
        assert abs(nota_cautata.get_val_nota()-9.95) < 0.001
        
        id_nota2 = 9
        stud2 = Student(3,"Messi")
        disc2 = Disciplina(5,"Sport","Prof Sport")
        val_nota2 = 10
        nota2 = Nota(id_nota2,stud2,disc2,val_nota2)
        repoNotaF.adauga_nota(nota2) # 9,3,Messi,5,Sport,Prof Sport
        assert len(repoNotaF) == 1+6
        id_nota = 0
        stud = Student(3,"Messi")
        disc = Disciplina(2,"Analiza","Berinde Stefan")
        val_nota = 9.5
        nota = Nota(id_nota,stud,disc,val_nota)
        repoNotaF.adauga_nota(nota)
        assert len(repoNotaF) == 2+6
        try:
            repoNotaF.adauga_nota(nota)
            assert False
        except RepoError as re:
            assert str(re) == "Nota existenta!"
        assert len(repoNotaF) == 2+6
        try:
            repoNotaF.adauga_nota(Nota(1,Student(99,"a"),Disciplina(99,"a","a"),10))
            assert False
        except RepoError as re:
            assert str(re) == "Nota existenta!"
        stud2 = Student(11,"Andrei George")
        nota_modif = Nota(id_nota,stud2,disc,10)
        repoNotaF.modifica_nota(nota_modif)
        nota_modif_gr = Nota(id_nota+99,stud2,disc,4)
        try:
            repoNotaF.modifica_nota(nota_modif_gr)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
        gasit = repoNotaF.cauta_nota(id_nota)
        assert gasit == nota_modif
        try:
            repoNotaF.cauta_nota(id_nota+99)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
        tot = repoNotaF.get_note()
        assert len(tot) == 2+6
        try:
            repoNotaF.sterge_nota(id_nota+99)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
        repoNotaF.sterge_nota(id_nota)
        assert len(repoNotaF) == 1+6
        try:
            repoNotaF.sterge_nota(id_nota)
            assert False
        except RepoError as re:
            assert str(re) == "Nota inexistenta!"
            
            
        """
        test get toate notele de la o disciplina
        """      
        disc = Disciplina(1,"a","a")
        note_disc = repoNotaF.get_note_by_disc(disc)
        assert note_disc == [["Chef Scarlatescu",9.95],["Chef Dumitrescu",9.8],["Messi",7.474]]
        disc2 = Disciplina(99,"a","a")
        note_disc2 = repoNotaF.get_note_by_disc(disc2)
        assert note_disc2 == []
        
        """
        test sterge note de la stud
        """
        id_stud = 2
        repoNotaF.sterge_note_stud(id_stud)
        assert len(repoNotaF) == 5
        id_stud2 = 99
        repoNotaF.sterge_note_stud(id_stud2)
        assert len(repoNotaF) == 5
        id_stud3 = 3
        repoNotaF.sterge_note_stud(id_stud3)
        assert len(repoNotaF) == 3
    
    
        """
        test sterge note de la disc
        """
        assert len(repoNotaF) == 3
        id_disc = 2
        repoNotaF.sterge_note_disc(id_disc)
        assert len(repoNotaF) == 1
        id_disc2 = 99
        repoNotaF.sterge_note_disc(id_disc2)
        assert len(repoNotaF) == 1
    
    
    def test_func(self):
        repoStud = RepositoryStud()
        srvNota = ServiceNota(RepositoryNota(),ValidatorNota(),repoStud,ValidatorStudent(),RepositoryDisc(),ValidatorDisciplina())
        note_disc = [["nutu",5],["andrei",10],["aandrei",4.5],["nutu",7],["cosmin",10]]
        srvNota.sort_by_nume_stud(note_disc)
        assert note_disc == [["aandrei",4.5],["andrei",10],["cosmin",10],["nutu",7],["nutu",5]]
        note_disc2 = []
        srvNota.sort_by_nume_stud(note_disc2)
        assert note_disc2 == []
        
        note_disc3 = [["nutu",5],["cosmin",10],["andrei",10],["aandrei",4.5],["nutu",7]]
        srvNota.sort_by_nota(note_disc3)
        assert note_disc3 == [["andrei",10],["cosmin",10],["nutu",7],["nutu",5],["aandrei",4.5]]
        note_disc4 = []
        srvNota.sort_by_nota(note_disc4)
        assert note_disc4 == []
        
        s1 = Student(1,"Chef Scarlatescu")
        s2 = Student(2,"Chef Dumitrescu")
        s3 = Student(5,"Turturica Dorin")
        repoStud.adauga_stud(s1)
        repoStud.adauga_stud(s2)
        repoStud.adauga_stud(Student(3,"Messi"))
        repoStud.adauga_stud(Student(4,"Ronaldo"))
        repoStud.adauga_stud(s3)
        repoStud.adauga_stud(Student(6,"a"))
        repoStud.adauga_stud(Student(7,"b"))
        repoStud.adauga_stud(Student(8,"c"))
        repoStud.adauga_stud(Student(9,"d"))
        repoStud.adauga_stud(Student(10,"e"))
        studenti = repoStud.get_studenti()
        d1 = Disciplina(1,"Analiza","Berinde")
        d2 = Disciplina(2,"Algebra","Mo2")
        d3 = Disciplina(4,"ASC","Vancea")
        note = [Nota(1,s1,d1,9.95),Nota(2,s2,d2,5),Nota(3,s2,d1,9.80),Nota(4,s2,d1,7),Nota(6,s1,d3,9),Nota(7,s3,d1,10)]
        medii = srvNota.get_lista_nume_si_medie(studenti,note)
        assert abs(medii[0][1]-9.475) < 0.001
        assert abs(medii[1][1]-7.2666) < 0.1
        assert abs(medii[4][1]-10) < 0.001
        assert abs(medii[2][1]-0) < 0.001
        
        
        
        