#!/usr/bin/python3
import os

def generate_invitations(tamplate, attendees):
    if not template:
        print('Error: Tamplate is empty, no output files generated.')
        return
    if not attendees:
        print('Error: Template is empty, no output files generated.')
        return
    if not isinstance(template, str):
        print('Error: Invalid input')
        return
    if (not isinstance(attendees, list) or
        not all(isinstance(item, dict) for item in attendees)):
        print('Error Invalid input')
        return
    for index, attendee in enumerate(attendees, start=1):
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = '{' + f'{key}' + '}'
            value = attendee.get(key) or "N/A"
            template_schema = template_schema.replace(placeholder, value)
            
        file_name = f'output_{index}.txt'
        
        if not os.path.exists(file_name):
            try:
                with open(file_name, 'w') as file:
                    file.write(template_schema)
            except Exception as e:
                print(f'Error writing file {file_name}: {e}')
        else:
            print(f'Error: file {file_name} already exists')
    
if __name__ == "__main__":
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print('Error: Template file not found.')
        exit()
    except Exception as e:
        print(f'Error reading template: {e}')
        exit()
    
    attendees = [
         {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]
    
    generate_invitations(template_content, attendees)