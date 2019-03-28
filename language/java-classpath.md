# Classpath

`classpath`는 JVM 이나 자바 컴파일러에 사용자가 정의한(user-defined) 클래스나 패키지의 위치를 전달하는 파라미터다. 자바 기본 클래스가 아닌 사용자가 정의한 클래스의 경우 클래스 파일의 경로를 지정해주어야 실행시 로드할 수 있다.

JVM은 클래스가 처음 사용될 때 다음과 같은 순서로 클래스를 로드한다.

- Bootstrap 클래스
  - `jre/lib/rt.jar`에 담긴 JDK 클래스 파일을 로드한다.
  - [Java Class Library](https://en.wikipedia.org/wiki/Java_Class_Library)와 JCL에서 사용하는 내부 클래스가 포함된다
- Extension 클래스
  - `jre/lib/ext`폴더나 `java.ext.dirs` 환경변수로 지정된 폴더에 있는 클래스 파일을 로드한다.
- 사용자 정의 클래스
  - `classpath` 파라미터로 전달된 경로에 있는 클래스 파일을 로드한다.
  - JAR 파일의 경우 [Manifest](https://docs.oracle.com/javase/tutorial/deployment/jar/manifestindex.html)의  [Class-Path](https://docs.oracle.com/javase/tutorial/deployment/jar/downman.html)에 정의된 경로를 사용한다.

## 클래스패스 지정

클래스패스는 다음과 같은 우선순위를 갖는다.

- `-classpath` 파라미터 값
- `CLASSPATH` 환경변수
- 현재 경로

예를 들어 `-classpath` 파라미터 값이 존재할 경우 `CLASSPATH`를 덮어쓴다.

다음과 같은 파일이 있을 경우

    D:\program
        ├ classes
        └ source
            └ com.raegon.example
                ├ Main.java
                └ Util.java

다음 명령어로 컴파일 하면

    D:\program>javac -d classes -sourcepath source source\com\raegon\example\Main.java

`-d` 옵션으로 지정된 `classes`에 클래스 파일이 생성된다.

    D:\program
        ├ classes
        │   └ com.raegon.example
        │       ├ Main.class
        │       └ Util.class
        └ source
            └ com.raegon.example
                ├ Main.java
                └ Util.java

`-classpath` 파라미터로 `classes`를 설정해서 Main 을 실행할 수 있다.

    java -classpath D:\program\classes com.raegon.example.Main

환경변수로 `CLASSPATH`를 설정한 뒤 실행할 수도 있다:

    set CLASSPATH=D:\classes
    java com.raegon.example.Main

## JAR 사용

다음과 같이 `library.jar` 를 사용해야 할 경우

    D:\program
        ├ lib
        │   └ library.jar
        │       └ com.raegon.library
        │           └ Library.class
        ├ classes
        │   └ com.raegon.example
        │       ├ Main.class
        │       └ Util.class
        └ source
            └ com.raegon.example
                ├ Main.java
                └ Util.java

클래스패스에 jar 파일의 경로를 지정해주면 된다. 이 때 기존 경로는 `;`으로 구분한다. `CLASSPATH`도 동일한 방식으로 설정할 수 있다.

    D:\program>java -classpath classes;lib\library.jar com.raegon.example.Main

특정 경로의 모든 jar 파일을 포함할 경우 와일드카드 `*`를 사용한다.

    D:\program>java -classpath classes;lib\* com.raegon.example.Main

`-classpath`에 지정된 jar 파일은 폴더의 개념으로 사용된다. 위와 같이 실행할 경우 다음과 같은 패키지와 클래스에 접근이 가능하다.

    com.raegon.example
        ├ Main.class
        └ Util.class
    com.raegon.library
        └ Library.class

## 더 읽어보기

- [How Classes are Found](https://docs.oracle.com/javase/8/docs/technotes/tools/findingclasses.html)
- [JAR (파일 포맷)](https://ko.wikipedia.org/wiki/JAR_(%ED%8C%8C%EC%9D%BC_%ED%8F%AC%EB%A7%B7)#%EC%8B%A4%ED%96%89_%EA%B0%80%EB%8A%A5%ED%95%9C_JAR_%ED%8C%8C%EC%9D%BC)
- [Java, Classpath, Classloading => Multiple Versions of the same jar/project](https://stackoverflow.com/questions/6105124/java-classpath-classloading-multiple-versions-of-the-same-jar-project)
- [Java 9 모듈 프로그래밍](http://www.hanbit.co.kr/store/books/look.php?p_code=B7608640342)