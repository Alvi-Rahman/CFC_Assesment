"""
FileWriter

A class for writing data to a JSON file.

Methods:
    write_to_json_file(data, output_file):
        Writes the data to a JSON file.
"""

import json


class FileWriter:
    @staticmethod
    def write_to_json_file(data, output_file):
        """
        Writes the data to a JSON file.

        Args:
            data (dict): Data to be written to the JSON file.
            output_file (str): Path to the output JSON file.
        """
        try:
            output_file = (f"{output_file}.json" if output_file.lower().split('.')[-1] != 'json'
                           else output_file)
            with open(output_file, 'w+') as file:
                json.dump(data, file, indent=4)
            return True, None
        except Exception as e:
            return False, e.args[0]

    @staticmethod
    def write_logs(data, output_file):
        """
        Writes the data to a JSON file.

        Args:
            data (dict): Data to be written to the JSON file.
            output_file (str): Path to the output JSON file.
        """
        try:
            output_file = (f"{output_file}.log" if output_file.lower().split('.')[-1] != 'log'
                           else output_file)
            with open(output_file, 'w+') as file:
                json.dump(data, file, indent=4)
            return True, None
        except Exception as e:
            return False, e.args[0]
