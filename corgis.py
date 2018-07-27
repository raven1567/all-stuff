import school_scores
list_of_record = school_scores.get_all()

# print(list_of_record[0])

# for row in list_of_record:
#     print(row['State']['Name'],row['Year'])

for dictionary in list_of_record:
    print(dictionary['Total']['Test-takers'])
