import json


def recurse(data, values_list):
    if isinstance(data, dict):
        for key in data.keys():
            if isinstance(data[key], list):
                for i in data[key]:
                    recurse(i, values_list)
            else:
                for i in values_list:
                    if i['id'] == data[key]:
                        data['value'] = i['value']
    return data


with open('tests.json') as file_tests:
    tests_str = file_tests.read()
    tests = json.loads(tests_str)

with open('values.json') as file_values:
    values_str = file_values.read()
    values = json.loads(values_str)
    list_values = values['values']

report = recurse(data=tests, values_list=list_values)

with open('report.json', 'w') as f:
    json.dump(report, f, sort_keys=True, indent=2)
