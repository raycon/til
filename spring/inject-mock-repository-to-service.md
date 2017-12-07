# Inject mock repository to service

[Boot feature testing](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-testing.html) 참조

스프링 부트 실행 환경에서 서비스를 테스트를 할 경우 Repository 를 주입해야 한다.
`@TestConfiguration` 어노테이션으로 테스트 안에 클래스를 정의해서 빈을 생성하도록 한다.

```java
@RunWith(SpringRunner.class)
// @SpringBootTest
public class MyTest {

    @Autowired
    private MyService service;

    @Autowired
    private MyRepository repository;  // Mock Object

    @TestConfiguration
    static class Config {
        @Bean
        @Primary  // 빈 중복 정의 에러 해결
        public MyRepository repository() {
            return Mockito.mock(MyRepository.class);
        }
    }
}
```

파일을 분리해서 `@Import(MyTestsConfiguration.class)` 를 쓰는 방법도 있다.