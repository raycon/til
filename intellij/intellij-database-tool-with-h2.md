# IntelliJ Database Tool로 H2 접속하기

## 기본 사항

스프링 부트에서 H2 데이터베이스를 사용할 경우 `spring.datasource.url`의 기본 값은

## H2 Console 사용

- 스프링 부트 애플리케이션을 실행한다.
- `localhost:8080/h2-console` 에 접속한다.
- `src/main/resources/schema.sql`에서 정의한 테이블과 `src/main/resources/data.sql`에서 추가한 데이터를 확인할 수 있다.
- 브라우저와 IDE 화면 전환을 해야하기 때문에 번거롭다.

IntelliJ가 제공하는 Database 툴을 사용하면 IDE 화면 안에서 여러 종류의 데이터베이스에 접속해서 쿼리를 실행할 수 있다.

## In-Memory Database 설정

H2 데이터베이스를 사용할 경우 `spring.datasource.url`의 기본 값은 `jdbc:h2:mem:testdb`가 사용된다.

다음의 순서로 데이터베이스 툴을 설정할 수 있다.

- 스프링 부트 애플리케이션 실행
- Database 패널에서 `+ > Data Source from URL` 을 선택
- `jdbc:h2:mem:testdb` 입력
- Connection type: In-memory, Driver: H2 로 지정됨
- `Test Connection` 버튼으로 연결 확인
- **`testdb > TESTDB> PUBLIC` 만 보이고 `schema.sql`, `data.sql` 로 추가한 테이블과 데이터는 확인할 수 없다.**

## 문제 해결

문제의 원인은 다음과 같다.

- In-memory database는 두가지 커넥션으로 접근할 수 없다.
- 스프링 부트 앱을 실행하면 App용 커넥션이 생성된다.
- Database Tool 에서 접속할 경우 커넥션이 따로 생성된다.
- 같은 주소 `jdbc:h2:mem:testdb` 를 사용해도 다른 인스턴스에 접속된다.

이를 해결하기 위해서는 In-memory 방식이 아닌 File 방식으로 H2를 설정해야 한다. 다음과 같이 `application.properties`에 `spring.datasource.url`을 설정한다.

    spring.datasource.url=jdbc:h2:file:~/h2db;AUTO_SERVER=true

- `~/h2db`는 사용자 디렉토리의 `h2db` 파일을 의미한다. 파일의 경로는 절대 경로를 사용할 수도 있다.
- `AUTO_SERVER`의 값을 `TRUE`로 설정하면 여러 프로세스에서 동일한 데이터베이스에 접근할 수 있다.

## 작동 원리

`AUTO_SERVER`는 다음과 같이 동작한다.

- 첫번째 커넥션을 열게 되면 `embedded` 모드로 커넥션이 생성되고, 내부적으로 서버가 실행된다.
- IP 주소와 포트 번호는 `.lock.db` 파일에 저장된다.
- 두번째 커넥션을 열게 되면 `server` 모드로 커넥션이 생성된다.
- 첫번째 커넥션을 닫게 되면 서버가 멈추는데, 이 때 다른 열려있는 커넥션 중 하나가 서버를 시작한다.
- 첫번째 커넥션을 닫게 되면 다른 커넥션들의 트랜잭션이 롤백된다.
- `AUTO_SERVER_PORT=9090`으로 포트 번호를 지정할 수도 있다.

## File 기반 Database 설정

- 스프링 부트 애플리케이션 실행
- Database 패널에서 `+ > Data Source from URL` 을 선택
- `jdbc:h2:file:~/h2db;AUTO_SERVER=true` 입력
- Connection type: Embedded, Driver: H2 로 지정됨
- User에 `sa` 를 입력한다
- `Test Connection` 버튼으로 연결 확인
- `testdb > TESTDB> PUBLIC` 아래에 `schema.sql`로 추가한 테이블을 확인할 수 있다.
- 테이블을 선택하면 `data.sql`로 추가한 데이터도 확인할 수 있다.

## 참고

- <https://www.youtube.com/watch?v=8QBJMxyXIqc>
- [AUTO_SERVER](http://h2database.com/html/features.html?highlight=AUTO_SERVER&search=auto_server#auto_mixed_mode)
