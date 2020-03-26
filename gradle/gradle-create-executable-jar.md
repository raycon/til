# Create executable jar

실행 가능한 jar 파일을 만들기 위해서 `build.gradle`에 다음 내용을 추가한다.

```groovy
jar {
    manifest {
        attributes 'Main-Class': 'com.example.app.MainApplication'
    }
    from {
        configurations.compile.collect { it.isDirectory() ? it : zipTree(it) }
    }
}
```