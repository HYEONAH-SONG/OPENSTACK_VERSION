# openstack_versioning



[TOC]



### 개발 환경 및 도구  

+ 개발 환경 

  + Windows 10 Pro (프로세서-Intel® Core™ i3-8130U, RAM-12.0GB, 

    SSD-WDS250G2B0B-00YS70(250GB))

  + Ubuntu 18.04.4 LTS (프로세서-Intel® Core™ i7-6700, RAM-23.0GB, 

    HDD- ST1000DM003-1SB1(1TB))

+ 수행 환경 : Visual Sutdio Code

+ 개발 도구 : Python(3.8.3), Django(2.1), Openstack API

+ 협업 도구 : Github



### Django 환경 구축

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





### Django 주요 스크립트 설명

### 버전관리 시스템 적용 개발 동작 - 시퀀스 다이어그램



