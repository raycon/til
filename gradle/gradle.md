# 그레이들

`build.gradle` : task를 구성하는 스크립트
`settings.gradle` : 어떤 프로젝트가 빌드에 포함되는지 설정하는 스크립트

## gradle init

    gradle init --type <name>
r
name :

- java-application
- java-library
- scala-library
- groovy-library
- basic

## 용어

- `task` : 특정 작업을 수행
- `type` : `task`의 속성을 정의
- `project` : `task`의 모음

## task

```gradle
task copy(type: Copy, group: "Custom", description: "Copies sources to the dest directory") {
    from "src"
    into "dest"
}
```

## Plugin

[Standard Plugin](https://docs.gradle.org/current/userguide/standard_plugins.html)과 [Community Plugin](https://plugins.gradle.org/)이 있다.

```gradle
plugins {       // `build.gradle` 파일의 최상단에 위치해야 한다.
    id 'java'   // 표준 플러그인
    id 'com.jfrog.bintray' version '0.4.1'  // 커뮤니티 플러그인
}
```

축약형 :

```gradle
apply plugin: 'java'
apply plugin: JavaPlugin
```

## Standard Plugin

### [base](https://docs.gradle.org/current/userguide/base_plugin.html)

zip, tar, jar로 아카이빙할 때 사용되는 convention property 을 추가한다.

- `archiveBaseName` - 기본값: `$project.name`
- `distDirName` - 기본값: `distributions`
- `libsDirName` - 기본값: `libs`

### [java](https://docs.gradle.org/current/userguide/java_plugin.html)

자바 빌드에 사용되는 task와 properties를 추가한다.

- `sourceCompatibility` - 소스를 컴파일하는 자바 버전
- `targetCompatibility` - class 파일을 생성하는 자바 버전, 기본값: `sourceCompatibility`
- `archivesBaseName` - jar 파일 이름, 기본값: `projectName`
- `manifest` - manifest 정의

## QnA

- Type 에서 사용할 수 있는 속성을 보려면?
  - [Gradle Build Language Reference](https://docs.gradle.org/current/dsl/) 참고
- 모든 taks 출력?

    > ./gradlew tasks

- 모든 속성 출력?

    > ./gradlew properties