# 이클립스 콘솔에 logback-spring.xml 설정 적용하기

이클립스의 Boot Dashboard에서 스프링 부트 어플리케이션을 실행하면, 콘솔에 표시되는 로그는 `logback-spring.xml` 설정이 적용되지 않는다. 이를 적용하려면 다음 내용을 추가하면 된다.

`application.yml` :

    logging:
      config: classpath:logback-spring.xml

`application.properties` :

    logging.config=classpath:logback-spring.xml