class ActiuneUndo:
    
    def __init__(self, cmd_undo, cmd_redo, entitate_undo, entitate_redo):
        self.__cmd_undo = cmd_undo
        self.__cmd_redo = cmd_redo
        self.__entitate_undo = entitate_undo
        self.__entitate_redo = entitate_redo
        

    def get_cmd_undo(self):
        return self.__cmd_undo


    def get_cmd_redo(self):
        return self.__cmd_redo


    def get_entitate_undo(self):
        return self.__entitate_undo

    
    def get_entitate_redo(self):
        return self.__entitate_redo

