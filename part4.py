import json
from pprint import pprint


# Open a json file and append entries to the file.
f = open("survey.json", "r")
data = json.load(f)
print(type(data))
print(data)
f.close()

# '''
# Do some analysis with your data.
# You can do whatever you choose, but this code calculates
# the average age of people in your data set.
# '''

# Example of how to iterate over the list of dictionaries and pull out particular pieces of information.
ages = []
for s in range(len(data)):
    # if data[s]['age'] is not '': # Catches and skips over blank entries.
    age_as_string = data[s['age']]
    age_as_int = int(age_as_string)
    ages.append(age_as_int)

print(ages)
total = sum(ages)
average = total/len(ages)

print(average)
