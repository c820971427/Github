import csv


outputFile = open('../tmp_files/output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 6])
outputFile.close()

exampleFile = open('../tmp_files/output.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
# print(exampleData)
for row in exampleData:
    print(row)
