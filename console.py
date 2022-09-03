#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
#from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None

# ========== Class Variables  =======================
    
    __class_Ind = {
            'BaseModel' : BaseModel
            }
# ============ COMMAND FUNCTIONS =================
    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self):
        """
        Quit loop at the end of a file
        """
    def do_create(self, arg):
        """
        This creates an instance of an inputed class
        """
        val = self.__arg_ver(arg)
        if val is None:
            pass
        else:
            newInstance = self.__class_Ind.get(arg)()
            #newInstance.save()
            print(newInstance.id)


# ============= NON COMMAND FUNCTIONS ===========
    def emptyline(self):
        pass

    def __arg_ver(self, value):

        listStore = value.split()
        listLen = len(listStore)

        if listLen == 0:
            print("**class name missing**")
            return None
        elif listStore[0] not in self.__class_Ind.keys():
            print("class dosen't exist")
            return None
        else:
            return value


# ========== Under Construction ===========================

    def __id_ver(self, value):
        
        listStore = value.split()
        listLen = len(listStore)

        if listLen < 2:
            print ("** instance id missing **")

# ========================================================

if __name__ == '__main__':
    HBNBCommand().cmdloop()
