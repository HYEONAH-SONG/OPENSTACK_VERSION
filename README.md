# openstack_versioning

<br>


## 🧑‍💻 개발 환경 및 도구  

+ 개발 환경 

  + Windows 10 Pro (프로세서-Intel® Core™ i3-8130U, RAM-12.0GB, 

    SSD-WDS250G2B0B-00YS70(250GB))

  + Ubuntu 18.04.4 LTS (프로세서-Intel® Core™ i7-6700, RAM-23.0GB, 

    HDD- ST1000DM003-1SB1(1TB))

+ 수행 환경 : Visual Sutdio Code

+ 개발 도구 : Python(3.8.3), Django(2.1), Openstack API

+ 협업 도구 : Github

<br>
<br>




## 🔧 Django 환경 구축

Django는 파이썬으로 만들어진 무료 오픈소스 웹 애플리케이션 프레임워크이다.

Django를 사용하기 위해서는 파이썬이 필요하다. 만약 파이썬이 설치가 안되어 있으면 먼저 파이썬을 설치해야 한다. (파이썬 설치 사이트 : https://www.python.org/downloads/)

파이썬 설치를 완료했다면 파이썬이 설치된 경로에서 Scripts 디렉토리로 이동한다.

그리고 아래와 같은 명령어를 통해 Django를 설치한다.

```
$ python -m django --version
```

 

Django 설치가 완료되면 프로젝트를 생성한다. (프로젝트 이름은 python 또는 Django에서 사용중인 이름은 피해야 한다.)

```
$ django-admin startproject <프로젝트 이름>
```

프로젝트를 생성하면 아래와 같은 스크립트가 생성된다. (프로젝트 이름이 mysite인 경우)

![image](https://user-images.githubusercontent.com/48307561/97712078-4adf5680-1b01-11eb-9158-d8e33368f70e.png)

 

그리고 개발을 하기위한 앱을 생성한다.

```
$ python manage.py startapp <앱 이름>
```

 

그러면 아래와 같은 스크립트가 생성된다. (앱 이름이 polls인 경우)

![image](https://user-images.githubusercontent.com/48307561/97712113-5763af00-1b01-11eb-8b52-9ccf6629bc5b.png)

 

위와 같은 방법으로 Django 환경을 구축한다.

<br>
<br>



## 📒 Django 주요 스크립트 설명

[settings.py]

![image](https://user-images.githubusercontent.com/48307561/97781792-1509a300-1bd1-11eb-9840-c21200365e3e.png)

setting.py 파일에서 로그 설정, APP 등록, Templates 설정, DB설정, 다국어 및 지역 시간 설정, 정적파일 설정 등의 장고 프레임워크의 모든 개발환경 세팅을 한다.



[urls.py]

![image](https://user-images.githubusercontent.com/48307561/97781837-4edaa980-1bd1-11eb-92b6-3548bea4afe6.png)

urls.py 파일에 URL 경로에 관한 논리를 정의한다.

urlpatterns에 특정 URL을 기준으로 views.py에 정의한 view 함수를 매핑시킨다. 그래서 만약 지정된 URL 패턴과 일치하는 HTTP 요청이 수신된다면 관련된 view 함수가 실행된다.



[templates]

![image](https://user-images.githubusercontent.com/48307561/97781858-631ea680-1bd1-11eb-9440-8b7e59362285.png)

templates는 파일의 구조나 레이아웃(예: HTML 페이지)을 정의하고, 실제 내용을 보여주는데 사용되는 텍스트 파일을 저장하는 폴더이다.

+ cloudservice.html : 코딩 교육 환경 웹페이지.
+ rechecklan.html : 웹 페이지에서 언어 항목 선택하지 않고 submit 했을 경우.
+ recheckname.html : 웹 페이지에서 강의실명 작성하지 않고 submit 했을 경우.



[forms.py]

![image](https://user-images.githubusercontent.com/48307561/97781871-7e89b180-1bd1-11eb-8030-cc93b29e3bc8.png)

form은 웹 페이지상에서 한 개 이상의 필드나 위젯들의 묶음을 말하며, 사용자로부터 정보를 수집하여 서버에 제출하는데 사용된다. 

forms.py에서는 Language(코딩 언어)의 종류를 저장하는 form을 정의한다.



<br>
<br>

## 📍 버전관리 시스템 적용 개발 동작 - 시퀀스 다이어그램

![image](https://user-images.githubusercontent.com/48307561/97959268-59c05480-1df2-11eb-9952-60ac79fe4f48.png)

1. USER가 서버(127.0.0.1:8000)에 접속하면 views.py의 view()함수가 호출.
2. view()함수는 cloudservice.html로 웹페이지 생성.
3. 만들어진 웹페이지에서 코딩 교육 환경의 리소스 정보를 사용자가 입력.
   + 강의실명을 적지 않고 제출할 경우 recheckname.html로 웹페이지 생성
   + 언어를 선택하지 않고 제출할 경우 rechecklan.html로 웹페이지 생성
4. 입력이 완료되면 views.py의 send()함수를 호출.
5. 사용자에게 입력한 리소스 정보를 바탕으로 코딩 교육 환경 생성


<br>
<br>

## 📍 실제 동작

### 👉 Major 버전 갱신 (운영체제 비교)

+ 웹 인터페이스를 통해 코딩 교육 환경의 운영체제를 선택

+ 기존의 인덱스 파일에서 앞선 버전과 다른 운영체체의 코딩 환경을 생성할 경우, Major 버전을 갱신하여  index파일에 저장하고 환경에 맞는 VM을 생성.

#### Ubuntu Linux 64-bit를 선택한 경우
![스크린샷 2021-05-06 오전 10 42 31](https://user-images.githubusercontent.com/48307561/117230302-c2e35c00-ae57-11eb-8787-7756706a5ea3.png)

![스크린샷 2021-05-06 오전 10 42 43](https://user-images.githubusercontent.com/48307561/117230314-ca0a6a00-ae57-11eb-8a10-8f0b18083be0.png)

#### CentOS 7 x86-64를 선택한 경우
![스크린샷 2021-05-06 오전 10 44 15](https://user-images.githubusercontent.com/48307561/117230420-00e08000-ae58-11eb-87b7-0e3535e4a981.png)

![스크린샷 2021-05-06 오전 10 44 23](https://user-images.githubusercontent.com/48307561/117230428-05a53400-ae58-11eb-971f-4f4520117ad3.png)

#### Major 버전이 갱신된 index 파일
![스크린샷 2021-05-06 오전 10 44 54](https://user-images.githubusercontent.com/48307561/117230456-181f6d80-ae58-11eb-8f2a-39d28eea2759.png)


<br>


### 👉 Major 버전 갱신 (프로그래밍 언어 비교)

+ 웹 인터페이스를 통해 코딩 교육 환경에서 사용할 프로그래밍 언어 선택
+ 기존의 인덱스 파일에서 앞선 버전과 다른 언어의 코딩 환경을 생성할 경우,  Major 버전을 갱신하여  index파일에 저장하고 환경에 맞는 VM을 생성.

#### C언어를 선택한 경우
![스크린샷 2021-05-06 오전 10 47 23](https://user-images.githubusercontent.com/48307561/117230614-72203300-ae58-11eb-9f5e-7e44d88d31e2.png)


![스크린샷 2021-05-06 오전 10 47 33](https://user-images.githubusercontent.com/48307561/117230623-76e4e700-ae58-11eb-8834-b5081b6f39b1.png)


#### C++언어를 선택한 경우

![스크린샷 2021-05-06 오전 10 47 43](https://user-images.githubusercontent.com/48307561/117230637-7cdac800-ae58-11eb-8e37-7e893f11fa56.png)


![스크린샷 2021-05-06 오전 10 47 52](https://user-images.githubusercontent.com/48307561/117230648-819f7c00-ae58-11eb-8c91-c51293991b15.png)

#### Major 버전이 갱신된 index 파일
![스크린샷 2021-05-06 오전 10 48 01](https://user-images.githubusercontent.com/48307561/117230664-86fcc680-ae58-11eb-974a-ec1d4bac2746.png)

<br>


### 👉 Minor 버전 갱신 (리소스 정보 비교)

+ 웹 인터페이스를 통해 코딩 교육 환경에 수강 인원을 입력
+ 인원에 대해 리소스(flavor) 할당
+ 기존의 인덱스 파일에서 앞선 버전과 다른 flavor의 경우, Minor 버전을 갱신하여 index파일에 저장하고 환경에 맞는 VM을 생성.

#### 학생 10명을 선택한 경우
![스크린샷 2021-05-06 오전 10 50 13](https://user-images.githubusercontent.com/48307561/117230813-d642f700-ae58-11eb-8280-e452c0374d23.png)

#### 학생 100명을 선택한 경우
![스크린샷 2021-05-06 오전 10 50 19](https://user-images.githubusercontent.com/48307561/117230821-d93de780-ae58-11eb-91e1-254df5f88194.png)

#### Minor 버전이 갱신된 index 파일
![스크린샷 2021-05-06 오전 10 50 25](https://user-images.githubusercontent.com/48307561/117230832-dd6a0500-ae58-11eb-8e7e-341bc05faf37.png)

<br>

### 👉 각 버전의 리소스 정보를 포함하고 있는 인덱스 파일
![스크린샷 2021-05-06 오전 10 51 24](https://user-images.githubusercontent.com/48307561/117230885-01c5e180-ae59-11eb-8d31-fb1cea012eca.png)

<br>


### 👉 템플릿 파일과 인텍스 파일이 저장된 오브젝트 스토리지
![스크린샷 2021-05-06 오전 10 51 35](https://user-images.githubusercontent.com/48307561/117230895-068a9580-ae59-11eb-8d54-837b706d97c6.png)

