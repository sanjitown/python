import smtplib #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
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
        server.login(my_sender,"Joker1234")  #括号中对应的是发件人邮箱账号、邮箱密码msg=msg1
        print('login success')
        server.sendmail(my_sender,[my_user,],msg.as_string())  #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件msg=msg1
        print('send success')
        server.quit()  #这句是关闭连接的意思
    except Exception:  #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    if ret: print('ok')
    return ret

mail('2247531586@qq.com',MIMEText('test from m1','plain','utf-8'))
