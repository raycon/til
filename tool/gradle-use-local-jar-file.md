# 로컬에 있는 JAR 파일 사용하기

`dependencies`에 다음 내용을 추가한다.

파일 추가:

```groovy
dependencies {
    compile files('folder/library.jar')
}
```

폴더 추가:

```groovy
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```

> 참고: <https://stackoverflow.com/questions/20700053/how-to-add-local-jar-file-dependency-to-build-gradle-file>