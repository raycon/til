# DataSource auto-configuration in test

`application.properties` 에 다음과 같이 설정하면 파일 기반 H2 데이터베이스를 사용할 수 있다.

```properties
spring.datasource.url=jdbc:h2:file:~/h2db;AUTO_SERVER=true
```

하지만 JUnit 테스트에서 `@JdbcTest`를 사용해서 실행하면 정의된 embedded `DataSouce`로 교체된다.

    beddedDataSourceBeanFactoryPostProcessor : Replacing 'dataSource' DataSource bean with embedded version
    o.s.j.d.e.EmbeddedDatabaseFactory        : Starting embedded database: url='jdbc:h2:mem:4a54f46e-d49a-4519-b333-7ddd95198dd4;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=false', username='sa'

## DataSource

`@JdbcTest`는 다음과 같은 어노테이션 정의를 갖는다:

```java
...
@AutoConfigureCache
@AutoConfigureJdbc
@AutoConfigureTestDatabase  // Test용 데이터베이스 설정
@ImportAutoConfiguration
public @interface JdbcTest {
    ...
}
```

`spring-boot-test-autoconfigure` 라이브러리의 [`META-INF\spring.factories`](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-project/spring-boot-autoconfigure/src/main/resources/META-INF/spring.factories) 에 다음과 같이 정의되어 있다.

```
# AutoConfigureTestDatabase auto-configuration imports
org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase=\
org.springframework.boot.test.autoconfigure.jdbc.TestDatabaseAutoConfiguration,\
org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration
```

`AutoConfigureTestDatabase` 어노테이션에 의해 `TestDatabaseAutoConfiguration`에 정의된 `EmbeddedDataSourceBeanFactoryPostProcessor` Bean이 등록된다. `EmbeddedDataSourceBeanFactoryPostProcessor`는 기존에 등록된 `DataSouce`를 Bean 목록에서 삭제하고 Embedded DataSource를 생성해서 등록한다.

## 자동 설정 무시하기

- `spring.test.database.replace` 속성 값을 `none`으로 지정하거나
- `@AutoConfigureTestDatabase`의 `replace` 속성 값을 `NONE`으로 지정한다.

```java
@JdbcTest(properties = "spring.test.database.replace=none")
public class MyJdbcTest {
    ...
}

@JdbcTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
public class MyJdbcTest {
}
```

## 참고

- `@JdbcTest`뿐만 아니라 `@DataJdbcTest`, `@DataJpaTest`, `@JooqTest`도 동일하게 DataSource가 교체된다.
- `spring.factories`에 정의된 Factory에서 생성되는 Bean은 `@ComponentScan`으로 등록된 Bean을 대체한다.
- <https://stackoverflow.com/questions/44134297/h2-embedded-database-not-picking-up-properties-during-test-on-spring-boot>
- <https://docs.spring.io/spring-boot/docs/current/reference/html/appendix-test-auto-configuration.html#test-auto-configuration>
- <https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-developing-auto-configuration.html>
- <https://www.baeldung.com/spring-boot-data-sql-and-schema-sql>

## 더 알아보기

- `BeanDefinitionRegistryPostProcessor`
