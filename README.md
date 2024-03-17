# 서비스 소개

<div align="center">
오늘의 식사 메뉴를 추천해주고,<br>
내가 필요한 레시피를 검색할 수 있는 플랫폼
<h3>오늘의 밥</h3>
</div>

<br>
<br>

# 📌 기능

- OPENAI를 이용하여 날씨 및 그날 기분에 따라서 오늘의 식사 메뉴를 추천
- 자신이 좋아하거나, 자주먹는 음식을 즐겨찾기
- 검색과 동시에 추천된 음식의 리스트에서 음식을 골라 음식점 위치 확인 및 리뷰 확인하기
- 냉장고에 남아 있는 재료를 가지고 만들 수 있는 레시피를 검색
- 편의점 꿀조합 레시피 보기
- 방송에서 핫한 레피시 보기
- 음식 양념 레시피 보기

<br>
<br>

# 🖥️ Getting Start

## 필수 사항
시작하기 전에 시스템에 다음이 설치되어 있는지 확인하십시오.
- Python

## Make Postgresql Database For mac
- brew services start postgresql
- psql postgres
- create database obab;

## Make Postgresql Database For window
- PostgreSQL을 다운로드하고 설치합니다 : https://www.postgresql.org/download/windows/
- 설치가 완료되면 pgAdmin을 실행시킵니다.
- Databases에 obab 테이블을 만듭니다.

## Start Project
1. 저장소를 로컬과 연결합니다.
- git clone https://github.com/O-BAB/obab-server.git

2. manage.py가 있는 프로젝트 디렉토리로 이동합니다.
- cd obab_server 

3. 프로젝트 종속성을 설치합니다.
- pip install -r requirements.txt

4. 데이터베이스 마이그레이션을 실행합니다.
- python manage.py makemigrations --settings=obab_server.settings.local_settings
- python manage.py migrate --settings=obab_server.settings.local_settings

5. 프로젝트를 실행합니다.
- python manage.py runserver --settings=obab_server.settings.local_settings

6. 웹 브라우저를 열고 http://localhost:8000에 접속하여 애플리케이션을 확인할 수 있습니다.

<br>
<br>

# 서버 환경
- pyton 3.11.6
- Django 5.0.3
- DRF : 3.14.0
- Database : Postgresql
- AWS (plan)
- API : Kakao API, Google API, Naver API, OPENAI API
<br>
<br>

# 아키텍처

- 추후 작성

# 프로젝트 구조
<a href="https://github.com/O-BAB/obab-server/blob/develop/tree.txt">프로젝트 구조</a>
