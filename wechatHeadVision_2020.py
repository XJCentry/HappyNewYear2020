import itchat
import os
import PIL.Image as Image
from os import listdir
import math
import random
def login_wechat():
	itchat.auto_login(hotReload=True)

	friends = itchat.get_friends(update=True)[0:]
	print(len(friends))
	user = friends[0]["UserName"]
	username=user
	print(user)

	os.mkdir(user)

	num = 0

	for i in friends:
		img = itchat.get_head_img(userName=i["UserName"])
		fileImage = open(user + "/" + str(num) + ".jpg", 'wb')
		fileImage.write(img)
		fileImage.close()
		num += 1
	return username
def make_pci(yearlist,username):
	r = 8
	num_count = len(yearlist)

	pics = listdir(username)  # listdir(user)

	numPic = len(pics)
	if numPic<208:
		return "好友数量太少，无法生成理想图片"
	tot_eachcol = math.ceil(numPic / 208)#208是2020四个数字中“1”的数量总和，这里做了向上取整，防止出来的图片会遗漏一些好友的头像

	print('numPic', numPic)
	print('tot_eachcol', tot_eachcol)

	eachsize = int(math.sqrt(float(640 * 640) / numPic))#图片压缩的尺寸

	# print(eachsize)
	print('eachsize', eachsize)


	final_size = (eachsize * tot_eachcol * r) * num_count#生成的图片宽度
	toImage = Image.new('RGBA', (final_size, eachsize * 12))# eachsize * 12为图片高度，12为每个数字list的行数
	print("final_size", final_size)

	try:

		x = 0
		y = 0
		cur_img_index = 0
		progressbar=0
		temp = 0
		for eachnum in yearlist:
			# 拼接图片
			# print('eachnum', eachnum)
			for eachrow in eachnum:
				# print('eachrow',eachrow)
				for eachcol in eachrow:
					for tempnum in range(0, tot_eachcol, 1):
						# print('eachcol',eachcol)
						if eachcol == 1:
							try:
								# 打开图片
								img = Image.open(username + "/" + pics[cur_img_index])
							except IOError:
								print("Error: 没有找到文件或读取文件失败")
							# print('pics[cur_img_index]', pics[cur_img_index])
							if cur_img_index<numPic-2:
								cur_img_index += 1
								progressbar+=1
							else:
								cur_img_index=random.randint(0,numPic-1)
							print('%s%%' % str(math.ceil(progressbar / (numPic - 1) * 100)),
								  '-' * int(progressbar / (numPic - 1) * 100))
						else:
							try:
								# 打开图片
								img = Image.open('blank.jpg')#blank图片为640*640的白色纯色图片，用来占位
							except IOError:
								print("Error: 没有找到文件或读取文件失败")

						img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
						toImage.paste(img, (x * eachsize, y * eachsize))
						x += 1
				x = temp * tot_eachcol * r
				y += 1
			temp += 1

			x = temp * tot_eachcol * r
			y = 0

	except IOError:
		print("Error: ")

	toImage.save(username + ".png")
if __name__ == '__main__':
	username=login_wechat()
	
	year_2020 = [[
		[1, 1, 1, 1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1, 1, 1, 0],
		[0, 0, 0, 0, 1, 1, 1, 0],
		[0, 0, 0, 0, 1, 1, 1, 0],
		[0, 0, 0, 0, 1, 1, 1, 0],
		[1, 1, 1, 1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1, 1, 1, 0],
		[1, 1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1, 1, 1, 0]],
		[[0, 0, 0, 1, 1, 0, 0, 0],
		 [0, 0, 1, 1, 1, 1, 0, 0],
		 [0, 1, 1, 1, 1, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 1, 1, 1, 1, 0],
		 [0, 0, 1, 1, 1, 1, 0, 0],
		 [0, 0, 0, 1, 1, 0, 0, 0]],
		[[1, 1, 1, 1, 1, 1, 1, 0],
		 [1, 1, 1, 1, 1, 1, 1, 0],
		 [0, 0, 0, 0, 1, 1, 1, 0],
		 [0, 0, 0, 0, 1, 1, 1, 0],
		 [0, 0, 0, 0, 1, 1, 1, 0],
		 [1, 1, 1, 1, 1, 1, 1, 0],
		 [1, 1, 1, 1, 1, 1, 1, 0],
		 [1, 1, 1, 0, 0, 0, 0, 0],
		 [1, 1, 1, 0, 0, 0, 0, 0],
		 [1, 1, 1, 0, 0, 0, 0, 0],
		 [1, 1, 1, 1, 1, 1, 1, 0],
		 [1, 1, 1, 1, 1, 1, 1, 0]],
		[[0, 0, 0, 1, 1, 0, 0, 0],
		 [0, 0, 1, 1, 1, 1, 0, 0],
		 [0, 1, 1, 1, 1, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 0, 0, 1, 1, 0],
		 [0, 1, 1, 1, 1, 1, 1, 0],
		 [0, 0, 1, 1, 1, 1, 0, 0],
		 [0, 0, 0, 1, 1, 0, 0, 0]]]

	make_pci(year_2020,username)
	# 2：60，0：44
	itchat.send_image(username + ".jpg", 'filehelper')

