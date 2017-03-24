# 스프링 부트 테스트

> [Testing](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-testing.html) 문서 참고

## Dependencies

`build.gradle`에 다음 내용을 추가한다 :

```gradle
dependencies {
  testCompile("org.springframework.boot:spring-boot-starter-test")
}
```

`spring-boot-starter-test`는 다음과 같은 라이브러리를 포함한다 :

- JUnit
- Spring Test
- AssertJ
- Hamcrest
- Mockito 1.x
- JSONAssert
- JsonPath

## Auto-configured tests

스프링 부트의 컴포넌트 스캔을 사용한 Auto-configuration 시스템은 어플리케이션 실행에서 잘 작동 하지만, 테스트 실행에는 과도하게 많은 설정을 하는 경우가 있다. 테스트 클래스에 어노테이션을 지정해서 불필요한 설정이 로드되지 않도록 제한할 수 있다. 자세한 사항은 [공식문서](https://docs.spring.io/spring-boot/docs/current/reference/html/test-auto-configuration.html)를 참고한다.

### @SpringBootTest

스프링 어플리케이션을 테스트할 때 사용하며 모든 설정을 로드한다.

### @JsonTest

JSON 변환 로직을 테스트할 때 사용한다. 다음과 같은 설정을 로드한다 :

- `@JsonComponent`
- Jackson `ObjectMapper`
- Jackson `Modules`

### @WebMvcTest(Controller.class)

컨트롤러 로직을 테스트할 때 사용한다. 다음과 같은 설정을 로드한다 :

- `@Controller`
- `@ControllerAcvice`
- `@JsonComponent`
- `Filter`
- `WebMvcConfigurer`
- `HandlerMethodArgumentResolver`
- `MockMvc`
- `WebClient`
- `WebDriver`

### @DataJpaTest

JPA 로직을 테스트할 때 사용한다. 다음과 같은 설정을 로드한다 :

- `@Entity`
- `TestEntityManager`
- in-memory embedded database
- Spring Data JPA repository

### @JdbcTest

JDBC 로직을 테스트할 때 사용한다. 다음과 같은 설정을 로드한다 :

- `JdbcTemplate`
- in-memory embedded database

### @DataMongoTest

MongoDB 로직을 테스트할 때 사용한다. 다음과 같은 설정을 로드한다 :

- `@Document`
- `MongoTemplate`
- in-memory embedded MongoDB

### @RestClientTest(Service.class)

클라이언트 로직을 테스트할 때 사용한다. 다음과 같은 설정을 로드한다 :

- Jackson, Gson support
- `RestTemplateBuilder`
- `MockRestServiceServer`

## DataSource 사용

테스트에서 `in-memory embeded database` 대신 `DataSource`에 정의된 데이터베이스를 사용하려면 다음과 같이 설정한다 :

```java
@RunWith(SpringRunner.class)
@DataJpaTest
@AutoConfigureTestDatabase(replace=Replace.NONE)
// @ActiveProfiles("profile-name")
public class ExampleRepositoryTests {

    // ...

}
```

자동으로 설정된 테스트용 데이터베이스가 아무것도(`None`) 대체하지 않도록 설정하는 것을 의미한다.
`@ActiveProfiles("profile-name")`을 사용해서 프로필을 지정할 수도 있다.

## Example

실제 테스트 코드를 작성하는 방법은 [스프링 부트 샘플 프로젝트](https://github.com/spring-projects/spring-boot/tree/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test)를 보면 좋다.

### Domain 테스트

- [POJO 테스트](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test/domain/VehicleIdentificationNumberTests.java)
- [@DataJpaTest : JPA Entity 테스트](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test/domain/UserEntityTests.java)
- [@DataJpaTest : JPA Repository 테스트](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test/domain/UserRepositoryTests.java)

### Service 테스트

- [@RestClientTest](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test/service/RemoteVehicleDetailsServiceTests.java)

### Controller 테스트

- [@WebMvcTest](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test/web/UserVehicleControllerTests.java)

### 기타

- [@SpringBootTest](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test/SampleTestApplicationWebIntegrationTests.java)
- [@JsonTest](https://github.com/spring-projects/spring-boot/blob/master/spring-boot-samples/spring-boot-sample-test/src/test/java/sample/test/service/VehicleDetailsJsonTests.java)