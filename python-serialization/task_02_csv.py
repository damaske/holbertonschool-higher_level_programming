#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(CSV_filename):
        """Convert a CSV file to JSON format and write the result to data.json."""
        try:
            with open(CSV_filename, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = [row for row in csv_reader]

            with open("data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

            return True
        except FileNotFoundError:
            return False
