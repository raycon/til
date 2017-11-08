# Useful Eclipse Java Code Template

> <https://stackoverflow.com/questions/1028858/useful-eclipse-java-code-templates>

`Logger` 정의하느라 여기저기 찾아다니다 불편해서 찾아보니 템플릿 기능을 활용하면 쉽게 할 수 있었다.

`Window->Preferences->Java -> Editor -> Templates` 에서 다음을 `logger`로 정의한다.

```java
${:import(org.slf4j.Logger,org.slf4j.LoggerFactory)}
private static final Logger LOG = LoggerFactory.getLogger(${enclosing_type}.class);
```

- 에디터 창에서 `logger`를 입력하고 `Ctrl+Space`를 눌러서 해당 항목을 선택하면 자동으로 입력된다.
- `Ctrl+Space`를 누르고 `logger`를 입력하면 더 쉽게 입력 가능하다.
