import os #載入作業系統 operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if'商品,價格' in line:
				continue #繼續，進入下一回迴圈
			name, price = line.strip().split(',') #用,當作切割
			products.append([name, price])
		print(products)
	return products

#輸入商品
def user_input(products):
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
	return products

#印出商品
def print_products(products):
	print(products)
	print(products[0][0])

	for product in products:
		print(product)
		print(product[0])  

#寫入商品
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8' ) as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p [1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案在不在
 		print('已找到檔案！')
 		products = read_file(filename)
	else:
		print('未找到檔案~')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()