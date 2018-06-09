password = 'a123456' #正確密碼
x = 3 #嘗試機會次數
while x > 0:
	x = x - 1
	pwd = input('請輸入密碼，最多可嘗試３次：')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if x > 0:
			print('還有', x,'次機會')
		else:
			print('沒機會了！要鎖帳號囉！')