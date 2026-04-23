# Security Checklist

## OWASP Top 10

- [ ] A01:2021 – Broken Access Control
  - Проверка: Может ли пользователь A получить ticket пользователя B?
  - Статус: FAIL

- [ ] A02:2021 – Cryptographic Failures
  - Проверка: Пароли хэшируются? Используется HTTPS?
  - Статус: PARTIAL

- [ ] A03:2021 – Injection
  - Проверка: SQL/Command injection через параметры?
  - Статус: PASS

- [ ] A04:2021 – Insecure Design
  - Проверка: Логические ошибки в бизнес-логике?
  - Статус: PARTIAL

- [ ] A05:2021 – Security Misconfiguration
  - Проверка: Debug mode? Дефолтные пароли?
  - Статус: PARTIAL

- [ ] A06:2021 – Vulnerable Components
  - Проверка: Устаревшие библиотеки?
  - Статус: PASS

- [ ] A07:2021 – Identification Failures
  - Проверка: Слабые пароли? JWT валидация?
  - Статус: FAIL

- [ ] A08:2021 – Integrity Failures
  - Проверка: Проверка целостности данных?
  - Статус: PARTIAL

- [ ] A09:2021 – Logging Failures
  - Проверка: Логируются ли попытки взлома?
  - Статус: FAIL

- [ ] A10:2021 – SSRF
  - Проверка: Возможны запросы к внутренним ресурсам?
  - Статус: PASS

## MASVS Mobile

- [ ] M1 – Insecure Data Storage
  - Проверка: Токены в SharedPreferences открыто?
  - Статус: FAIL

- [ ] M2 – Insecure Communication
  - Проверка: Certificate Pinning?
  - Статус: FAIL

- [ ] M3 – Insecure Authentication
  - Проверка: Локальная аутентификация без сервера?
  - Статус: PASS

- [ ] M4 – Insufficient Authorization
  - Проверка: Клиентские проверки прав?
  - Статус: FAIL

- [ ] M5 – Reverse Engineering
  - Проверка: Обфускация кода?
  - Статус: PARTIAL

## Итого

| Категория    | Пройдено | Всего |
|--------------|----------|-------|
| OWASP Top 10 | 3        |    10 |
| MASVS        | 1        |     5 |
| **Общий**    | **4**    | **15**|

**Вердикт:** Требуется доработка безопасности.