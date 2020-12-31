# Covid19-request-GUI

### 결과화면 (12/31일자 집계)
<img width="273" alt="corona_result" src="https://user-images.githubusercontent.com/69226719/103399903-8ab8cd80-4b86-11eb-876f-6781f2df3c6c.PNG">

### 라이브러리
- Pyinstaller
```
1. pip install pyinstaller
2. pyinstaller corona.py(exe파일로 만들 py파일명)
3. 설치완료 후 dist폴더 생성되어있는지 확인
4. dist폴더 안에 생성된 corona.exe 실행 
```
- BeautifulSoup
```
- 관리자 cmd 실행
- cd C:\Users\<사용자계정>\AppData\Local\Programs\Python\Python<버전>\Scripts
- pip 업데이트 : python.exe -m pip install --upgrage pip
- pip.exe install beautifulsoup4
- 터미널에서 from bs4 import BeautifulSoup 실행 후 에러없으면 설치완료
```
- PyQt5
```
(ex)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
```

### 한국 코로나 현황 사이트(request) : https://www.worldometers.info/coronavirus/country/south-korea/




