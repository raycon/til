# Dotenv

> 환경변수 설정을 `.env` 파일로 할 수 있도록 해주는 모듈 <https://www.npmjs.com/package/dotenv>

## 설치

    npm install dotenv --save

## 사용법

어플리케이션 파일의 제일 상단에 아래 코드를 넣는다.

    require('dotenv').config();

프로젝트 루트 폴더에 `.env` 파일을 만들어서 변수를 설정한다.

    DB_HOST=localhost
    DB_USER=root
    DB_PASS=password

위 값은 `process.env` 에 할당된다.

```js
db.connect({
    host: process.env.DB_HOST,
    username: process.env.DB_USER,
    password: process.env.DB_PASS
});
```