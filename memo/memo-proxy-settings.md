# Proxy settings

> What The Proxy!

Proxy 세팅 및 서버 인증서 확인을 안하도록 하는 설정 모음

## AWS

환경 변수 설정 :

    set HTTP_PROXY=http://a.b.c.d:e
    set HTTPS_PROXY=http://a.b.c.d:e

`--no-verify-ssl` 옵션 사용으로 https 인증서 무시 :

     aws s3 ls --no-verify-ssl

## APM (~/.atom/.apm/.apmrc)

    proxy=http://a.b.c.d:e/
    https-proxy=http://a.b.c.d:e/
    strict-ssl=false

## NPM (~/.npmrc)

    proxy=http://a.b.c.d:e/
    https-proxy=http://a.b.c.d:e/
    registry=http://registry.npmjs.org/
    strict-ssl=false

## bower (~/.bowerrc)

    {
        "proxy": "http://a.b.c.d:e/",
        "https-proxy": "http://a.b.c.d:e/",
        "strict-ssl": false
    }

## git (~/.gitconfig)

    [http]
    proxy = http://a.b.c.d:e
    sslVerify = false
    [https]
    proxy = http://a.b.c.d:e
    sslVerify = false
    [url "https://"]
    insteadOf = git://

프록시를 적용하지 않을 호스트를 지정할 수 있다.

    no_proxy=.my.company,localhost,127.0.0.1,::1

도메인별로 프록시를 설정할 수 있다.

    [http]
    sslVerify = true
    [http "https://www.example.com/"]
    sslVerify = false

명령어는 다음과 같다.

    $ git config --bool --get-urlmatch http.sslVerify https://www.example.com false
    $ git config --get-urlmatch http https://www.example.com
    http.sslverify false

## gradle (~/.gradle/gradle.properties)

    systemProp.http.proxyHost=xxx.xxx.xxx.xxx
    systemProp.http.proxyPort=80
    systemProp.http.proxyUser=
    systemProp.http.proxyPassword=
    systemProp.http.nonProxyHosts=localhost

## gralde mavenCentral() (~/.gradle/init.gradle)

`https://repo1.maven.org/maven2/`에 접속할 수 없을 경우 아래 내용 추가

    allprojects {
        buildscript.repositories {
            maven { url "http://repo1.maven.org/maven2/" }
            jcenter{
                url "jcenter.bintray.com"
            }
        }
        repositories {
            maven { url "http://repo1.maven.org/maven2/" }
        }
    }

## VSCode (~/AppData/Roaming/Code/User/settings.json)

    {
        "http.proxy": "http://a.b.c.d:e",
        "http.proxyStrictSSL": false,
        "http.proxyAuthorization": null
    }

## Eclipse

__Windows > Preference > General > Network Connections__ 에서 Active Provider 를 `Manual`로 설정하고 `HTTP`, `HTTPS` 프록시를 설정함. Proxy bypass 에는 `localhost`, `127.0.0.1`을 추가함

## Maven (~/.m2/settings.xml)

```xml
<settings>
    <proxies>
        <proxy>
            <active>true</active>
            <protocol>http</protocol>
            <host>xxx.xxx.xxx.xxx</host>
            <port>80</port>
            <username></username>
            <password></password>
            <nonProxyHosts></nonProxyHosts>
        </proxy>
        <proxy>
            <active>true</active>
            <protocol>https</protocol>
            <host>xxx.xxx.xxx.xxx</host>
            <port>80</port>
            <username></username>
            <password></password>
            <nonProxyHosts></nonProxyHosts>
        </proxy>
    </proxies>
</settings>
```

## Ruby

gem 소스 변경으로 `SSL verification error` 해결

    gem sources -r https://rubygems.org/
    gem sources -a http://rubygems.org/

gem 인스톨시 proxy 지정

    gem install --http-proxy http://host:port bundler

## Ubuntu

### /etc/hosts

    xxx.xxx.xxx.xxx proxy

### /etc/environment

    http_proxy=http://a.b.c.d:e
    https_proxy=http://a.b.c.d:e
    ftp_proxy=http://a.b.c.d:e

### /etc/apt/apt.conf

    Acquire::http::Proxy "http://a.b.c.d:e";

## Certificates

### Ubuntu 인증서 추가

    $ sudo cp my-com.crt /usr/share/ca-certificates/
    $ sudo vi /etc/ca-certificates.conf
    마지막 줄에 my-com.crt 라고 추가
    $ sudo update-ca-certificates

    // 다른 방법
    sudo mkdir /usr/share/ca-certificates/extra
    sudo cat 인증서.crt
    // 인증서 내용 붙여넣고 저장
    sudo dpkg-reconfigure ca-certificates
    // 인증서 선택하여 적용

### Windows java 인증서 추가

JDK, JRE 둘 다 설정해 줘야 한다.

    "%JAVA_HOME%\bin\keytool.exe" -importcert -keystore "%JAVA_HOME%\jre\lib\security\cacerts" -file c:\인증서.crt

비밀번호 `changeit` > 인증서 확인 창에서 `y` 입력

> 인증서 관리는 [KeyStore Explorer](http://keystore-explorer.org/)를 사용하면 편리하다.