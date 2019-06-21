# Spring Boot and MySQL Load Data

`JdbcTemplate`을 사용해서 다음 명령 실행시

```sql
LOAD DATA LOCAL INFILE '[FILENAME]'
REPLACE INTO TABLE [TABLE]
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
```

다음과 같은 에러가 발생할 경우

    java.sql.SQLSyntaxErrorException: The used command is not allowed with this MySQL version

`datasource` 주소에 `allowLoadLocalInfile`을 `true`로 설정한다.

```yaml
spring:
  datasource:
    url: jdbc:mysql://127.0.0.1:3306?allowLoadLocalInfile=false
```

로드하는 데이터 중 `"Hello\"` 와 같은 값이 있을 경우, 이스케이프 문자를 제거해서 로드한다.

```sql
...
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY ''
LINES TERMINATED BY '\n'
...
```