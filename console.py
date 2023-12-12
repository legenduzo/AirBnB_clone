#!/usr/bin/python3
"""
Command Interpreter Entry Point Module
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import cmd

clss = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}
"""clss (dict): A dictionary of all external classes
used for commandline data manipulation
"""


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
            return
        if args[0] not in clss.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

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
            return
        if args[0] not in clss.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
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
        if line and line not in clss.keys():
            print("** class doesn't exist **")
            return
        instances = [
                str(obj) for key, obj in storage.all().items()
                if not line or key.startswith(line)]

        print(instances)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id,
        by adding or updating an attribute. (saved to the JSON file)

        Usage:
            (hbnb) update <cls_name> <id> <attr_name> "<attr_value>"

        Example:
            (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
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
        attr_name, attr_val = args[2], args[3]
        if attr_val.startswith('"') and attr_val.endswith('"'):
            attr_value = attr_val.strip('"')
        elif hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            attr_value = attr_type(attr_val)
        else:
            try:
                attr_value = (
                        int(attr_val)
                        if '.' not in attr_val
                        else float(attr_val)
                        )
            except Exception:
                attr_value = str(attr_val)

        setattr(instance, attr_name, attr_value)
        storage.save()

    def do_count(self, line):
        """
        Count the number of instances of a class.
        """
        storage.reload()
        all_objects = storage.all()
        count = 0
        for key in all_objects:
            if key.startswith(f"{line}"):
                count += 1
        print(count)

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

    def default(self, line):
        """
        Default method
        """
        if '.' in line and '()' in line:
            cls, command = line.split('.', 1)
            command = command[:-2]
            if command == 'all' and cls in clss.keys():
                self.do_all(cls)
            elif command == 'count' and cls in clss.keys():
                self.do_count(cls)
        elif '.' in line and '(' in line and ')' in line:
            cls, command = line.split('.', 1)
            command, itemid = command.split('(')
            itemid = itemid.strip('")')
            if ',' in itemid:
                update_str = itemid.split(',')
                itemid = update_str[0].strip('" ')
                attr_name = update_str[1].strip(' "')
                attr_val = update_str[2].strip(' "')
            if command == 'show' and cls in clss.keys():
                self.do_show(cls + ' ' + itemid)
            elif command == 'destroy' and cls in clss.keys():
                self.do_destroy(cls + ' ' + itemid)
            elif command == 'update' and cls in clss.keys():
                args = [cls, itemid, attr_name, attr_val]
                self.do_update(' '.join(args))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
