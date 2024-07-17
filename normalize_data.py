import csv

input_data = {
            "id": {
                    "0":"5vYA1mW9g2Coh1HUFUSmlb",
                    "1":"2klCjJcucgGQysgH170npL",
                    "2":"093PI3mdUvOSlvMYDwnV1e",
                    "3":"64yrDBpcdwEdNY9loyEGbX",
                    "4":"2jiI8bNSDu7UxTtDCOqh3L"
                },
            "title": {
                        "0":"3AM",
                        "1":"4 Walls",
                        "2":"11:11",
                        "3":"21 Guns",
                        "4":"21"
                    }

}

headers = [k for k in input_data.keys()]

values = []
n = len(next(iter(input_data.values())))

for heading in headers:
    vals = []
    for i in range(n):
        vals.append(input_data[heading][str(i)])
    values.append(vals)


with open('output.csv', 'w') as csvoutput:
    writer = csv.writer(csvoutput)
    writer.writerow(headers)
    writer.writerow(zip(*values))

