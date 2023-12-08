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

    def do_create(self, line):
        """
    Create a new instance of the given class.
    Save it to the JSON file and print its ID.

    Usage:
        (hbnb) create <class_name>

    Example:
        (hbnb) create BaseModel
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
    Display the string representation of an instance,
    given its class name and ID.

    Usage:
        (hbnb) show <class_name> <instance_id>

    Example:
        (hbnb) show BaseModel 1234-1234-1234
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        if args[0] not in clss.keys():
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")

        storage.reload()
        objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in objs:
            print(str(objs[key]))
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
    Delete an instance based on the class name and ID.
    Changes are saved to the JSON file.

    Usage:
        (hbnb) destroy <class_name> <instance_id>

    Example:
        (hbnb) destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        if args[0] not in clss.keys():
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        storage.reload()
        objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
    Display the string representation of all instances,
    filtered by an optional class name.

    Usage:
        (hbnb) all <class_name(optional)>

    Examples:
        (hbnb) all BaseModel
        (hbnb) all
        """
        storage.reload()
        objs = storage.all()
        args = line.split()
        if len(args) > 0:
            if args[0] in clss.keys():
                instances = [
                    obj for k, obj in storage.all().items()
                    if k.startswith(f"{args[0]}")
                ]
            else:
                print("** class doesn't exist")
                return
        else:
            instances = list(storage.all().values())

        for inst in instances:
            print(str(inst))

    def do_update(self, line):
        """
    Updates an instance based on the class name and id,
    by adding or updating an attribute. (saved to the JSON file)

    Usage:
        (hbnb) update <class_name> <id> <attribute_name> "<attribute_value>"

    Example:
        (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name is missing **")
            return
        if len(args) > 0:
            if args[0] not in clss.keys():
                print("** class doesn't exist **")
                return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs = storage.all()
        if len(args) > 1:
            key = f"{args[0]}.{args[1]}"
            if key not in objs:
                print("** no instance found **")
                return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        instance = objs[key]
        if hasattr(instance, args[2]):
            origin = type(getattr(instance, args[2]))
            setattr(instance, args[2], origin(args[3]))
        else:
            setattr(instance, args[2], args[3])
        storage.save()

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
