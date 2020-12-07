from domeniu.entitateUndoRedo import ActiuneUndo
from infrastructura.repositoryStud import RepositoryStud
from domeniu.entitateStud import Student
from infrastructura.repositoryUndo import RepositoryUndo
from erori.exceptii import RepoError
from business.serviceUndo import ServiceUndo
from business.serviceStud import ServiceStudUndo
from validare.validareStud import ValidatorStudent

class TesteUndo:
    
    
    def test_domeniuUndo(self):
        repoStud = RepositoryStud()
        cmd_undo = repoStud.sterge_stud
        cmd_redo = repoStud.adauga_stud
        id_stud = 1
        nume_stud = "Dorin"
        stud = Student(id_stud,nume_stud)
        actUndo = ActiuneUndo(cmd_undo,cmd_redo,id_stud,stud)
        assert actUndo.get_cmd_undo() == cmd_undo
        assert actUndo.get_cmd_redo() == cmd_redo
        assert actUndo.get_entitate_undo() == id_stud
        assert actUndo.get_entitate_redo() == stud
        
    
    def test_repoUndo(self):
        repoUndo = RepositoryUndo()
        try:
            repoUndo.peek()
            assert False
        except RepoError as re:
            assert str(re) == "Undo indisponibil!"
        repoStud = RepositoryStud()
        cmd_undo = repoStud.sterge_stud
        cmd_redo = repoStud.adauga_stud
        id_stud = 1
        nume_stud = "Dorin"
        stud = Student(id_stud,nume_stud)
        actUndo = ActiuneUndo(cmd_undo,cmd_redo,id_stud,stud)
        repoUndo.push(actUndo)
        assert len(repoUndo) == 1
        assert repoUndo.peek() == actUndo
        cmd_undo2 = repoStud.adauga_stud
        cmd_redo2 = repoStud.sterge_stud
        id_stud2 = 2
        nume_stud2 = "Dorin2"
        stud2 = Student(id_stud2,nume_stud2)
        actUndo2 = ActiuneUndo(cmd_undo2,cmd_redo2,stud2,id_stud2)
        repoUndo.push(actUndo2)
        assert len(repoUndo) == 2
        assert repoUndo.peek() == actUndo2
        repoUndo.pop()
        assert len(repoUndo) == 1
        cmd_undo3 = repoStud.modifica_stud
        cmd_redo3 = repoStud.modifica_stud
        id_stud3 = 1
        nume_stud3 = "Dorin3"
        stud3_precedent = Student(id_stud3,nume_stud)
        stud3 = Student(id_stud3,nume_stud3)
        actUndo3 = ActiuneUndo(cmd_undo3,cmd_redo3,stud3_precedent,stud3)
        repoUndo.push(actUndo3)
        assert len(repoUndo) == 2
        assert repoUndo.peek() == actUndo3
        try:
            repoUndo.pull()
            assert False
        except RepoError as re:
            assert str(re) == "Redo indisponibil!"
        repoUndo.pop()
        assert len(repoUndo) == 1
        repoUndo.pop()
        assert len(repoUndo) == 0
        try:
            repoUndo.peek()
            assert False
        except RepoError as re:
            assert str(re) == "Undo indisponibil!"
        repoUndo.pull()
        assert len(repoUndo) == 1

    
    def test_srvUndo(self):
        repoUndo = RepositoryUndo()
        srvUndo = ServiceUndo(repoUndo)
        srvStud = ServiceStudUndo(RepositoryStud(),ValidatorStudent(),repoUndo)
        id_stud = 1
        nume_stud = "Dorin"
        stud = Student(id_stud,nume_stud)
        srvStud.adauga_stud(id_stud, nume_stud)
        id_stud2 = 2
        nume_stud2 = "Dorin2"
        srvStud.adauga_stud(id_stud2, nume_stud2)
        srvUndo.act_undo()
        assert len(srvStud) == 1
        srvUndo.act_undo()
        assert len(srvStud) == 0
        srvUndo.act_redo()
        assert len(srvStud) == 1
        tot = srvStud.get_studenti()
        assert tot == [stud]
        nume_stud_modif = "Dorin3"
        stud_modif = Student(id_stud,nume_stud_modif)
        srvStud.modifica_stud(id_stud, nume_stud_modif)
        srvUndo.act_undo()
        tot2 = srvStud.get_studenti()
        assert tot2 == [stud]
        srvUndo.act_redo()
        tot3 = srvStud.get_studenti()
        assert tot3 == [stud_modif]
        
        
    
        
        
        
    
    
        
    
        
        
        