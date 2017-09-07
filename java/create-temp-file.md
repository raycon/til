# 자바에서 제공하는 임시 폴더에 임시 파일 만들기

[File.createTempFile(...)](http://docs.oracle.com/javase/8/docs/api/java/io/File.html#createTempFile-java.lang.String-java.lang.String-) 메소드를 사용하면 된다.

```java
try{
    // CreateKv
    File temp = File.createTempFile("filename", ".tmp");
    // Write
    BufferedWriter bw = new BufferedWriter(new FileWriter(temp));
    bw.write("line1");
    bw.newLine();
    bw.write("line2");
    bw.close();
} catch(IOException e){
    e.printStackTrace();
}
```

`filename.tmp`는 `C:\Users\사용자명\AppData\Local\Temp` 에 저장된다.

이와 비슷하게 `File.createTempDir()` 도 있다.