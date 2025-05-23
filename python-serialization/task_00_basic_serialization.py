#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """Serializes and save data to the specified file"""
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Loads and deserializes data from the specified file"""
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data