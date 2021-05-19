data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1  #有等號，就會變成新增
# for word in wc:
# 	if wc[word] > 100:
# 		print(word, wc[word])

while True:
	word = input('請輸入單字:')
	if word in wc:
		print(word, wc[word])
	else:
		print('這個字沒有出現過')
	if word == 'q':
		print('感謝使用')
		break
# print(len(data))



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
print(len(good))


good2 = [d for d in data if 'good' in d]
print(len(good2))



bad = ['bad' in d for d in data]
print(bad)

bad = []
for d in data:
	bad.append('bad' in d)
print(bad)