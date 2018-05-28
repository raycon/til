# Gradle Eclipse Plugin

## [STS Gradle Integration](https://github.com/spring-projects/eclipse-integration-gradle)

- 스프링 프로젝트의 일부로 개발된 기능
- 현재 최소 유지보수 상태로 관리되고 있음. [스프링 문서](http://docs.spring.io/sts/nan/v372/NewAndNoteworthy.html) 참고
- 앞으로 Phase out 될 예정

## [Buildship](https://github.com/eclipse/buildship)

- 이클립스 공식 프로젝트
- Spring Tool Suite에서도 지원함
- Eclipse Marketplace 를 통해서 설치 가능

## Migration

[Spring Tool Suite](https://spring.io/tools/sts/all)를 설치하면 기본으로 `STS Gradle Integration`이 설치 되는데, [마이그레이션 가이드](https://github.com/eclipse/buildship/wiki/Migration-guide-from-STS-Gradle-to-Buildship)에 `STS Gradle`을 `Buildship`으로 마이그레이션 하는 방법이 자세히 설명되어 있다.

## 문제해결

### 프로젝트 이름이 중복되는 경우

`Buildship`으로 마이그레이션 도중 프로젝트 이름이 중복되어서 Import에 실패하는 경우가 있다. 프로젝트를 선택하고 `F2`키를 눌러서 이름을 변경해도 다시 원래 이름(폴더 이름)으로 돌아온다. `Buidship`이 폴더 이름을 프로젝트 이름으로 사용하기 때문이다. [FAQ](https://github.com/eclipse/buildship/blob/master/docs/user/Faq.md)를 보면 맨 처음에 해결방법이 있는걸로 봐서 많은 사람들이 겪는 문제인듯 하다.

공식 문서 해결 방법은 다음과 같다 :

```gradle
if (project != rootProject) {
  eclipse.project.name = (rootProject.name + project.path).replaceAll(':', '-')
}
```

당연하게도 위의 코드를 `build.gradle`에 넣으면 에러가 난다. 왜때문이냐면 `eclipse`가 정의되어 있지 않아서이다.

다음과 같이 사용해야 에러가 발생하지 않는다 :

```gradle
apply plugin: 'eclipse'
if (project != rootProject) {
  eclipse.project.name = (rootProject.name + project.path).replaceAll(':', '-')
}
```

간단하게 써도 된다 :

```gradle
apply plugin: 'eclipse'
eclipse.project.name = 'MyProject'
```

모든 `build.gradle`에 위 내용을 입력하기 싫으면, `~/.gradle/init.gradle` 파일에 다음과 같이 입력해서 사용한다 :

```gradle
allprojects {
  ...
  apply plugin:'eclipse'
  if (project != rootProject) {
    eclipse.project.name = (rootProject.name + project.path).replaceAll(':', '-')
  }
  ...
}
```

### Buildship을 인식하지 않는 경우

Marketplace에서 Buildship을 설치했는데도 `New > Spring Starter Project` 화면에서 `Gradle (Buildship)`을 선택할 경우 다음과 같은 에러가 발생한다.

    Cannot import using Gradle (Buildshiop) because Buildship Gradle Tooling is not installed.

STS 버전이 낮아서 발생하는 문제로 [Issue 90](https://github.com/spring-projects/spring-ide/issues/90)에서 내용을 확인할 수 있다. 2017-03-22일 기준으로 비교적 최근에 발생한 이슈로, 수정 사항이 포함된 정식 릴리즈 버전이 없으므로 nightly 빌드 버전을 받아서 사용하면 해결할 수 있다.

`Help > Install New Software...` 메뉴를 누르고 Work with: 에 다음 주소를 입력한다 :

    http://dist.springframework.org/snapshot/IDE/nightly

`Core / Spring IDE` 밑의 항목을 체크해서 설치하고 재시작한다.