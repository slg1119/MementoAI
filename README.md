# MomentoAI 과제

## 1. 개발 환경
- Python 3.11
- FastAPI
- MySQL
- Docker
- Docker-compose

## 2. 실행 방법
```bash
$ docker-compose up
$ docker-compose exec web alembic upgrade head
```

## 3. MySQL 선택 이유
- 제일 익숙한 RDBMS
- MongoDB를 사용해 보고 싶었지만, 익숙한 MySQL을 선택