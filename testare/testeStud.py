from domeniu.entitateStud import Student
from validare.validareStud import ValidatorStudent
from infrastructura.repositoryStud import RepositoryStud
from business.serviceStud import ServiceStud
from erori.exceptii import ValidError,RepoError

class TesteStud:

    def test_domeniuStud(self):
        id_stud = 1
        nume_stud = "Mircea Augustin"
        stud = Student(id_stud,nume_stud)
        assert stud.get_id_stud() == id_stud
        assert stud.get_nume_stud() == nume_stud
        assert str(stud) == "1 | Mircea Augustin"
        stud2 = Student(id_stud,"Horatiu Murdar")
        assert stud == stud2
        
        
    def test_validareStud(self):
        validStud = ValidatorStudent()
        stud = Student(1,"Caine Rau")
        validStud.valideaza_stud(stud)
        stud2 = Student(-1,"")
        try:
            validStud.valideaza_stud(stud2)
            assert False
        except ValidError as ve:
            assert str(ve) == "Id student invalid!Nume student invalid!"
    
    
    def test_repoStud(self, repoStud,lung_init):
        assert len(repoStud) == 0+lung_init
        id_stud = 0
        nume_stud = "Mircea Augustin"
        stud = Student(id_stud,nume_stud)
        repoStud.adauga_stud(stud)
        assert len(repoStud) == 1+lung_init
        try:
            repoStud.adauga_stud(stud)
            assert False
        except RepoError as re:
            assert str(re) == "Student existent!"
        gasit = repoStud.cauta_stud(id_stud)
        assert gasit.get_nume_stud() == "Mircea Augustin"
        try:
            repoStud.cauta_stud(id_stud+99)
            assert False
        except RepoError as re:
            assert str(re) == "Student inexistent!" 
        stud_modif = Student(id_stud,"Mirciulica Schimbat")
        repoStud.modifica_stud(stud_modif)
        gasit = repoStud.cauta_stud(id_stud)
        assert gasit.get_nume_stud() == "Mirciulica Schimbat"
        stud_modif_rau = Student(id_stud+99,"")
        try:
            repoStud.modifica_stud(stud_modif_rau)
            assert False
        except RepoError as re:
            assert str(re) == "Student inexistent!"
        alll = repoStud.get_studenti()
        assert len(alll) == 1+lung_init
        repoStud.sterge_stud(id_stud)
        assert len(repoStud) == 0+lung_init
        try:
            repoStud.sterge_stud(id_stud)
            assert False
        except RepoError as re:
            assert str(re) == "Student inexistent!"
        
        
    def test_srvStud(self):
        repoStud = RepositoryStud()
        validStud = ValidatorStudent()
        srvStud = ServiceStud(repoStud,validStud)
        id_stud = 1
        nume_stud = "Mircea Augustin"
        srvStud.adauga_stud(id_stud,nume_stud)
        studenti = srvStud.get_studenti()
        assert len(studenti) == 1
        assert studenti[0].get_id_stud() == id_stud
        assert studenti[0].get_nume_stud() == nume_stud
        try: 
            srvStud.adauga_stud(id_stud,nume_stud)
            assert False
        except RepoError as re:
            assert str(re) == "Student existent!"
        srvStud.sterge_stud(id_stud)
        assert len(srvStud) == 0
        try:
            srvStud.sterge_stud(id_stud)
            assert False
        except RepoError as re:
            assert str(re) == "Student inexistent!"

    
    def test_repoStudFile(self,repoStudF):
        lung_init = len(repoStudF)
        assert lung_init == 6
        self.test_repoStud(repoStudF,lung_init)
        id_stud = 1
        nume_stud = "Mircea Augustin"
        stud = Student(id_stud,nume_stud)
        try:
            repoStudF.adauga_stud(stud)
            assert False
        except RepoError as re:
            assert str(re) == "Student existent!"
        assert len(repoStudF) == lung_init
        
        
        
            
    