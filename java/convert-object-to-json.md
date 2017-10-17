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