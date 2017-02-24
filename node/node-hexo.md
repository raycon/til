# HEXO 로 만드는 정적 블로그

마크다운 문서를 웹페이지로 만들어주는 툴.
HEXO 를 선택한 이유는 아래와 같다. :

- 노드 기반이라서 기존 환경에 잘 어울린다.
- 마크다운을 지원한다.
- 깃헙 페이지를 지원한다.
- VSCode 플러그인이 있다.

## 설치

설치는 [Getting Started](https://hexo.io/docs/) 문서를 보고 하면 쉽게 가능하다.

## 환경설정

`_config.yml`을 열고 아래와 같이 설정했다.

```yml
# Site
language: ko
timezone: Asia/Seoul

# URL
url: http://raegon.kim
root: /

# Writing
new_post_name: :year-:month-:day-:title.md

# Deployment
deploy:
  type: git
  repo: https://github.com/raycon/raycon.github.io
```

## 서버 실행

`hexo server` 명령어로 서버를 실행하고 <http://localhost:4000> 으로 접속하면 블로그 내용을 확인할 수 있다.

## 명령어

### 글 생성

    hexo new [layout] <title>

레이아웃은 `post`, `draft`, `page`가 기본이고, 사용자가 `scaffolds` 폴더 밑에 md 파일로 추가할 수 있다.  기본값은 `post`로 `_config.yml`에 정의되어 있다.

레이아웃에 따라 생성된 파일은 다음과 같은 경로에 저장된다 :

    draft : source/_drafts/TITLE.md
    post  : source/_posts/TITLE.md
    page  : source/TITLE/index.md

### 글 발행

임시로 글을 만들고 나중에 발행할 수 있다. 임시 글은 블로그에 노출되지 않는다.

임시 글 생성 :

    hexo new draft <title>

임시 글 발행 :

    hexo publish [layout] <title>

## Github Pages 반영

hexo-deployer-git 설치 :

    npm install hexo-deployer-git --save