# 빌드 버전에 현재 날짜 지정하는 방법

```gradle
jar {
    version = '1.0.'+getDate()
}

def getDate() {
    def date = new Date()
    def formattedDate = date.format('yyyyMMddHHmmss')
    return formattedDate
}
```

짧게 줄일수도 있다.

```gradle
def getDate() {
    new Date().format('yyyyMMddHHmmss')
}
```