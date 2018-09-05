# Python SSLError 해결

방화벽 사용시 SSL 인증서 관련해서 다음과 같은 에러가 발생한다.

    Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1045)'))': /simple/tensorflow/

`pip` 명령어에 `--trusted-host` 파라미터를 추가하면 에러가 발생하지 않는다.

    pip install <PACKAGE_NAME> --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org

이 설정을 저장해서 사용하려면

`%APPDATA%/pip/pip.ini` 파일을 생성하고 아래 내용을 추가한다.

    [global]
    trusted-host=
      pypi.python.org
      pypi.org
      files.pythonhosted.org
      github.com
      raw.githubusercontent.com

참고:

<https://github.com/pypa/pip/issues/5288>