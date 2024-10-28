# Мониторинг доступности с помощью Prometheus и Blackbox Exporter

Этот проект содержит конфигурацию для мониторинга доступности сайта с помощью Prometheus и Blackbox Exporter. С этими инструментами можно непрерывно собирать метрики о доступности и времени отклика указанных адресов, что помогает анализировать их доступность и производительность.

## Описание

Prometheus — это мощный инструмент с открытым исходным кодом для сбора и запроса метрик, а Blackbox Exporter — специализированный экспортер для Prometheus, который позволяет проверять доступность конечных точек (HTTP, HTTPS, DNS и других). В этой конфигурации Prometheus проверяет доступность `https://ptsecurity.com` с помощью Blackbox Exporter и сохраняет информацию о статусе и времени ответа.

## Требования

- **Prometheus**: для сбора и хранения метрик.
- **Blackbox Exporter**: для проверки доступности конечных точек.

## Установка и запуск

### 1. Клонирование репозитория

Клонируйте репозиторий с файлами конфигурации:

```bash
git clone https://github.com/CyberSolo99/testTaskDevOps.git
cd testTaskDevOps
```

### 2. Файлы конфигурации

Репозиторий содержит следующие файлы конфигурации:

prometheus.yml: конфигурация Prometheus для проверки доступности с помощью Blackbox Exporter.
blackbox.yml: конфигурация Blackbox Exporter для выполнения проверки по HTTP.

### 3. Конфигурация Prometheus (prometheus.yml)

В файле prometheus.yml в блоке scrape_configs указывается, где искать Blackbox Exporter и какие цели мониторить.

### 4. Конфигурация Blackbox Exporter (blackbox.yml)

В файле blackbox.yml определяется модуль http_2xx, который описывает, как Blackbox Exporter будет проверять доступность.

### 5. Запуск Prometheus и Blackbox Exporter

Запустите Prometheus и Blackbox Exporter в отдельных терминалах

```bash
# Запуск Blackbox Exporter (порт по умолчанию 9115)
./blackbox_exporter --config.file=blackbox.yml

# Запуск Prometheus
./prometheus --config.file=prometheus.yml

```

### 6. Просмотр метрик

После запуска Prometheus и Blackbox Exporter метрики можно просматривать через интерфейс Prometheus:

1. Перейдите в браузере по адресу <http://localhost:9090>, чтобы открыть интерфейс Prometheus.
2. Используйте запросы, например, probe_success, чтобы увидеть доступность цели, или probe_duration_seconds, чтобы проверить время отклика.

## Описание метрик

**probe_success**: бинарная метрика, где 1 указывает, что цель доступна, а 0 — что цель недоступна.
**probe_duration_seconds**: измеряет время, затраченное на проверку, и позволяет мониторить скорость отклика.
**probe_http_status_code**: код ответа HTTP, который позволяет видеть, например, успешные коды 2xx, а также ошибки 404, 500 и другие. Так можно анализировать есть ли проблемы, если да, то с какой части - серверной или клиентской.
