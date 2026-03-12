# Mes del Año

Sensor que devuelve el **número y nombre del mes actual** del año.

## Estado del sensor

El sensor devuelve un valor entre `1` (Enero) y `12` (Diciembre).

## Atributos disponibles

- `month_name` — Nombre del mes en inglés (ej. `March`)
- `month_name_es` — Nombre del mes en español (ej. `Marzo`)
- `month_number` — Número del mes (ej. `3`)
- `year` — Año actual (ej. `2026`)

## Configuración mínima en `configuration.yaml`

```yaml
sensor:
  - platform: mes_del_ano
    name: "Mes actual"
```
