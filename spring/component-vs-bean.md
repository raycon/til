# @Component vs @Bean

- `org.springframework.context.annotation.Bean`
  - 메소드에 적용하는 어노테이션.
  - 클래스와 빈을 명시적으로 매핑할 때 사용한다.
  - 주로 외부 라이브러리의 객체를 빈으로 등록할 때 사용된다.
- `org.springframework.stereotype.Component`
  - 타입에 적용하는 어노테이션.
  - 스프링에 의해 자동으로 구성된다.
  - 클래스와 빈이 묵시적으로 1:1 매핑 된다.
  - `org.springframework.stereotype` 패키지에는 `Component`, `Controller`, `Repository`, `Service`가 있다.

인터페이스 코드 :

    @Target(ElementType.TYPE)
    @Retention(RetentionPolicy.RUNTIME)
    @Documented
    public @interface Component { ... }

    @Target({ElementType.METHOD, ElementType.ANNOTATION_TYPE})
    @Retention(RetentionPolicy.RUNTIME)
    @Documented
    public @interface Bean { ... }