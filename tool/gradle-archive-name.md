# Gradle Archive Name

> <https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Jar.html>

- Gradle의 기본 archiveName 은 `[baseName]-[appendix]-[version]-[classifier].[extension]` 형식이다.

기본값:

- `baseName`: `project.archivesBaseName` -> `project.name` -> `project.getPath()` 순으로 기본값을 갖는다.
- `appendix`: `null`
- `version`: `project.version` -> `unspecified`
- `classifier`: `null`. 동일한 코드로 빌드를 했지만 분류가 필요한 경우 사용. 예를들면 `jdk14`, `jdk15`가 될 수 있다.

Git 리비전과 해시를 포함하기:

    ext.revision = 'git rev-list --count HEAD'.execute().text.trim()
    ext.hash = 'git rev-parse --short HEAD'.execute().text.trim()
    version = new Date().format('yyMMdd.HHmm') + ".r${revision}.${hash}"

위와 같이 지정하면 `project-180102.0304.r10.a1b2c3d.jar` 형식의 파일이 생성된다.