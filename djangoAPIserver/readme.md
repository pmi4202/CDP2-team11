# 사용방법(윈도우 기준, 가상환경설정 뺴고는 다 같음)
- 가상환경 접속(콘솔에 절대경로\djangoAPIserver\venv\Scripts\activate 입력)
- python manage.py runserver 입력
- post로 동영상파일 전송 (post로 파일전송방법은 insomnia혹은 postman프로그램 참조)
![image](https://user-images.githubusercontent.com/46833758/114305417-19889f00-9b13-11eb-9bb9-62f0122a64a1.png)

- 서버폴더에 post로 받은 동영상파일과 결과파일 생성됨을 확인

# 더 구현해야하는 것
- 현재 편집히스토리(json)는 내장되어있음. 편집히스토리와 비디오파일을 매칭해서 편집하기
- 동영상파일을 요청한 클라이언트에 전송하기 (전송 후 디스크에서 제거)
