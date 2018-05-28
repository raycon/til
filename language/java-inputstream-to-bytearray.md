# `InputStream` into a `ByteArray`

build.gradle 에 아래 내용 추가

`compile group: 'commons-io', name: 'commons-io', version: '2.5'`

아래 코드로 읽으면 된다.

```java
InputStream is;
byte[] bytes = IOUtils.toByteArray(is);
```

## 참조

> http://stackoverflow.com/questions/1264709/convert-inputstream-to-byte-array-in-java
> https://mvnrepository.com/artifact/commons-io/commons-io