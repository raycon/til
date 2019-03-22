# MyBatis Spring

## Installation

다음 의존성을 추가한다.

```xml
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis-spring</artifactId>
  <version>x.x.x</version>
</dependency>
```

## Quick Setup

마이바티스를 스프링과 함께 사용하려면, `SqlSessionFactory`와 한개 이상의 매퍼 인터페이스가 필요하다.

`SqlSessionFactory`는 `SqlSessionFactoryBean` 사용해서 생성한다. `SqlSessionFactoryBean`은 스프링의 `FactoryBean`을 구현한다. 프로퍼티로 `dataSource`가 지정되어야 한다.

```xml
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
  <property name="dataSource" ref="dataSource" />
  <property name="mapperLocations" value="classpath*:sample/config/mappers/**/*.xml" />
</bean>
```

위의 `mapperLocations` 프로퍼티는 지정된 패키지 아래와 그 하위 패키지 모두 검색해서 매퍼 XML 파일을 모두 로드한다.

`configuration` 프로퍼티를 사용하면 별도의 XML 설정 없이 설정 값을 지정할 수 있다.

```xml
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
  <property name="dataSource" ref="dataSource" />
  <property name="configuration">
    <bean class="org.apache.ibatis.session.Configuration">
      <property name="mapUnderscoreToCamelCase" value="true"/>
    </bean>
  </property>
</bean>
```

매퍼 인터페이스는 `MapperFactoryBean`을 사용해서 생성한다.

```xml
<bean id="userMapper" class="org.mybatis.spring.mapper.MapperFactoryBean">
  <property name="mapperInterface" value="org.mybatis.spring.sample.mapper.UserMapper" />
  <property name="sqlSessionFactory" ref="sqlSessionFactory" />
</bean>
```

이렇게 생성된 매퍼 빈을 다른 객체에 주입해서 사용한다.

## 트랜잭션

스프링의 `DataSourceTransactionManager`를 사용해서 트랜잭션을 관리한다. 스프링의 트랜잭션을 가능하게 하려면 다음과 같이 설정한다:

```xml
<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
  <property name="dataSource" ref="dataSource" />
</bean>
```

`dataSource`는 `SqlSessionFactoryBean`에 전달된 것과 같은 것이어야 한다.

## SqlSessionTemplate

- `SqlSessionTemplate`은 `SqlSession`을 **구현**하고 코드에서 `SqlSession`을 대체한다.
- `SqlSession`과는 다르게 쓰레드에 안전하고, 여러개의 DAO나 매퍼에서 공유할 수 있다.
- 필요한 시점에 세션을 닫고, 커밋하거나 롤백하는 것을 포함한 세션의 생명주기를 관리한다.
- 마이바티스 예외를 스프링의 `DataAccessException`으로 변환한다.

생성:

```xml
<bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
  <constructor-arg index="0" ref="sqlSessionFactory" />
</bean>

<bean id="userDao" class="org.mybatis.spring.sample.dao.UserDaoImpl">
  <property name="sqlSession" ref="sqlSession" />
</bean>
```

사용:

```java
public class UserDaoImpl implements UserDao {
  private SqlSession sqlSession;
  public void setSqlSession(SqlSession sqlSession) {
    this.sqlSession = sqlSession;
  }
  public User getUser(String userId) {
    return (User) sqlSession.selectOne("org.mybatis.spring.sample.mapper.UserMapper.getUser", userId);
  }
}
```

## SqlSessionDaoSupport

`SqlSessionDaoSupport`를 상속받아서 `getSqlSession()` 메소드를 통해 `SqlSessionTemplate`를 얻을 수도 있다. 이때 `sqlSessionFactory`나 `sqlSessionTemplate` 프로퍼티를 설정해야 한다.

```java
public class UserDaoImpl extends SqlSessionDaoSupport implements UserDao {
  public User getUser(String userId) {
    return (User) getSqlSession().selectOne("org.mybatis.spring.sample.mapper.UserMapper.getUser", userId);
  }
}
```

```xml
<bean id="userMapper" class="org.mybatis.spring.sample.mapper.UserDaoImpl">
  <property name="sqlSessionFactory" ref="sqlSessionFactory" />
</bean>
```

## Mapper

매퍼를 사용하면 `SqlSession`을 직접 사용 할 필요가 없다. 마이바티스 스프링 연동 모듈이 알아서 처리하기 때문에 세션을 생성하거나 열고 닫을 필요가 없다.

### XML 매퍼 등록

`MapperFactoryBean`을 사용해서 매퍼를 등록한다.

```xml
<bean id="userMapper" class="org.mybatis.spring.mapper.MapperFactoryBean">
  <property name="mapperInterface" value="org.mybatis.spring.sample.mapper.UserMapper" />
  <property name="sqlSessionFactory" ref="sqlSessionFactory" />
</bean>
```

매퍼 인터페이스와 같은 경로의 클래스패스에 XML 매퍼 파일이 있으면 `MapperFactoryBean`이 자동으로 파싱을 한다. 다른 경로에 있다면 `SqlSessionFactoryBean`의 `configLocation` 프로퍼티를 설정해야 한다.

### 자동 스캔

자동스캔을 사용하는데는 3가지 방법이 있다.

#### <mybatis:scan/>

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:mybatis="http://mybatis.org/schema/mybatis-spring"
  xsi:schemaLocation="
  http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
  http://mybatis.org/schema/mybatis-spring http://mybatis.org/schema/mybatis-spring.xsd">

  <mybatis:scan base-package="org.mybatis.spring.sample.mapper" />

</beans>
```

- `base-package`는 세미콜론이나 콤마를 구분자로 사용해서 한개 이상의 패키지를 설정할 수 있다.
- 매퍼의 이름에서 첫글자를 소문자로 변환한 형태로 빈 이름을 사용할 것이다

#### @MapperScan

```java
@Configuration
@MapperScan("org.mybatis.spring.sample.mapper")
public class AppConfig {

  @Bean
  public DataSource dataSource() {
    return new EmbeddedDatabaseBuilder().addScript("schema.sql").build()
  }

  @Bean
  public SqlSessionFactory sqlSessionFactory() throws Exception {
    SqlSessionFactoryBean sessionFactory = new SqlSessionFactoryBean();
    sessionFactory.setDataSource(dataSource());
    return sessionFactory.getObject();
  }
}
```

#### MapperScannerConfigurer

```xml
<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
  <property name="basePackage" value="org.mybatis.spring.sample.mapper" />
</bean>
```

## 참고

- [MyBatis Spring Demo](https://github.com/mybatis/spring/tree/master/src/test/java/org/mybatis/spring/sample)