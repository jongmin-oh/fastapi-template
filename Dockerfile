FROM python:3.11.5-slim

#설치시 질문 안나오게 설정
ARG DEBIAN_FRONTEND=noninteractive

ARG DIR
ENV DIR $DIR

# 디렉터리 생성
RUN mkdir $DIR

# 소스코드 복사
COPY . $DIR

#작업 폴더 설정
WORKDIR $DIR

# 파이썬 패키지 설치
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "./start_service.sh"]
ENTRYPOINT ["./start_service.sh"]