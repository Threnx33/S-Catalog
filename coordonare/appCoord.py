from infrastructura.repositoryStud import RepositoryStud, RepositoryStudFile
from infrastructura.repositoryDisc import RepositoryDisc, RepositoryDiscFile
from infrastructura.repositoryNota import RepositoryNota, RepositoryNotaFile
from infrastructura.repositoryUndo import RepositoryUndo
from validare.validareStud import ValidatorStudent
from validare.validareDisc import ValidatorDisciplina
from validare.validareNota import ValidatorNota
from business.serviceStud import ServiceStud, ServiceStudUndo
from business.serviceDisc import ServiceDisc, ServiceDiscUndo
from business.serviceNota import ServiceNota, ServiceNotaUndo
from business.serviceUndo import ServiceUndo
from prezentare.consola import UI

class AppCoord:
    
    def start(self):
        #repoStud = RepositoryStud()
        repoStud = RepositoryStudFile("infrastructura/lista_stud.txt")
        #repoDisc = RepositoryDisc()
        repoDisc = RepositoryDiscFile("infrastructura/lista_disc.txt")
        #repoNota = RepositoryNota()
        repoNota = RepositoryNotaFile("infrastructura/lista_note.txt")
        repoUndo = RepositoryUndo()
        srvUndo = ServiceUndo(repoUndo)
        validStud = ValidatorStudent()
        srvStud = ServiceStudUndo(repoStud,validStud,repoUndo)
        validDisc = ValidatorDisciplina()
        srvDisc = ServiceDiscUndo(repoDisc,validDisc,repoUndo)
        validNota = ValidatorNota()
        srvNota = ServiceNotaUndo(repoNota,validNota,repoStud,validStud,repoDisc,validDisc,repoUndo)
        cons = UI(srvStud,srvDisc,srvNota,srvUndo)
        cons.run()
    
    
    
    



