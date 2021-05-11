# 내 현재 IP를 찾아서 설정한 메일로 보내준다.

Python 2.x, 3.x 작동

[블로그 포스팅 보기](https://peterabbit.com/python-%ed%8c%8c%ec%9d%b4%ec%8d%ac%ec%9c%bc%eb%a1%9c-ip%ec%a3%bc%ec%86%8c-%ed%99%95%ec%9d%b8%ed%95%b4%ec%84%9c-%eb%a9%94%ec%9d%bc-%eb%b3%b4%eb%82%b4%ea%b8%b0/, '개발동기')  
메일을 받을 주소는 send_ip.py 파일에서 설정해줘야 한다.

config.py를 설정하면 바로 사용가능하다.  

config.py 예시  
MAIL_SENDER = " 메일 보내는 계정 주소 "  
MAIL_PASSWORD = " 메일 보내는 계정의 앱 비밀번호 "  
MAIL_SUBJECT = " 보내는 메일 제목 "  
MAIL RECEIVER = " 메일을 받을 주소 "  
