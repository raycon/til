# Print JPA Queries

실행중인 쿼리를 확인하고 싶을 경우 application.yml 에 다음과 같이 설정한다.

    spring:
      jpa:
        properties:
          hibernate:
            show_sql: true
            format_sql: true
            use_sql_comments: true

    logging:
      level:
        org:
          hibernate:
            type:
              descriptor:
                sql: trace
