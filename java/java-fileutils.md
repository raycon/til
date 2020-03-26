# FileUtils

## API

<https://commons.apache.org/proper/commons-io/javadocs/api-2.5/org/apache/commons/io/FileUtils.html>

## Gradle

    compile group: 'commons-io', name: 'commons-io', version: '2.5'

## Usage

`listFiles` : 디렉토리 안의 **파일만** 찾을 경우 사용

```java
listFiles(File directory, IOFileFilter fileFilter, IOFileFilter dirFilter)
listFiles(File directory, String[] extensions, boolean recursive)

// dir 바로 밑의 파일만 찾는다.
FileUtils.listFiles(dir, TrueFileFilter.TRUE, null)
// dir 밑의 모든 폴더에서 파일을 찾는다.
FileUtils.listFiles(dir, TrueFileFilter.TRUE, TrueFileFilter.TRUE);
```

`listFilesAndDirs` : 디렉토리와 파일을 모두 찾을 경우 사용

```java
// dir 밑의 파일과 디렉토리를 찾는다.
FileUtils.listFilesAndDirs(dir, TrueFileFilter.TRUE, TrueFileFilter.TRUE);
// dir 밑의 디렉토리만 찾는다.
FileUtils.listFilesAndDirs(dir, FileFilterUtils.notFileFilter(TrueFileFilter.TRUE), TrueFileFilter.TRUE);
```

`FileFilterUtils.notFileFilter` : 필터 조건을 만족하지 않는 경우에 true가 되는 필터 생성

```java
// temp 단어가 들어가는 모든 파일과 디렉토리를 제외
IOFileFilter exclusionFilter = FileFilterUtils.notFileFilter(new WildcardFileFilter("*temp*"));
Collection<File> files = FileUtils.listFilesAndDirs(dir, exclusionFilter, exclusionFilter);
```

`FileFilterUtils.suffixFileFilter` : 특정 문자로 끝나는 파일 검사

```java
// .md 파일을 확장자 대소문자 구분 없이 필터링
IOFileFilter markdownFilter = FileFilterUtils.suffixFileFilter(".md", IOCase.INSENSITIVE);
```