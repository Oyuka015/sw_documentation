# W05: OpenAPI 3.0, Swagger UI & Redoc

Corg.ly Pet Onboarding & Translation API-ийн баримтжуулалт.

## Хүлээлгэн өгөх зүйлс

| Зүйл | Байршил |
|---|---|
| OpenAPI 3.0.3 spec (5 endpoint) | [openapi/openapi.yaml](openapi/openapi.yaml) |
| Python code samples | [samples/](samples/) |
| Bhatti 5 зарчмын аудит | [audit.md](audit.md) |
| Swagger UI vs Redoc тайлан | [decision-report.md](decision-report.md) |

## Public URL

- Redoc (унших харагдац): https://oyuka015.github.io/sw_documentation/
- Swagger UI (sandbox): https://oyuka015.github.io/sw_documentation/swagger/

## Локал дээр ажиллуулах

    npm install -g @redocly/cli
    redocly lint docs/W05/openapi/openapi.yaml
    npx @stoplight/prism-cli mock docs/W05/openapi/openapi.yaml

Өөр терминалд:

    cd docs/W05/samples
    API_BASE_URL=http://127.0.0.1:4010 python register_webhook.py

## Хязгаарлалт

- `api.corg.ly` жинхэнэ сервер биш. Хариуг Prism mock-оор баталгаажуулсан.
- Public Swagger UI дээр Try-It-Out жинхэнэ сервер байхгүй тул амжилтгүй болно.