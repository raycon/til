# MyBatis

> MyBatis [공식 문서](http://www.mybatis.org/mybatis-3/ko/getting-started.html) 요약

- [MyBatis](#mybatis)
  - [용어정리](#%EC%9A%A9%EC%96%B4%EC%A0%95%EB%A6%AC)
  - [시작하기](#%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
    - [SqlSessionFactory](#sqlsessionfactory)
    - [XML 설정](#xml-%EC%84%A4%EC%A0%95)
    - [JAVA 설정](#java-%EC%84%A4%EC%A0%95)
    - [SqlSession](#sqlsession)
    - [Mapping](#mapping)
    - [스코프와 생명주기](#%EC%8A%A4%EC%BD%94%ED%94%84%EC%99%80-%EC%83%9D%EB%AA%85%EC%A3%BC%EA%B8%B0)
  - [마이바티스 설정](#%EB%A7%88%EC%9D%B4%EB%B0%94%ED%8B%B0%EC%8A%A4-%EC%84%A4%EC%A0%95)
    - [properties](#properties)
    - [settings](#settings)
    - [typeAliases](#typealiases)
    - [typeHandlers](#typehandlers)
    - [objectFactory](#objectfactory)
    - [plugins](#plugins)
    - [environments](#environments)
    - [transactionManager](#transactionmanager)
    - [dataSource](#datasource)
    - [databaseIdProvider](#databaseidprovider)
    - [mappers](#mappers)
  - [매퍼 XML 파일](#%EB%A7%A4%ED%8D%BC-xml-%ED%8C%8C%EC%9D%BC)
    - [공통 어트리뷰트](#%EA%B3%B5%ED%86%B5-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%ED%8A%B8)
    - [select](#select)
    - [insert, update](#insert-update)
    - [sql](#sql)
    - [Parameters](#parameters)
    - [String substitution](#string-substitution)
    - [Result Maps](#result-maps)
    - [resultMap](#resultmap)
      - [id, result](#id-result)
      - [constructor](#constructor)
      - [association](#association)
      - [collection](#collection)
      - [discriminator](#discriminator)
    - [Auto-mapping](#auto-mapping)
    - [Cache](#cache)
      - [사용자 지정 캐시 사용](#%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%A7%80%EC%A0%95-%EC%BA%90%EC%8B%9C-%EC%82%AC%EC%9A%A9)
      - [cache-ref](#cache-ref)
  - [동적 SQL](#%EB%8F%99%EC%A0%81-sql)
    - [if](#if)
    - [choose, when, otherwise](#choose-when-otherwise)
    - [trim, where, set](#trim-where-set)
    - [foreach](#foreach)
  - [자바 API](#%EC%9E%90%EB%B0%94-api)
    - [SqlSession](#sqlsession-1)
    - [Mapper 사용하기](#mapper-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
  - [Logging](#logging)

## 용어정리

- 구문: SQL 쿼리
- 구문 ID: 매퍼 파일에 정의된 구문 ID
- 엘리먼트: XML element
- 어트리뷰트: XML attribute
- 프로퍼티: XML property element

## 시작하기

[mybatis-x.x.x.jar](https://github.com/mybatis/mybatis-3/releases) 파일을 클래스패스에 추가한다.

### SqlSessionFactory

`org.apache.ibatis.session` 패키지에 속한다.

- `SqlSession`을 생성하는데 쓰인다.
- `Configuration`을 `SqlSessionFactoryBuilder`에 전달해서 `SqlSessionFactory`를 생성한다.
- `Configuration`은 XML 을 파싱해서 생성하거나, 자바 코드로 생성할 수 있다.

```java
package org.apache.ibatis.session;
import java.sql.Connection;
public interface SqlSessionFactory {
    SqlSession openSession();
    SqlSession openSession(boolean var1);
    SqlSession openSession(Connection var1);
    SqlSession openSession(TransactionIsolationLevel var1);
    SqlSession openSession(ExecutorType var1);
    SqlSession openSession(ExecutorType var1, boolean var2);
    SqlSession openSession(ExecutorType var1, TransactionIsolationLevel var2);
    SqlSession openSession(ExecutorType var1, Connection var2);
    Configuration getConfiguration();
}
```

### XML 설정

XML 기반의 설정 파일을 사용할 수 있다.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
  <environments default="development">
    <environment id="development">
      <transactionManager type="JDBC"/>
      <dataSource type="POOLED">
        <property name="driver" value="${driver}"/>
        <property name="url" value="${url}"/>
        <property name="username" value="${username}"/>
        <property name="password" value="${password}"/>
      </dataSource>
    </environment>
  </environments>
  <mappers>
    <mapper resource="org/mybatis/example/BlogMapper.xml"/>
  </mappers>
</configuration>
```

### JAVA 설정

자바 코드로 `SqlSessionFactory`를 생성해서 사용한다.

의존성:

    Datasource         ─┬─▶ Environment ─┬─▶ Configuration ─▶ SqlSessionFactory
    TransactionFactory ─┘        Mapper ─┘

설정 예제:

```java
DataSource dataSource = BlogDataSourceFactory.getBlogDataSource();
TransactionFactory transactionFactory = new JdbcTransactionFactory();
Environment environment = new Environment("development", transactionFactory, dataSource);
Configuration configuration = new Configuration(environment);
configuration.addMapper(BlogMapper.class);
SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(configuration);
```

### SqlSession

- 데이터베이스에 대해 SQL명령어를 실행하기 위해 필요한 모든 메소드 가지고 있음
- 쿼리 실행, 매퍼 조회, 트랜잭션 관리를 하는데 사용

구문 ID로 쿼리 실행:

```java
SqlSession session = sqlSessionFactory.openSession();
try {
  Blog blog = session.selectOne("org.mybatis.example.BlogMapper.selectBlog", 101);
} finally {
  session.close();
}
```

SQL 구문의 파라미터와 리턴 값을 설명하는 인터페이스 (매퍼) 사용:

```java
SqlSession session = sqlSessionFactory.openSession();
try {
  BlogMapper mapper = session.getMapper(BlogMapper.class);
  Blog blog = mapper.selectBlog(101);
} finally {
  session.close();
}
```

### Mapping

- XML을 사용해서 정의한다.
- 한 개의 매퍼 XML 파일에는 여러개의 매핑 구문을 정의할 수 있다.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="org.mybatis.example.BlogMapper">
  <select id="selectBlog" resultType="Blog">
    select * from Blog where id = #{id}
  </select>
</mapper>
```

- 위의 매핑 파일은 `org.mybatis.example.BlogMapper.selectBlog` 매핑을 정의한다.
- `namespace` => 패키지 + 클래스
- `id` => 메소드

매핑 구문 id 사용:

```java
Blog blog = (Blog) session.selectOne("org.mybatis.example.BlogMapper.selectBlog", 101);
```

매핑 인터페이스 사용:

```java
BlogMapper mapper = session.getMapper(BlogMapper.class);
Blog blog = mapper.selectBlog(101);
```

매핑 인터페이스를 사용하는 경우, SQL 쿼리를 어노테이션으로 지정할 수도 있다.

```java
package org.mybatis.example;
public interface BlogMapper {
  @Select("SELECT * FROM blog WHERE id = #{id}")
  Blog selectBlog(int id);
}
```

### 스코프와 생명주기

- `SqlSessionFactoryBuilder`
  - 메소드 스코프
  - 메소드 안에서 지역변수로 사용
- `SqlSessionFactory`
  - 애플리케이션 스코프
  - 애플리케이션을 실행하는 동안 존재해야한다.
  - 싱글톤으로 사용하는 것이 좋음
- `SqlSession`
  - 요청 또는 메소드 스코프
  - HTTP 요청을 받을 때 마다 만들고, 응답을 리턴할 때 마다 닫을 수 있다.
  - `SqlSession`은 사용 후 항상 `close()`해야한다.
- 매퍼 인터페이스
  - 매퍼 인터페이스의 인스턴스는 `SqlSession`이 생성하기 때문에 스코프는 SqlSession과 동일하다.

`SqlSession.close()` 예제:

```java
SqlSession session = sqlSessionFactory.openSession();
try {
    BlogMapper mapper = session.getMapper(BlogMapper.class);
} finally {
    session.close();
}
```

## 마이바티스 설정

마이바티스 XML 설정파일은 다양한 엘리먼트와 프로퍼티를 갖는다.

### properties

프로퍼티를 정의해서 설정 내 다른 프로퍼티의 값으로 사용할 수 있다. 여러 파일에 나눠서 저장할 수 있고, 이 때 설정 파일의 처리 순서는 다음과 같다:

- `properties` 엘리먼트에 명시된 프로퍼티를 읽어들인다.
- `properties` 엘리먼트의 `resource`나 `url` 어트리뷰트를 사용해서 프로퍼티를 읽는다. 이미 값이 있을 경우 덮어쓴다.
- `SqlSessionFactoryBuilder`의 `build()`메소드 파라미터로 전달된 프로퍼티를 사용한다. 이미 값이 있을 경우 덮어쓴다.

```xml
<properties resource="org/mybatis/example/config.properties">
  <property name="username" value="dev_user"/>
  <property name="password" value="F2Fa3!33TYyg"/>
</properties>
```

- `username`과 `password` 프로퍼티를 정의하고, `config.properties`를 읽어들인다.

이 값은 placeholder 형식으로 사용할 수 있다. 예: `${username:default_user}`

### settings

여러 설정 값을 `settings` 엘리먼트에 지정해서 동작을 변경할 수 있다. [공식 문서](http://www.mybatis.org/mybatis-3/ko/configuration.html) 참고

설정 예제:

```xml
<settings>
  <setting name="cacheEnabled" value="true"/>
  <setting name="lazyLoadingEnabled" value="true"/>
</settings>
```

### typeAliases

자바 타입에 대한 짧은 이름을 지정한다. XML을 간결하게 유지하기 위해 사용한다.

`typeAlias` 사용:

```xml
<typeAliases>
  <typeAlias alias="Blog" type="domain.blog.Blog"/>
</typeAliases>
```

위와 같이 선언하고 `Blog`를 `domain.blog.Blog` 대신 사용할 수 있다.

`package` 사용:

```xml
<typeAliases>
  <package name="domain.blog"/>
</typeAliases>
```

위와 같이 선언하면, `domain.blog` 패키지 밑의 클래스를 검색하고, 첫 문자를 소문자로 전환한 이름으로 별칭을 등록한다. `@Alias("name")`를 사용하면 원하는 별칭을 지정할 수 있다.

자바 내장 타입은 기본으로 제공되는 별칭이 있다. (Integer -> integer, int -> _int 등)

### typeHandlers

- `PreparedStatement`에 파라미터 값을 설정할 때, 자바 타입을 JDBC 타입으로 변환한다.
  - `ps.setInt(i, year.getValue());`
- `ResultSet`에서 값을 가져올 때, JDBC 타입을 자바 타입으로 변환한다.
  - `int year = rs.getInt(columnName);`
- `BaseTypeHandler`를 상속받아서 구현한다.
- 마이바티스는 데이터베이스에 정의된 타입을 확인하지 않기 때문에 핸들러는 정확한 매핑을 지정해야한다.

타입 핸들러 등록:

```xml
<!-- mybatis-config.xml -->
<typeHandlers>
  <typeHandler handler="org.mybatis.example.ExampleTypeHandler"/>
</typeHandlers>
```

패키지로 등록:

```xml
<!-- mybatis-config.xml -->
<typeHandlers>
  <package name="org.mybatis.example"/>
</typeHandlers>
```

- 마이바티스는 핸들러에 정의된 제네릭 타입을 체크해서 핸들러가 다루는 자바 타입을 확인한다.
- 핸들러 클래스에 `@MappedTypes`, `@MappedJdbcTypes`를 어노테이션으로 타입을 지정할 수 있다.
- `typeHandler` 추가 어트리뷰트로 `javaType`, `jdbcType`을 지정해서 명시적으로 타입을 지정할 수 있다. 이 경우 어노테이션은 무시된다.

매퍼 정의에서 컬럼, 프로퍼티 변환을 할 때, `resultMap`에 사용할 타입 핸들러를 지정할 수 있다.

```xml
<mapper namespace="org.apache.ibatis.submitted.rounding.Mapper">
    <resultMap type="org.apache.ibatis.submitted.rounding.User" id="usermap2">
        <id column="id" property="id"/>
        <result column="roundingMode" property="roundingMode" typeHandler="org.apache.ibatis.type.EnumTypeHandler"/>
    </resultMap>

    <select id="getUser2" resultMap="usermap2">
        select * from users2
    </select>

    <insert id="insert2">
        insert into users2 (id, roundingMode) values (
            #{id}, #{roundingMode, typeHandler=org.apache.ibatis.type.EnumTypeHandler}
        )
    </insert>
</mapper>
```

### objectFactory

- 결과 객체의 인스턴스를 만드는 역할
- `DefaultObjectFactory`가 기본으로 사용되고, 이를 상속받아서 재정의할 수 있다.

```xml
<!-- mybatis-config.xml -->
<objectFactory type="org.mybatis.example.CustomObjectFactory">
  <property name="someProperty" value="100"/>
</objectFactory>
```

### plugins

특정 클래스의 메소드 호출을 가로채서 원하는 동작을 하게 지정할 수 있다. 마이바티스 동작에 큰 영향을 줄 수 있으므로 주의해서 사용해야 한다. [공식 문서](http://www.mybatis.org/mybatis-3/ko/configuration.html) 참고

- `Executor` (update, query, flushStatements, commit, rollback, getTransaction, close, isClosed)
- `ParameterHandler` (getParameterObject, setParameters)
- `ResultSetHandler` (handleResultSets, handleOutputParameters)
- `StatementHandler` (prepare, parameterize, batch, update, query)


### environments

- 환경에 따라 다른 설정 값을 적용할 수 있다.
- `SqlSessionFactory` 인스턴스는 하나의 `environment`를 지정해서 생성된다.
- 여러 데이터베이스에 접속하려면 여러 `SqlSessionFactory` 인스턴스가 필요하다.

```java
SqlSessionFactory factory = new SqlSessionFactoryBuilder().build(reader, environment);
SqlSessionFactory factory = new SqlSessionFactoryBuilder().build(reader, environment, properties);
// environment 파라미터가 없으면 디폴트 환경이 로드된다
SqlSessionFactory factory = new SqlSessionFactoryBuilder().build(reader);
SqlSessionFactory factory = new SqlSessionFactoryBuilder().build(reader, properties);
```

설정 예제:

```xml
<environments default="development">
  <environment id="development">
    <transactionManager type="JDBC">
      <property name="..." value="..."/>
    </transactionManager>
    <dataSource type="POOLED">
      <property name="driver" value="${driver}"/>
      <property name="url" value="${url}"/>
      <property name="username" value="${username}"/>
      <property name="password" value="${password}"/>
    </dataSource>
  </environment>
</environments>
```

위 설정에서 `default="development"` 기본 환경을 development로 지정한다.

### transactionManager

마이바티스는 `TransactionFactory`와 `Transacton` 인터페이스를 사용해서 트랜잭션을 처리한다.

```java
public interface TransactionFactory {
  void setProperties(Properties props);  
  Transaction newTransaction(Connection conn);
  Transaction newTransaction(DataSource dataSource, TransactionIsolationLevel level, boolean autoCommit);
}
```

```java
public interface Transaction {
  Connection getConnection() throws SQLException;
  void commit() throws SQLException;
  void rollback() throws SQLException;
  void close() throws SQLException;
  Integer getTimeout() throws SQLException;
}
```

마이바티스는 두가지 타입의 트랜잭션 매니저를 제공한다.

- `JDBC`: JDBC가 트랜잭션을 관리한다.
  - `JdbcTransactionFactory`에서 `TransactionFactory`를 구현함.
- `MANAGED`: 컨테이너가 트랜잭션의 모든 생명주기를 관리한다.
  - `ManagedTransactionFactory`에서 `TransactionFactory`를 구현함.
  - 커넥션을 닫는 것 까지 매뉴얼로 하려면 `closeConnection` 프로퍼티 값을 `false`로 지정한다.

    ```xml
    <transactionManager type="MANAGED">
    <property name="closeConnection" value="false"/>
    </transactionManager>
    ```

> 스프링에서 마이바티스를 사용하는 경우, 스프링 설정이 이전에 정의된 transactionManager 설정을 덮어쓰기 때문에 지정할 필요가 없다.

### dataSource

표준 JDBC `javax.sql.DataSource` 인터페이스를 사용하며 3가지 타입이 있다. 데이터소스는 `DataSourceFactory`를 통해 생성한다.

```java
public interface DataSourceFactory {
  void setProperties(Properties props);
  DataSource getDataSource();
}
```

UNPOOLED:

- `UnpooledDataSourceFactory`에서 `UnpooledDataSource`를 생성한다.
- 요청마다 커넥션을 열고 닫는다.

POOLED:

- `PooledDataSourceFactory`에서 `PooledDataSource`를 생성한다.
- 새로운 Connection 인스턴스를 생성하기 위해 매번 초기화하는 것을 방지한다.

> 자세한 프로퍼티 정리 필요

JNDI:

- `JndiDataSourceFactory`에서 `initial_context`나 `data_source` 값을 사용해서 데이터 소스를 검색한다.
- 컨테이너가 제공하는 DataSource를 사용한다.

### databaseIdProvider

`dataSource`로부터 데이터베이스의 이름을 가져오는 역할을 한다. 프로퍼티로 실제 이름과 새로운 이름을 정의해서 사용할 수 있다. 이렇게 정의된 이름을 구문(statement)의 `databaseId` 어트리뷰트의 값으로 지정해서 해당 구문이 실행될 데이터베이스를 지정할 수 있다.

```xml
<databaseIdProvider type="DB_VENDOR">
  <property name="SQL Server" value="sqlserver"/>
  <property name="DB2" value="db2"/>
  <property name="Oracle" value="oracle" />
</databaseIdProvider>
```

### mappers

매퍼 정의 파일이 어디에 위치하는지 지정한다.

클래스패스의 상대경로의 `resource` 사용:

```xml
<mappers>
  <mapper resource="org/mybatis/builder/AuthorMapper.xml"/>
  <mapper resource="org/mybatis/builder/BlogMapper.xml"/>
  <mapper resource="org/mybatis/builder/PostMapper.xml"/>
</mappers>
```

절대경로의 `url` 사용:

```xml
<mappers>
  <mapper url="file:///var/mappers/AuthorMapper.xml"/>
  <mapper url="file:///var/mappers/BlogMapper.xml"/>
  <mapper url="file:///var/mappers/PostMapper.xml"/>
</mappers>
```

매퍼 `class` 사용:

```xml
<mappers>
  <mapper class="org.mybatis.builder.AuthorMapper"/>
  <mapper class="org.mybatis.builder.BlogMapper"/>
  <mapper class="org.mybatis.builder.PostMapper"/>
</mappers>
```

`package` 안의 모든 매퍼 인터페이스를 등록:

```xml
<mappers>
  <package name="org.mybatis.builder"/>
</mappers>
```

## 매퍼 XML 파일

매퍼 XML 파일은 다음과 같은 element를 갖는다.

- `cache`: 해당 네임스페이스을 위한 캐시 설정
- `cache-ref`: 다른 네임스페이스의 캐시 설정에 대한 참조
- `resultMap`: 데이터베이스 결과 데이터를 객체에 로드하는 방법을 정의하는 엘리먼트
- ~~`parameterMap`: 비권장됨! 예전에 파라미터를 매핑하기 위해 사용되었으나 현재는 사용하지 않음~~
- `sql`: 다른 구문에서 재사용하기 위한 SQL 조각
- `insert`: 매핑된 INSERT 구문
- `update`: 매핑된 UPDATE 구문
- `delete`: 매핑된 DELEETE 구문
- `select`: 매핑된 SELECT 구문

### 공통 어트리뷰트

`select`, `insert`, `update`, `delete` 엘리먼트는 다음과 같은 공통 어트리뷰트를 갖는다:

- `id`: 구문 ID
- `parameterType`: 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭
- ~~`parameterMap`: deprecated~~
- `flushCache`: 구문이 호출될때마다 로컬, 2nd 레벨 캐시가  지워짐, 기본값: `false`
- `timeout`: 데이터베이스 응답 대기 최대 시간, 기본값 없음
- `statementType`: `STATEMENT`, `PREPARED`, `CALLABLE` 중 하나, 기본값: `PREPARED`
- `databaseId`: 구문의 대상이 되는 데이터베이스 ID (databaseIdProvider에 정의됨)

### select

데이터베이스에서 데이터를 가져온다.

`select` 엘리먼트는 다음과 같은 어트리뷰트를 갖는다:

- `useCache`: 구문의 결과가 2nd 레벨 캐시에 저장됨, 기본값: `true`
- `fetchSize`: 지정된 수만큼의 결과를 리턴, 기본값 없음
- `resultType`: 패키지 경로를 포함한 전체 클래스명이나 별칭
- `resultMap`: 외부 resultMap 의 참조명
- `resultOrdered`: 내포된 결과 조회, 기본값: `false`
- `resultSetType`: `FORWARD_ONLY`, `SCROLL_SENSITIVE`, `SCROLL_INSENSITIVE` 중 하나, 기본값 없음

다음 구문의 이름은 `selectPerson`이고 `int`타입의 파라미터를 가진다. 그리고 결과 데이터는 `HashMap` 에 저장된다.

```xml
<select id="selectPerson" parameterType="int" resultType="hashmap">
  SELECT * FROM PERSON WHERE ID = #{id}
</select>
```

### insert, update

`insert`, `update` 엘리먼트는 다음과 같은 어트리뷰트를 갖는다.

- `useGeneratedKeys`: 데이터베이스에서 내부적으로 생성한 키를 사용하도록 설정. 기본값: `false`
- `keyProperty`: 키를 셋팅할 프로퍼티를 지정. `,`로 구분한다. 기본값 없음
- `keyColumn`: 생성키를 가진 테이블의 컬럼명을 셋팅. 키 컬럼이 테이블의 첫번째 칼럼이 아닌 데이터베이스(PostgreSQL 처럼)에서만 필요. `,`로 구분한다. 기본값 없음

예제:

```xml
<insert
  id="insertAuthor"
  parameterType="domain.blog.Author"
  flushCache="true"
  statementType="PREPARED"
  keyProperty=""
  keyColumn=""
  useGeneratedKeys=""
  timeout="20">

<update
  id="updateAuthor"
  parameterType="domain.blog.Author"
  flushCache="true"
  statementType="PREPARED"
  timeout="20">
```

데이터베이스가 생성하는 키 사용:

```xml
<insert id="insertAuthor" useGeneratedKeys="true" keyProperty="id">
  insert into Author (username,password,email,bio)
  values (#{username},#{password},#{email},#{bio})
</insert>
```

데이터베이스가 다중 레코드 입력을 지원하는 경우:

```xml
<insert id="insertAuthor" useGeneratedKeys="true" keyProperty="id">
  insert into Author (username, password, email, bio) values
  <foreach item="item" collection="list" separator=",">
    (#{item.username}, #{item.password}, #{item.email}, #{item.bio})
  </foreach>
</insert>
```

데이터베이스가 자동생성키 컬럼을 지원하지 않는 경우, `selectKey` 사용:

```xml
<insert id="insertAuthor">
  <selectKey keyProperty="id" resultType="int" order="BEFORE">
    select CAST(RANDOM()*1000000 as INTEGER) a from SYSIBM.SYSDUMMY1
  </selectKey>
  insert into Author
    (id, username, password, email,bio, favourite_section)
  values
    (#{id}, #{username}, #{password}, #{email}, #{bio}, #{favouriteSection,jdbcType=VARCHAR})
</insert>
```

위 예제에서 `selectKey` 구문이 먼저 실행되고 결과 `id` 프로퍼티에 지정된다.

### sql

다른 구문에서 재사용 가능한 구문을 정의한다.

```xml
<sql id="sometable">
  ${prefix}Table
</sql>

<sql id="someinclude">
  from
    <include refid="${include_target}"/>
</sql>

<select id="select" resultType="map">
  select
    field1, field2, field3
  <include refid="someinclude">
    <property name="prefix" value="Some"/>
    <property name="include_target" value="sometable"/>
  </include>
</select>
```

위 구문은 다음과 같다:

    select
        field1, field2, field3
    from
        SomeTable

### Parameters

원시 타입:

```xml
<select id="selectUsers" resultType="User">
  select id, username, password
  from users
  where id = #{id}
</select>
```

파라미터 객체:

```xml
<insert id="insertUser" parameterType="User">
  insert into users (id, username, password)
  values (#{id}, #{username}, #{password})
</insert>
```

`User` 객체의 `id`, `username`, `password` 프로퍼티를 찾아서 `PreparedStatement`의 파라미터로 전달한다.

특정 컬럼에 `null` 이 전달되면 `jdbcType` 값이 필요하다.

    #{middleInitial, jdbcType=VARCHAR}

> 다양항 옵션은 공식문서 참고

### String substitution

`${name}` 문법으로 전달된 파라미터를 바로 사용할 수 있다. 이 경우 마이바티스는 문자열을 변경하거나 이스케이프 처리하지 않으므로 SQL 주입 공격에 노출될 수 있다. 사용자가 입력하는 값에는 이 방법을 사용하면 안된다.

    ORDER BY ${columnName}

### Result Maps

 `ResultSet`에서 데이터를 가져올때 작성되는 JDBC코드를 줄여준다.

다음 매핑은 `id`, `username`, `hashedPassword`를 키로 갖는 맵을 반환한다.

```xml
<select id="selectUsers" resultType="map">
  select id, username, hashedPassword
  from some_table
  where id = #{id}
</select>
```

컬럼명과 프로퍼티명이 같을 경우:

```xml
<select id="selectUsers" resultType="com.someapp.model.User">
  select id, username, hashedPassword
  from some_table
  where id = #{id}
</select>
```

컬럼명과 프로퍼티명이 같을 경우, `typeAlias` 사용:

```xml
<!-- XML설정파일에서 -->
<typeAlias type="com.someapp.model.User" alias="User"/>

<!-- SQL매핑 XML파일에서 -->
<select id="selectUsers" resultType="User">
  select id, username, hashedPassword
  from some_table
  where id = #{id}
</select>
```

컬럼명과 프로퍼티명이 다를 경우, 데이터베이스 별칭 사용:

```xml
<select id="selectUsers" resultType="User">
  select
    user_id             as "id",
    user_name           as "userName",
    hashed_password     as "hashedPassword"
  from some_table
  where id = #{id}
</select>
```

컬럼명과 프로퍼티명이 다를 경우, `resultMap` 사용:

```xml
<resultMap id="userResultMap" type="User">
  <id property="id" column="user_id" />
  <result property="username" column="username"/>
  <result property="password" column="password"/>
</resultMap>

<select id="selectUsers" resultMap="userResultMap">
  select user_id, user_name, hashed_password
  from some_table
  where id = #{id}
</select>
```

### resultMap

#### id, result

```xml
<id property="id" column="post_id"/>
<result property="subject" column="post_subject"/>
```

어트리뷰트:

- `property`: 필드나 프로퍼티
- `column`: 컬럼명이나 별칭
- `javaType`: 패키지 경로를 포함한 전체 클래명이나 타입 별칭, HashMap 으로 매핑할 경우 명시해야함
- `jdbcType`: `null` 입력이 가능한 컬럼에 지정하는 JDBC 타입. JDBC의 요구사항. 지원하는 타입은 [공식문서](http://www.mybatis.org/mybatis-3/ko/sqlmap-xml.html#Result_Maps) 참조
- `typeHandler`: 패키지를 포함한 전체 클래스명이나 타입 별칭

#### constructor

매핑된 타입의 생성자에 전달하는 값을 지정한다. `name`을 사용할 경우 정의된 순서는 상관이 없다. 자세한 어트리뷰트는 공식문서 참고.

```xml
<constructor>
   <idArg column="id" javaType="int" name="id" />
   <arg column="age" javaType="_int" name="age" />
   <arg column="username" javaType="String" name="username" />
</constructor>
```

#### association

`has-one` 타입의 관계를 다룬다. 마이바티스는 두가지 방법으로 내포된 데이터를 다룬다.

- Nested Select: 관계된 데이터를 가지고 오기 위해 추가로 구문을 실행한다.
- Nested Results: 조인된 결과물에서 관계된 데이터를 가져온다.

Nested Select:

```xml
<resultMap id="blogResult" type="Blog">
  <association property="author" column="author_id" javaType="Author" select="selectAuthor"/>
</resultMap>

<select id="selectBlog" resultMap="blogResult">
  SELECT * FROM BLOG WHERE ID = #{id}
</select>

<select id="selectAuthor" resultType="Author">
  SELECT * FROM AUTHOR WHERE ID = #{id}
</select>
```

위 예제에서 `author_id` 컬럼의 값이 `selectAuthor` 구문의 `id`로 전달되고, 이 구문의 실행 결과가 Blog의 `author` 프로퍼티에 매핑된다.

Nested Results:

```xml
<select id="selectBlog" resultMap="blogResult">
  select
    B.id            as blog_id,
    B.title         as blog_title,
    B.author_id     as blog_author_id,
    A.id            as author_id,
    A.username      as author_username,
    A.password      as author_password,
    A.email         as author_email,
    A.bio           as author_bio
  from Blog B left outer join Author A on B.author_id = A.id
  where B.id = #{id}
</select>

<resultMap id="blogResult" type="Blog">
  <id property="id" column="blog_id" />
  <result property="title" column="blog_title"/>
  <association property="author" column="blog_author_id" javaType="Author" resultMap="authorResult"/>
</resultMap>

<resultMap id="authorResult" type="Author">
  <id property="id" column="author_id"/>
  <result property="username" column="author_username"/>
  <result property="password" column="author_password"/>
  <result property="email" column="author_email"/>
  <result property="bio" column="author_bio"/>
</resultMap>
```

위 예제에서는 `authorResult`를 따로 정의해서 재사용 가능하게 했다. `association`의 `columnPrefix`와 함께 사용해서 재사용성을 더욱 높일 수 있다.

#### collection

`has-many` 타입의 관계를 다룬다.

Nested Select:

```xml
<resultMap id="blogResult" type="Blog">
  <!-- <collection property="posts" javaType="ArrayList" column="id" ofType="Post" select="selectPostsForBlog"/> -->
  <collection property="posts" column="id" ofType="Post" select="selectPostsForBlog"/>
</resultMap>

<select id="selectBlog" resultMap="blogResult">
  SELECT * FROM BLOG WHERE ID = #{id}
</select>

<select id="selectPostsForBlog" resultType="Post">
  SELECT * FROM POST WHERE BLOG_ID = #{id}
</select>
```

`javaType`은 지정하지 않아도 된다.

Nested Results:

```xml
<select id="selectBlog" resultMap="blogResult">
  select
  B.id as blog_id,
  B.title as blog_title,
  B.author_id as blog_author_id,
  P.id as post_id,
  P.subject as post_subject,
  P.body as post_body,
  from Blog B
  left outer join Post P on B.id = P.blog_id
  where B.id = #{id}
</select>

<resultMap id="blogResult" type="Blog">
  <id property="id" column="blog_id" />
  <result property="title" column="blog_title"/>
  <collection property="posts" ofType="Post">
    <id property="id" column="post_id"/>
    <result property="subject" column="post_subject"/>
    <result property="body" column="post_body"/>
  </collection>
</resultMap>
```

`association`과 동일한 어트리뷰트를 설정할 수 있으며, `ofType`이 추가로 적용된다.

#### discriminator

컬럼 값을 기준으로 `resultType`이나 `resultMap`을 변경할 수 있다.

```xml
<resultMap id="vehicleResult" type="Vehicle">
  <id property="id" column="id" />
  <result property="vin" column="vin"/>
  <result property="year" column="year"/>
  <result property="make" column="make"/>
  <result property="model" column="model"/>
  <result property="color" column="color"/>
  <discriminator javaType="int" column="vehicle_type">
    <case value="1" resultMap="carResult"/>
    <case value="2" resultMap="truckResult"/>
    <case value="3" resultMap="vanResult"/>
    <case value="4" resultMap="suvResult"/>
  </discriminator>
</resultMap>
```

`vehicle_type` 값이 1~4 사이의 값이라면 정의된 `reusltMap`을 사용한다. 이외의 값이라면 `vehicleResult`에 지정된 매핑을 사용한다.

```xml
<resultMap id="carResult" type="Car">
  <result property="doorCount" column="door_count" />
</resultMap>
```

`vehicle_type` 값이 1이면 `carResult` 매핑이 사용된다. 이때 `doorCount` 이외의 값은 매핑되지 않는다. 다른 `resultMap`에 정의된 매핑을 포함하려면 `extends` 어트리뷰트를 지정한다.

```xml
<resultMap id="carResult" type="Car" extends="vehicleResult">
  <result property="doorCount" column="door_count" />
</resultMap>
```

`vehicleResult`와 `carResult`의 모든 프로퍼티들이 로드된다.

### Auto-mapping

이바티스는 컬럼명을 가져와서 대소문자를 무시한 같은 이름의 프로퍼티를 찾는다. 

자동 매핑 예제:

```xml
<select id="selectUsers" resultMap="userResultMap">
  select
    user_id             as "id",
    user_name           as "userName",
    hashed_password
  from some_table
  where id = #{id}
</select>

<resultMap id="userResultMap" type="User">
  <result property="password" column="hashed_password"/>
</resultMap>
```

위 예제에서 `id`, `userName`은 `resultMap`에 정의하지 않아도 자동으로 `User`의 프로퍼티와 매핑이 된다.

`autoMappingBehavior` 설정으로 다음 3가지 값 중 하나를 설정할 수 있다.

- `NONE`: 자동 패밍을 사용하지 않는다.
- `PARTIAL`: 내포된 결과 매핑을 제외하고 자동 매핑한다. (기본값)
- `FULL`: 모든 것을 자동 매핑한다. 내포된 결과에 잘못된 값이 자동으로 매핑될 위험이 있다.

이외에 매핑별로 `autoMapping` 어트리뷰트를 지정해서 설정할 수 있다.

```xml
<resultMap id="userResultMap" type="User" autoMapping="false">
  <result property="password" column="hashed_password"/>
</resultMap>
```

참고: `colunm_name`을 `columnName`으로 매핑하기 위해서는 `mapUnderscoreToCamelCase`를 `true`로 설정해야 한다.

```xml
<!-- mybatis-config.xml -->
<configuration>
    <settings>
        <setting name="mapUnderscoreToCamelCase" value="true">
    </settings>
</configuration>
```

### Cache

기본적으로는 캐시가 작동하지 않는다. 캐시를 사용하려면 SQL 매핑 파일에 다음 한줄을 추가한다.

    <cache/>

위 설정은 다음과 같은 동작을 정의한다.

- 매핑 구문 파일내 select 구문의 모든 결과를 캐시한다.
- 매핑 구문 파일내 insert, update 그리고 delete 구문은 캐시를 지운다. (flush)
- LRU 알고리즘을 사용한다.
- 시간 순서대로 지워지지 않는다.
- 1024개의 참조를 저장한다.
- 읽기/쓰기 캐시로 작동한다.

어트리뷰트는 다음과 같다:

- `flushInterval`: 지정한 시간이 지난 캐시를 지운다. 단위는 밀리세컨드
- `eviction`: 캐시를 지울때 사용할 알고리즘을 지정한다. `LRU`, `FIFO`, `SOFT`, `WEAK` 선택 가능
- `size`: 캐시 사이즈를 지정한다.
- `readOnly`: `true`일 경우 읽고 쓰는 캐시는 캐시된 객체의 복사본을 리턴한다. `false`일 경우 모든 호출자에게 캐시된 객체의 같은 인스턴스를 리턴한다.

#### 사용자 지정 캐시 사용

`type`에 `org.mybatis.cache.Cache` 인터페이스의 구현체를 지정해서 다른 솔루션을 사용할 수 있다.

```xml
<cache type="com.domain.something.MyCustomCache">
  <property name="cacheFile" value="/tmp/my-custom-cache.tmp"/>
</cache>
```

위 예제는 구현체를 지정하고, `MyCustomCache.setCacheFile(String file)`을 호출해서 프로퍼티를 전달한다. `InitializingObject`를 구현해서 placeholder(`${cache.file}`)를 사용해 값을 지정할 수도 있다.

#### cache-ref

네임스페이스간의 캐시 설정과 인스턴스를 공유하고자 할 때 사용한다.

```xml
<cache-ref namespace="com.someone.application.data.SomeMapper"/>
```

## 동적 SQL

### if

테스트 결과가 참일 경우 구문을 포함시킨다.

```xml
<select id="findActiveBlogLike" 
     resultType="Blog">
  SELECT * FROM BLOG WHERE state = ‘ACTIVE`
  <if test="title != null">
    AND title like #{title}
  </if>
  <if test="author != null and author.name != null">
    AND author_name like #{author.name}
  </if>
</select>
```

### choose, when, otherwise

여러 조건 중 하나를 선택한다.

```xml
<select id="findActiveBlogLike" 
     resultType="Blog">
  SELECT * FROM BLOG WHERE state = ‘ACTIVE’
  <choose>
    <when test="title != null">
      AND title like #{title}
    </when>
    <when test="author != null and author.name != null">
      AND author_name like #{author.name}
    </when>
    <otherwise>
      AND featured = 1
    </otherwise>
  </choose>
</select>
```

### trim, where, set

if, choose 구문을 사용할 때 다음과 같이 생성된 쿼리가 문법에 맞지 않는 상황이 발생할 수 있다.

    SELECT * FROM BLOG
    WHERE
    AND title like ‘someTitle’

이를 방지하기 위해 `<where>`, `<set>` 엘리먼트나 `<trim>` 엘리먼트를 사용한다.

```xml
<select id="findActiveBlogLike"
     resultType="Blog">
  SELECT * FROM BLOG
  <where>
    <if test="state != null">
         state = #{state}
    </if>
    <if test="title != null">
        AND title like #{title}
    </if>
    <if test="author != null and author.name != null">
        AND author_name like #{author.name}
    </if>
  </where>
</select>
```

위 예제에서는 `where` 엘리먼트의 내용이 `AND`나 `OR`로 시작된다면 이를 제거한다.

```xml
<update id="updateAuthorIfNecessary">
  update Author
    <set>
      <if test="username != null">username=#{username},</if>
      <if test="password != null">password=#{password},</if>
      <if test="email != null">email=#{email},</if>
      <if test="bio != null">bio=#{bio}</if>
    </set>
  where id=#{id}
</update>
```

위 예제에서는 `set` 엘리먼트의 내용이 `,` 로 끝난다면 이를 제거한다.

각각 `trim`으로 변환하면 다음과 같다.

```xml
<trim prefix="WHERE" prefixOverrides="AND |OR ">
  ...
</trim>

<trim prefix="SET" suffixOverrides=",">
  ...
</trim>
```

### foreach

컬렉션에 대한 반복 처리를 한다.

```xml
<select id="selectPostIn" resultType="domain.blog.Post">
  SELECT *
  FROM POST P
  WHERE ID in
  <foreach item="item" index="index" collection="list"
      open="(" separator="," close=")">
        #{item}
  </foreach>
</select>
```

`item`: 리스트의 `index` 번째 항목이나 맵의 `index` 키 값으로 저장된 객체를 의미한다.

## 자바 API

`SqlSessionFactoryBuilder`에 설정 파일을 전달해서 `SqlSessionFactory` 인스턴스를 생성한다.

```java
String resource = "org/mybatis/builder/mybatis-config.xml";
InputStream inputStream = Resources.getResourceAsStream(resource);
SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
SqlSessionFactory factory = builder.build(inputStream);
```

`SqlSessionFactory`는 `openSession(...)` 메소드로 `SqlSession` 인스턴스를 생성한다.

```java
SqlSession openSession()
SqlSession openSession(boolean autoCommit)
SqlSession openSession(Connection connection)
SqlSession openSession(TransactionIsolationLevel level)
SqlSession openSession(ExecutorType execType,TransactionIsolationLevel level)
SqlSession openSession(ExecutorType execType)
SqlSession openSession(ExecutorType execType, boolean autoCommit)
SqlSession openSession(ExecutorType execType, Connection connection)
Configuration getConfiguration();
```

- `autoComit`: 자동 커밋 활성화 여부를 지정
- `Connection`: 자체 커넥션을 제공
- `TransactionIsolationLevel`: `java.sql.Connection`에 정의된 트랜젝션 레벨을 사용하는 `enum`
  - `NONE`, `READ_COMITTED`, `READ_UNCOMITTED`, `REPEATABLE_READ`, `SERIALIZABLE` 중 하나
- `ExecutorType`:
  - `SIMPLE`: 구문 실행마다 새로운 `PreparedStatement`를 생성한다.
  - `REUSE`: `PreparedStatement`를 재사용한다.
  - `BATCH`: 모든 update 구문을 배치처리하고, 중간에 select가 실행될 경우 필요하다면 경계를 표시(demarcate)한다.

### SqlSession

```java
package org.apache.ibatis.session;
public interface SqlSession extends Closeable {

    // 오직 하나의 메소드만 리턴한다.
    // 한개 이상을 리턴하거나 null이 리턴된다면 예외가 발생한다.
    <T> T selectOne(String statement);
    <T> T selectOne(String statement, Object parameter);
    <E> List<E> selectList(String statement);
    <E> List<E> selectList(String statement, Object parameter);
    // rowBounds는 offset과 limit으로 페이지를 구현한다.
    <E> List<E> selectList(String statement, Object parameter, RowBounds rowBounds);
    // 객체의 프로퍼티 중 하나를 키로 사용한다.
    <K, V> Map<K, V> selectMap(String statement, String mapKey);
    <K, V> Map<K, V> selectMap(String statement, Object parameter, String mapKey);
    <K, V> Map<K, V> selectMap(String statement, Object parameter, String mapKey, RowBounds rowBounds);
    // 커서는 리스트와 동일한 결과를 제공한다. 하지만 데이터 조회는 iterator를 사용할 때 수행된다.
    <T> Cursor<T> selectCursor(String statement);
    <T> Cursor<T> selectCursor(String statement, Object parameter);
    <T> Cursor<T> selectCursor(String statement, Object parameter, RowBounds rowBounds);
    // 쿼리 결과를 ResultHandler로 처리한다.
    void select(String statement, Object parameter, ResultHandler handler);
    void select(String statement, ResultHandler handler);
    void select(String statement, Object parameter, RowBounds rowBounds, ResultHandler handler);
    // 반환되는 값은 실행된 구문에 영향을 받은 레코드 수를 의미한다.
    int insert(String statement);
    int insert(String statement, Object parameter);
    int update(String statement);
    int update(String statement, Object parameter);
    int delete(String statement);
    int delete(String statement, Object parameter);
    // autoCommit이 false 이거나 외부 트랜잭션 관리자를 사용하지 않았을 경우
    // commit, rollback 메소드로 트랜잭션을 제어할 수 있다.
    // 기본적으로 마이바티스는 insert, update, delete를 호출해서 데이터가 변경된 경우만 커밋한다.
    void commit();
    void commit(boolean force);
    void rollback();
    void rollback(boolean force);
    // ExecutorType을 BATCH로 설정한 경우 flushStatements 메소드로 배치 업데이트를 언제든 실행할 수 있다.
    List<BatchResult> flushStatements();
    // 사용 후 반드시 닫아야 한다.
    @Override
    void close();
    // 세션 레벨의 캐시를 지운다
    void clearCache();
    Configuration getConfiguration();

    <T> T getMapper(Class<T> type);
    Connection getConnection();
}
```

마이바티스는 로컬 캐시와 2-Level 캐시를 사용한다.

로컬 캐시:

- 새로운 세션과 함께 생성된다.
- 수행된 쿼리의 결과가 캐시에 저장된다.
- 같은 구문을 같은 파라미터로 수행하면 데이터베이스를 조회하지 않고 캐시를 사용한다.
- 데이터 갱신이나 커밋, 롤백, 커넥션 close가 발생하는 경우 초기화된다.
- `localCacheScope`가 `SESSION`일 경우 마이바티스는 항상 같은 객체를 반환하므로, 이 객체를 수정하면 안된다.

`SqlSession`은 사용 후 반드시 닫아야 한다.

### Mapper 사용하기

`SqlSession`의 select, insert, update, delete를 사용하는 대신에 매퍼 클래스를 사용할 수 있다. 이 때 구문 ID를 전달하는 것 대신 메소드의 이름을 구문 ID와 동일하게 선언해야 한다.

매퍼 어노테이션을 사용하면 쿼리와 매핑을 자바 코드로 선언할 수 있다. 자세한 사항은 [Quick Guide to MyBatis](https://www.baeldung.com/mybatis) 참고

## Logging

마이바티스는 다음 순서로 로그 구현체 중 하나를 사용한다.

- SLF4J
- Apache Commons Logging
- Log4j 2
- Log4j
- JDK logging

패키지, 매퍼 클래스, 메소드명을 지정해서 레벨을 설정할 수 있다. (네임스페이스를 사용하는것과 동일하다.)

```properties
log4j.logger.org.mybatis.example.BlogMapper.selectBlog=TRACE
log4j.logger.org.mybatis.example.BlogMapper=TRACE
log4j.logger.org.mybatis.example=DEBUG
```