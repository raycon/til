# ATOM Perforce

> 아톰에서 퍼포스 패키지를 사용하는 방법

## 설정환경

- 퍼포스 커맨드라인 인터페이스가 설치된 상태
- 퍼포스 워크 스페이스가 만들어진 상태

## 패키지 설치

[atom-perforce](https://github.com/mattsawyer77/atom-perforce) 패키지를 설치한다.

## 패키지 사용

수정할 파일을 열고 `Ctrl+Shift+P` 를 눌러서 아래 명령을 입력한다.

- Perforce: Add `Alt+P A`
- Perforce: Edit `Alt+P E`
- Perforce: Sync `Alt+P S`
- Perforce: Revert `Alt+P R`

## 패키지 설정

`Ctrl+,` > `Packages` > `atom-perforce` > `Settings` 에서 아래 옵션을 켜면 명령 입력을 자동화 할 수 있다.

- Auto-Add
- Auto-Edit
- Auto-Revert

## 워크스페이스 설정

p4 cli 가 사용할 워크스페이스를 설정한다. 워크스페이스를 설정하지 않으면 파일이 `읽기전용` 모드로 열려서 수정후 저장할 수 없다.

```
p4 set P4CLIENT=[WORKSPACE_NAME]
```
