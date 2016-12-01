# Spring Boot DevTools

클래스 바이트코드를 교체하는 HotSwap 방식으로 구현된 `spring-loaded` 를 사용하고 있었는데, 메소드 추가나 어노테이션 추가등을 제대로 인식하지 않는 문제가 있어서 다른 방법을 찾던 중 `spring-boot-devtools` 를 발견했다. `devtools`는 클래스파일의 변화를 감지하고 있다가 서버를 빠르게 재시작한다.

참고 :

* [DevTools in Spring Boot 1.3](https://spring.io/blog/2015/06/17/devtools-in-spring-boot-1-3)
* [Using Spring Boot Developer tools](http://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/html/using-boot-devtools.html)

build.gradle 에 아래 내용을 추가한다 :

```gradle
dependencies {
    compile("org.springframework.boot:spring-boot-devtools")
}
```

Eclipse(STS) 에서 gradle dependencies 를 업데이트하고, `Project > Build Automatically` 옵션을 켠다. 부트 앱을 실행한 뒤 java 파일을 수정하고 저장하면 앱이 재실행된다.