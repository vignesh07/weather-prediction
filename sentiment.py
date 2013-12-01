import csv
from nltk.corpus import stopwords
from collections import Counter
from collections import defaultdict

f= file('train.csv',"rb")
reader = csv.reader(f)

## List of lists to accomodate all tweets matching the respective sentiments as lists. Intersection is NOT zero

cant_tell=[[]]
negative=[[]]
neutral =[[]]
positive =[[]]
not_related=[[]]


i=0

for row in reader:
	i=i+1
	if(i==1):
		continue    ## to take care of omitting the heading from csv file, haven't figured out how else to do that
	
	if(float(row[4])>0):
		cant_tell.append(row[1])
	if(float(row[5])>0):	
		negative.append(row[1])
	if(float(row[6])>0):
		neutral.append(row[1])
	if(float(row[7])>0):
		positive.append(row[1])
	if(float(row[8])>0):
		not_related.append(row[1])
f.close()

## All the operations from here on take place on the list of lists and the data generated from the files



cant_tell_tokenised=[]

##testing code

for i in range(1,3):
	print cant_tell[i].split()
##testing code ends
	

## Dealing with Can't tell list of lists

cant_tell_tokenised=[]    ##contains the splits of the lists from cant_tell

for i in range(1,len(cant_tell)):
	cant_tell_tokenised.append(cant_tell[i].split()) 

cant_tell_words=[]  ##contains all the individual words parsed from cant_tell_tokenised 

for i in range(0,len(cant_tell_tokenised)):
	for j in range(0,len(cant_tell_tokenised[i])):
		cant_tell_words.append(cant_tell_tokenised[i][j])

print "length of ctt"

print len(cant_tell_tokenised)

print "length of cant tell words"
print len(cant_tell_words)

## Do a similar strip for positive, negative, neutral and not_related


negative_tokenised=[]  ##contains the splits of the lists from negative

for i in range(1,len(negative)):
	negative_tokenised.append(negative[i].split())

negative_words=[]  ##contains allt the individual words parsed from negative_tokenised

for i in range(0,len(negative_tokenised)):
	for j in range(0,len(negative_tokenised[i])):
		negative_words.append(negative_tokenised[i][j])



neutral_tokenised= [] ##contains the splits of the lists from neutral

for i in range(1,len(neutral)):
	neutral_tokenised.append(neutral[i].split())

neutral_words=[]  ##contains all the individual words parsed from neutral_tokenised

for i in range(0,len(neutral_tokenised)):
	for j in range(0,len(neutral_tokenised[i])):
		neutral_words.append(neutral_tokenised[i][j])


positive_tokenised=[]  ##contains the splits of the lists from positive

for i in range(1,len(positive)):
	positive_tokenised.append(positive[i].split())

positive_words=[]  ##contains all the individual words parsed from postive_tokenised

for i in range(0,len(positive_tokenised)):
	for j in range(0,len(positive_tokenised[i])):
		positive_words.append(positive_tokenised[i][j])


not_related_tokenised=[]  ##contains the splits of the lists from not_related

for i in range(1,len(not_related)):
		not_related_tokenised.append(not_related[i].split())

not_related_words=[]  ##contains all the individual words parsed from not_related_tokenised

for i in range(0,len(not_related_tokenised)):
	for j in range(0,len(not_related_tokenised[i])):
			not_related_words.append(not_related_tokenised[i][j])



##going to use NLP-Kit to remove all the stopwords from the word lists, so that we can use the remaining words to make the vector space


print "before running stopword loops"

print "length of cant, neg, neu, pos, not"

print len(cant_tell_words)
print len(negative_words)
print len(neutral_words)
print len(positive_words)
print len(not_related_words)

cant_tell_stop_removed =cant_tell_words[:]
negative_stop_removed = negative_words[:]
neutral_stop_removed = neutral_words[:]
positive_stop_removed = positive_words[:]
not_related_stop_removed = not_related_words[:]

for w in stopwords.words('english'):
	if w in cant_tell_stop_removed:
		cant_tell_stop_removed.remove(w)

	if w in neutral_stop_removed:
		neutral_stop_removed.remove(w)

	if w in negative_stop_removed:
		negative_stop_removed.remove(w)

	if w in positive_stop_removed:
		positive_stop_removed.remove(w)

	if w in not_related_stop_removed:
		not_related_stop_removed.remove(w)


print "AFTER RUNNING STOP"

print len(cant_tell_stop_removed)
print len(neutral_stop_removed)
print len(negative_stop_removed)
print len(positive_stop_removed)
print len(not_related_stop_removed)

print "SUCCESS :)"

print len(cant_tell_stop_removed)
print len(neutral_stop_removed)
print len(negative_stop_removed)
print len(positive_stop_removed)
print len(not_related_stop_removed)


##removing my own set of twitter stop words 

twitter_stop = ['@mention', 'RT']   ##should add more words as and when I come up.

for w in twitter_stop:
	if w in cant_tell_stop_removed:
		cant_tell_stop_removed.remove(w)

	if w in neutral_stop_removed:
		neutral_stop_removed.remove(w)

	if w in negative_stop_removed:
		negative_stop_removed.remove(w)

	if w in positive_stop_removed:
		positive_stop_removed.remove(w)

	if w in not_related_stop_removed:
		not_related_stop_removed.remove(w)

print "AFTER RUNNING STOP and MY STOP"

print len(cant_tell_stop_removed)
print len(neutral_stop_removed)
print len(negative_stop_removed)
print len(positive_stop_removed)
print len(not_related_stop_removed)

print "SUCCESS :)"

cant_tell_set = set(cant_tell_stop_removed)
neutral_set = set(neutral_stop_removed)
negative_set = set(negative_stop_removed)
positive_set = set(positive_stop_removed)
not_related_set = set(not_related_stop_removed)

print "set length?"

print len(cant_tell_set)
print len(neutral_set)
print len(negative_set)
print len(positive_set)
print len(not_related_set)

## Each list contains count of each word occuring in the list in the order present in the SET

cant_tell_count=defaultdict(int) 
neutral_count=defaultdict(int) 
negative_count=defaultdict(int) 
positive_count=defaultdict(int) 
not_related_count=defaultdict(int) 

for w in cant_tell_stop_removed:
	cant_tell_count[w]+=1

for w in neutral_stop_removed:
	neutral_count[w]+=1

for w in negative_stop_removed:
	negative_count[w]+=1

for w in positive_stop_removed:
	positive_count[w]+=1

for w in not_related_stop_removed:
	not_related_count[w]+=1

cant_tell_sum=0
neutral_sum=0
negative_sum=0
positive_sum=0
not_related_sum=0

for w in cant_tell_set:
	cant_tell_sum+=cant_tell_count[w]

for w in neutral_set:
	neutral_sum+=neutral_count[w]

for w in negative_set:
	negative_sum+=negative_count[w]

for w in positive_set:
	positive_sum+=positive_count[w]

for w in not_related_set:
	not_related_sum+=not_related_count[w]


## dividing each value by total value (normalized term frequency)
for w in cant_tell_set:
	cant_tell_sum+=cant_tell_count[w]

for w in neutral_set:
	neutral_sum+=neutral_count[w]

for w in negative_set:
	negative_sum+=negative_count[w]

for w in positive_set:
	positive_sum+=positive_count[w]

for w in not_related_set:
	not_related_sum+=not_related_count[w]









