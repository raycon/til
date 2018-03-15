# Executable jar

gradle로 jar 파일을 만들 경우 Main-Class를 찾을 수 없다는 에러 메시지가 발생할 때 해결 방법.
둘 중 하나를 적용한다.

## MANIFEST.MF

`src/main/java/META-INF/MANIFEST.MF` 파일을 만들고 `main` 메소드를 갖는 클래스를 지정한다.

    Manifest-Version: 1.0
    Main-Class: com.example.app.MainClass

## Gradle

`build.gradle`에 다음 내용을 추가한다.


!! 아래 내용 적용 후 수정 필요

    jar {
      baseName = 'Alex-DEV'
        version = '1.0.'+getDate()
        if (project.hasProperty('cl')) {
            version = version+'.'+project.cl
        }
      manifest {
        attributes "Main-Class": "com.samsung.music.porter.alex.AlexApplication"
      }

      from {
        configurations.compile.collect { it.isDirectory() ? it : zipTree(it) }
      }
    }

    def getDate() {
        new Date().format('yyMMdd.HHmm')
    }
