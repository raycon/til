# 테스트에서 프로퍼티 사용하는법

## 요약

테스트에서 프로퍼티를 재정의해서 사용하고 싶은 경우 다음 방법 중 한가지를 사용할 수 있다.

- 전체 프로퍼티 교체
  - `src/test/resources/application.yml` 에 모든 프로퍼티를 재정의
- 일부 프로퍼티 재정의
  - `@TestPropertySource` 사용
  - `@SpringBootTest`의 `properties` 속성 사용
  - `@ActiveProfiles` 사용

## 전체 프로퍼티 교체

- `src/test/resources/application.yml` 파일을 생성해서 프로퍼티를 정의할 수 있다.
- 테스트에서 사용되는 모든 프로퍼티를 포함해야 한다.

## 일부 프로퍼티 재정의

### 준비

아래의 리소스들를 사용한다.

```yml
# src/main/resources/application.yml
foo: main-foo (default)
bar: main-bar (default)
---
spring:
  profiles: dev
bar: main-bar (dev)
---
spring:
  profiles: test
bar: main-bar (test)
```

```yml
# src/test/resources/application-test.yml
bar: test-bar (test)
```

```properties
# src/test/resources/test.properties
foo=custom-property-source-foo
bar=custom-property-source-bar
```

### @SpringBootTest

- `properties`를 사용해서 프로퍼티를 재정의 할 수 있다.
- `@SpringBootTest` 이외에도 부트가 제공하는 `Test` 로 끝나는 어노테이션은 `properties` 를 지정할 수 있다. (`@WebMvcTest`, `@JsonTest` ...)

```java
@SpringBootTest(properties = {"bar=annotation-bar"})
public class SpringBootTestPropertiesTest {

  @Value("${foo}")
  private String foo;

  @Value("${bar}")
  private String bar;

  @Test
  void test() {
    // foo from src/main/resources/application.yml
    assertThat(foo).isEqualTo("main-foo (default)");
    // bar from annotation
    assertThat(bar).isEqualTo("annotation-bar");
  }

}
```

### @TestPropertySource

- `locations`를 사용해서 설정 파일의 경로를 지정할 수 있다.
- `properties`를 사용해서 프로퍼티를 재정의 할 수 있다.
- `yml` 파일은 공식적으로 지원하지 않는다. (테스트 해보니까 `yml`도 되는데 더 확인이 필요함)

```java
@SpringBootTest
@TestPropertySource(locations = "classpath:test.properties", properties = {"bar=annotation-bar"})
public class PropertySourceLocationsPropertiesTest {

  @Value("${foo}")
  private String foo;

  @Value("${bar}")
  private String bar;

  @Test
  void test() {
    // foo from src/test/resources/test.properties
    assertThat(foo).isEqualTo("custom-property-source-foo");
    // bar from annotation
    assertThat(bar).isEqualTo("annotation-bar");
  }

}
```

### @ActiveProfiles

`@ActiveProfiles` 어노테이션으로 활성화 할 프로파일을 지정할 수 있다.

```java
@SpringBootTest
@ActiveProfiles("dev")
public class DevProfileTest {

  @Value("${foo}")
  private String foo;

  @Value("${bar}")
  private String bar;

  @Test
  void fooTest() {
    // foo from src/main/resources/application.yml
    assertThat(foo).isEqualTo("main-foo (default)");
    // bar from src/main/resources/application.yml
    assertThat(bar).isEqualTo("main-bar (dev)");
  }

}
```

`src/test/resources` 경로에 `application-test.yml` 파일을 따로 생성할 수 있다. `test` 프로파일은 `src/main/resources/application.yml`과 `src/test/resources/application-test.yml`에 중복되서 정의되어 있는데, 이중에서 `application-test.yml`에 정의된 값이 사용된다.

```java
@SpringBootTest
@ActiveProfiles("test")
public class TestProfileTest {

  @Value("${foo}")
  private String foo;

  @Value("${bar}")
  private String bar;

  @Test
  void fooTest() {
    // foo from src/main/resources/application.yml
    assertThat(foo).isEqualTo("main-foo (default)");
    // bar from src/test/resources/application-test.yml
    assertThat(bar).isEqualTo("test-bar (test)");
  }

}
```

## 참고

- https://www.baeldung.com/spring-tests-override-properties
- https://www.baeldung.com/spring-test-property-source
- https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-external-config
- https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-testing-spring-boot-applications-detecting-config
- https://github.com/spring-projects/spring-framework/issues/18486
