import socket
import smtplib
import socket
from email.mime.text import MIMEText
from config import * #중요정보는 config파일에 분리 저장(메일 이름, 메일 주소, 보내는 메일 주소, 보내는 메일 앱비밀번호)

def send_email(who, msg):
	msg = MIMEText(msg)
	msg['Subject'] = MAIL_SUBJECT
	msg['To'] = who
	s.sendmail(MAIL_SENDER, who, msg.as_string())

if __name__ == '__main__':
	#소켓을 이용해 아이피 확인
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	print(s.getsockname()[0])
	s.close()
	#smtp 메일 전송
	s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	s.login(MAIL_SENDER, MAIL_PASSWORD)
	send_email(MAIL RECEIVER, ip)
	s.quit()
