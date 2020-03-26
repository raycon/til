# WEB-INF

[WAR (file format)](https://en.wikipedia.org/wiki/WAR_(file_format)) 스펙에 정의된 폴더 이름이다. 이 폴더는 `web.xml` 파일을 갖는다.

`WEB-INF/web.xml` :

- 특정 URL 요청이 어떤 servlet으로 라우팅 되어야 하는지에 관한 내용을 정의한다.
- servlet에서 참조하는 context variable을 정의한다.
- 리소스 의존성을 정의한다. 예) 메일세션

`WEB-INF/classes`, `WEB-INF/libs` 폴더는 [classpath](https://en.wikipedia.org/wiki/Classpath_(Java))에 포함된다.