# MockMvc 사용법

## POST 요청

```java
MvcResult result = mvc.perform(post("/url")
                          .contentType(MediaType.APPLICATION_FORM_URLENCODED)
                          .content(EntityUtils.toString(new UrlEncodedFormEntity(
                                  Arrays.asList(new BasicNameValuePair("param", "1234"))))))
                      .andExpect(status().isOk())
                      .andReturn();
String content = result.getResponse().getContentAsString();
assertThat(content).contains("content string");

MvcResult result = mvc.perform(post("/url")
                .contentType(MediaType.APPLICATION_FORM_URLENCODED).param("param", "1234"))
                .andExpect(status().isOk())
                .andReturn();
String content = result.getResponse().getContentAsString();
assertThat(content).contains("content string");
```
