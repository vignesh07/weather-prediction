## supposed to be in another file
from sentiment import *
from math import log,trunc


tf_idf_cant_tell=[]
tf_idf_neutral=[]
tf_idf_positive=[]
tf_idf_negative=[]
tf_idf_not_related=[]

#for cant_tell document

for w in cant_tell_set:
	idf_score=0
	normalized_tf=float((float(cant_tell_count[w])/cant_tell_sum))
	if w in cant_tell_set:
		idf_score+=1
	if w in neutral_set:
		idf_score+=1
	if w in positive_set:
		idf_score+=1
	if w in negative_set:
		idf_score+=1
	if w in not_related_set:
		idf_score+=1

	logidf=float(log(5/float(idf_score)))
	tf_idf_cant_tell.append(float(normalized_tf*logidf))


#for neutral document
for w in neutral_set:
	idf_score=0
	normalized_tf=float((float(neutral_count[w])/neutral_sum))
	if w in cant_tell_set:
		idf_score+=1
	if w in neutral_set:
		idf_score+=1
	if w in positive_set:
		idf_score+=1
	if w in negative_set:
		idf_score+=1
	if w in not_related_set:
		idf_score+=1

	logidf=float(log(5/float(idf_score)))
	tf_idf_neutral.append(float(normalized_tf*logidf))
	
# for positive set

for w in positive_set:
	idf_score=0
	normalized_tf=float((float(positive_count[w])/positive_sum))
	if w in cant_tell_set:
		idf_score+=1
	if w in neutral_set:
		idf_score+=1
	if w in positive_set:
		idf_score+=1
	if w in negative_set:
		idf_score+=1
	if w in not_related_set:
		idf_score+=1

	logidf=float(log(5/float(idf_score)))
	tf_idf_positive.append(float(normalized_tf*logidf))


#for negative 

for w in negative_set:
	idf_score=0
	normalized_tf=float((float(negative_count[w])/negative_sum))
	if w in cant_tell_set:
		idf_score+=1
	if w in neutral_set:
		idf_score+=1
	if w in positive_set:
		idf_score+=1
	if w in negative_set:
		idf_score+=1
	if w in not_related_set:
		idf_score+=1

	logidf=float(log(5/float(idf_score)))
	tf_idf_negative.append(float(normalized_tf*logidf))


# for not related 

for w in not_related_set:
	idf_score=0
	normalized_tf=float((float(not_related_count[w])/not_related_sum))
	if w in cant_tell_set:
		idf_score+=1
	if w in neutral_set:
		idf_score+=1
	if w in positive_set:
		idf_score+=1
	if w in negative_set:
		idf_score+=1
	if w in not_related_set:
		idf_score+=1

	logidf=float(log(5/float(idf_score)))
	tf_idf_not_related.append(float(normalized_tf*logidf))


if len(cant_tell_set) == len(tf_idf_cant_tell):
	print "cant tell ok"

if len(positive_set)==len(tf_idf_positive):
	print "positive ok"

if len(negative_set)==len(tf_idf_negative):
	print "negative ok"

if len(neutral_set)==len(tf_idf_neutral):
	print "neutral ok"

if len(not_related_set)==len(tf_idf_not_related):
	print "not related ok"

print "tf-idf vectors calculated"

print "printing samples"

for i in range(0,10):
	print tf_idf_cant_tell[i]
	print tf_idf_positive[i]
	print tf_idf_negative[i]
	print tf_idf_neutral[i]
	print tf_idf_not_related[i]

