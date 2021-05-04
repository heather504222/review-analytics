data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
print(len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為',sum_len/len(data),'個字')
