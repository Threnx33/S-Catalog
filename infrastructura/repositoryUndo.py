from erori.exceptii import RepoError

class RepositoryUndo:
    
    
    def __init__(self):
        self.__stiva = []
        self.__index = -1
        
    def push(self,act_undo):
        if len(self.__stiva) == len(self):
            self.__stiva.append(act_undo)
        else:
            self.__stiva[self.__index + 1] = act_undo
        self.__index += 1
        
    def pop(self):
        self.__index -= 1
        
    def pull(self):
        if len(self) == len(self.__stiva):
            raise RepoError("Redo indisponibil!")
        self.__index += 1
    
    def peek(self):
        if len(self) == 0:
            raise RepoError("Undo indisponibil!")
        return self.__stiva[self.__index]
    
    def __len__(self):
        return self.__index + 1
    
    
    



