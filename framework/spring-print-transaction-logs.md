# Print transaction logs

`logback-spring.xml` 에 아래 내용을 추가한다.

    <logger name="org.hibernate.transaction.JDBCTransaction" level="DEBUG"/>
    <logger name="org.hibernate.jdbc.ConnectionManager" level="DEBUG"/>
    <logger name="org.springframework.orm.jpa.JpaTransactionManager" level="DEBUG"/>