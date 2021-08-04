import csv


crimes = []

with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "2015" in row["Date"]:
            crimes.append(row["Primary Type"])

crimes.sort()

set_of_crimes = sorted(set(crimes))

string_for_counting = ""

for crime in crimes:
    string_for_counting += crime

count_of_crimes = {}

count_of_crimes.fromkeys(set_of_crimes[0])

for crime in set_of_crimes:
    count = string_for_counting.count(crime)
    count_of_crimes[crime] = count

print(max(count_of_crimes, key=count_of_crimes.get))        # just key
print(max(count_of_crimes.items(), key=lambda k: k[1]))     # key & value
