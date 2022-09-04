#!/usr/bin/python3

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None

# ========== Class Variables  =======================
    __file_path = "file.json"
    __class_Ind = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
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

    def do_all(self, arg):
        """
        This method prints all string representation of all 
        instances based or not on the class name 
        e.g all or all BaseModel
        """
        all_objects = storage.all()

        listStore = arg.split()
        listLen = len(listStore)
        resList = [ ]

        if listLen == 0:
            for obj in all_objects.values():
                resList.append(str(obj))
            print(resList)
        else:
            if listStore[0] in self.__class_Ind.keys():
                for key, value in all_objects.items():
                    if key.startswith(listStore[0]):
                        resList.append(str(value))
                print(resList)
            else:
                print("** class doesn't exist **")


    def do_update(self, arg):
        """
        This  Updates an instance based on the class name 
        and id by adding or updating attribute 
        (save the change into the JSON file)
        """
        int_values = [
            'number_rooms',
            'number_bathrooms',
            'max_guest',
            'price_by_night'
        ]

        float_values = [
            'latitude',
            'longitude'
        ]

        val = self.__arg_ver( arg)
        all_objects = storage.all()
        if val is not None:

            objId = self.__id_ver(arg, all_objects)

            if objId is not None:
                
                listStore = arg.split()
                listLen = len(listStore)
                
                if listLen > 2:
                    
                    if listLen > 3:

                        if listStore[0] == "Place":
                            if listStore[2] in int_values:
                                try:
                                    listStore[3] = int(listStore[3])

                                except Exception:
                                    listStore[3] = 0

                            elif listStore[2] in float_values:
                                try:
                                    listStore[3] = float(listStore[3])
                                except Exception:
                                    listStore[3] = 0

                            obKey = listStore[0] + '.' + listStore[1]
                            setattr(all_objects[obKey], listStore[2], listStore[3])
                        else:
                            objKey = listStore[0] + '.' + listStore[1]
                            setattr(all_objects[objKey], listStore[2], listStore[3])
                            storage.save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")

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
