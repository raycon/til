# MultipleBagFetchException

스프링 부트를 1.3에서 1.4로 업데이트 했다. [Release Note](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-1.4-Release-Notes#hibernate-5) 를 보면 Hibernate도 4.3에서 5.0으로 업그레이드 되었다.

소스 수정 없이 실행하면 다음과 같은 에러가 발생한다.

    Caused by: org.hibernate.loader.MultipleBagFetchException: cannot simultaneously fetch multiple bags : ...

이 에러를 [Stack overflow](http://stackoverflow.com/questions/4334970/hibernate-cannot-simultaneously-fetch-multiple-bags)에 검색해보면 이런 내용이 나온다.

```java
@OneToMany(mappedBy="parent", fetch=FetchType.EAGER)
private List<Child> childs;
```

위와 같은 코드에서 문제가 발생하는데. 해결법은 다음과 같다.

    Simply change from 'List' type to 'Set' type.
