#!python 查询12306余票并发送邮件
#coding:utf-8  #强制使用utf-8编码格式
import smtplib #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
import time
import requests

def ticket(url,train_mun): #查询是否有票
    wb_data=requests.get(url)
    info=str(wb_data.text).split(",")
    # for i in info:
    #     print(i)
    train_info=[]
    set=0
    for i,j in enumerate(info):
        train_info.append(j)
    train_info1=[]
    #print('traininfogot')
    for t in train_info:
        train_info1.append(t.split("|"))
    for j in train_info1:
        if len(j)>7:
            if j[3]==train_mun:
                if j[28]!='无':
                    #print('yes  ',j[28])
                    set=1
                #else: print('no')
    return set
def time1():
    t=0
    import time
    a=time.asctime( time.localtime(time.time()) )
    b=[]
    b.append(a[11])
    b.append(a[12])
    c=int(b[0])*10 +int(b[1])
    if c>=6:
        if c<=23:
         t=1
    return t

def mail(add,msg1): #发送邮件
    my_sender='sanjitown@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
    my_user=add #收件人邮箱账号，为了后面易于维护，所以写成了变量
    ret=True
    try:
        msg=msg1
        msg['From']=formataddr(["AI",my_sender])  #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["😄",my_user])  #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="抢票通知" #邮件的主题，也可以说是标题
        server=smtplib.SMTP("smtp.163.com",25) #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"Joker1234")  #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  #这句是关闭连接的意思
    except Exception:  #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    if set: print('ok')
    return ret

def main():
    import time
    date='2018-02-28'
    url='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=WHN&purpose_codes=0X00'.format(date)
    train_mun='Z4'
    het=0
    set=0
    while 1:
        t=time1()
        if t:
            print('get tickets info start!')
            state=mail('2247531586@qq.com',MIMEText('working good','plain','utf-8'))
            try:
                set=ticket(url,train_mun)
                if set==1:
                    if het==0:
                        het=mail('1339561314@qq.com',MIMEText('现在有票','plain','utf-8'))
                    #else: print('email sent before')
                else: print('no ticket yet! wait for 5 min')
            except Exception:
                print('error')

        else: print('it is not the right time')
        time.sleep(3000)

main()
