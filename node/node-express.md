# Node Express

> <http://expressjs.com/en/3x/api.html>

## JSON Response

아래 옵션으로 JSON response를 Format 하는 방법을 설정할 수 있다.

```js
// json spaces JSON response spaces for formatting, defaults to 2 in development, 0 in production
app.set('json spaces', 2);
// json replacer JSON replacer callback, null by default
app.set('json replacer', replacer);
```

`res.json([status|body], [body])` 방식으로 사용한다.


```js
res.json(null);
res.json({ user: 'tobi' });
res.json(500, { error: 'message' });
```

`res.json()` 함수는 아래 동작을 수행하고 최종적으로 `res.send()` 함수로 응답을 처리한다.

- `json spaces`, `json replacer`를 사용해서 객체를 변환한다.
- `charset='utf-8'` , `ContentType='application/json'` 으로 설정한다.