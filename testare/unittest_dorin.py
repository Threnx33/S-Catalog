from domeniu.entitateStud import Student
from domeniu.entitateDisc import Disciplina
from domeniu.entitateNota import Nota
from validare.validareStud import ValidatorStudent
from validare.validareDisc import ValidatorDisciplina
from validare.validareNota import ValidatorNota
from infrastructura.repositoryStud import RepositoryStud, RepositoryStudFile
from infrastructura.repositoryDisc import RepositoryDisc,RepositoryDiscFile
from infrastructura.repositoryNota import RepositoryNota, RepositoryNotaFile
from business.serviceStud import ServiceStud
from business.serviceDisc import ServiceDisc
from business.serviceNota import ServiceNota
from erori.exceptii import ValidError,RepoError
import unittest as u

class TestDomainValidator(u.TestCase):
    
    def test_domain_validator(self):
        """
        test domeniu pt student
        """
        id_stud = 1
        nume_stud = "Mircea Augustin"
        stud = Student(id_stud,nume_stud)
        self.assertEqual(stud.get_id_stud(),id_stud)
        self.assertEqual(stud.get_nume_stud(),nume_stud)
        self.assertEqual(str(stud),"1 | Mircea Augustin")
        stud2 = Student(id_stud,"Horatiu Murdar")
        self.assertEqual(stud,stud2)
        """
        test validator student
        """
        validStud = ValidatorStudent()
        stud = Student(1,"Caine Rau")
        validStud.valideaza_stud(stud)
        stud2 = Student(-1,"")
        self.assertRaisesRegex(ValidError,"Id student invalid!Nume student invalid!",validStud.valideaza_stud,stud2)
        """
        test domeniu pt disc
        """
        id_disc = 1
        nume_disc = "Analiza"
        nume_prof = "Berinde Stefan"
        disc = Disciplina(id_disc,nume_disc,nume_prof)
        self.assertEqual(disc.get_id_disc(),id_disc)
        self.assertEqual(disc.get_nume_disc(),nume_disc)
        self.assertEqual(disc.get_nume_prof(),nume_prof)
        self.assertEqual(str(disc),"1 | Analiza | Berinde Stefan")
        disc2 = Disciplina(id_disc,"Logica","Pop")
        self.assertEqual(disc,disc2)
        """
        test validare disc
        """
        validDisc = ValidatorDisciplina()
        id_disc = 1
        nume_disc = "Analiza"
        nume_prof = "Berinde Stefan"
        disc = Disciplina(id_disc,nume_disc,nume_prof)
        validDisc.valideaza_disc(disc)
        disc_gresit = Disciplina(-1,"","")
        self.assertRaisesRegex(ValidError,"Id disciplina invalid!Nume disciplina invalid!Nume profesor invalid!",validDisc.valideaza_disc,disc_gresit)
        """
        test domeniu pt note
        """
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
        self.assertEqual(nota.get_id_nota(),id_nota)
        self.assertEqual(nota.get_stud(),stud)
        self.assertEqual(nota.get_disc(),disc)
        self.assertEqual(nota.get_val_nota(),val_nota)
        nota2 = Nota(id_nota,Student(0,"a"),Disciplina(0,"a","a"),5.4)
        self.assertEqual(nota,nota2)
        """
        test validare pt note - BlackBox
        """
        validNota = ValidatorNota()
        stud = Student(0,"a")
        disc = Disciplina(0,"a","a")
        validNota.valideaza_nota(Nota(3,Student(3,"Chef Scarlatescu"),Disciplina(2,"Analiza","Berinde Stefan"),5.4))
        validNota.valideaza_nota(Nota(0,Student(-1,"a"),Disciplina(0,"","a"),1))
        validNota.valideaza_nota(Nota(0,stud,disc,10))
        self.assertRaisesRegex(ValidError,"Id nota invalid! Valoare nota invalida!",validNota.valideaza_nota, Nota(-1,stud,disc,0.9) )
        self.assertRaisesRegex(ValidError,"Id nota invalid! Valoare nota invalida!",validNota.valideaza_nota, Nota(-50,stud,disc,0) )
        self.assertRaisesRegex(ValidError,"Valoare nota invalida!",validNota.valideaza_nota, Nota(0,stud,disc,-1) )
        self.assertRaisesRegex(ValidError,"Valoare nota invalida!",validNota.valideaza_nota, Nota(0,stud,disc,10.1) )
        self.assertRaisesRegex(ValidError,"Valoare nota invalida!",validNota.valideaza_nota, Nota(0,stud,disc,50) )
        
        
    
class TestRepoStud(u.TestCase):
        
    def setUp(self):
        self.__repoStud = RepositoryStud()
        self.__repoStud.adauga_stud(Student(0,"Chef Dumitrescu"))
        self.__repoStud.adauga_stud(Student(1,"Chef Scarlatescu"))
        
    def tearDown(self):
        self.__repoStud.sterge_studenti()
        
    def test_adauga_len_stud(self):
        self.assertEqual(len(self.__repoStud),2)
        self.assertRaisesRegex(RepoError,"Student existent!",self.__repoStud.adauga_stud,Student(0,"Chef Bontea"))
        self.assertEqual(len(self.__repoStud),2)
        
    def test_modifica_cauta_stud(self):
        self.__repoStud.modifica_stud(Student(1,"Chef Bontea"))
        stud = self.__repoStud.cauta_stud(1)
        self.assertEqual(stud.get_nume_stud(),"Chef Bontea")
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__repoStud.modifica_stud,Student(99,"Gicu Camataru"))
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__repoStud.cauta_stud,99)
    
    def test_sterge_get_stud(self):
        self.__repoStud.sterge_stud(1)
        studenti = self.__repoStud.get_studenti()
        self.assertEqual(studenti,[Student(0,"Chef Dumitrescu")])
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__repoStud.sterge_stud,1)
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__repoStud.sterge_stud,99)
        self.__repoStud.sterge_studenti()
        self.assertEqual(len(self.__repoStud),0)
    
    
class TestRepoStudFile(u.TestCase):
    
    def setUp(self):
        self.__repoStud = RepositoryStudFile("test_unit_lista_stud.txt")
        self.__repoStud.adauga_stud(Student(1,"Chef Scarlatescu"))
        self.__repoStud.adauga_stud(Student(2,"Chef Dumitrescu"))
    
    def tearDown(self):
        self.__repoStud.sterge_studenti()
        
    def test_load_studenti(self):
        repoStud2 = RepositoryStudFile("test_unit_lista_stud.txt")
        self.assertEqual(repoStud2.get_studenti(),[Student(1,"Chef Scarlatescu"),Student(2,"Chef Dumitrescu")])
        
    def test_append_student(self):
        self.__repoStud.adauga_stud(Student(3,"Chef Bontea"))
        repoStud2 = RepositoryStudFile("test_unit_lista_stud.txt")
        self.assertEqual(len(repoStud2),3)
    
    def test_store_student(self):
        self.__repoStud.sterge_stud(2)
        repoStud2 = RepositoryStudFile("test_unit_lista_stud.txt")
        self.assertEqual(len(repoStud2),1)
        
    
class TestSrvStud(u.TestCase):

    def setUp(self):
        self.__srvStud = ServiceStud(RepositoryStud(),ValidatorStudent())
        self.__srvStud.adauga_stud(0,"Chef Dumitrescu")
        self.__srvStud.adauga_stud(1,"Chef Scarlatescu")
    
    def tearDown(self):
        self.__srvStud.sterge_studenti()
        
    def test_adauga_len_stud(self):
        self.assertEqual(len(self.__srvStud),2)
        self.assertRaisesRegex(RepoError,"Student existent!",self.__srvStud.adauga_stud,0,"Chef Bontea")
        
    def test_modifica_cauta_stud(self):
        self.__srvStud.modifica_stud(1,"Chef Bontea")
        stud = self.__srvStud.cauta_stud(1)
        self.assertEqual(stud.get_nume_stud(),"Chef Bontea")
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__srvStud.modifica_stud,99,"Gicu Camataru")
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__srvStud.cauta_stud,99)
    
    def test_sterge_get_stud(self):
        self.__srvStud.sterge_stud(1)
        studenti = self.__srvStud.get_studenti()
        self.assertEqual(studenti,[Student(0,"Chef Dumitrescu")])
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__srvStud.sterge_stud,1)
        self.assertRaisesRegex(RepoError,"Student inexistent!",self.__srvStud.sterge_stud,99)
        self.__srvStud.sterge_studenti()
        self.assertEqual(len(self.__srvStud),0)
    

class TestRepoDisc(u.TestCase):
    
    def setUp(self):
        self.__repoDisc = RepositoryDisc()
        self.__repoDisc.adauga_disc(Disciplina(0,"Analiza","Berinde"))
        self.__repoDisc.adauga_disc(Disciplina(1,"Algebra","Mo2"))
    
    def test_adauga_len_disc(self):
        self.assertEqual(len(self.__repoDisc),2)
        self.assertRaisesRegex(RepoError,"Disciplina existenta!",self.__repoDisc.adauga_disc,Disciplina(1,"Algbra","Mo2"))
        self.assertEqual(len(self.__repoDisc),2)
    
    def test_modifica_cauta_disc(self):
        self.__repoDisc.modifica_disc(Disciplina(1,"Logica","Pop :|"))
        self.assertEqual(self.__repoDisc.cauta_disc(1),Disciplina(1,"Logica","Pop"))
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__repoDisc.modifica_disc,Disciplina(99,"Sport","Gicu Camataru"))
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__repoDisc.cauta_disc,99)
        
    def test_sterge_get_disc(self):
        self.__repoDisc.sterge_disc(1)
        self.assertEqual(self.__repoDisc.get_discipline(),[Disciplina(0,"Analiza","Berinde")])
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__repoDisc.sterge_disc,1)
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__repoDisc.sterge_disc,99)
        self.__repoDisc.sterge_discipline()
        self.assertEqual(len(self.__repoDisc),0)


class TestRepoDiscFile(u.TestCase):
    
    def setUp(self):
        self.__repoDisc = RepositoryDiscFile("test_unit_lista_disc.txt")
        self.__repoDisc.adauga_disc(Disciplina(0,"Analiza","Berinde"))
        self.__repoDisc.adauga_disc(Disciplina(1,"Algebra","Mo2"))
    
    def tearDown(self):
        self.__repoDisc.sterge_discipline()
        
    def test_load_discipline(self):
        repoDisc2 = RepositoryDiscFile("test_unit_lista_disc.txt")
        self.assertEqual(repoDisc2.get_discipline(),[Disciplina(0,"Analiza","Berinde"),Disciplina(1,"Algebra","Mo2")])
    
    def test_append_disc(self):
        self.__repoDisc.adauga_disc(Disciplina(2,"Logica","Pop :|"))
        repoDisc2 = RepositoryDiscFile("test_unit_lista_disc.txt")
        self.assertEqual(len(repoDisc2),3)
        
    def test_store_discipline(self):
        self.__repoDisc.sterge_disc(1)
        repoDisc2 = RepositoryDiscFile("test_unit_lista_disc.txt")
        self.assertEqual(len(repoDisc2),1)
        

class TestSrvDisc(u.TestCase):
    
    def setUp(self):
        self.__srvDisc = ServiceDisc(RepositoryDisc(),ValidatorDisciplina())
        self.__srvDisc.adauga_disc(0,"Analiza","Berinde")
        self.__srvDisc.adauga_disc(1,"Algebra","Mo2")
    
    def test_adauga_len_disc(self):
        self.assertEqual(len(self.__srvDisc),2)
        self.assertRaisesRegex(RepoError,"Disciplina existenta!",self.__srvDisc.adauga_disc,1,"Algbra","Mo2")
    
    def test_modifica_cauta_disc(self):
        self.__srvDisc.modifica_disc(1,"Logica","Pop :|")
        self.assertEqual(self.__srvDisc.cauta_disc(1),Disciplina(1,"Logica","Pop"))
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__srvDisc.modifica_disc,99,"Sport","Gicu Camataru")
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__srvDisc.cauta_disc,99)
        
    def test_sterge_get_disc(self):
        self.__srvDisc.sterge_disc(1)
        self.assertEqual(self.__srvDisc.get_discipline(),[Disciplina(0,"Analiza","Berinde")])
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__srvDisc.sterge_disc,1)
        self.assertRaisesRegex(RepoError,"Disciplina inexistenta!",self.__srvDisc.sterge_disc,99)
        self.__srvDisc.sterge_discipline()
        self.assertEqual(len(self.__srvDisc),0)
        

class TestRepoNota(u.TestCase):
    
    def setUp(self):
        self.__repoNota = RepositoryNota()
        self.__repoNota.adauga_nota(Nota(0,Student(0,"Chef Scarlatescu"),Disciplina(0,"Analiza","Berinde"),10))
        self.__repoNota.adauga_nota(Nota(1,Student(1,"Chef Dumitrescu"),Disciplina(1,"Algebra","Modoi"),4.5))
        self.__repoNota.adauga_nota(Nota(3,Student(0,"Chef Scarlatescu"),Disciplina(1,"Algebra","Modoi"),8.55))
    
    def test_adaugare_len_nota(self):
        self.assertEqual(len(self.__repoNota),3)
        self.assertRaisesRegex(RepoError,"Nota existenta!",self.__repoNota.adauga_nota,Nota(3,Student(0,"Chef Scarlatescu"),Disciplina(1,"Algebra","Modoi"),8.55))
        self.assertEqual(len(self.__repoNota),3)
    
    def test_modifica_cauta_nota(self):
        self.__repoNota.modifica_nota(Nota(3,Student(5,"Gicu Camataru"),Disciplina(5,"Sport","Nicu Camataru"),1))
        self.assertEqual(self.__repoNota.cauta_nota(3).get_stud(),Student(5,"Gicu Camataru"))
        self.assertRaisesRegex(RepoError,"Nota inexistenta!",self.__repoNota.modifica_nota,Nota(99,Student(5,"Gicu Camataru"),Disciplina(5,"Sport","Nicu Camataru"),1))
        self.assertRaisesRegex(RepoError,"Nota inexistenta!",self.__repoNota.cauta_nota,99)
    
    def test_sterge_get_nota(self):
        self.__repoNota.sterge_nota(1)
        self.assertEqual(self.__repoNota.get_note(),[Nota(0,Student(0,"Chef Scarlatescu"),Disciplina(0,"Analiza","Berinde"),10),Nota(3,Student(0,"Chef Scarlatescu"),Disciplina(1,"Algebra","Modoi"),8.55)])
        self.assertRaisesRegex(RepoError,"Nota inexistenta!",self.__repoNota.sterge_nota,99)
        self.__repoNota.sterge_note()
        self.assertEqual(len(self.__repoNota),0)
    
    def test_get_note_by_disc(self):
        self.assertEqual(self.__repoNota.get_note_by_disc(Disciplina(1,"Algebra","Modoi")),[["Chef Dumitrescu",4.5],["Chef Scarlatescu",8.55]])
        self.assertEqual(self.__repoNota.get_note_by_disc(Disciplina(0,"Analiza","Berinde")),[["Chef Scarlatescu",10]])
        self.assertEqual(self.__repoNota.get_note_by_disc(Disciplina(99,"a","a")),[])
    
    def test_modifica_stud_note(self):
        self.__repoNota.modifica_stud_note(Student(0,"Chef Bontea"))
        note = [Nota(0,Student(0,"Chef Bontea"),Disciplina(0,"Analiza","Berinde"),10), Nota(1,Student(1,"Chef Dumitrescu"),Disciplina(1,"Algebra","Modoi"),4.5), Nota(3,Student(0,"Chef Bontea"),Disciplina(1,"Algebra","Modoi"),8.55)]
        self.assertEqual(self.__repoNota.get_note(),note)
        self.__repoNota.modifica_stud_note(Student(99,"a"))
        self.assertEqual(self.__repoNota.get_note(),note) 
    
    def test_modifica_disc_note(self):
        self.__repoNota.modifica_disc_note(Disciplina(1,"Logica","Pop"))
        note = [Nota(0,Student(0,"Chef Scarlatescu"),Disciplina(0,"Analiza","Berinde"),10), Nota(1,Student(1,"Chef Dumitrescu"),Disciplina(1,"Logica","Pop"),4.5), Nota(3,Student(0,"Chef Scarlatescu"),Disciplina(1,"Logica","Pop"),8.55)]
        self.assertEqual(self.__repoNota.get_note(),note)
        self.__repoNota.modifica_disc_note(Disciplina(99,"a","a"))
        self.assertEqual(self.__repoNota.get_note(),note)
    
    def test_sterge_note_stud(self):
        self.__repoNota.sterge_note_stud(0)
        note = [Nota(1,Student(1,"Chef Dumitrescu"),Disciplina(1,"Algebra","Modoi"),4.5)]
        self.assertEqual(self.__repoNota.get_note(),note)
        self.__repoNota.sterge_note_stud(99)
        self.assertEqual(self.__repoNota.get_note(),note)
        
    def test_sterge_note_disc(self):
        self.__repoNota.sterge_note_disc(1)
        note = [Nota(0,Student(0,"Chef Scarlatescu"),Disciplina(0,"Analiza","Berinde"),10)]
        self.assertEqual(self.__repoNota.get_note(),note)
        self.__repoNota.sterge_note_disc(99)
        self.assertEqual(self.__repoNota.get_note(),note)


class TestRepoNotaFile(u.TestCase):
    
    def setUp(self):
        self.__repoNota = RepositoryNotaFile("test_unit_lista_note.txt")
        self.__repoNota.adauga_nota(Nota(0,Student(0,"Chef Scarlatescu"),Disciplina(0,"Analiza","Berinde"),10))
        self.__repoNota.adauga_nota(Nota(1,Student(1,"Chef Dumitrescu"),Disciplina(1,"Algebra","Modoi"),4.5))
        self.__repoNota.adauga_nota(Nota(3,Student(0,"Chef Scarlatescu"),Disciplina(1,"Algebra","Modoi"),8.55))
    
    def tearDown(self):
        self.__repoNota.sterge_note()
    
    def test_load_note(self):
        repoNota2 = RepositoryNotaFile("test_unit_lista_note.txt")
        self.assertEqual(repoNota2.get_note(), [Nota(0,Student(0,"Chef Scarlatescu"),Disciplina(0,"Analiza","Berinde"),10), Nota(1,Student(1,"Chef Dumitrescu"),Disciplina(1,"Algebra","Modoi"),4.5), Nota(3,Student(0,"Chef Scarlatescu"),Disciplina(1,"Algebra","Modoi"),8.55) ] )
    
    def test_append_nota(self):
        self.__repoNota.adauga_nota(Nota(2,Student(3,"Gicu Camataru"),Disciplina(4,"Sport","Gicu Necamataru"),10))
        repoNota2 = RepositoryNotaFile("test_unit_lista_note.txt")
        self.assertEqual(len(repoNota2), 4)
    
    def test_store_note(self):
        self.__repoNota.sterge_nota(1)
        repoNota2 = RepositoryNotaFile("test_unit_lista_note.txt")
        self.assertEqual(len(repoNota2), 2)
        
        
class TestSrvNota(u.TestCase):
    
    def setUp(self):
        self.__repoStud = RepositoryStud()
        self.__repoStud.adauga_stud(Student(0,"Chef Dumitrescu"))
        self.__repoStud.adauga_stud(Student(1,"Chef Scarlatescu"))
        self.__repoStud.adauga_stud(Student(2,"Chef Bontea"))
        self.__repoStud.adauga_stud(Student(3,"Chef Dorin"))
        self.__repoDisc = RepositoryDisc()
        self.__repoDisc.adauga_disc(Disciplina(0,"Analiza","Berinde"))
        self.__repoDisc.adauga_disc(Disciplina(1,"Algebra","Mo2"))
        self.__repoDisc.adauga_disc(Disciplina(2,"Logica","Pop"))
        self.__repoNota = RepositoryNota()
        self.__srvNota = ServiceNota( self.__repoNota, ValidatorNota(), self.__repoStud, ValidatorStudent(), self.__repoDisc, ValidatorDisciplina(),)
        self.__srvNota.adauga_nota(0,0,0,10)
        self.__srvNota.adauga_nota(2,0,1,10)
        self.__srvNota.adauga_nota(4,0,2,10)
        self.__srvNota.adauga_nota(1,1,1,4.5)
        self.__srvNota.adauga_nota(3,2,1,7.5)
        self.__srvNota.adauga_nota(5,1,2,9.5)
    
    def test_adaugare_len_nota(self):
        self.assertEqual(len(self.__srvNota),6)
        self.assertRaisesRegex(RepoError,"Nota existenta!",self.__srvNota.adauga_nota,0,0,0,8.6)
        self.assertEqual(len(self.__srvNota),6)
    
    def test_modifica_cauta_nota(self):
        self.__srvNota.modifica_nota(3,1,0,2.5)
        self.assertEqual(self.__srvNota.cauta_nota(3),Nota(3,Student(1,"Chef Scarlatescu"),Disciplina(0,"Analiza","Berinde"),2.5))
        self.assertRaisesRegex(RepoError,"Nota inexistenta!",self.__srvNota.modifica_nota,99,2,1,10)
        self.assertRaisesRegex(RepoError,"Nota inexistenta!",self.__srvNota.cauta_nota,99)
    
    def test_sterge_get_nota(self):
        self.__srvNota.sterge_nota(1)
        self.assertEqual(len(self.__srvNota),5)
        self.assertRaisesRegex(RepoError,"Nota inexistenta!",self.__srvNota.sterge_nota,99)
        self.__srvNota.sterge_note()
        self.assertEqual(len(self.__srvNota),0)
    
    def test_sort_by_nume(self):
        note_disc = self.__repoNota.get_note_by_disc(Disciplina(1,"Algebra","Mo2"))#[['Chef Dumitrescu', 10], ['Chef Scarlatescu', 4.5], ['Chef Bontea', 7.5]]
        self.__srvNota.sort_by_nume_stud(note_disc)
        self.assertEqual(note_disc,[['Chef Bontea', 7.5], ['Chef Dumitrescu', 10], ['Chef Scarlatescu', 4.5]])

    def test_sort_by_nota(self):
        note_disc = self.__repoNota.get_note_by_disc(Disciplina(1,"Algebra","Mo2"))#[['Chef Dumitrescu', 10], ['Chef Scarlatescu', 4.5], ['Chef Bontea', 7.5]]
        self.__srvNota.sort_by_nota(note_disc)
        self.assertEqual(note_disc,[ ['Chef Dumitrescu', 10], ['Chef Bontea', 7.5], ['Chef Scarlatescu', 4.5] ])
    
    def test_get_lista_nume_si_medie_AND_get_sort_medii(self):
        studenti = self.__repoStud.get_studenti()
        note = self.__repoNota.get_note()
        stud_si_medii = self.__srvNota.get_lista_nume_si_medie(studenti, note)
        self.assertEqual(stud_si_medii, [ ["Chef Dumitrescu",10], ["Chef Scarlatescu",7], ["Chef Bontea",7.5], ["Chef Dorin",0] ] )
        self.__srvNota.get_sort_nume_si_medie(stud_si_medii)
        self.assertEqual(stud_si_medii, [ ["Chef Dumitrescu",10], ["Chef Bontea",7.5], ["Chef Scarlatescu",7], ["Chef Dorin",0] ] )
    
    def test_get_sorted_note_disc_by_nume_sau_nota(self):
        note_disc, nume_disc = self.__srvNota.get_sorted_note_disc_by_nume_sau_nota(1, 0)#nesortat[['Chef Dumitrescu', 10], ['Chef Scarlatescu', 4.5], ['Chef Bontea', 7.5]]
        self.assertEqual(note_disc,[['Chef Bontea', 7.5], ['Chef Dumitrescu', 10], ['Chef Scarlatescu', 4.5]] )
        note_disc2, nume_disc2 = self.__srvNota.get_sorted_note_disc_by_nume_sau_nota(1, 1)
        self.assertEqual(note_disc2,[ ['Chef Dumitrescu', 10], ['Chef Bontea', 7.5], ['Chef Scarlatescu', 4.5] ])
        
    def test_get_top_medii(self):
        self.assertEqual(self.__srvNota.get_top_medii(),[ ['Chef Dumitrescu', 10] ])
        
        
        
if __name__ == "__main__":
    u.main()
        
        
        
        
        
        
        
        
        
        
        
        