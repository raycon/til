# src/main/resources 폴더의 xml 파일 읽는법

```java
Resource resource = appContext.getResource("classpath:data.xml");
Properties properties = new Properties();

try (InputStream is = resource.getInputStream()) {
    properties.loadFromXML(is);
} catch (IOException e) {
    e.printStackTrace();
}
```