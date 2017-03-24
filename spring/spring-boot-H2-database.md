# 스프링 부트에서 H2 데이터베이스 사용하기

스프링 부트는 [H2](http://www.h2database.com/), [HSQL](http://hsqldb.org/), [Derby](https://db.apache.org/derby/)와 같은 Embeded 데이터베이스를 지원한다. DB URL을 명시할 필요 없이 빌드 디펜던시에 명시하기만 하면 자동으로 설정되어서 사용하기에 편리하다.

이중에서 `H2`를 사용하는 방법을 정리해본다. 스프링 부트에서 데이터베이스를 사용하는 자세한 방법은 [Working with SQL databases](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-sql.html)를 참고한다.

## H2 Database Engine

H2는 다음과 같은 특성을 갖는 Java SQL 데이터베이스다.

- Very fast, open source, JDBC API
- Embedded and server modes; in-memory databases
- Browser based Console application
- Small footprint: around 1.5 MB jar file size

## DataSource 설정

스프링 부트에서 사용하는 `DataSource`는 `application.properties` 파일에 다음과 같이 설정 가능하다.

    spring.datasource.url=jdbc:mysql://localhost/test
    spring.datasource.username=dbuser
    spring.datasource.password=dbpass
    spring.datasource.driver-class-name=com.mysql.jdbc.Driver

> `driver-class-name` 값은 `url`을 통해서 추론해 낼 수 있기 때문에 생략할 수 있다.

## H2 사용

`build.gradle` 파일에 아래 내용을 추가한다 :

``` gradle
dependencies {
    ...
    compile("com.h2database:h2")
    ...
}
```

이 외의 설정은 필요 없다. 스프링 부트는 사용자가 정의한 `DataSource`가 없을 경우자동으로 `H2`를 내장 데이터베이스로 사용하도록 구성한다. 위에서 언급된 `spring.datasource...` 값을 정의하지 않으면 된다. 내장 데이터베이스는 개발, 테스트 단계에서만 사용하도록 권장된다.

## H2 Console 사용

`H2`는 데이터베이스에 접근할 수 있는 웹 인터페이스를 제공한다. 스프링 부트는 다음과 같은 조건이 충족되면 [H2 Console](http://www.h2database.com/html/quickstart.html#h2_console)을 자동으로 구성해준다.

- 웹 어플리케이션 프로젝트
- `com.h2database:h2`가 클래스패스에 존재할 경우
- [`Spring Boot's developer tools`](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-devtools.html)를 사용할 경우

`gradle.build` 파일에 아래 내용을 추가한다 :

```gradle
dependencies {
    ...
    compile("org.springframework.boot:spring-boot-starter-web")
    compile("org.springframework.boot:spring-boot-starter-data-jpa")
    compile("org.springframework.boot:spring-boot-devtools")
    compile("com.h2database:h2")
    ...
}
```

어플리케이션을 실행하고 <http://localhost:8080/h2-console>에 접속하면 콘솔을 확인할 수 있다. 로그인 아이디와 비밀번호를 따로 수정하지 않고 `Connect`버튼을 누르면 로그인된다. 어플리케이션이 실행되고 있는 동안 발생하는 DB 조작을 콘솔을 통해서 확인할 수 있으며, DB 내용은 어플리케이션이 시작될 때 마다 초기화된다.

### H2 Console 주소 변경

콘솔 주소는 `/h2-console`이 기본 값이며 `application.properties` 파일에서 변경할 수 있다 :

    spring.h2.console.path=/db-console

## 데이터베이스 초기화

어플리케이션이 시작되는 시점에 데이터베이스에 기초 데이터를 입력할 수 있다.

스프링에서 DB를 초기화하는 방법은 아래와 같은 두 가지 방법이 있다. 이 문서에서는 `spring.jpa.hibernate.ddl-auto`를 사용해서 정의하는 방법을 알아본다. 나머지 내용의 자세한 사항은 [Database initialization](https://docs.spring.io/spring-boot/docs/current/reference/html/howto-database-initialization.html) 문서를 참고한다.

- `spring.jpa.generate-ddl` (Boolean) 스프링 기능. 기본값 `false`
- `spring.jpa.hibernate.ddl-auto` (Enum) Hibernate 기능. 기본값 사용하는 DB에 따라 다름

`ddl-auto`는 다음과 같은 속성을 갖는다

- `none` : DB 초기화 관련 작업 수행하지 않음
- `create` : 시작할 때 스키마를 지우고 다시 생성한다. classpath에서 `import.sql` 파일이 존재할 경우 파일에 정의된 쿼리를 수행한다.
- `create-drop` : 시작은 `create`와 동일하지만, 종료될 때 스키마를 삭제한다.
- `update` : 도메인 객체와 DB 스키마를 비교해서 DB를 업데이트한다.
- `validate` : 도메인 객체가 DB 스키마와 일치하는지 검사한다.

스프링 부트는 `H2`와 같은 내장 데이터베이스를 사용할 경우 `ddl-auto`의 값으로 `create-drop`을 기본으로 사용한다. 내장 데이터베이스가 아닐경우 `none`이 기본 값으로 사용된다.

> 운영단계에서 `ddl-auto`값은 반드시 `none`이어야 한다. 아니면 어플리케이션이 재시작될 때 데이터가 모두 날아간다.

### import.sql

프로젝트의 `src/main/resource` 폴더에 `import.sql`을 생성해 놓으면 어플리케이션이 시작될 때 정의된 쿼리가 수행된다. 개발에 필요한 기초 데이터를 입력해 놓으면 편리하다. [spring-boot-sample-data-jpa](https://github.com/spring-projects/spring-boot/tree/master/spring-boot-samples/spring-boot-sample-data-jpa/src/main/resources) 프로젝트를 보면 참고할만한 `import.sql`이 정의되어 있다. 테이블을 생성하고, 데이터를 입력하는 동작을 확인할 수 있다.