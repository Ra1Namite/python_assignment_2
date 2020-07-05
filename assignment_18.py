import json

my_dict = {'name': 'Sanjay Rai', 'age': 23}

print('\nSerializing dictionary to JSON string...')
json_string = json.dumps(my_dict)
print(json_string)

print('\nDeserializing JSON back to Python..')
python_format = json.loads(json_string)
print(python_format)