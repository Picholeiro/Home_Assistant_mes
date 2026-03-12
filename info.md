# Mes del Año

Sensor que devuelve el **nombre del mes actual** en inglés como estado, ideal para automatizaciones sencillas con `condition: state`.

## Estado del sensor

El estado es el nombre del mes en inglés en minúsculas:

| Mes | Estado |
|-----|--------|
| Enero | `january` |
| Febrero | `february` |
| Marzo | `march` |
| ... | ... |
| Diciembre | `december` |

## Atributos disponibles

- `month_name_es` — Nombre del mes en español (ej. `Marzo`)
- `month_number` — Número del mes (ej. `3`)
- `year` — Año actual (ej. `2026`)

## Configuración mínima en `configuration.yaml`

```yaml
sensor:
  - platform: mes_del_ano
    name: "Mes actual"
```
