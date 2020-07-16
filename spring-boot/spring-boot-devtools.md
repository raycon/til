# Spring Boot DevTools

자바 파일을 수정할 경우 어플리케이션을 재시작 하지 않고 수정사항을 반영하는 방법

`build.gradle`에 `devtools` 의존성을 추가한다:

```
dependencies {
    ...
    runtimeOnly 'org.springframework.boot:spring-boot-devtools'
    ...
}
```

Run/Debug Configuration > Spring Boot > Running Application Update Policies 를 다음과 같이 설정한다.

- On 'Update' action: Hot swap classes and update trigger file if failed
- On frame deactivation: Update classes and resources

어플리케이션을 **디버그 모드**로 실행한다.

파일을 수정하고 `Run > Update [APP] Applicaton` 메뉴를 선택하거나 `Ctrl + F10` 단축키를 누르면 수정사항이 반영된다.
