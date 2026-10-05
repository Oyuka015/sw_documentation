# W05 Code Sample Audit (Bhatti's 5 Principles)

Тест орчин: Prism 5.14.2 mock server (`http://127.0.0.1:4010`), spec: `openapi/openapi.yaml`.

## Sample 1: POST /pets/upload-photo

Энэ код тэжээвэр амьтны зургийг `pet_id`-тай хамт multipart хэлбэрээр илгээж, хадгалагдсан зургийн URL-ийг буцаана. `CORGLY_TOKEN` болон локал `einstein.jpg` шаардлагатай.

Код: [`samples/upload_photo.py`](samples/upload_photo.py)

```
200 {'pet_id': 'corgi_98231', 'photo_url': 'https://media.corg.ly/photos/einstein.jpg'}
```

## Sample 2: POST /audio/translate-bark

Энэ код бичигдсэн bark аудио файлыг илгээж, утга болон найдвартай байдлын хувийг буцаана.

Код: [`samples/translate_bark.py`](samples/translate_bark.py)

```
200 {'translation': 'I want to play fetch', 'confidence': 0.92}
```

## Sample 3: POST /webhooks/subscribe

Энэ код серверийн хаягийг бүртгэж, тэжээвэр амьтны үйл явдлыг тэр хаяг руу илгээлгэнэ.

Код: [`samples/register_webhook.py`](samples/register_webhook.py)

```
201 {'webhook_id': 'wh_5521', 'status': 'active'}
```

## Scorecard

| Sample | Explained | Concise | Clear | Usable | Trustworthy |
|---|---|---|---|---|---|
| POST /pets/upload-photo | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| POST /audio/translate-bark | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| POST /webhooks/subscribe | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |

**Дундаж: 4.5 / 5.0 (90%)**

## Үнэлгээний тайлбар

- **Concise (4★):** upload/translate sample-д `with open(...)` болон multipart tuple нэмэлт мөр шаарддаг.
- **Usable (4★):** `your_jwt_token` нь хэрэглэгч өөрөө солих placeholder хэвээр. `foo/bar/test` байхгүй.
- **Trustworthy (4★):** Хариуг Prism mock-оор баталгаажуулсан. Жинхэнэ production сервер байхгүй тул 5★ өгөөгүй.

## Хийсэн засвар (refactoring)

- Эхний хувилбарт `data=` ашигласан нь Prism-ийн multipart parser-ийг унагаасан. Талбар бүрт `Content-Type` тодорхой зааж (`(None, value, "text/plain")`) засав.
- Base URL болон token-ийг `os.environ`-оос авдаг болгож, CI болон mock-д ашиглах боломжтой болгосон.