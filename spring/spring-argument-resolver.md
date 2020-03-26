# HandlerMethodArgumentResolver

`HandlerMethodArgumentResolver` :

- 컨트롤러에서 파라미터를 바인딩 해주는 역할을한다.
- 리퀘스트의 파라미터를 다른 클래스의 인스턴스나 값으로 변환할 수 있다.
- 리퀘스트의 공통된 로직을 분리할 수 있다.

----

데이터 정의 :

- 맵을 상속받으면 안된다.

```java
public class RequestParam {

    String param;

    public RequestParam(String parameter) {
        this.param = parameter;
    }

    public String getParam() {
        return param;
    }

}
```

HandlerMethodArgumentResolver 구현 :

```java
public class RequestParamResolver implements HandlerMethodArgumentResolver {

    @Override
    public boolean supportsParameter(MethodParameter parameter) {
        return RequestParam.class.isAssignableFrom(parameter.getParameterType());
    }

    @Override
    public Object resolveArgument(MethodParameter parameter, ModelAndViewContainer mavContainer,
            NativeWebRequest webRequest, WebDataBinderFactory binderFactory) throws Exception {
        return new RequestParam(webRequest.getParameter("param"));
    }

}
```

ArgumentResolver 등록 :

```java
@Configuration
public class WebConfig extends WebMvcConfigurerAdapter {
    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> argumentResolvers) {
        argumentResolvers.add(new RequestParamResolver());
    }
}
```

컨트롤러에서 사용 :

```java
@RestController
public class RequestController {

    @GetMapping("test")
    public RequestParam testRequestParam(RequestParam param){
        return param;
    }
}
```
