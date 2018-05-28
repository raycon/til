# 시놀로지 서버에 HTTPS로 연결하는 방법

## DDNS 설정

DDNS 서비스를 사용해서 유동 아이피를 고정된 도메인으로 연결한다.

시놀로지 자체 서비스 사용시 : `DSM 제어판 > 외부 액세스 > DDNS` 메뉴에서 `[name].sylology.me` 도메인을 신청한다.

ipTIME 공유기 사용시 : 공유기 관리자 화면에서 `고급설정 > 특수기능 > DDNS 설정` 메뉴에서 `[name].iptime.org` 도메인을 신청한다.

## CNAME 설정

도메인 관리 페이지에서 `CNAME` 을 등록한다. 예를 들면 다음과 같다 :

    Host : nas.domain.com
    Type : CNAME
    Content : [name].iptime.org or [name].synology.me

## Let's Encrypt 인증서 발급

HTTPS 연결을 사용하기 위해서 인증서를 추가한다. 자세한 사항은 [공식문서](https://www.synology.com/ko-kr/knowledgebase/DSM/help/DSM/AdminCenter/connection_certificate) 참조.

DSM 제어판 > 보안 > 인증서 > 추가 > 새 인증서 추가 > Let's Encrypt에서 인증서 얻기 (기본 인증서로 설정 체크)

    도메인 이름    : 도메인 제공업체에 등록한 도메인을 입력.
                    domain.com
    이메일        : 인증서 등록에 사용한 이메일 주소를 입력.
                    my@email.com
    주제 대체 이름 : 하나의 인증서가 여러 도메인에 적용되도록 허용하려면 여기에 기타 도메인 이름을 입력.
                    nas.domain.com;domain.com

주의사항 :

- Let's Encrypt 를 통해 발급받은 인증서는 90일 동안 유효하다. DSM 은 인증서가 만료되기 이전에 자동으로 갱신한다.
- 인증서 발급/갱신을 할 때 80포트가 접속 가능해야 한다.

## HTTPS 사용 설정

`DSM 제어판 > 네트워크 > DSM 설정` 에서 다음 기능을 활성화한다.

- HTTP 연결에서 HTTPS로 자동으로 리디렉션
- HTTP/2 활성화