#!/usr/bin/python3
"""
Command Interpreter Entry Point Module
"""
from models.base_model import BaseModel
from models import storage
import cmd

clss = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command Interpreter Class"""
    prompt = "(hbnb) "

    # commands to add:
        # create
        # show
        # destroy
        # all
        # update

    def do_create(self, line):
        """
        Creates an new instance of the given class. Saves it to the JSON file.
        And prints its id.
        
        Usage: (hbnb) create <class_name>
        Ex: (hbnb) create BaseModel
        """
        if line:
            if line in clss.keys():
                new = clss[line]()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        

        
    def do_show(self, line):
        """
        Prints the string representation of an instance,
        given its class name and id.

        Usage: show <instance_class_name> <instance_id>
        Ex: show BaseModel 1234-1234-1234
        """
        if line:
            print(line[0])
    
        
    def do_destroy(self, line):
        pass
        
    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

    def emptyline(self):
        """"Handles empty line input."""
        pass

    def do_quit(self, line):
        """Quit command to exit the console."""
        return True
        
    def do_EOF(self, line):
        """Handles EOF input."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
