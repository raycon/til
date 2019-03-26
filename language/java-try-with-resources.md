# Try with resources

> Java SE 7 이후에 추가됨

`resource`는 프로그램이 종료된 이후 반드시 `close`되어야 하는 객체를 의미한다. `try-with-resources`를 사용하면 각각의 리소스가 `close`되는 것을 보장한다.

- 모든 리소스는 `java.lang.AutoCloseable`인터페이스를 구현해야 한다.
- 리소스는 `try` 블럭의 성공 여부에 상관 없이 `close`된다.
- 리소스는 `catch`, `finally` 블럭이 실행되기 전에 `close`된다.

하나의 리소를 선언하는 예제:

```java
try (BufferedReader br = new BufferedReader(new FileReader(path))) {
    return br.readLine();
}
```

두개의 리소스를 선언하는 예제:

- `;`를 구분자로 사용해서 한개 이상의 리소스를 선언할 수 있다.
- `close`가 되는 순서는 변수가 생성되는 순서의 **반대**다.

```java
try (
    java.util.zip.ZipFile zf = new java.util.zip.ZipFile(zipFileName);
    java.io.BufferedWriter writer = java.nio.file.Files.newBufferedWriter(outputFilePath, charset)
) {
    ...
}
```

위 코드에서 `writer` > `zf` 순으로 `close`가 호출된다.

## Suppressed Exceptions

`try` 블럭에서 예외 `A`가 발생한 뒤 리소스를 `close`하는 과정에서 예외 `B`가 발생하면, 예외 `B`는 무시된다. 이 때, 예외 `A`의 `Throwable.getSuppressed` 메소드를 사용해서 예외 `B`를 조회할 수 있다.

## AutoClosable and Closeable

각각의 문서를 통해 상속받는 인터페이스와 구현체를 확인할 수 있다.

- [AutoClosable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html)은 `Exception`을 던진다.
- [Closeable](https://docs.oracle.com/javase/8/docs/api/java/io/Closeable.html)은 `AutoCloseable`을 상속받아서 `IOException`을 던진다.