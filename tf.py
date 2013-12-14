## supposed to be in another file
from sentiment import *
from math import log,trunc


tf_idf_cant_tell=[]
count =0
for w in cant_tell_set:
	if(count==5):
		break
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
	print normalized_tf
	print idf_score
	print tf_idf_cant_tell[count]
	print "\n"
	count=count+1
##for i in range(0,5):
	##print tf_idf_cant_tell[i]

