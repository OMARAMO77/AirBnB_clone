#!/usr/bin/env python3
"""---"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
from os import path
from datetime import datetime
import shlex


class HBNBCommand(cmd.Cmd):
    """---"""
    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User", 'State',
                     'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D or the EOF character"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of the class"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objects = FileStorage().all()
        instance_key = "{}.{}".format(args[0], args[1])
        instance = all_objects.get(instance_key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objects = FileStorage().all()
        instance_key = "{}.{}".format(args[0], args[1])
        instance = all_objects.get(instance_key)
        if instance:
            del all_objects[instance_key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances or instances of a specific class"""
        all_objects = FileStorage().all()
        if arg:
            if arg in self.valid_classes:
                filtered_objects = {}
                for k, v in all_objects.items():
                    if arg in k:
                        filtered_objects[k] = v
                print([str(v) for v in filtered_objects.values()])
            else:
                print("** class doesn't exist **")
        else:
            print([str(v) for v in all_objects.values()])

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
