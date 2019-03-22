# MyBatis-Spring-Boot-Autoconfigure

## 의존성

Maven:

```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>1.3.2</version>
</dependency>
```

Gradle:

```groovy
dependencies {
    compile("org.mybatis.spring.boot:mybatis-spring-boot-starter:1.3.2")
}
```

## 역할

- `DataSource`를 감지해서 사용한다.
- `SqlSessionFactoryBean`에 `DataSource`를 전달해서 `SqlSessionFactory`를 생성하고 빈으로 등록한다.
- `SqlSessionFactory`로 `SqlSessionTemplate`를 생성하고 빈으로 등록한다.
- 매퍼를 스캔해서 `SqlSessionTemplate`와 연결하고 스프링 컨텍스트에 등록해서 다른 빈에 주입될 수 있도록 한다.

## 스캔

MyBatis-Spring-Boot-Autoconfigure는 `@Mapper` 어노테이션이 붙은 매퍼를 자동으로 스캔한다.

```java
@Mapper
public interface CityMapper {
    @Select("SELECT * FROM CITY WHERE state = #{state}")
    City findByState(@Param("state") String state);
}
```

`@MapperScan` 어노테이션을 사용해서 여러 옵션을 설정할 수 있다. [MyBatis-Spring](http://www.mybatis.org/spring/mappers.html#scan)문서 참고.

## SqlSession

`SqlSessionTemplate`의 인스턴스가 스프링에 등록되기 때문에, 다른 빈에 주입해서 사용할 수 있다.

```java
@Component
public class CityDao {

	private final SqlSession sqlSession;

	public CityDao(SqlSession sqlSession) {
		this.sqlSession = sqlSession;
	}

	public City selectCityById(long id) {
		return this.sqlSession.selectOne("selectCityById", id);
    }

}
```

## Configuration

`mybatis.`를 프리픽스로 사용하는 프로퍼티를 설정해서 `application.properties`나 `application.yml`에서 마이바티스 설정을 변경할 수 있다.

- `mybatis.config-location`: 마이바티스 XML 설정 파일 위치
- `mybatis.check-config-location`: 마이바티스 XML 설정 파일이 존재하는지를 체크
- `mybatis.mapper-locations`: 매퍼 XML 파일 위치
- `type-aliases-package`: 타입 별칭을 지정할 패키지
- `type-handlers-package`: 타입 핸들러가 위치한 패키지
- `executor-type`: `SIMPLE`, `REUSE`, `BATCH` 중 하나
- `configuration-properties`: 외부에 분리된 프로퍼티 모음. 마이바티스 설정 파일이나 매퍼 파일에서 placeholder로 사용할 수 있다.
- `configuration`: 마이바티스 `Configuration` 빈을 설정한다. 가능한 프로퍼티는 [Settings](http://www.mybatis.org/mybatis-3/configuration.html#settings) 참고
  
설정 예제:

```yml
mybatis:
    type-aliases-package: com.example.domain.model
    type-handlers-package: com.example.typehandler
    configuration:
        map-underscore-to-camel-case: true
        default-fetch-size: 100
        default-statement-timeout: 30
...
```

## ConfigurationCustomizer

`ConfigurationCustomizer`를 구현한 빈을 등록해서 설정을 커스터마이즈 할 수 있다.

```java
// @Configuration class
@Bean
ConfigurationCustomizer mybatisConfigurationCustomizer() {
    return new ConfigurationCustomizer() {
        @Override
        public void customize(Configuration configuration) {
            // customize ...
        }
    };
}
```