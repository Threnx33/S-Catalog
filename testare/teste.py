from testare.testeStud import TesteStud
from testare.testeDisc import TesteDisc
from testare.testeNota import TesteNota
from testare.testUndo import TesteUndo
from infrastructura.repositoryStud import RepositoryStud, RepositoryStudFile
from infrastructura.repositoryDisc import RepositoryDisc, RepositoryDiscFile

class Teste:
        
    def ruleaza_teste(self):
        """teste student"""
        ts = TesteStud()
        ts.test_domeniuStud()
        ts.test_validareStud()
        repoStud = RepositoryStud()
        ts.test_repoStud(repoStud,0)
        repoStudF = RepositoryStudFile("testare/test_lista_stud.txt")
        ts.test_repoStudFile(repoStudF)
        ts.test_srvStud()
        """teste disciplina"""
        td = TesteDisc()
        td.test_domeniuDisc()
        td.test_validareDisc()
        repoDisc = RepositoryDisc()
        td.test_repoDisc(repoDisc,0)
        repoDiscF = RepositoryDiscFile("testare/test_lista_disc.txt")
        td.test_repoDiscFile(repoDiscF)
        
        """teste nota"""
        tn = TesteNota()
        tn.test_domeniuNota()
        tn.test_validareNota()
        tn.test_repoNota()
        tn.test_srvNota()
        tn.test_repoNotaFile("testare/test_lista_note.txt","testare/test_lista_note2.txt")
        tn.test_func()
        """teste undo"""
        tu = TesteUndo()
        tu.test_domeniuUndo()
        tu.test_repoUndo()
        tu.test_srvUndo()
    
        