# Convert Object to JSON

Object to JSON :

```java
ObjectMapper mapper = new ObjectMapper();
Til til = new Til();

// Object > JSON file
mapper.writeValue(new File("c:\\til.json"), til);

// Object > JSON String
String json = mapper.writeValueAsString(til);
```

JSON to Object :

```java
ObjectMapper mapper = new ObjectMapper();
String json = "{'til' : 'convert-object-to-json'}";

// JSON file > Object
Til tilFromFile = mapper.readValue(new File("c:\\til.json"), Til.class);

// JSON String > Object
Til tilFromString = mapper.readValue(json, Til.class);
```

## Override toString()

> <https://stackoverflow.com/questions/16527932/ok-to-use-json-output-as-default-for-tostring> 참고

Reflections (Apache library):

```java
@Override
public String toString(){
    return org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(this);
}
```

JSON based implementation (GSON, Jackson libraries):

```java
// GSON library for JSON
@Override
public String toString(){
    return new com.google.gson.Gson().toJson(this);
}

// Jackson libabry for JSON/YAML
@Override
public String toString() {
    try {
        return new com.fasterxml.jackson.databind.ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(this);
    } catch (com.fasterxml.jackson.core.JsonProcessingException e) {
        e.printStackTrace();
    }
    return null;
}
```

ToStringBuilder (available with apache-commons library):

```java
@Override
public String toString() {
    return new org.apache.commons.lang3.builder.ToStringBuilder(this).
        append("field1", field1).
        append("field2", field2).
        toString();
}
```

Hard-core toString() implementation:

```java
@Override
public String toString() {
    return new StringBuilder()
        .append("field1:"+field1)
        .append("field2:"+field2)
        .toString();
}
```