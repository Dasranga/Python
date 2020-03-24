#Script to Create Table Schema for Fixed Width Files

colLength = [
    '8', '8', '8', '3', '15', '10', '10', '10', '10', '200', '10', '10', '20', '10', '10', '4', '10', '20', '38', '20',
    '10', '10', '1', '10', '200', '26', '200', '100', '200', '100', '10', '10', '40', '10', '10', '10', '20', '10',
    '60', '5', '19', '19', '19', '1', '100', '20', '20', '10', '10', '3', '20', '10', '10', '20', '10', '10', '10',
    '10', '40', '10', '10', '5', '100', '100', '10', '5', '3', '1', '8', '8', '8', '8', '10', '8', '30', '200', '10',
    '10', '19', '10', '10', '200', '600', '1', '1', '1', '1', '8', '8', '200', '10', '200', '100']

colNames = ['colNames as List']

dictionary = dict(zip(colNames, colLength))
print(dictionary)

# def getSubStringQuery(subStringQuery, i, crTable):
# getSubStringQuery(subStringQuery, i, crTable)

newTableName = "new_table"
sourceTableName = "source_table"
crTable = "CREATE TABLE " + newTableName + " AS " + "select row_number() over (order by data asc) as id, "
subStringQuery = "SUBSTR(data,"
i = 1
query = crTable
finalQuery = " from " + sourceTableName

# Query snippet
print(query)
for key in dictionary:
    # i + "," + dictionary[key] + ") as " + key
    if (i == 1):
        subQuery = subStringQuery + str(i) + "," + dictionary[key] + ") as " + key + ","
        i = i + int(dictionary[key])
    else:
        subQuery = subStringQuery + str(i) + "," + dictionary[key] + ") as " + key + ","
        i = i + int(dictionary[key])
    print(subQuery)
print(finalQuery)
