# 스프링 부트에서 로그백 사용하기

## 로그백

[Logback](https://logback.qos.ch)은 [SLF4J API](https://www.slf4j.org)의 구현체로 `log4j`의 후속 프로젝트다. `logback-core`, `logback-classic`, `logback-access`의 세가지 모듈로 구성되어 있다.

- `logback-core` : `classic`과 `access`에서 사용되는 공통 라이브러리
- `logback-classic` : `log4j`의 개선된 버전으로 [SLF4J API](https://www.slf4j.org)를 구현한다.
- `logback-access` : 서블릿 컨테이너의 로그를 남길 때 사용한다.

## Logger, LoggerFactory

`Logger`와 `LoggerFactory`는 `SLF4J`에 있는 인터페이스와 그 구현체다. 로거는 다음과 같이 생성한다.

    Logger logger = LoggerFactory.getLogger("logger-name");

이름을 지정해주면 싱글톤 인스턴스를 반환한다. 이름 대신 클래스를 넘길 수 있다.

    Logger logger = LoggerFactory.getLogger(Application.class);

이 경우 이름은 `패키지명` + `클래스명`으로 지정된다.

## 로그 레벨

로그 레벨은 `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`로 5개가 있다. 각각의 레벨은 다음과 같은 포함관계를 갖는다.

    > TRACE
    TRACE DEBUG INFO WARN ERROR
    > DEBUG
          DEBUG INFO WARN ERROR
    > INFO
                INFO WARN ERROR
    > WARN
                     WARN ERROR
    > ERROR
                          ERROR

로거의 이름에 대해 레벨을 출력하는 레벨을 지정한다.

```xml
<logger name="com.example.logback" level="TRACE"/>
<logger name="com.example.logback.logger" level="INFO"/>
<root level="DEBUG">
    <appender-ref ref="STDOUT" />
</root>
```

`root`는 `<logger name="">`과 같은 의미를 갖는다. `com.example.logback` 이하 모든 로거는 `TRACE`레벨을, `com.example.logback.logger`이하는 `INFO`레벨을 지정했다.

## 로그 출력

로그 기록은 [Appender](https://logback.qos.ch/manual/appenders.html)가 담당한다.

### ConsoleAppender

```xml
<configuration>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <!-- encoders are assigned the type
         ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
    <encoder>
      <pattern>%-4relative [%thread] %-5level %logger{35} - %msg %n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

### FileAppender

`OutputStreamAppender`의 자식클래스로 파일에 로그를 기록한다.

```xml
<configuration>

  <appender name="FILE" class="ch.qos.logback.core.FileAppender">
    <file>testFile.log</file>
    <append>true</append>
    <!-- set immediateFlush to false for much higher logging throughput -->
    <immediateFlush>true</immediateFlush>
    <!-- encoders are assigned the type
         ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
    <encoder>
      <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="FILE" />
  </root>
</configuration>
```

### RollingFileAppender

특정 규칙에 따라 로그 파일을 새로 만든다. 이 때 `rollingPolicy`를 다음과 같이 지정할 수 있다.

- `TimeBasedRollingPolicy` : 시간에 따라 롤링한다.
- `SizeAndTimeBasedRollingPolicy` : 파일의 크기나 시간에 따라 롤링한다.
- `FixedWindowRollingPolicy` : 정해진 갯수만큼만 롤링한다.

```xml
<configuration>
  <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>logFile.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
      <!-- daily rollover -->
      <fileNamePattern>logFile.%d{yyyy-MM-dd}.log</fileNamePattern>

      <!-- keep 30 days' worth of history capped at 3GB total size -->
      <maxHistory>30</maxHistory>
      <totalSizeCap>3GB</totalSizeCap>

    </rollingPolicy>

    <encoder>
      <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="DEBUG">
    <appender-ref ref="FILE" />
  </root>
</configuration>
```

### Pattern

패턴과 관련된 내용은 [Layouts](https://logback.qos.ch/manual/layouts.html)를 참고

## 스프링 부트 로그백 의존성

스프링 부트는 로그 모듈에 대한 필수적인 의존성(Dependency)이 없다. `logback`을 사용하려면 클래스 패스에 `logback`과 `jcl-over-slf4j`(Common Logging API의 구현체)를 추가해야한다. 부트를 사용하면 `spring-boot-starter-logging`를 의존성에 추가하면 된다. `spring-boot-starter-web`을 사용하는 경우 자동으로 포함된다.

## 스프링 부트 로그백 로그 레벨 지정

`appliation.properties`에 다음과 같이 로그 레벨을 지정할 수 있다 :

    logging.level.org.springframework.web=DEBUG
    logging.level.org.hibernate=ERROR

`logging.file` 프로퍼티를 지정해서 로그가 저장되는 파일을 지정할 수 있다.

## 스프링 부트 로그백 커스텀 설정

`logback.xml`을 클래스패스 루트에 생성한다. 스프링 부트는 `base.xml`로 기본 설정을 제공한다. 로그 레벨만 변경하려면 다음과 같이 설정할 수 있다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/base.xml"/>
    <logger name="org.springframework.web" level="DEBUG"/>
</configuration>
```

## 스프링 부트 로그백 템플릿 사용

스프링 부트의 `LoggingSystem`은 로그백 설정에 사용할 수 있는 환경 변수를 제공한다.

- `${PID}` : 현재 프로세스 ID
- `${LOG_FILE}` : `logging.file` 값
- `${LOG_PATH}` : `logging.path` 값
- `${LOG_EXCEPTION_CONVERSION_WORD}` : `logging.exception-conversion-word` 값

`logback-spring.xml`을 클래스패스 루트에 생성한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/defaults.xml" />
    <property name="LOG_FILE" value="${LOG_FILE:-${LOG_PATH:-${LOG_TEMP:-${java.io.tmpdir:-/tmp}}/}spring.log}"/>
    <include resource="org/springframework/boot/logging/logback/file-appender.xml" />
    <root level="INFO">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

스프링 부트 설정에 `logging.file=myapplication.log`을 지정한다.

