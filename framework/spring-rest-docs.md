# Spring RestDocs

> <https://docs.spring.io/spring-restdocs/docs/current/reference/html5>
> <https://spring.io/guides/gs/testing-restdocs/>

## Swagger vs Rest Docs

- Swagger
  - 코드에 어노테이션을 추가하는 방식
  - API 동작을 테스트하는 용도에 특화되어 있다.
  - 문서와 코드가 동기화 되지 않을 수 있다.
- Rest Docs
  - 테스트로 문서를 생성하는 방식
  - 테스트가 성공해야 문서가 작성된다.
  - 문서 제공용으로 사용하기 적합하다.

## 코드

> 코드 첨부 필요

## 테스트

테스트를 수행하면 `build/generated-snippets` 경로에 다음 파일이 생성된다.

    curl-request.adoc   // curl 요청
    http-request.adoc   // 테스트 수행시 컨트롤러에 전달된 Request. 예제로 사용.
    http-response.adoc  // 테스트 수행시 전달받은 http . 예제로 사용.
    httpie-request.adoc
    request-body.adoc   // 요청의 본문
    response-body.adoc  // 응답의 본문

> To make the path parameters available for documentation, the request must be built using one of the methods on RestDocumentationRequestBuilders rather than MockMvcRequestBuilders.

## 조합

- `generated-snippets`에 생성된 adoc 파일들을 include 해서 전체 문서를 만든다.
- Gradle의 경우 `src/docs/asciidoc/*.adoc` 파일이 `build/asciidoc/html5/*.html`로 변환된다.

`src/docs/asciidoc/API.adoc` 파일을 다음과 같이 생성한다.

```adoc
= Car API
:author: Raegon Kim
:email: raegon@gmail.com
:source-highlighter: highlightjs
:toc: left
:toclevels: 4
:sectnums:
:sectlinks:
:operation-http-request-title: Request structure
:operation-http-response-title: Example response

== Car

=== Create Car

operation::create-car[snippets='http-request,request-fields,response-fields,http-response']

=== Get Car

operation::get-car[snippets='http-request,path-parameters,response-fields,http-response']

=== Update Car

operation::update-car[snippets='http-request,path-parameters,request-fields,response-fields,http-response']

=== Delete Car

operation::delete-car[snippets='http-request,path-parameters,http-response']
```

다음 명령어를 실행한다

    gradlew asciidoctor

`build/asciidoc/html5/API.html` 파일이 생성된다.

## 코드 재사용

리턴되는 모델을 미리 정의해서 재사용할 수 있다.

```java
protected final LinksSnippet pagingLinks = links(
        linkWithRel("first").optional().description("The first page of results"),
        linkWithRel("last").optional().description("The last page of results"),
        linkWithRel("next").optional().description("The next page of results"),
        linkWithRel("prev").optional().description("The previous page of results"));

...

this.mockMvc.perform(get("/").accept(MediaType.APPLICATION_JSON))
    .andExpect(status().isOk())
    .andDo(document("example", this.pagingLinks.and(
            linkWithRel("alpha").description("Link to the alpha resource"),
            linkWithRel("bravo").description("Link to the bravo resource"))));
```

## 속성 추가

`attributes` 메소드로 다음과 같이 `custom` 속성을 추가할 수 있다

```java 
fieldWithPath("company").attributes(key("custom").value("커스텀값")).type(JsonFieldType.STRING).description("제조사").optional()
```

## ConstrainedFields

도메인 객체의 필드에 대한 제한 사항을 문서에 포함할 수 있다.

`ConstraintDescriptions`을 사용해서 타입의 필드에 대한 설명을 가져온 뒤 `constraints` 속성을 추가한다.

```java
ConstraintDescriptions constraintDescriptions = new ConstraintDescriptions(input);

fieldWithPath(path).attributes(key("constraints")
    .value(StringUtils.collectionToDelimitedString(
            constraintDescriptions.descriptionsForProperty(path),
            System.lineSeparator())
    ));
```

## Snippet 커스터마이징

- `test/resources/org/springframework/restdocs/template` 경로에 커스터마이징 하고 싶은 snippet 파일을 추가한다.
- `request-fields.snippet` 파일을 다음과 같이 정의해서 사용한다. [참고](https://docs.spring.io/spring-restdocs/docs/current/reference/html5/#documenting-your-api-customizing)

```mustache
{{#title}}.{{.}}{{/title}}
|===
|Path|Type|Optional|Custom|Description|Constraints

{{#fields}}
|{{#tableCellContent}}{{path}}{{/tableCellContent}}
|{{#tableCellContent}}{{type}}{{/tableCellContent}}
|{{#tableCellContent}}{{^optional}}true{{/optional}}{{/tableCellContent}}
|{{#tableCellContent}}{{#custom}}{{.}}{{/custom}}{{/tableCellContent}}
|{{#tableCellContent}}{{description}}{{/tableCellContent}}
|{{#tableCellContent}}{{constraints}}{{/tableCellContent}}

{{/fields}}
|===
```

- snippet 자체에 속성을 추가할 수 있다.

    ```java
    requestFields(
        attributes(key("title").value("Field for user creation")),
    ```

- 테이블이 깨지는 것을 막기 위해서 ``{{#tableCellContent}}`를 적용했다. [참고](https://docs.spring.io/spring-restdocs/docs/current/reference/html5/#working-with-asciidoctor-customizing-tables-formatting-problems)
- `{{custom}}` 으로 출력시 `custom` 속성이 없는 필드는 에러가 발생한다.
  - No method or field with name 'custom'
- `#`으로 존재 여부를 검사하고 `{{.}}`으로 값을 출력한다. [참고](https://stackoverflow.com/questions/25320065/what-is-in-mustache)
- 속성을 추가할 때 헤더도 같이 추가해야 테이블이 깨지지 않는다.

### 메시지 커스터마이징

- `test/resources/org/springframework/restdocs/constraints/ConstraintDescriptions.properties` 파일을 생성한다.
- `패키지명.클래스명.description=메시지`로 정의한다.

```properties
javax.validation.constraints.NotNull.description=값이 존재해야 합니다
```

한글이 깨져서 출력될 경우 `properties` 파일이 UTF-8로 저장되어 있는지 확인한다.

IntelliJ 의 경우 `Settings > Editor > File Encodings` 에서 다음과 같이 설정

- Global Encoding : `UTF-8`
- Project Encoding : `UTF-8`
- Default encoding for properties files: `UTF-8`
- Transparent native-to-ascii conversion 체크

## 테이블 폭 변경

snippet 에서 변경:

```adoc
[cols="1,1,1,2,2"]
|Path|Type|Optional|Custom|Description|Constraints
...
```

adoc 에서 변경:

```adoc
[cols="1,1,1,2,2"]
include::{snippets}/update-car/request-fields.adoc[]
```

## @AutoConfigureRestDocs

- 스프링 부트에서 제공하는 자동 설정
- `MockMvc`빈이 Spring REST Docs를 사용하도록 초기화한다.
- `@Autowired`로 주입받아서 사용할 수 있다.

### RestDocsMockMvcConfigurationCustomizer

> Spring Boot에서 제공하는 기능 [참고](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-testing.html#boot-features-testing-spring-boot-applications-testing-autoconfigured-rest-docs)
> 
추가적인 속성을 설정하고 싶을 때 `RestDocsMockMvcConfigurationCustomizer` 인터페이스를 상속받는 `@TestConfiguration`을 생성한다.

```java
@TestConfiguration
static class CustomizationConfiguration implements RestDocsMockMvcConfigurationCustomizer {
    @Override
    public void customize(MockMvcRestDocumentationConfigurer configurer) {
        configurer.uris()
                .withScheme("https")
                .withHost("www.example.com")
                .withPort(8080);
    }

    @Bean
    public RestDocumentationResultHandler restDocumentationResultHandler() {
        return MockMvcRestDocumentation.document("{method-name}", // output 경로를 파라미터로 설정
                preprocessRequest(prettyPrint()),   // Request body를 보기 좋게 만든다
                preprocessResponse(prettyPrint())); // Response body를 보기 좋게 만든다
    }
}
```

`{method-name}` 관련 내용은 공식문서 [참고](https://docs.spring.io/spring-restdocs/docs/current/reference/html5/#documentating-your-api-parameterized-output-directories)

다른 파일로 생성하고 테스트에 다음과 같이 포함할 수도 있다.

```java
@Import(CustomizationConfiguration.class)
public class CarControllerAutoConfigureAdvanceTest {
```

## Encoding

요청 응답의 샘플 데이터의 한글 인코딩이 깨질 경우, `contentType`을 `MediaType.APPLICATION_JSON_UTF8`로 설정한다.

> `MediaType.APPLICATION_JSON`의 경우 깨짐

```java
        ResultActions result = mockMvc.perform(
                put(request.getUri(), request.getVariables())
                        .content(mapper.writeValueAsString(getSample()))
                        .contentType(MediaType.APPLICATION_JSON_UTF8);
```

## 참고

- <https://docs.spring.io/spring-restdocs/docs/current/reference/html5/#documenting-your-api-request-parameters>
- <http://woowabros.github.io/experience/2018/12/28/spring-rest-docs.html>
- <https://docs.spring.io/spring-restdocs/docs/current/reference/html5/>
- adoc 템플릿
  - <https://raw.githubusercontent.com/eugenp/tutorials/master/spring-5/src/docs/asciidocs/api-guide.adoc>
- @`AutoConfigureRestDocs`, `RestDocsMockMvcConfigurationCustomizer`
  - <https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-testing.html#boot-features-testing-spring-boot-applications-testing-autoconfigured-rest-docs>
- Mustache
  - <https://taegon.kim/archives/4910>
  - <https://mustache.github.io/mustache.5.html>
- 테스트코드 참고
  - <https://github.com/spring-projects/spring-restdocs/tree/v2.0.3.RELEASE/samples/rest-notes-spring-hateoas/src>
  - 산출물
    - <https://docs.spring.io/spring-restdocs/docs/1.0.1.RELEASE/samples/restful-notes/api-guide.html>
  - ConstrainedFields
    - <https://github.com/spring-projects/spring-restdocs/blob/v2.0.3.RELEASE/samples/rest-notes-spring-hateoas/src/test/java/com/example/notes/ApiDocumentation.java>
- 스타일 변경
  - <https://github.com/asciidoctor/asciidoctor/tree/master/data/stylesheets>

    ```gradle
    asciidoctor {
    attributes "snippets": snippetsDir,
            "stylesheet": "custom.css"
    ```

- Encoding
  - <https://docs.spring.io/spring-restdocs/docs/1.2.6.RELEASE/reference/html5/#configuration-snippet-encoding>
- 기본 템플릿 코드
  - <https://github.com/spring-projects/spring-restdocs/tree/master/spring-restdocs-core/src/main/resources/org/springframework/restdocs/templates/asciidoctor>
- IDEA 에서 snippet 파일 수정시 이상한 자동완성이 작동할 경우
  - Settings > Editor > File types > AsciiDoc > + > `*.snippet` 추가
- 에러코드 정의 예제
  - <https://docs.spring.io/spring-restdocs/docs/1.0.1.RELEASE/samples/restful-notes/api-guide.html#overview-http-status-codes>
- {step} 사용 예제, Getting Started 만들 때 사용
  - <https://github.com/spring-projects/spring-restdocs/blob/master/samples/rest-notes-spring-data-rest/src/test/java/com/example/notes/GettingStartedDocumentation.java>
  - <https://docs.spring.io/spring-restdocs/docs/current/samples/restful-notes/getting-started-guide.html#_introduction>