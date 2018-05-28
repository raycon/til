# VSCode를 JAVA 스프링 IDE로 사용하기

[JAVA Extension Pack](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)을 설치한다. 아래 Extension을 포함한다.

- Language Support for Java(TM) by Red Hat
- Java Debug Extension for Visual Studio Code

`settings.json` 파일에 자바 경로와 프록시를 설정한다 :

```json
{
    // Language Support for Java(TM) by Red Hat
    "java.home": "C:/Program Files/Java/jdk1.8.0_144",
    "java.jdt.ls.vmargs": "-Dhttp.proxyHost=host.com -Dhttp.proxyPort=8080 -Dhttps.proxyHost=host.com -Dhttps.proxyPort=8080"
}
```

`F5` > `Java`를 선택해서 `.vscode/launch.json` 생성하고 다음과 같이 설정한다 :

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Debug (Launch)",
            "request": "launch",
            "mainClass": "com.example.spring.Application",
            "projectName": "ExampleApplication",
            "args": "--spring.profiles.active=dev"
        },
        {
            "type": "java",
            "name": "Debug (Attach)",
            "request": "attach",
            "hostName": "localhost",
            "port": 0
        }
    ]
}
```

## 문제해결

- `SpringApplication`을 찾지 못할 경우 `.classpath`와 `.project`파일을 삭제한 뒤 자동으로 재생성 되는 파일을 사용한다.
- `jar`로 묶여진 라이브러리를 사용할 경우 `.classpath`파일에 다음 내용을 추가한다.

      <classpathentry kind="lib" path="libs/library.jar"/>

## TODO

- 디버거에서 중단점 설정이 먹히지 않는다.