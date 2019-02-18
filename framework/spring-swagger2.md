# Spring Swagger2

> Swagger를 사용해서 REST API 문서를 자동으로 생성한다

## 환경

- Gradle: 4.10.2
- Spring Boot: 2.1.3.RELEASE

## 설치

`build.gradle`에 다음 의존성을 추가한다

```gradle
implementation 'io.springfox:springfox-swagger2:2.9.2'
implementation 'io.springfox:springfox-swagger-ui:2.9.2'
```

## 설정

`SwaggerConfig.java` 파일을 만들고 다음과 같이 설정한다.

```java
@Configuration
@EnableSwagger2
public class SwaggerConfig {

    @Bean
    public Docket api() {
        // Springfox Swagger 2를 활성화한다.
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.swagger"))
                .paths(PathSelectors.any())
                .build();
    }

}
```

- `@EnableSwagger2`: Springfox Swagger 2를 활성화한다.
- `1`: swagger 스펙 2.0에 맞게 초기화한다.
- `2`: `ApiSelectorBuilder`를 생성한다. (Swagger를 적용할 API를 선택하는 빌더)
- `3`: `apis()`
  - `any`, `none`, `withClassAnnotation`, `withMethodAnnotation`, `basePackage`로 지정 가능
  - 기본값은 `any()`
  - `com.example.swagger` 및 하위 패키지에서 컨트롤러를 검색한다
- `4`: `paths()`
  - `regex`, `ant`, `any`, `none` 지정 가능
  - 기본값은 `any()`

## 출력

- JSON 형태 : <http://localhost:8080/v2/api-docs>
- Swagger-UI : <http://localhost:8080/swagger-ui.html>

## JSON 파일 생성

> <https://github.com/Swagger2Markup/spring-swagger2markup-demo/blob/master/src/test/java/io/github/robwin/swagger2markup/petstore/Swagger2MarkupTest.java> 참고

다음과 같은 테스트를 작성한다.

```java
@WebMvcTest
@Import(SwaggerConfig.class)
@RunWith(SpringJUnit4ClassRunner.class)
public class SwaggerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void createSpringfoxSwaggerJson() throws Exception {
        String outputDir = "build/swagger";
        MvcResult mvcResult = this.mockMvc.perform(get("/v2/api-docs")
                .accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andReturn();

        MockHttpServletResponse response = mvcResult.getResponse();
        String swaggerJson = response.getContentAsString();
        Files.createDirectories(Paths.get(outputDir));
        try (BufferedWriter writer = Files.newBufferedWriter(Paths.get(outputDir, "swagger.json"), StandardCharsets.UTF_8)) {
            writer.write(swaggerJson);
        }
    }
}
```

## HTML 파일 생성

`src/docs/asciidoc/index.adoc` 파일을 추가한다.

```text
include::{generated}/overview.adoc[]
include::manual_content.adoc[]
include::{generated}/paths.adoc[]
include::{generated}/security.adoc[]
include::{generated}/definitions.adoc[]
```

`src/docs/asciidoc/manual_content.adoc` 파일을 추가한다.

```text
== Chapter of manual content 1

This is some dummy text

=== Sub chapter

Dummy text of sub chapter
```

`build.gradle`에 다음 내용을 추가한다.

```gradle
buildscript {
    repositories {
        jcenter()
        mavenCentral()
        maven { url 'http://oss.jfrog.org/artifactory/oss-snapshot-local/' }
    }

    dependencies {
        classpath 'io.github.swagger2markup:swagger2markup-gradle-plugin:1.3.3'
        classpath 'org.asciidoctor:asciidoctor-gradle-plugin:1.5.3'
        classpath 'org.asciidoctor:asciidoctorj-pdf:1.5.0-alpha.10.1'
    }
}

plugins {
    id 'io.franzbecker.gradle-lombok' version '2.1'
    id 'org.springframework.boot' version '2.1.3.RELEASE'
    id 'java'
}

apply plugin: 'io.spring.dependency-management'
apply plugin: 'io.github.swagger2markup'
apply plugin: 'org.asciidoctor.convert'

group = 'com.example.swagger'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '1.8'

repositories {
    mavenCentral()
}

ext {
    asciiDocOutputDir = file("${buildDir}/asciidoc/generated")
    swaggerOutputDir = file("${buildDir}/swagger")
    snippetsOutputDir = file("${buildDir}/asciidoc/snippets")
    springfoxVersion = '2.5.0'
}

dependencies {
...
}

ext {
    asciiDocOutputDir = file("${buildDir}/asciidoc/generated")
    swaggerOutputDir = file("${buildDir}/swagger")
    snippetsOutputDir = file("${buildDir}/asciidoc/snippets")
    springfoxVersion = '2.5.0'
}

convertSwagger2markup {
    dependsOn test
    swaggerInput "${swaggerOutputDir}/swagger.json"
    outputDir asciiDocOutputDir
    config = [
            'swagger2markup.pathsGroupedBy' : 'TAGS',
            'swagger2markup.extensions.springRestDocs.snippetBaseUri': snippetsOutputDir.getAbsolutePath()]
}

asciidoctor {
    dependsOn convertSwagger2markup
    sources {
        include 'index.adoc'
    }
    backends = ['html5', 'pdf']
    attributes = [
            doctype: 'book',
            toc: 'left',
            toclevels: '3',
            numbered: '',
            sectlinks: '',
            sectanchors: '',
            hardbreaks: '',
            generated: asciiDocOutputDir
    ]
}
```

다음 명령어를 실행한다.

    gradlew asciidoctor

`build/asciidoc/html5`, `build/asciidoc/pdf`에 결과물이 생성된다.

- PDF 의 경우 한글 설명이 표시되지 않는다.
- HTML 의 경우 `Table Of Content`라는 내용이 셀마다 출력되는데 없애는 방법 확인 필요.

## 기타

### Validator 사용

JSR-303 에 정의된 validator를 사용할 수 있다.

`build.gradle`에 다음 의존성을 추가한다

    implementation "io.springfox:springfox-bean-validators:2.9.2"

`@NotNull`, `@Min`, `@Max`, `@Size` 를 사용할 수 있다.

다음과 같이 사용할 경우 `required` 값을 지정해야 한다

```java
@NotNull
@ApiModelProperty(value = "이름D", required = true)
private String name;
```

`@NotNull`과 `@ApiModelProperty`가 함께 사용될 경우 `@ApiModelProperty`에 지정된 `required`값이 사용되는데 기본 값이 `false`여셔 `@NotNull`에 따른 필수값 지정이 되지 않는다.

`@NotNull(message="msg")`를 지정해도 출력되지는 않는다.

### 문제 해결

`POST`, `PUT` API의 응답에 `200`이 생성될 경우:

- 메소드 위에 `@ResponseStatus(HttpStatus.CREATED)`를 지정한다
- <https://github.com/springfox/springfox/issues/908>

`POST`, `PUT` API 응답에 `ResponseEntity`가 모델로 표시될 경우

  1. ResponseEntity 를 응답에서 Void로 변환하도록  초기화한다.

        ```java
        return new Docket(DocumentationType.SWAGGER_2)
            .directModelSubstitute(ResponseEntity.class, Void.class)
        ```

  2. `@ApiOperation`로 `response` 값으로 적절한 타입을 지정한다.

        ```java
        @ApiOperation(value = "Create",
                    notes = "On success article link will be returned",
                    response = Link.class)
        ```

  3. `@ApiResponses`로 StatusCode에 대한 응답 타입을 지정한다.

        ```java
        @ApiResponses({
                @ApiResponse(code = 201, message = "Created~~", response = Link.class)
        })
        ```

기본 응답 메시지 코드 사용하지 않을 경우 다음과 같이 초기화한다.

```java
return new Docket(DocumentationType.SWAGGER_2)
    .useDefaultResponseMessages(false)
```

## 참고

<http://springfox.github.io/springfox/docs/current>
<http://swagger2markup.github.io/swagger2markup/1.3.3>