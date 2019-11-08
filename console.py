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
