import os
import csv

csvRows = []
# 找到所有的csv目标文件
os.makedirs('../headerRemoved', exist_ok=True)
for csvFilename in os.listdir('../tmp_files'):
    if not csvFilename.endswith('.csv'):
        continue
    print(csvFilename)
    # 读入csv文件
    csvFile = open('../tmp_files/%s' % csvFilename)
    readerCsv = csv.reader(csvFile)
    for row in readerCsv:
        if readerCsv.line_num == 1:
            continue
        csvRows.append(row)
    csvFile.close()
print(csvRows)
# 写入csv文件，丢弃第一行
csvFileObj = open(os.path.join('../headerRemoved', 'finish_file.csv'), 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()
