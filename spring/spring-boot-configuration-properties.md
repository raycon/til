# @ConfigurationProperties

> 참조 [Type-safe Configuration Properties](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html)

`application.properties` 혹은 `application.yml`에 있는 속성을 `@Value("${property}")` 로 매핑해서 사용할 수 있다. 하지만 프로퍼티의 수가 늘어나면 관리하기가 어렵고 코드가 지저분해진다. 이를 막기위해서 스프링 부트에서는 `@ConfigurationProperties`를 사용해서 프로퍼티를 클래스에 매핑해서 사용할 수 있다.

```java
package com.example;

import java.net.InetAddress;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.springframework.boot.context.properties.ConfigurationProperties;

@ConfigurationProperties("foo")
public class FooProperties {

    private boolean enabled;

    private InetAddress remoteAddress;

    private final Security security = new Security();

    public boolean isEnabled() { ... }

    public void setEnabled(boolean enabled) { ... }

    public InetAddress getRemoteAddress() { ... }

    public void setRemoteAddress(InetAddress remoteAddress) { ... }

    public Security getSecurity() { ... }

    public static class Security {

        private String username;

        private String password;

        private List<String> roles = new ArrayList<>(Collections.singleton("USER"));

        public String getUsername() { ... }

        public void setUsername(String username) { ... }

        public String getPassword() { ... }

        public void setPassword(String password) { ... }

        public List<String> getRoles() { ... }

        public void setRoles(List<String> roles) { ... }

    }
}
```

프로퍼티를 로드할 클래스(`FooProperties`)를 생성하고, `@ConfigurationProperties(prefix="foo")` 어노테이션으로 사용할 프로퍼티의 prefix 를 지정한다. 위 클래스는 다음과 같은 프로퍼티가 주입된다.

- `foo.enabled`
- `foo.remote-address`
- `foo.security.name`
- `foo.security.password`
- `foo.security.roles`

이 프로퍼티 클래스를 사용하기 위해서는 다음과 같이 `@Configuration` 빈에 `@EnableConfigurationProperties` 어노테이션을 사용해서 프로퍼티 클래스를 지정해주어야 한다.

```java
@Configuration
@EnableConfigurationProperties(FooProperties.class)
public class MyConfiguration {
}
```

`@ConfigurationProperties`를 `@Component`와 같이 사용하면 `@EnableConfigurationProperties`는 생략 가능하다.

```java
@Component
@ConfigurationProperties(prefix="foo")
public class FooProperties {

    // ... see above

}
```

이렇게 정의된 프로퍼티는 다음과 같이 사용한다.

```java
@Service
public class MyService {

    private final FooProperties properties;

    @Autowired
    public MyService(FooProperties properties) {
        this.properties = properties;
    }

     //...

    @PostConstruct
    public void openConnection() {
        Server server = new Server(this.properties.getRemoteAddress());
        // ...
    }

}
```

## 프로퍼티 검증

`@Validated` 어노테이션을 사용해서 프로퍼티가 로드될 때 적절한 값이 입력되는지 검증할 수 있다. 검증에 실패할 경우 스프링 부트 어플리케이션이 실행되지 않는다.

```java
@ConfigurationProperties(prefix="connection")
@Validated
public class FooProperties {

    @NotNull
    private InetAddress remoteAddress;

    @Valid
    private final Security security = new Security();

    // ... getters and setters

    public static class Security {

        @NotEmpty
        public String username;

        // ... getters and setters

    }

}
```