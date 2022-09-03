#!/usr/bin/python3

import json
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None

# ========== Class Variables  =======================
    __file_path = "file.json"
    __class_Ind = {
            "BaseModel": BaseModel
            }

# ============ COMMAND FUNCTIONS =================

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """
        command to exit the program
        """
        return True

    def do_create(self, arg):
        """
        This creates an instance of an inputed class
        and prints the id after
        """
        val = self.__arg_ver(arg)

        if val is None:
            pass
        else:
            newInstance = self.__class_Ind.get(arg)()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, arg):
        """
        This prints the string representation
        of an instance based on the class name and id
        """
        all_objects = storage.all()

        val = self.__arg_ver(arg)

        if val is not None:
            objId = self.__id_ver(arg, all_objects)
            if objId is not None:
                listStore = arg.split()
                objKey = listStore[0] + '.' + listStore[1]
                objInstance = all_objects.get(objKey)
                print(str(objInstance))

    def do_destroy(self, arg):
        """
        This method deletes an instance based on the
        class name and id(saves the change to the JSON file)
        """
        all_objects = storage.all()

        val = self.__arg_ver(arg)

        if val is not None:
            objId = self.__id_ver(arg, all_objects)
            if objId is not None:
                listStore = arg.split()
                objKey = listStore[0] + '.' + listStore[1]
                del all_objects[objKey]
                storage.save()

# ============= NON COMMAND FUNCTIONS ===========

    def emptyline(self):
        """
        This function allows the cursor
        to continue when no string has been inserted
        """
        pass

# ====================== Value Verfication ================
    def __arg_ver(self, value):
        """
        This verifies the class name inserted
        """

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

# ========== For ID verification =======================
    def __id_ver(self, value, all_objects):
        """
        This verifies the argumen after the class name
        """

        listStore = value.split()
        listLen = len(listStore)

        if listLen < 2:
            print("** instance id missing **")
            return None

        objKey = listStore[0] + '.' + listStore[1]

        if objKey not in all_objects.keys():
            print("** no instance found **")
            return None
        else:
            return True
# ========================================================


if __name__ == '__main__':
    HBNBCommand().cmdloop()
