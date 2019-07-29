import os

import csv

election_csv = os.path.join("election_data.csv")
output_path = os.path.join("election_results.csv")

total_votes = 0
candidates = []
cdict = {}


with open(election_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidates.append(row[2])
    for candidate in candidates:
        if (candidate in cdict):
            cdict[candidate] += 1
        else:
            cdict[candidate] = 1
        
    print("Election Results")
    print("Total Votes: " + str(total_votes))

    for candidate in cdict:
        print(str(candidate) + ": " + str(round((cdict[candidate]/total_votes)*100,2)) + "% (" + str(cdict[candidate]) + ")")
    
    print("Winner: " + str(max(cdict, key=cdict.get)))

    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["Total Votes: " + str(total_votes)])

        for candidate in cdict:
            csvwriter.writerow([str(candidate) + ": " + str(round((cdict[candidate]/total_votes)*100,2)) + "% (" + str(cdict[candidate]) + ")"])
    
        csvwriter.writerow(["Winner: " + str(max(cdict, key=cdict.get))])
    