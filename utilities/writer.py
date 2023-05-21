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
        output_file = (f"{output_file}.json" if output_file.lower().split('.')[-1] != 'json'
                       else output_file)
        with open(output_file, 'w+') as file:
            json.dump(data, file, indent=4)
