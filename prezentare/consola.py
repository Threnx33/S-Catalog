from erori.exceptii import ValidError, RepoError, CmdError

class UI:
    
    def __init__(self, srvStud, srvDisc, srvNota, srvUndo):
        self.__srvStud = srvStud
        self.__srvDisc = srvDisc
        self.__srvNota = srvNota
        self.__srvUndo = srvUndo
        self.__comenzi = {
            "01":self.lista_comenzi,"02":self.ui_comenzi_multiple,
            "11":self.ui_adauga_stud,"12":self.ui_modifica_stud,"13":self.ui_cauta_stud,"14":self.ui_sterge_stud,"15":self.ui_adauga_studenti_r,
            "19":self.ui_afiseaza_studenti,
            "21":self.ui_adauga_disc,"22":self.ui_modifica_disc,"23":self.ui_cauta_disc,"24":self.ui_sterge_disc,"29":self.ui_afiseaza_discipline,
            "31":self.ui_adauga_nota,"32":self.ui_modifica_nota,"33":self.ui_cauta_nota,"34":self.ui_sterge_nota,"35":self.ui_nr_note_disc,"39":self.ui_afiseaza_note,
            "41":self.ui_note_disc_sort_by_nume,"42":self.ui_note_disc_sort_by_nota,"43":self.ui_top_20,
            "51":self.ui_undo,"52":self.ui_redo
            }
        self.__comenzi_m = {
            "01":self.lista_comenzi,
            "11":self.ui_adauga_stud_m,"12":self.ui_modifica_stud_m,"13":self.ui_cauta_stud_m,"14":self.ui_sterge_stud_m,"15":self.ui_adauga_studenti_r_m,
            "19":self.ui_afiseaza_studenti,
            "21":self.ui_adauga_disc_m,"22":self.ui_modifica_disc_m,"23":self.ui_cauta_disc_m,"24":self.ui_sterge_disc_m,"29":self.ui_afiseaza_discipline,
            "31":self.ui_adauga_nota_m,"32":self.ui_modifica_nota_m,"33":self.ui_cauta_nota_m,"34":self.ui_sterge_nota_m,"35":self.ui_nr_note_disc_m,"39":self.ui_afiseaza_note,
            "41":self.ui_note_disc_sort_by_nume_m,"42":self.ui_note_disc_sort_by_nota_m,"43":self.ui_top_20
            }
    
    
    def lista_comenzi(self):
        print("'Lista de comenzi'")
        print("00:Iesire din program\n01:Afiseaza lista comenzi\n02:Comenzi multiple")
        print("11:Adauga student\n12:Modifica student\n13:Cauta student dupa id\n14:Sterge student dupa id\n15:Adauga studenti random\n19:Afiseaza studentii")
        print("21:Adauga disciplina\n22:Modifica disciplina\n23:Cauta disciplina dupa id\n24:Sterge disciplina dupa id\n29:Afiseaza disciplina")
        print("31:Adauga nota\n32:Modifica nota\n33:Cauta nota dupa id\n34:Sterge nota dupa id\n35:Numar note la o disciplina\n39:Afiseaza note")
        print("41:Afiseaza note la disciplina sortate dupa nume\n42:Afiseaza note la disciplina sortate dupa nota")
        print("43:Afiseaza primii 20% din studenti dupa medie")
        print("51:Undo\n52:Redo")
    
    
    def ui_comenzi_multiple(self):
        print("'Comenzi multiple'")
        comenzi = input("Comenzi: ")
        comenzi = comenzi.split(";")
        for i in range(len(comenzi)):
            comanda = comenzi[i].split(",")
            for j in range(len(comanda)):
                comanda[j] = comanda[j].strip()
            param = comanda[1:]
            if comanda[0] in self.__comenzi_m:
                self.__comenzi_m[comanda[0]](param)
            else:
                raise CmdError("Comanda numarul "+str(i)+" nu a fost gasita")
    
    
    def ui_adauga_stud(self):
        print("'Adauga student'")
        id_stud = int(input("Id student: "))
        nume_stud = input("Nume student: ")
        self.__srvStud.adauga_stud(id_stud,nume_stud)
        
        
    def ui_adauga_studenti_r(self):
        print("'Adauga studenti random'")
        n = int(input("Numar studenti: "))
        self.__srvStud.adauga_studenti_r(n)


    def ui_modifica_stud(self):
        print("'Modifica student'")
        id_stud = int(input("Id student: "))
        nume_stud = input("Nume student: ")
        self.__srvNota.modifica_stud_si_note(id_stud,nume_stud)
        print("'Student modificat'")
    
    
    def ui_cauta_stud(self):
        print("'Cauta student dupa id'")
        id_stud = int(input("Id student: "))
        print("Studentul gasit: "+str(self.__srvStud.cauta_stud(id_stud)))
        
        
    def ui_sterge_stud(self):
        print("'Sterge student dupa id'")
        id_stud = int(input("Id student:"))
        self.__srvNota.sterge_stud_si_nota(id_stud)
        print("'Student sters'")


    def ui_afiseaza_studenti(self):
        print("'Afisare studenti'")
        studenti = self.__srvStud.get_studenti()
        if len(studenti) == 0:
            print("Nu exista studenti!")
        for el in studenti:
            print(el)
            
            
    def ui_adauga_disc(self):
        print("'Adauga disciplina'")
        id_disc = int(input("Id disciplina: "))
        nume_disc = input("Nume disciplina: ")
        nume_prof = input("Nume profesor: ")
        self.__srvDisc.adauga_disc(id_disc,nume_disc,nume_prof)
    
    
    def ui_modifica_disc(self):
        print("'Modifica disciplina'")
        id_disc = int(input("Id disciplina: "))
        nume_disc = input("Nume disciplina: ")
        nume_prof = input("Nume profesor: ")
        self.__srvDisc.modifica_disc(id_disc,nume_disc,nume_prof)
        
        
    def ui_cauta_disc(self):
        print("'Cauta disciplina dupa id'")
        id_disc = int(input("Id disciplina: "))
        print("Disciplina gasita: "+str(self.__srvDisc.cauta_disc(id_disc)))
        
        
    def ui_sterge_disc(self):
        print("'Sterge disciplina dupa id'")
        id_disc = int(input("Id disciplina: "))
        self.__srvNota.sterge_disc_si_note(id_disc)
        print("Disciplina stearsa")
    
    
    def ui_afiseaza_discipline(self):
        print("'Afiseaza discipline'")
        discipline = self.__srvDisc.get_discipline()
        if len(discipline) == 0:
            print("Nu exista discipline!")
        for el in discipline:
            print(el)
            
            
    def ui_adauga_nota(self):
        print("'Adauga nota'")
        id_nota = int(input("Id nota: "))
        id_stud = int(input("Id student: "))
        id_disc = int(input("Id disciplina: "))
        val_nota = float(input("Nota: "))
        self.__srvNota.adauga_nota(id_nota,id_stud,id_disc,val_nota)
        
        
    def ui_modifica_nota(self):
        print("'Modifica nota'")
        id_nota = int(input("Id nota: "))
        id_stud = int(input("Id student: "))
        id_disc = int(input("Id disciplina: "))
        val_nota = float(input("Nota: "))
        self.__srvNota.modifica_nota(id_nota,id_stud,id_disc,val_nota)
        
    
    def ui_cauta_nota(self):
        print("'Cauta nota dupa id'")
        id_nota = int(input("Id nota: "))
        print("Nota gasita: "+str(self.__srvNota.cauta_nota(id_nota)))
    
    
    def ui_sterge_nota(self):
        print("'Sterge nota dupa id'")
        id_nota = int(input("Id nota: "))
        self.__srvNota.sterge_nota(id_nota)
        print("Nota stearsa")
        

    def ui_afiseaza_note(self):
        print("'Afiseaza note'")
        note = self.__srvNota.get_note()
        if len(note) == 0:
            print("Nu exista note")
        for el in note:
            print(el)
            
            
    def ui_note_disc_sort_by_nume(self):
        print("'Afiseaza note la disciplina sortate dupa nume'")
        id_disc = int(input("Id disciplina: "))
        caz = 0
        sorted_disc_note, nume_stud = self.__srvNota.get_sorted_note_disc_by_nume_sau_nota(id_disc,caz)
        if len(sorted_disc_note) == 0:
            print("Nu sunt note la disciplina "+str(nume_stud))
        else:
            print("Notele de la disciplina "+str(nume_stud)+" sunt:")
            for el in sorted_disc_note:
                print(str(el[0])+" | "+str(el[1]))
                
                
    def ui_note_disc_sort_by_nota(self):
        print("'Afiseaza note la disciplina sortate dupa nota'")
        id_disc = int(input("Id disciplina: "))
        caz = 1
        sorted_disc_note, nume_disc = self.__srvNota.get_sorted_note_disc_by_nume_sau_nota(id_disc,caz)
        if len(sorted_disc_note) == 0:
            print("Nu sunt note la disciplina "+str(nume_disc))
        else:
            print("Notele de la disciplina "+str(nume_disc)+" sunt:")
            for el in sorted_disc_note:
                print(str(el[0])+" | "+str(el[1]))
                
            
    def ui_top_20(self):
        print("'Afiseaza primii 20% din studenti dupa medie'")
        top = self.__srvNota.get_top_medii()
        if len(top) == 0:
            print("Nu sunt suficienti studenti pentru a se efectua un top")
        else:
            for el in top:
                print(str(el[0])+" | "+str(el[1]))
            
    
    def ui_nr_note_disc(self):
        print("'Numar note la o disciplina'")
        id_disc = int(input("Id disciplina: "))
        nr, materie = self.__srvNota.get_nr_note_disc(id_disc)
        if nr == 0:
            print("Nu sunt note la "+str(materie))
        else:
            print("Numarul de note la "+str(materie)+" este: "+str(nr))
    
    
    def ui_undo(self):
        print("'Undo'")
        self.__srvUndo.act_undo()
        
    
    def ui_redo(self):
        print("'Redo'")
        self.__srvUndo.act_redo()
    
    
    
    """------comenzi multiple-------"""
    
    
    
    
    def ui_adauga_stud_m(self,param):
        print("'Adauga student'")
        id_stud = int(param[0])
        nume_stud = param[1]
        self.__srvStud.adauga_stud(id_stud,nume_stud)
        
        
    def ui_adauga_studenti_r_m(self, param):
        print("'Adauga studenti random'")
        n = int(param[0])
        self.__srvStud.adauga_studenti_r(n)


    def ui_modifica_stud_m(self,param):
        print("'Modifica student'")
        id_stud = int(param[0])
        nume_stud = param[1]
        self.__srvStud.modifica_stud(id_stud,nume_stud)
        print("'Student modificat'")
    
    
    def ui_cauta_stud_m(self,param):
        print("'Cauta student dupa id'")
        id_stud = int(param[0])
        print("Studentul gasit: "+str(self.__srvStud.cauta_stud(id_stud)))
        
        
    def ui_sterge_stud_m(self,param):
        print("'Sterge student dupa id'")
        id_stud = int(param[0])
        self.__srvStud.sterge_stud(id_stud)
        print("'Student sters'")
            
            
    def ui_adauga_disc_m(self,param):
        print("'Adauga disciplina'")
        id_disc = int(param[0])
        nume_disc = param[1]
        nume_prof = param[2]
        self.__srvDisc.adauga_disc(id_disc,nume_disc,nume_prof)
    
    
    def ui_modifica_disc_m(self,param):
        print("'Modifica disciplina'")
        id_disc = int(param[0])
        nume_disc = param[1]
        nume_prof = param[2]
        self.__srvDisc.modifica_disc(id_disc,nume_disc,nume_prof)
        
        
    def ui_cauta_disc_m(self,param):
        print("'Cauta disciplina dupa id'")
        id_disc = int(param[0])
        print("Disciplina gasita: "+str(self.__srvDisc.cauta_disc(id_disc)))
        
        
    def ui_sterge_disc_m(self,param):
        print("'Sterge disciplina dupa id'")
        id_disc = int(param[0])
        self.__srvDisc.sterge_disc(id_disc)
        print("Disciplina stearsa")
            
            
    def ui_adauga_nota_m(self,param):
        print("'Adauga nota'")
        id_nota = int(param[0])
        id_stud = int(param[1])
        id_disc = int(param[2])
        val_nota = float(param[3])
        self.__srvNota.adauga_nota(id_nota,id_stud,id_disc,val_nota)
        
        
    def ui_modifica_nota_m(self,param):
        print("'Modifica nota'")
        id_nota = int(param[0])
        id_stud = int(param[1])
        id_disc = int(param[2])
        val_nota = float(param[3])
        self.__srvNota.modifica_nota(id_nota,id_stud,id_disc,val_nota)
        
    
    def ui_cauta_nota_m(self,param):
        print("'Cauta nota dupa id'")
        id_nota = int(param[0])
        print("Nota gasita: "+str(self.__srvNota.cauta_nota(id_nota)))
    
    
    def ui_sterge_nota_m(self,param):
        print("'Sterge nota dupa id'")
        id_nota = int(param[0])
        self.__srvNota.sterge_nota(id_nota)
        print("Nota stearsa")
            
            
    def ui_note_disc_sort_by_nume_m(self,param):
        print("'Afiseaza note la disciplina sortate dupa nume'")
        id_disc = int(param[0])
        caz = 0
        sorted_disc_note, nume_disc = self.__srvNota.get_sorted_note_disc_by_nume_sau_nota(id_disc,caz)
        if len(sorted_disc_note) == 0:
            print("Nu sunt note la disciplina "+str(nume_disc))
        else:
            print("Notele de la disciplina "+str(nume_disc)+" sunt:")
            for el in sorted_disc_note:
                print(str(el[0])+" | "+str(el[1]))
                
    def ui_note_disc_sort_by_nota_m(self,param):
        print("'Afiseaza note la disciplina sortate dupa nota'")
        id_disc = int(param[0])
        caz = 1
        sorted_disc_note, nume_disc = self.__srvNota.get_sorted_note_disc_by_nume_sau_nota(id_disc,caz)
        if len(sorted_disc_note) == 0:
            print("Nu sunt note la disciplina "+str(nume_disc))
        else:
            print("Notele de la disciplina "+str(nume_disc)+" sunt:")
            for el in sorted_disc_note:
                print(str(el[0])+" | "+str(el[1]))
                

    def ui_nr_note_disc_m(self,param):
        print("'Numar note la o disciplina'")
        id_disc = int(param[0])
        nr, materie = self.__srvNota.get_nr_note_disc(id_disc)
        if nr == 0:
            print("Nu sunt note la "+str(materie))
        else:
            print("Numarul de note la "+str(materie)+" este: "+str(nr))
    
    
    """consola"""
    
    
    def run(self):
        self.lista_comenzi()
        while True:
            cmd = input(">>>")
            if cmd == "00":
                print("Ai iesit din program!")
                return 
            if cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except ValueError:
                    print("Valoare numerica invalida!")
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
                except CmdError as ce:
                    print(ce)
            else:
                print("Comanda invalida!")
    