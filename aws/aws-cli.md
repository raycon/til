# AWS CLI

## Install

Windows:

[64비트](https://s3.amazonaws.com/aws-cli/AWSCLI64.msi) 또는 [32비트](https://s3.amazonaws.com/aws-cli/AWSCLI32.msi) Windows 설치 프로그램을 다운로드해서 실행한다.

Mac 및 Linux:

Python 2.6.5 이상이 필요. pip를 사용하여 설치한다.

    pip install awscli

프록시 사용시 다음과 같이 설치:

    set HTTP_PROXY=http://host:port
    set HTTPS_PROXY=http://host:port
    pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org awscli

SSL 인증서 에러 발생시 다음과 같이 사용:

    aws s3 ls --no-verify-ssl