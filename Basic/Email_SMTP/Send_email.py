import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


'''
msg = MIMEText("hello,test!",_charset="utf-8")
msg["From"] = "546517050@qq.com"
msg["To"] = "mzhihuia@163.com"
msg["Subject"] = "python发邮件测试"
'''


msg = MIMEMultipart()
msg["From"] = "546517050@qq.com"
msg["To"] = "mzhihuia@163.com"
msg["CC"] = "moonlightzhihui@163.com"
msg["Subject"] = "python - 发送附件测试"

msg_sub = MIMEText("hello,test!",_charset="utf-8")
#将文本内容添加到msg中
msg.attach(msg_sub)


#图片
import os
img_data = open(os.getcwd()+"/image-attach.png","rb").read()
msg_img = MIMEImage(img_data)
msg_img.add_header("Content-Disposition","attachment",filename="image-test.png")
msg_img.add_header("Content-ID","<0>")
msg.attach(msg_img)

#html作为附件
html_content = open(os.getcwd()+"/html-attach.html",encoding="utf-8").read()
msg_html = MIMEText(html_content,"html","utf-8")
msg_html.add_header("Content-Disposition","attachment",filename="html-attach.html")
msg.attach(msg_html)



#step1:直接使用smtplib模块发送邮件，set_debuglevel1:打印出于SMTP服务器交互的所有信息
s = smtplib.SMTP_SSL("smtp.qq.com",465)
#s.set_debuglevel(1)
s.login("546517050","rrwkvtpayzjsbfaj")    #授权码
s.sendmail("546517050@qq.com","mzhihuia@163.com",msg.as_string())  #多个收件人用列表
s.close()

#邮件的发送
#step2:查看收件人的邮件，会发现没有发件人、没有主题、没有收件人信息
#      这是因为邮件主题、如何显示发件人、收件人等信息并不是通过STMP协议发送
#      而是包含在发送的文本中的，所以必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件


#step3:发送附件
#      带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身
#      可以构造一个MIMEMultipart对象代表邮件本身
#      然后往里面加上一个MIMRText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可



