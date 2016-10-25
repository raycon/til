# VSCode Proxy
> VSCode에 확장을 설치하려는데 네트워크 커넥션 에러가 발생해서 프록시를 설정했다.

`파일 > 기본설정 > 사용자 설정` 을 누른다.

왼쪽 창에서 아래 내용을 찾아 오른쪽 창(`settings.json`)에 복사한다.

    // 사용할 프록시 설정입니다. 설정되지 않으면 http_proxy 및 https_proxy 환경 변수에서 가져옵니다.
    "http.proxy": "",

    // 제공된 CA 목록에 대해 프록시 서버 인증서를 확인해야 하는지 여부를 나타냅니다.
    "http.proxyStrictSSL": true,

    // 모든 네트워크 요청에 대해 'Proxy-Authorization' 헤더로 보낼 값입니다.
    "http.proxyAuthorization": null

각 항목에 맞는 값을 설정해준다.