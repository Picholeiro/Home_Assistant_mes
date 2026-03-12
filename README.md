# 📅 Mes del Año — Integración para Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/Picholeiro/Home_Assistant_mes.svg)](https://github.com/Picholeiro/Home_Assistant_mes/releases)
![Mantenido](https://img.shields.io/maintenance/yes/2026.svg)

Integración custom para **Home Assistant** que expone un sensor con el **número y nombre del mes actual** del año, útil para automatizaciones estacionales o condicionales.

---

## ✨ Características

- 🔢 Devuelve el **número del mes** (1–12) como estado del sensor
- 🌍 Incluye el **nombre del mes en español e inglés** como atributos
- ♻️ Se actualiza automáticamente **cada hora** (detecta cambio de mes al instante)
- ⚡ Sin dependencias externas

---

## 📦 Instalación via HACS (recomendado)

1. Abre **HACS** en Home Assistant
2. Ve a **Integraciones** → menú de tres puntos → **Repositorios personalizados**
3. Añade la URL: `https://github.com/Picholeiro/Home_Assistant_mes`
4. Categoría: **Integración**
5. Busca `Mes del Año` y pulsa **Instalar**
6. Reinicia Home Assistant

---

## 🛠 Instalación manual

1. Copia la carpeta `custom_components/mes_del_ano/` a tu directorio `config/custom_components/`
2. Reinicia Home Assistant

---

## ⚙️ Configuración

Añade en tu `configuration.yaml`:

```yaml
sensor:
  - platform: mes_del_ano
    name: "Mes actual"
```

---

## 📊 Estado y Atributos del sensor

| Campo | Valor de ejemplo |
|---|---|
| **Estado** | `3` |
| `month_name` | `March` |
| `month_name_es` | `Marzo` |
| `month_number` | `3` |
| `year` | `2026` |

---

## 💡 Ejemplo de automatización

```yaml
automation:
  - alias: "Activar modo verano"
    trigger:
      - platform: state
        entity_id: sensor.mes_actual
    condition:
      - condition: template
        value_template: "{{ states('sensor.mes_actual') | int in [6, 7, 8] }}"
    action:
      - service: input_boolean.turn_on
        target:
          entity_id: input_boolean.modo_verano
```

---

## 📝 Licencia

MIT © [Picholeiro](https://github.com/Picholeiro)
