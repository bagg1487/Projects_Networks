# Saga для создания пользователя

## project_code: users-s14

## Шаги саги
1. Создать заказ (NEW)
2. Зарезервировать email (NEW)
3. Подтвердить email (PAID)
4. Создать пользователя (DONE)

## Компенсации
- При ошибке PAY_FAIL - отмена заказа (CANCELLED)

## Переходы состояний
- NEW + PAY_OK = PAID
- NEW + PAY_FAIL = CANCELLED
- PAID + CREATE_USER = DONE
- Любая ошибка = CANCELLED
## Диаграмма переходов статусов
stateDiagram-v2
    [*] --> NEW
    NEW --> PAID: PAY_OK
    NEW --> CANCELLED: PAY_FAIL
    PAID --> DONE: CREATE_USER
    PAID --> CANCELLED: FAIL
    CANCELLED --> NEW: RETRY