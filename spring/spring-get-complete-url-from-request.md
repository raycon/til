# HttpServletRequest to complete URL

> <http://stackoverflow.com/questions/2222238/httpservletrequest-to-complete-url>

The HttpServletRequest has the following methods:

- `getRequestURL()` - returns the part of the full URL before query string separator character
- `getQueryString()` - returns the part of the full URL after query string separator character

So, to get the full URL, just do:

```java
public static String getFullURL(HttpServletRequest request) {
    StringBuffer requestURL = request.getRequestURL();
    String queryString = request.getQueryString();

    if (queryString == null) {
        return requestURL.toString();
    } else {
        return requestURL.append('?').append(queryString).toString();
    }
}
```