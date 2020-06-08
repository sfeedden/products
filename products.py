products = []
while True:
	name = input('請輸入商品名：')
	if name == 'quit':
		break
	price = input('請輸入價格：')
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