# Вопросы для самопроверки

1. Почему мы создаем Deployment, а не сразу Pod?
Deployment - сам чинит поды, Pod без него - нет
2. В чем разница между Liveness и Readiness пробами? Что произойдет, если провалится каждая из них?
Liveness - перезапуск, Readiness - убрать из сервиса.
3. Что такое "requests" и "limits" для CPU и памяти? Почему важно их указывать?
Requests - минимум, Limits - максимум. Без них соседей задавит.
4. Как Service находит свои Pod-ы? (Подсказка: Labels & Selectors).
По лейблам: selector в Service = labels в Pod.
5. Какой тип сервиса (ClusterIP, NodePort, LoadBalancer) используется для внутреннего общения, а какой — для внешнего доступа?
ClusterIP - внутри, NodePort/LoadBalancer - снаружи.
6. Что такое "Rolling Update" в контексте Деплоймента?
Rolling Update - плавная замена старых подов на новые без простоя.