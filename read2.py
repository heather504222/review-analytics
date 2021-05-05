data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
print(len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為',sum_len/len(data),'個字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆留言小於100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言包含good這個字')
print(good[0])