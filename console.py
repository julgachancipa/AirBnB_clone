#!/usr/bin/python3
"""
Console that is the entry point of the program
"""
import cmd
import sys

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
            print("Create instance of", line)

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
            print("Show instance of", arg[1])

    def do_destroy(self, line):
        """Destroy instance of BaseModel"""
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif arg[1] != "id":
            print("** no instance found **")
        else:
            print("destroy instance of", arg[1])

    def do_all(self, line):
        """Display all instances """
        pass

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
