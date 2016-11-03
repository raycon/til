# 워크스페이스에서 파일 무시하는 방법

    p4 set P4IGNORE=.p4ignore

`P4IGNORE` 변수에 파일 이름을 지정한다. 퍼포스는 `P4IGNORE` 파일에 있는 룰을 기반으로 파일을 무시한다.

## .p4ignore 예제

> https://www.perforce.com/perforce/r15.2/manuals/cmdref/P4IGNORE.html

    # Ignore .p4ignore files
    .p4ignore

    # Ignore object files, shared libraries, executables
    *.dll
    *.so
    *.exe
    *.o

    # Ignore all HTML files except the readme file
    *.html
    !readme.html

    # Ignore the bin directory
    bin/

    # Ignore the build.properties file in this directory
    /build.properties

    # Ignore all text files in test directories
    test/**.txt
