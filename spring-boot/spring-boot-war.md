# Spring Boot War

스프링 부트 웹 프로젝트를 빌드해서 생성되는 jar 파일은 `java -jar` 명령어로 실행하면 Embeded Tomcat이 구동되면서 서버가 실행된다. Embeded Tomcat을 사용하지 않고 war 파일을 생성해서 배포하려면 다음과 같이 설정한다.

`war` 플러그인을 적용한다.

    apply plugin: 'war'

Embeded Tomcat을 `providedRuntime`으로 정의한다.

    dependencies {
        ...
        providedRuntime 'org.springframework.boot:spring-boot-starter-tomcat'
        ...
    }

`build` 명령어로 war 파일을 생성한다.

    gradle build

## 참고자료

- [Packaging executable wars deployable](https://docs.spring.io/spring-boot/docs/current/gradle-plugin/reference/html/#packaging-executable-wars-deployable)
