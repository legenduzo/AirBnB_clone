#!/usr/bin/python3
"""
AirBnB console. Extends pythons's cmd module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class
    Forms the basis for the console repl

    Attributes:
        prompt (str): Custom prompt '(hbnb)'
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Handles 'EOF'
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Catches empty lines and does nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
