# AWS CLI

> <https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/install-windows.html>

## Install

Windows Installer:

[64비트](https://s3.amazonaws.com/aws-cli/AWSCLI64.msi) 또는 [32비트](https://s3.amazonaws.com/aws-cli/AWSCLI32.msi) Windows 설치 프로그램을 다운로드해서 실행한다.

PIP:

다음 명령어로 설치

    pip3 install awscli --upgrade --user

.py와 연결된 프로그램이 없다는 오류 발생시

    assoc .py=pyautofile
    ftype pyautofile="C:\Anaconda2\python.exe" "%1" %*
