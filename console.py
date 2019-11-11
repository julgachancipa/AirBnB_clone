#!/usr/bin/python3
"""
Console that is the entry point of the program
"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Class for HBNB command
    """
    use_rawinput = False

    prompt = "(hbnb) "

    def do_create(self, line):
        """Create instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **") 
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """Show instance of BaseModel"""
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            dict1 = storage.all()
            list_obj = list(dict1.values())
            flag = 0
            for obj in list_obj:
                if obj.id == arg[1]:
                    print(obj)
                    flag = 1
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy instance of BaseModel"""
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            storage.reload()
            dict1 = storage.all()
            key = arg[0] + "." + arg[1]
            obj = dict1.get(key)
            if obj is None:
                print("** no instance found **")
            else:
                if obj.id == arg[1]:
                    del dict1[key]
            storage.save()

    def do_all(self, line):
        """Display all instances """
        if line != "BaseModel":
            print("** class doesn't exist **")
        else:
            storage = FileStorage()
            dict1 = storage.all()
            for key, val in dict1.items():
                print(val)

    def do_update(self, line):
        """Update an instances of BaseModel"""
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif arg[1] != "id":
            print("** no instance found **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            print("update attribut", arg[2])

    def do_quit(self, line):
        """Quit command to exit the program

        """
        sys.exit(1)

    def do_EOF(self, line):
        """
         Exit
        """
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
