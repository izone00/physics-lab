# 로컬 개발 환경

이 프로젝트는 Jekyll 기반이며 Docker Compose로 실행합니다. Ruby와 gem을 호스트
시스템에 직접 설치할 필요가 없습니다.

## 1. Docker 런타임

이 Mac에는 관리자 권한 없이 사용할 수 있는 Docker CLI와 Colima가 설치되어 있습니다.
재부팅 후 Docker 엔진이 실행 중이 아니면 다음 명령으로 시작합니다.

```bash
make engine-start
```

설치 여부와 엔진 연결은 아래 명령으로 확인합니다.

```bash
docker --version
docker compose version
docker info
```

다른 Mac에서 처음 구성할 때는 다음 패키지를 설치하면 됩니다.

```bash
brew install docker docker-compose docker-buildx colima
```

Docker Desktop을 이미 정상 사용 중인 환경이라면 Colima 없이 그대로 진행할 수 있습니다.

## 2. 최초 빌드 및 실행

프로젝트 루트에서 실행합니다.

```bash
make setup
make serve
```

빌드가 끝나면 다음 주소를 엽니다.

<http://localhost:8080/physics-lab/>

`_config.yml`의 `baseurl`이 `/physics-lab`이므로 로컬에서도 이 경로가 필요합니다.
파일 변경은 자동으로 반영되며, `_config.yml` 변경 시 Jekyll 서버가 재시작됩니다.

## 3. 자주 쓰는 명령

```bash
make start    # 백그라운드 실행
make logs     # 로그 확인
make status   # 컨테이너 상태 확인
make restart  # 서버 재시작
make stop     # 서버 종료
make build    # _site/에 정적 사이트 생성
make engine-stop # Colima 종료
```

`Gemfile` 또는 `Gemfile.lock`이 변경되면 이미지를 다시 빌드합니다.

```bash
make setup
```

전체 명령 목록은 `make help`로 확인할 수 있습니다.
