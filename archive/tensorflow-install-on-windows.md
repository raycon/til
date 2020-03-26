# Windows에 Tensorflow 설치하기

Python 3.6.6을 [다운로드](https://www.python.org/downloads/release/python-366)해서 설치한다. 설치시 `PATH` 에 추가하는 옵션에 체크한다. 2018년 8월 30일 기준으로 `3.7.0` 버전에서는 tensorflow 설치시 오류가 발생하는 [이슈](https://github.com/tensorflow/tensorflow/issues/20444)가 있다.

    > python -V
    Python 3.6.6

`pip`를 업데이트한다. `SSLError`가 발생하면 [Python SSLError](../language/python-ssl-error)를 참고한다.

    python -m pip install --upgrade pip

`tensorflow`를 설치한다. (CPU Only 버전)

    pip3 install --upgrade tensorflow

다음 내용으로 `test.py`를 생성하고 실행한다.

```py
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

    python test.py

다음과 같은 오류가 발생한다.

    Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2

관련 [StackOverflow](https://stackoverflow.com/questions/47068709/your-cpu-supports-instructions-that-this-tensorflow-binary-was-not-compiled-to-u)를 보면  `AVX2`라는 기능을 사용하도록 컴파일 된 `tensorflow`를 설치하면 된다고 한다.

[tensorflow-windows-wheel](https://github.com/fo40225/tensorflow-windows-wheel) 리포지토리에서 원하는 버전의 파일(1.9.0\py36\CPU\avx2)을 찾아서 URL 을 확인한뒤 다음 명령어로 설치한다.

    pip install --ignore-installed --upgrade https://github.com/fo40225/tensorflow-windows-wheel/raw/master/1.9.0/py36/CPU/avx2/tensorflow-1.9.0-cp36-cp36m-win_amd64.whl

테스트 파일을 실행하면 다음과 같이 출력된다.

    > python test.py
    b'Hello, TensorFlow!'

참고:

<https://www.tensorflow.org/install/install_windows>