# Proxy settings

> What The Proxy!

Proxy 세팅 및 서버 인증서 확인을 안하도록 하는 설정 모음

## APM (~/.atom/.apm/.apmrc)

    proxy=http://xxx.xxx.xxx.xxx:80/
    https-proxy=http://xxx.xxx.xxx.xxx:80/
    strict-ssl=false

## NPM (~/.npmrc)

    proxy=http://xxx.xxx.xxx.xxx:80/
    https-proxy=http://xxx.xxx.xxx.xxx:80/
    registry=http://registry.npmjs.org/
    strict-ssl=false

## bower (~/.bowerrc)

    {
        "proxy": "http://xxx.xxx.xxx.xxx:80/",
        "https-proxy": "http://xxx.xxx.xxx.xxx:80/",
        "strict-ssl": false
    }

## git (~/.gitconfig)

    [http]
    proxy = http://xxx.xxx.xxx.xxx:80
    sslVerify = false
    [https]
    proxy = http://xxx.xxx.xxx.xxx:80
    sslVerify = false
    [url "https://"]
    insteadOf = git://

## gradle (~/.gradle/gradle.properties)

    systemProp.http.proxyHost=xxx.xxx.xxx.xxx
    systemProp.http.proxyPort=80
    systemProp.http.proxyUser=
    systemProp.http.proxyPassword=
    systemProp.http.nonProxyHosts=localhost

## VSCode (~/AppData/Roaming/Code/User/settings.json)

    {
        "http.proxy": "http://xxx.xxx.xxx.xxx:80",
        "http.proxyStrictSSL": false,
        "http.proxyAuthorization": null
    }

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

## Ubuntu

### /etc/hosts

    xxx.xxx.xxx.xxx proxy

### /etc/environment

    http_proxy=http://xxx.xxx.xxx.xxx:80
    https_proxy=http://xxx.xxx.xxx.xxx:80
    ftp_proxy=http://xxx.xxx.xxx.xxx:80

### /etc/apt/apt.conf

    Acquire::http::Proxy "http://xxx.xxx.xxx.xxx:80";

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

    keytool -storepass changeit -import -file "c:\인증서.crt" -keystore "C:\Program Files\Java\jre1.8.0_102\lib\security\cacerts" -alias mycert
