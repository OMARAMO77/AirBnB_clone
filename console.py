#!/usr/bin/python3
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
import ast


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

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = shlex.split(arg)
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

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        all_objects = FileStorage().all()
        class_instances = []
        for obj in all_objects.values():
            if obj.__class__.__name__ == args[0]:
                class_instances.append(obj)
        print(len(class_instances))

    def default(self, line):
        """
        Handle class name followed by .all(), .count(),
        .show(), .destroy(), or .update()
        """
        parts = line.split('.')
        if len(parts) == 2:
            if parts[0] in self.valid_classes:
                if parts[1] == "all()":
                    self.do_all(parts[0])
                elif parts[1] == "count()":
                    self.do_count(parts[0])
                elif parts[1].startswith("show(") and parts[1].endswith(")"):
                    id_str = parts[1][6:-2]
                    self.do_show(parts[0] + " " + id_str)
                elif parts[1].startswith("destroy(") and \
                        parts[1].endswith(")"):
                    id_str = parts[1][9:-2]
                    self.do_destroy(parts[0] + " " + id_str)
                elif parts[1].startswith("update(") and parts[1].endswith(")"):
                    if "{" in parts[1]:
                        args = parts[1][7:-1].split(', ',1)
                        dict_repr = args[1].replace("'", "\"")
                        dict_repr = ast.literal_eval(dict_repr)
                        if type(dict_repr) == dict:
                            for key, value in dict_repr.items():
                                self.do_update(parts[0] + " " + args[0] + " " +
                                               str(key) + " " + str(value))
                    else:
                        args = parts[1][7:-1].split(', ')
                        if len(args) == 3:
                            self.do_update(parts[0] + " " + args[0] + " " +
                                           args[1] + " " + args[2])
                return

        cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
