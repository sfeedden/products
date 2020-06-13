import os #載入作業系統 operating system

products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('已找到檔案！')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if'商品,價格' in line:
				continue #繼續，進入下一回迴圈
			name, price = line.strip().split(',') #用,當作切割
			products.append([name, price])
		print(products)
else:
	print('未找到檔案~')



while True:
	name = input('請輸入商品名：')
	if name == 'quit':
		break
	price = input('請輸入價格：')
	price = int(price)
	# 方法一：p = []
	#        p.append(name)
	#        p.append(price)

	p = [name, price]  # 方法二
	products.append(p)

    # 方法三：producsts.append([name, price])
print(products)
print(products[0][0])

for product in products:
	print(product)
	print(product[0])  

with open('products.csv', 'w', encoding='utf-8' ) as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')