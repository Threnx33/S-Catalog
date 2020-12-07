class ServiceUndo:
    
    def __init__(self, repoUndo):
        self.__repoUndo = repoUndo
    
    
    def act_undo(self):
        act_tot = self.__repoUndo.peek()
        self.__repoUndo.pop()
        act_undo = act_tot.get_cmd_undo()
        param_undo = act_tot.get_entitate_undo()
        act_undo(param_undo)
    
    
    def act_redo(self):
        self.__repoUndo.pull()
        act_tot = self.__repoUndo.peek()
        act_redo = act_tot.get_cmd_redo()
        param_redo = act_tot.get_entitate_redo()
        act_redo(param_redo)



