#!/usr/bin/python3
"""Class Base"""

import json
import csv
import os.path



class Base:
    """"
        Class Base
        Attr :
                id: number
    """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        self.id = id

    @property
    def id(self):
        """Doc"""
        return self.__id

    @id.setter
    def id(self, value):
        """Doc"""
        if value is None:
            self.__id = self.__nb_objects
        else:
            self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """Doc"""
        if list_dictionaries is None or \
                len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        list_objs_dict = []
        with open(cls.__name__ + '.json', "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            elif type(list_objs) == list:
                for obj in list_objs:
                    list_objs_dict.append(obj.to_dictionary())
                file.write(cls.to_json_string(list_objs_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or \
                len(json_string) == 0:
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(4, 3)
        if cls.__name__ == "Square":
            dummy_instance = cls(4)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from file"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                serialized_content = file.read()
        except FileNotFoundError:
            return list()

        deserialized_content = cls.from_json_string(serialized_content)

        instances_list = []
        for instance_dict in deserialized_content:
            instances_list.append(cls.create(**instance_dict))
        return instances_list
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
