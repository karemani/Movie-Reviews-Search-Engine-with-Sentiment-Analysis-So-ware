import sys
import csv

tempFnameOr =[]
tempFnameAnd = []
tempFnameAndNot= []
intersectionAnd = []

result = []
def queryProcessing():
    command = []
    print("Enter the query")
    command = raw_input()
    if (command == "exit"):
        print "Exit Sucessful"
        sys.exit()
    operands = []
    query = command.split(" ")
    remove_stopwords(query)
    query =[x.lower() for x in query]
    i=0
#-----------------------------------Seperation of the operand and operations---------------------------------
    while i < len(query):
        if ("and" == query[i] or "or" == query[i] or ("and" == query[i] and "not" == query[i+1])):
            if("and" in query[i] and "not" in query[i+1]):
                operator = "and not"
                i = i+2
            else:
                operator = query[i]
                i = i+1
            while i<len(query):
                if ("and" == query[i] or "or" == query[i] or ("and" == query[i] and "not" == query[i+1])):
                    operand = []
                    break
                else:
                    operands.append(query[i])
                    i = i + 1
            action(operator,operands)
    resultList = []
    finalList = []
    finalList2 = []
    final=[]
    if(len(result)==0):
        print "No Result"
    else:
        fileout=open("output.txt","w")
        for x in result:
            print x , docTable[x][0]

    return

def action(operator,operands):
    # print "operator =",operator
    # print "operand =",operands
    tempFname = {}
    for x in operands:
        if(dic.has_key(x)):
            temp_index = dic[x]
            index = temp_index[0]
            docFrequency = int(index[0])
            #print docFrequency
            offset =  int(index[1])
            end = offset + docFrequency
            while offset<end:
                value = posting[offset]
                if(tempFname.has_key(x)):
                    tempFname[x].append(value[0])
                else:
                    tempFname.setdefault(x,[])
                    tempFname[x].append(value[0])
                offset += 1
    #print tempFname.items()
    if(operator == "and"):
         tempFnameAnd = tempFname.values()
         #print "printing the interection"
         global intersectionAnd
         if(len(tempFnameAnd)>0):
            intersectionAnd = set.intersection(*map(set, tempFnameAnd))
            intersectionAnd =  list(intersectionAnd)
         # print "inside the and"
         global result
         result= intersectionAnd[:]
         # print result
    if(operator == "and not"):
         tempFnameAndNot = tempFname.values()
         tempUnionAndNot = []
         tempDiffAndNOt = []
         # print tempFnameAndNot
         for x in tempFnameAndNot:
             tempUnionAndNot = list(set(tempUnionAndNot).union(x))

         tempDiffAndNOt = set(intersectionAnd) - set(tempUnionAndNot)

        # global result
         result = list(tempDiffAndNOt)
         #print result
         #print result


    if(operator == "or"):
         tempFnameOr = tempFname.values()
         unionOr = []
         for x in tempFnameOr:
             unionOr = list(set(unionOr).union(x))
        # print unionOr
         #global result
         result = unionOr[:]
         #print result
#----------------------------Check the operator and Call the particular function--------------------------
    del operands[:]
    return
def remove_stopwords(words):
    while "a" in words: words.remove("a")
    while "the" in words: words.remove("the")
    while "an" in words: words.remove("an")
    while "by" in words: words.remove("by")
    while "from" in words: words.remove("from")
    while "for" in words: words.remove("for")
    while "hence" in words: words.remove("hence")
    while "of" in words: words.remove("of")
    while "with" in words: words.remove("with")
    while "in" in words: words.remove("in")
    while "within" in words: words.remove("within")
    while "who" in words: words.remove("who")
    while "within" in words: words.remove("within")
    while "when" in words: words.remove("when")
    while "where" in words: words.remove("where")
    while "why" in words: words.remove("why")
    while "how" in words: words.remove("how")
    while "was" in words: words.remove("was")
    while "whom" in words: words.remove("whom")
    while "have" in words: words.remove("have")
    while "had" in words: words.remove("had")
    while "has" in words: words.remove("has")
    while "for" in words: words.remove("for")
    while "do" in words: words.remove("do")
    while "does" in words: words.remove("does")
    while "done" in words: words.remove("done")
    while "but" in words: words.remove("but")
    while " " in words: words.remove(" ")
    return;
dic={ }
with open('Dictionary.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
      dic.setdefault(row[0],[])
      dic[row[0]].append((row[1],row[2]))
posting = []
counter = 0
i=0
with open('Posting.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
      if(counter == 0):
          counter = 1
          pass
      else:
        val = (row[0],row[1])
        posting.append(val)
        i = i+1
counter1 = 1
docTable = { }
with open('DocsTable.txt') as f:
    next(f) # throw away header
    next(f) # throw away |-----+-----|
    for line in f:
        docTable.setdefault(line[:9],[])
        docTable[line[:9]].append((line[11:72].strip(),line[74:101].strip(),line[103:457].strip(),line[459:460]))
intersectionAnd = []
queryProcessing()
