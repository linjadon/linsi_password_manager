import pymysql
import time
import os
import sys
from re import search
from tkinter import *
import tkinter.messagebox
from tkinter import dialog
from tkinter import filedialog
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


#mysqldump -u xxxxxxxxx -p xxxx pass>xxxxxx.sql

'''   
		PASSWORD ENCRYPT AND DECRYPT
#UPDATE users SET password = AES_ENCRYPT(password, 'my secret key')

-- Decrypt the password field in the users table
SELECT AES_DECRYPT(password, 'my secret key') FROM users
'''
def query_account():
#	for item in tree.selection():
#		tree.delete(item)
	conn	= pymysql.connect(	host='127.0.0.1',
								port=3306,
								user='xxxxxx',
								password='xxxxxxxx',
								db='xxxxxxxx',
								charset='utf8')
	cursor = conn.cursor()#SQL会话
	sql_filter = entry_3.get()
	sql = ''' select * from PASS where PLATFORM regexp '%s' '''%(sql_filter)
	cursor.execute(sql)#执行SQL语句
	result1 = cursor.fetchall()#获取SQL语句输出的信息
	if len(result1) == 0:
		sql = ''' select * from PASS where NAME regexp '%s' '''%(sql_filter)
		cursor.execute(sql)
		result2 = cursor.fetchall()
		if len(result2) ==0:
			pass
#			display_lin.insert('insert',"Warning please retry input filter!")
		else:
			for i in result2:
				info = i[1]+'\n\t'+i[2]+'\n\t'+str(i[3])+'\n'
				display_lin.insert('insert',info)
#				tree.insert("",0,text=i[0],values=(i[1],i[2],str(i[3])),tags = ('odd',))
	else:
		x=2
		for i in result1:
			info = i[1]+'\n\t'+i[2]+'\n\t'+str(i[3])+'\n'
			display_lin.insert('insert',info)
#			tree.insert("",0,text=i[0],values=(i[1],i[2],i[3]),tags = ('odd',))
			x=x+1
	cursor.close()
	conn.close()

def change_info():
	conn	= pymysql.connect(	host='127.0.0.1',
							port=3306,
							user='xxxxxx',
							password='xxxxxxxxx',
							db='xxxxxxxx',
							charset='utf8')
	cursor=conn.cursor()
	change_field = entry_1.get()
	change_value = entry_2.get()
	index_ID	 = entry_4.get()
	sql = ''' update PASS set %s = '%s' where ID regexp '%s'
			'''%(change_field,change_value,index_ID)
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()


def add_user():
	def exe():
		conn	= pymysql.connect(	host='127.0.0.1',
							port=3306,
							user='xxxxxxxxx',
							password='xxxxxxxxx',
							db='xxxxxxxx',
							charset='utf8')
		platform= add_entry_1.get()
		name	= add_entry_2.get()
		password= add_entry_3.get()
		descrip	= add_entry_4.get()
		sql		= "insert into PASS(PLATFORM,NAME,PWD,DESCRIPTION)\
				values('%s','%s','%s','%s');"%(platform,name,password,descrip)
		cursor	= conn.cursor()
		result	= cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()

	add_tool = Tk()
	add_tool.title("add tool")
	add_tool.geometry("300x200-1+1")
	add_tool["bg"]="Royal Blue"
#输入平台名称
	add_label_1	= Label(add_tool,
						text="platform:",
						font=('微软雅黑',12),
						bg='Royal Blue',
						fg='white')
	add_label_1.place(x=10,y=20)
	add_entry_1	= Entry(add_tool)
	add_entry_1.place(x=120,y=20)
#输入账号
	add_label_2	= Label(add_tool,
						text="name:",
						font=('微软雅黑',12),
						bg='Royal Blue',
						fg='white')
	add_label_2.place(x=10,y=40)
	add_entry_2	= Entry(add_tool)
	add_entry_2.place(x=120,y=40)
#输入密码
	add_label_3	= Label(add_tool,
						text="pwd:",
						font=('微软雅黑',12),
						bg='Royal Blue',
						fg='white')
	add_label_3.place(x=10,y=60)
	add_entry_3	= Entry(add_tool)
	add_entry_3.place(x=120,y=60)
#输入描述
	add_label_4	= Label(add_tool,
						text="desc:",
						font=('微软雅黑',12),
						bg='Royal Blue',
						fg='white')
	add_label_4.place(x=10,y=80)
	add_entry_4	= Entry(add_tool)
	add_entry_4.place(x=120,y=80)
#获取账号用户名和密码
	add_button_1= Button(add_tool,
						text='start',
						fg='white',
						bg='blue',
						width=10,
						command=exe)
	add_button_1.place(x=140,y=120)
	add_tool.mainloop()

def export_data():
	conn	= pymysql.connect(	host='127.0.0.1',
							port=3306,
							user='xxxxxxxxx',
							password='xxxxxxxxx',
							db='xxxxxxxx',
							charset='utf8')
	cursor=conn.cursor()
	sql = ''' select * from PASS;'''
	cursor.execute(sql)#执行SQL语句
	conn.commit()
	result = cursor.fetchall()
	file = open("pass.txt",'a+',encoding='utf-8')
	print(result)
	for i in result:
		file.write(str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\n')
	file.close()
	cursor.close()
	conn.close()


if __name__ == '__main__':
	linsi_tool = Tk()
	linsi_tool.title("linsi tool")
	linsi_tool.geometry("500x500-1+1")
	linsi_tool["bg"]="Royal Blue"
#	linsi_tool.iconbitmap("boy.ico")
#输入账号
	label_1	= Label(linsi_tool,
						text="Field:",
						font=('微软雅黑',12),
						bg='Royal Blue',
						fg='white')
	label_1.place(x=10,y=20)
	entry_1	= Entry(linsi_tool)
	entry_1.place(x=120,y=23)
#输入密码
	label_2	= Label(linsi_tool,
						text="Value:",
						font=('微软雅黑',12),
						bg='Royal Blue',
						fg='white')
	label_2.place(x=10,y=60)
	entry_2	= Entry(linsi_tool)
	entry_2.place(x=120,y=60)
	label_3 = Label(linsi_tool,
						text="Filter:",
						font=('微软雅黑',12),
						bg="Royal Blue",
						fg='white')
	label_3.place(x=10,y=90)
	entry_3 = Entry(linsi_tool)
	entry_3.place(x=120,y=90)
	label_4 = Label(linsi_tool,
						text="ID:",
						font=('微软雅黑',12),
						bg="Royal Blue",
						fg='white')
	label_4.place(x=10,y=120)
	entry_4 = Entry(linsi_tool)
	entry_4.place(x=120,y=120)
#获取账号用户名和密码
	button_1= Button(linsi_tool,
						text='query_account',
						fg='white',
						bg='blue',
						width=10,
						command=query_account)
	button_1.place(x=260,y=20)
#获取IP列表
	button_3= Button(linsi_tool,
						text='change_info',
						fg='white',
						bg='blue',
						width=10,
						command=change_info)
	button_3.place(x=260,y=80)
#开始配置或者备份
	button_4=Button(linsi_tool,
						text='add_user',
						fg='white',
						bg='blue',
						width=10,
						command=add_user)
	button_4.place(x=260,y=130)
#
#	scrolledText is 多级窗口控件
#
#创建表控件
#	table = ttk.Notebook(linsi_tool)
#	sub_table = ttk.Frame(table,width=150)
#	table.add(sub_table,text="display")
#	table.place(x=5,y=200,width=350,heigh=150)
#创建标签控件
#	display = ttk.LabelFrame(sub_table,width=350,height=150)
#	display.place(x=1,y=1)
#创建显示文档控件
#	display_lin = ScrolledText(display,width=350,height=100)
#	display_lin.place(x=1,y=1)


#	Text 文本框

	scroll = tkinter.Scrollbar(linsi_tool)
	scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
	display_lin = tkinter.Text(linsi_tool,width=50,
								height=15,
								yscrollcommand=scroll.set)
	display_lin.pack(side=tkinter.RIGHT,fill=tkinter.Y)
	scroll.config(command=display_lin.yview)
	display_lin.place(x=1,y=200)

	style = ttk.Style()
	style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
	style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
	style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
	linsi_tool.mainloop()


#######################			tree directory				########################
'''
	tree=ttk.Treeview(linsi_tool,style="mystyle.Treeview",)
	tree["columns"] = ("one","two","three")

	tree.column("#0", width=50, minwidth=50)
	tree.column("one", width=120, minwidth=80)
	tree.column("two",width=120,minwidth=80)
	tree.column("three",width=150,minwidth=80)

	tree.heading("#0", text="ID",anchor=tkinter.W)
	tree.heading("one", text="Platform",anchor=tkinter.W)
	tree.heading("two", text="Name",anchor=tkinter.W)
	tree.heading("three", text="Pass",anchor=tkinter.W)

	tree.tag_configure('even', background='#E8E8E8')
	tree.tag_configure('odd', background='#DFDFDF')
	tree.place(x=1,y=250)
'''


#	change_info('root','123456')
#delete from pass where ID=1
