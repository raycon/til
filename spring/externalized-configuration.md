# Externalized Configuration

> [Externalized Configuration](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html) 참고

`application-{profile}.properties` 파일이나 `application.yml` 파일을 외부에 설정하는 방법.

- Properties from `SPRING_APPLICATION_JSON` (inline JSON embedded in an environment variable or system property)
  - 환경변수에 저장하는 방법.
- Profile-specific application properties outside of your packaged jar (`application-{profile}.properties` and YAML variants)
  - jar 파일 외부에 `application-{profile}.properties`나 `application.yml` 파일을 두는 방법.
  - jar 파일을 실행하는 루트에 파일을 두면 된다.
  - `외부 O, 내부 O` : 외부 속성 사용
  - `외부 X, 내부 O` : 내부 속성 사용