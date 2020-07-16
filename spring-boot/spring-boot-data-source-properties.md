# Datasource Properties

Datasource URL 을 작성할 때 `useTimeZone` 이나 `serverTimezone` 같은 옵션을 보통 아래와 같은 형식으로 작성한다.

```yml
spring:
  datasource:
    hikari:
      jdbc-url: jdbc:mysql://localhost:3306/til?&useTimeZone=true&serverTimezone=UTC
```

옵션이 많아지면 주소가 길어지고 가독성이 떨어지게 되는데, `data-source-properties`를 사용해서 이를 해결 할 수 있다.

```yml
spring:
  datasource:
    hikari:
      jdbc-url: jdbc:mysql://localhost:3306/til
      data-source-properties:
        useTimeZone: true
        serverTimezone: UTC
```

참고: Hikari is default connection pool and `.hikari` is no longer necessary.
