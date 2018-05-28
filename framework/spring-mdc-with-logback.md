# MDC with Logback

> Mapped Diagnostic Contexts

- 스레드 단위로 관리되는 맵을 사용할 수 있게 한다.
- 서버에서 여러 요청을 동시에 처리할 때 이를 구분할 수 있게 해준다.
- Neil Harrison이 Patterns for Logging Diagnostic Messages 책에서 소개함.

## 인터페이스

MDC 의 인터페이스는 다음과 같다.

```java
package org.slf4j;

public class MDC {
  //Put a context value as identified by key
  //into the current thread's context map.
  public static void put(String key, String val);

  //Get the context identified by the key parameter.
  public static String get(String key);

  //Remove the context identified by the key parameter.
  public static void remove(String key);

  //Clear all entries in the MDC.
  public static void clear();
}
```

## 기본 사용법

`MDC`의 static 메소드를 사용해서 맵에 값을 `Key`, `Value` 형식으로 저장한다.

```java
MDC.put("first", "Richard");
MDC.put("last", "Nixon");
logger.info("I am not a crook.");
logger.info("Attributed to the former US president. 17 Nov 1973.");
```

logback 설정의 pattern layout을 `#X{KEY}`로 지정하면 `KEY`로 저장된 값을 로그에 출력한다.

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
  <layout>
    <Pattern>%X{first} %X{last} - %m%n</Pattern>
  </layout>
</appender>
```

위 코드의 출력은 다음과 같다.

```txt
Richard Nixon - I am not a crook.
Richard Nixon - Attributed to the former US president. 17 Nov 1973.
```

## Spring 사용법

`org.springframework.web.servlet.HandlerInterceptor`를 구현한 클래스를 정의한다. 이 때 불필요한 메소드도 있으므로 스프링에서 제공하는 `org.springframework.web.servlet.handler.HandlerInterceptorAdapter`를 상속받아서 정의한다.

```java
public class LoggerInterceptor extends HandlerInterceptorAdapter {

    protected static final Logger LOGGER = LoggerFactory.getLogger(LoggerInterceptor.class);

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response,
            Object handler) throws Exception {
        String requestId = "#" + UUID.randomUUID().toString().substring(0, 7) + " -";
        MDC.put("RequestId", requestId);  // RequestId를 키로 사용
        return true;
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler,
            ModelAndView modelAndView) throws Exception {
        MDC.clear();
    }

}
```

`src/resource/logback-spring.xml`의 pettern layout에 `%X{RequestId}`를 추가한다.

```xml
<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
  <encoder>
    <pattern>%d{yyyy:MM:dd HH:mm:ss.SSS} %-5level [%15.15thread] %-30.30logger{29} : %X{RequestId} %msg %n</pattern>
  </encoder>
</appender>

<root level="INFO">
  <appender-ref ref="STDOUT" />
</root>
```

`LoggerInterceptor`를 빈으로 등록한다.

```java
@Configuration
public class ApplicationConfig {
    @Bean
    public WebMvcConfigurerAdapter webMvcConfigurerAdapter() {
        return new WebMvcConfigurerAdapter() {
            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                registry.addInterceptor(new LoggerInterceptor());
            }
        };
    }
}
```

위와 같이 설정할 경우 출력은 다음과 같다.

    2017:09:01 01:46:13.666 INFO  [nio-8080-exec-7] a.b.c.d.logger.mdcwithlogback  : #1efdf05 - Hello
    2017:09:01 01:46:13.666 INFO  [nio-8080-exec-7] a.b.c.d.logger.mdcwithlogback  : #1efdf05 - World!