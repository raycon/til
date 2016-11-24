# VIM - YouCompleteMe

> 자동완성 플러그인

## Windows

VIM 설치 : <https://bintray.com/micbou/generic/vim>

YouCompleteMe는 Python을 지원하도록 컴파일된 VIM 을 사용해야함.

Vundle 설정 : <https://github.com/VundleVim/Vundle.vim>

Vundle 에 YouCompleteMe 추가 :

```vimrc
Plugin 'Valloric/YouCompleteMe'
```

아래 프로그램 설치 :

- Python 2.7.9 : <https://www.python.org/downloads/release/python-279>
- CMake : <https://cmake.org/download>
- Visual Studio 2015 Community : <https://www.visualstudio.com/ko/free-developer-offers>
  - Visual Studio > File > New Project > Templates > Visual C++ > Install Visual C++ 2015 Tools for Windows Desktop 메뉴로 툴을 설치해야 CMake 가 컴파일러를 사용할 수 있음
- 7zip : <http://www.7-zip.org/download.html>

아래 명령어로 설치 :

```cmd
cd %USERPROFILE%/vimfiles/bundle/YouCompleteMe
install.py --tern-completer
```