# Using YAML instead of Properties

`application.properties` 또는 `applicaton-[profile].properties` 대신에 `application.yml`을 사용해서 어플리케이션 속성을 지정할 수 있다. `SpringApplication`은 `SnakeYAML` 라이브러리가 클래스패스에 존재할 경우 YAML 속성 파일을 지원하며, `SnakeYAML`은 `spring-boot-starter`에 포함되어 있다.

## YAML 설정

```yml
environments:
    dev:
        url: http://dev.bar.com
        name: Developer Setup
    prod:
        url: http://foo.bar.com
        name: My Cool App
```

위 YAML은 아래와 같다.

```properties
environments.dev.url=http://dev.bar.com
environments.dev.name=Developer Setup
environments.prod.url=http://foo.bar.com
environments.prod.name=My Cool App
```

## 멀티 프로파일

```yml
server:
    address: 192.168.1.100
---
spring:
    profiles: development
server:
    address: 127.0.0.1
---
spring:
    profiles: production
server:
    address: 192.168.1.120
```

위와 같이 설정할 경우 `profile`에 따라 값을 변경할 수 있다.

## YAML 리스트

```yml
foo:
  list:
    - name: my name
      description: my description
    - name: another name
      description: another description
---
spring:
  profiles: dev
foo:
  list:
     - name: my another name
```

위와 같이 설정할 경우 `dev` 프로파일이 활성화 되면 foo의 list 는 `my another name`만을 자식으로 갖는다. 리스트는 병합되지 않고 교체된다.