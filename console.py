#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
#from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None

# ========== Class Variables  =======================
    
    class_Ind = {
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
        if arg == '':
            print("**class name missing**")
        
        elif arg not in self.class_Ind.keys():
            print("class dosen't exist")
        else:
            newInstance = self.class_Ind.get(arg)()
            #newInstance.save()
            print(newInstance.id)
# ============= NON COMMAND FUNCTIONS ===========
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
