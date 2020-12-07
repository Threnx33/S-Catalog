from domeniu.entitateStud import Student
from domeniu.entitateDisc import Disciplina
from domeniu.entitateNota import Nota
from domeniu.entitateUndoRedo import ActiuneUndo

class ServiceNota:
    
    def __init__(self, repoNota, validNota, repoStud, validStud, repoDisc, validDisc):
        self._repoNota = repoNota
        self._validNota = validNota
        self._repoStud = repoStud
        self._validStud = validStud
        self._repoDisc = repoDisc
        self._validDisc = validDisc
        
    
    def __len__(self):
        return len(self._repoNota)
    
    
    def adauga_nota(self,id_nota,id_stud,id_disc,val_nota):
        """
        metoda care adauga nota | sau eroare daca exista deja
        date de intrare:
            nota-nota pe care vrem sa o aduagam
        date de iesire:-
        date de exceptie:
            RepoError-"Nota existenta!"
        """
        stud = self._repoStud.cauta_stud(id_stud)
        disc = self._repoDisc.cauta_disc(id_disc)
        nota = Nota(id_nota,stud,disc,val_nota)
        self._validNota.valideaza_nota(nota)
        self._repoNota.adauga_nota(nota)
        return nota

    
    def modifica_nota(self,id_nota,id_stud,id_disc,val_nota):
        """
        metoda care modifica nota in lista de note dupa id, id-ul ramanand la fel | sau eroare daca nu o gaseste
        date de intrare:
            nota_modif-noua nota pe care vrem sa o schimbam
        date de iesire:-
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        stud = self._repoStud.cauta_stud(id_stud)
        disc = self._repoDisc.cauta_disc(id_disc)
        nota_modif = Nota(id_nota,stud,disc,val_nota)
        self._validNota.valideaza_nota(nota_modif)
        nota_precedenta = self._repoNota.modifica_nota(nota_modif)
        return [nota_precedenta,nota_modif]
    
    
    def cauta_nota(self,id_nota):
        """
        metoda care returneaza o nota dupa id in lista de note | sau eroare daca nu o gaseste
        date de intrare:
            id_nota-idul notei pe care o cautam
        date de iesire:
            el-nota pe care o cautam
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        key_nota = Nota(id_nota,Student(1,"a"),Disciplina(1,"a","a"),10)
        self._validNota.valideaza_nota(key_nota)
        return self._repoNota.cauta_nota(id_nota)
        
    
    def sterge_nota(self,id_nota):
        """
        metoda care sterge nota dupa id | sau eroare daca nu o gaseste
        date de intrare:
            id_nota-idul notei
        date de iesire:-
        date de exceptie:
            RepoError-"Nota inexistenta!"
        """
        nota = self._repoNota.cauta_nota(id_nota)
        self._validNota.valideaza_nota(nota)
        self._repoNota.sterge_nota(id_nota)
        return nota
             
    
    def sterge_note(self):
        """
        metoda care sterge toate notele
        """
        self._repoNota.sterge_note()
        
             
    def get_note(self):
        """
        metoda care returneaza toate notele
        date de intrare:-
        date de iesire:
            self._note[:]-copie dupa lista cu note
        """
        return self._repoNota.get_note()         
           
    """
    fucntii
    """      
    
    def sort_by_nume_stud(self,note_disc):
        """
        metoda care sorteaza o lista de studenti si notele lor la o materie, alfabetic, dupa numele studentilor. Daca au acelas nume se
            nota mai mare va fi prima
        date de intrare:
            note_disc-lista de lista, [nume_student,nota]
        date de iesire:
            note_disc-aceeasi lista dar sortata dupa nume
        exceptii:-
        """
        for i in range(len(note_disc)):
            for j in range(i+1,len(note_disc)):
                if (note_disc[i][0] > note_disc[j][0]) or (note_disc[i][0] == note_disc[j][0] and note_disc[i][1] < note_disc[j][1]):
                    aux = note_disc[i]
                    note_disc[i] = note_disc[j]
                    note_disc[j] = aux
    
    
    def sort_by_nota(self,note_disc):
        """
        metoda care sorteaza o lista de studenti si notele lor la o materie, dupa nota. Daca doi studenti au aceeasi nota se va lua
            lua in ordine alfabetica dupa nume
        date de intrare:
            note_disc-lista de lista, [nume_student,nota]
        date de iesire:
            note_disc-aceeasi lista dar sortata dupa nume
        exceptii:-
        """
        for i in range(len(note_disc)):
            for j in range(i+1,len(note_disc)):
                if (note_disc[i][1] < note_disc[j][1]) or (note_disc[i][1] == note_disc[j][1] and note_disc[i][0] > note_disc[j][0]):
                    aux = note_disc[i]
                    note_disc[i] = note_disc[j]
                    note_disc[j] = aux
    
    
    def get_lista_nume_si_medie(self,studenti,note):
        """
        metoda care returneaza studentii si mediile lor
        date de intrare:
            note-lista de note
            studenti-lista de studenti
        date de iesire:
            stud_si_medii-lista studenti si mediile lor
        exceptii:-
        """
        info_medie = [] #[id_stud,suma_note,nr_note]
        for stud in studenti:
            info_medie.append([stud.get_id_stud(),0,0])
        for nota in note:
            id_stud = nota.get_stud().get_id_stud()
            val_nota = nota.get_val_nota()
            for i in range(len(info_medie)):
                if info_medie[i][0] == id_stud:
                    info_medie[i][1] += val_nota
                    info_medie[i][2] += 1
        stud_si_medii = []
        for i in range(len(info_medie)):
            nume_stud = self._repoStud.cauta_stud(info_medie[i][0]).get_nume_stud()
            if info_medie[i][2] == 0:
                medie_stud = 0
            else:
                medie_stud = info_medie[i][1]/info_medie[i][2]
            stud_si_medii.append([nume_stud,medie_stud])
        return stud_si_medii
        
        
    def get_sort_nume_si_medie(self,stud_si_medii):
        """
        metoda care sorteaza si returneaza mediile studentilor [nume,medie]
        """
        for i in range(len(stud_si_medii)):
            for j in range(i+1,len(stud_si_medii)):
                if stud_si_medii[i][1] < stud_si_medii[j][1]:
                    aux = stud_si_medii[i]
                    stud_si_medii[i] = stud_si_medii[j]
                    stud_si_medii[j] = aux
        
    """
    sfarsit functii
    """
    
    
    def get_sorted_note_disc_by_nume_sau_nota(self,id_disc,caz):
        """
        metoda care ia toate notele de la o disciplina, iar apoi le sorteaza dupa numele studentului sau nota si le returneaza
        caz=0 -> sort dupa nume, caz=1 -> sort dupa val_nota
        date de intrare:
            id_disc-id-ul disciplinei
        date de iesire:
            note_disc-lista de studenti si note la o disciplina sortata dupa numele studentului
        exceptii:-
        """
        disc = self._repoDisc.cauta_disc(id_disc)
        nume_disc = disc.get_nume_disc()
        note_disc = self._repoNota.get_note_by_disc(disc) #[nume_stud,val_nota]
        if caz == 0:
            self.sort_by_nume_stud(note_disc)
        elif caz == 1:
            self.sort_by_nota(note_disc)
        return [note_disc,nume_disc]

    
    def get_top_medii(self):
        """
        metoda care returneaza primii 20% dintre studenti si mediile lor
        [nume_stud,medie]
        date de intrare:-
        date de iesire:
            top-lista cu primii 20% dintre studenti si mediile lor
        exceptii:-
        """
        note = self._repoNota.get_note()
        studenti = self._repoStud.get_studenti()
        nume_si_medii = self.get_lista_nume_si_medie(studenti,note)
        self.get_sort_nume_si_medie(nume_si_medii)
        nr_stud_din_top_cerut = int(len(studenti)/5)
        if len(studenti)%5 != 0:
            nr_stud_din_top_cerut += 1
        top = nume_si_medii[:nr_stud_din_top_cerut]
        return top
    
    
    def get_nr_note_disc(self,id_disc):
        """
        'cerinta de la profa'
        metoda care returneaza nr de note la o anumita disciplina
        """
        key_disc = Disciplina(id_disc,"a","a")
        self._validDisc.valideaza_disc(key_disc)
        note = self._repoNota.get_note()
        nr = 0
        for nota in note:
            if nota.get_disc().get_id_disc() == id_disc:
                nr += 1
        disc = self._repoDisc.cauta_disc(id_disc)
        nume_disc = disc.get_nume_disc()
        return [nr,nume_disc]
    
    
    def modifica_stud_si_note(self,id_stud,nume_stud):
        """
        metoda care modifica un student si modifica toate notele care contin studentul respectiv
        """
        stud_modif = Student(id_stud,nume_stud)
        self._validStud.valideaza_stud(stud_modif)
        self._repoStud.modifica_stud(stud_modif)
        self._repoNota.modifica_stud_note(stud_modif)
        
    
    def modifica_disc_si_note(self,id_disc,nume_disc,nume_prof):
        """
        metoda care modifica o disciplina si modifica toate notele care contin disciplina respectiva
        """
        disc_modif = Disciplina(id_disc,nume_disc,nume_prof)
        self._validDisc.valideaza_disc(disc_modif)
        self._repoDisc.modifica_disc(disc_modif)
        self._repoNota.modifica_disc_note(disc_modif)
        
    
    def sterge_stud_si_nota(self,id_stud):
        """
        metoda care sterge student si notele care contin studentul dupa id_stud | sau eroare daca nu o gaseste
        date de intrare:
            id_stud-idul studentului
        date de iesire:-
        date de exceptie:
            RepoError-"Student inexistent!"
        """
        stud = Student(id_stud,"a")
        self._validStud.valideaza_stud(stud)
        self._repoStud.sterge_stud(id_stud)
        self._repoNota.sterge_note_stud(id_stud)
        
    
    def sterge_disc_si_note(self,id_disc):
        """
        metoda care sterge disciplina si notele care contin disciplina dupa id_disc | sau eroare daca nu o gaseste
        date de intrare:
            id_disc-idul disciplinei
        date de iesire:-
        date de exceptie:
            RepoError-"Disciplina inexistenta!"
        """
        disc = Disciplina(id_disc,"a","a")
        self._validDisc.valideaza_disc(disc)
        self._repoDisc.sterge_disc(id_disc)
        self._repoNota.sterge_note_disc(id_disc)
    
    
        


class ServiceNotaUndo(ServiceNota):
    
    
    def __init__(self, repoNota, validNota, repoStud, validStud, repoDisc, validDisc, repoUndo):
        ServiceNota.__init__(self, repoNota, validNota, repoStud, validStud, repoDisc, validDisc)
        self._repoUndo = repoUndo
    
    
    def adauga_nota(self, id_nota, id_stud, id_disc, val_nota):
        nota = ServiceNota.adauga_nota(self, id_nota, id_stud, id_disc, val_nota)
        act_undo = ActiuneUndo(self._repoNota.sterge_nota,self._repoNota.adauga_nota,id_nota,nota)
        self._repoUndo.push(act_undo)


    def modifica_nota(self, id_nota, id_stud, id_disc, val_nota):
        nota_precedenta,nota = ServiceNota.modifica_nota(self, id_nota, id_stud, id_disc, val_nota)
        act_undo = ActiuneUndo(self._repoNota.modifica_nota,self._repoNota.modifica_nota,nota_precedenta,nota)
        self._repoUndo.push(act_undo)


    def sterge_nota(self, id_nota):
        nota = ServiceNota.sterge_nota(self, id_nota)
        act_undo = ActiuneUndo(self._repoNota.adauga_nota,self._repoNota.sterge_nota,nota,id_nota)
        self._repoUndo.push(act_undo)
