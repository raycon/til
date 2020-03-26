# JAVA Build Tools

![Evolution of build systems](https://karussell.files.wordpress.com/2009/09/build-system-evolution13.png)

출처 : [Evolution of build systems](https://karussell.wordpress.com/2009/09/29/evolution-of-build-systems/)

## MAKE

태초에 [Make](http://www.gnu.org/software/make/)가 있었다. `Make`로 자바를 빌드하면 **파일별**로 `javac`가 수행된다. 빌드 속도가 느리기 때문에 대안으로 `Ant`, `Maven` 같은 빌드툴이 등장했다.

참고 : [Why is no one using make for java](http://stackoverflow.com/questions/2209827/why-is-no-one-using-make-for-java)

## Ant with Ivy

[Ant](http://ant.apache.org/)는 2000년에 발표된 자바 빌드 빛 코드 실행을 위한 프레임워크다. 빌드 파일로는 `build.xml`을 사용한다.

장점 :

- Procedual Programming 개념을 적용함.
- 이해하기 쉽다.

단점 :

- XML 이 절차적 프로그래밍과 잘 어우러지지 않음
- XML 파일이 사용하기 어려울 정도로 커지는 경향이 있다.

[Apache Ivy](http://ant.apache.org/ivy/)는 종속성 관리를 위한 플러그인이다.

## Maven

[Maven](http://maven.apache.org/)은 2004년에 릴리즈됐다. Ant의 단점을 보완하기 위해 만들어졌다. Ant와는 전혀 다른 XML 구조를 사용한다. 빌드 파일로 `pom.xml`을 사용한다. `pom`은 Project Object Model의 약자다.

장점 :

- 다양한 옵션(디렉토리 구조, Task, Life Cycle)을 미리 정의해서 바로 사용 가능하다.
- 종속된 모듈을 네트워크에서 다운로드 할 수 있다. (이 기능은 나중에 Ivy 를 통해서 Ant에도 구현되었다.)

단점 :

- 라이브러리의 버전 충돌을 매끄럽게 처리하지 못한다.
- 복잡하고 커스터마이즈된 XML 빌드 스크립트를 작성하는것이 Ant보다 어렵다.

~~아무도 안쓰는것같다~~

참고 : [Why do so few people use Maven? Are there alternative tools?](http://stackoverflow.com/questions/1077477/why-do-so-few-people-use-maven-are-there-alternative-tools)

## Gradle

Gradle은 2012년에 릴리즈됐다. Ant와 Maven의 장점 및 여러 개선 사항을 포함하고 있다. 구글이 Android의 기본 빌드 툴로 사용하면서 짧은 시간안에 많은 관심을 얻었다. Ant와 Maven이 XML을 사용하는것과 달리 Gradle은 [Groovy](http://groovy-lang.org/)에 기반한 자신만의 DSL(Domain Specific Language)를 사용한다.

- DSL을 사용해서 Ant와 Maven보다 빌드 스크립트가 간단하고 명확하다.

## 참고

<https://technologyconversations.com/2014/06/18/build-tools/>