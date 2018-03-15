import nltk
import pymysql.cursors
from nltk import sent_tokenize, word_tokenize, pos_tag

where_clause = ""
nouns = []
result = ""

quantifier = {"ALL":"*"}

where_list = ['where', 'which', 'who', 'whom', 'whose']
select_list = ['Give', 'Show', 'Provide']

db = {'student': ['name', 'age','class', 'subject'], 'teacher': ['name', 'age', 'subject']}
statement = "give name from students whose age is between sajjad and waleed."
sqlQuery = "Select "
table="students"

tokened = word_tokenize(statement)
print("tokened: ",end="")
print(tokened)

for word in tokened:
    if word in where_list:
        #where_clause += word
        index = tokened.index(word)
        where_clause = tokened[index:]
        rest_clause = tokened[:index]

print(where_clause)
print(rest_clause)
print(pos_tag(tokened))

is_noun = lambda pos: pos[:2] == 'NN'

for (word,pos) in pos_tag(tokened):
    if is_noun(pos):
        nouns.append(word)
print(nouns)

i = 0
if table in tokened:
    i = tokened.index(table)

attributes = ["name","age","class","subject"]
attributeIndex = 0
attribute = ""
result = []
conditions = []


if "all" in tokened:
    sqlQuery += "* FROM "+table
    if len(tokened) < i:
        print(sqlQuery)
        sys.exit()
    sqlQuery += " WHERE "

for attribute in tokened:
    if attribute in attributes and not(attribute in table):
        sqlQuery += attribute+","

    #sqlQuery.strip(',')
sqlQuery += " FROM "+table+ " WHERE "

if "is" in tokened and not("between" in tokened):
    for elem in attributes:
        if elem in tokened:
            attribute = elem
    val = tokened[tokened.index("is") + 1]
    sqlQuery += attribute+"='"+val+"'"

if "between" in tokened:
    for elem in attributes:
        if elem in tokened:
            attribute = elem
    val = tokened[tokened.index("between") + 1]
    sqlQuery += attribute+"='"+val+"'"
    val = tokened[tokened.index("between") + 3]
    sqlQuery += " and "+attribute+"='"+val+"'"

print(sqlQuery)
# for word in tokened:
#     if word in select_list:
#         result += "Select"

