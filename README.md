# 컨테이너 오리엔티드 프로그래밍

> 예전엔 3개의 서비스를 연결하는 것으로도 충분한 서비스를 만들어낼 수 있었고 그것은 지금도 유효하다. 하지만 단일 서비스를 만들어내기가 너무나 쉬워진 요즘에는 굳이 분리된 환경의 갯수를 제한할 필요가 없어졌다. 그러다보니 함수를 개발하는 데에 걸리는 시간보다 인프라를 구성하는데 걸리는 시간이 더 오래걸리고 있다는 생각이 드는 요즘, 어차피 미래에 만들게 될 것들을 미리 만들어보려 한다. 



## 아키텍쳐

   하나씩 그려나가보겠다. 가능한 많은 것을 연결시킬 것이기 때문에 로컬이든 클라우드든 이것저것 다 붙여볼 계획이다. 



## 구성

   심심할 때마다 하나씩 하나씩 늘려간다. 그 시작은 언제나 그러했듯이 Nginx로 시작하겠다. 



## Quick Start

Docker network 추가

```bash
docker network create net1
```



Docker volume 추가

```bash
docker volume create mariadb_volume
docker volume create mysql_volume
docker volume create postgres_volume
docker volume create mongo_volume
docker volume create redis_volume 
docker volume create rabbitmq_volume
docker volume create elasticsearch_volume
```



실행

```bash
# 최초 1번, 그리고 docker image를 업데이트하고싶을 때 실행
docker compose build

# 실행
docker compose up -d
```



옵션 - replica 추가

```
docker-compose.yaml 파일에서 replica의 숫자를 바꾸면 됨. (Loadbalancer 제외)
```









## 기타

- OS에 상관없이 도커나 kubectl을 실행시킬 수 있다면 어디서든 실행될 수 있도록 만든다. 