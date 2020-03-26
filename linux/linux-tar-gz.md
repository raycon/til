# tar.gz

- tar: 여러 파일을 하나의 파일로 묶는다.
- gzip: 파일 하나를 gz 파일로 압축한다.

## gzip 사용법

gz 압축 풀기:

    gzip -d gilename.gz

gz 압축 하기:

    gzip filename.ext

`filename.ext`가 없어지고 `filename.gz` 파일이 생성된다.

## tar 사용법

tar 만들기:

    tar -cf archive.tar foo bar

tar 내부 파일 목록 출력:

    tar -tvf archive.tar

tar 풀기:

    tar -xf archive.tar

`v` 옵션을 추가하면 로그를 출력한다.

## 한꺼번에 사용하기

tar.gz 만들기:

    tar -czvf archive.tar.gz foo bar

tar.gz 풀기:

    tar -xzvf archive.tar.gz

## zip 파일 압축 풀기

`unzip` 패키지 설치:

    apt-get install unzip

`unzip` 명령어 사용:

    unzip archive.zip