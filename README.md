# 📅 Mes del Año — Integración para Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/Picholeiro/Home_Assistant_mes.svg)](https://github.com/Picholeiro/Home_Assistant_mes/releases)
![Mantenido](https://img.shields.io/maintenance/yes/2026.svg)

Integración custom para **Home Assistant** que expone un sensor con el **nombre del mes actual** como estado, permitiendo automatizaciones sencillas con `condition: state`, al estilo de los sensores de fecha nativos de HA.

---

## ✨ Características

- 🗓️ Devuelve el **nombre del mes en inglés** (`january` … `december`) como estado del sensor
- 🌍 Incluye el **nombre en español** y el **número de mes** como atributos
- ♻️ Se actualiza automáticamente **cada hora** (detecta el cambio de mes de forma inmediata)
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

Puedes añadirlo desde la UI de Home Assistant (**Ajustes → Dispositivos y servicios → Añadir integración → Mes del Año**) o en `configuration.yaml`:

```yaml
sensor:
  - platform: mes_del_ano
    name: "Mes actual"
```

---

## 📊 Estado y Atributos del sensor

El **estado** (`state`) del sensor es el nombre del mes en inglés en minúsculas:

| Mes | Estado |
|-----|--------|
| Enero | `enero` |
| Febrero | `febrero` |
| Marzo | `marzo` |
| Abril | `abril` |
| Mayo | `mayo` |
| Junio | `junio` |
| Julio | `julio` |
| Agosto | `agosto` |
| Septiembre | `septiembre` |
| Octubre | `octubre` |
| Noviembre | `noviembre` |
| Diciembre | `diciembre` |

### Atributos adicionales

| Atributo | Valor de ejemplo |
|---|---|
| `month_name_es` | `Marzo` |
| `month_number` | `3` |
| `year` | `2026` |

---

## 💡 Ejemplos de automatización

### Condición simple por nombre de mes

```yaml
automation:
  - alias: "Activar modo verano"
    trigger:
      - platform: state
        entity_id: sensor.mes_actual
        to: "junio"
    action:
      - service: input_boolean.turn_on
        target:
          entity_id: input_boolean.modo_verano
```

### Condición con varios meses usando `condition: state`

```yaml
condition:
  - condition: state
    entity_id: sensor.mes_actual
    state:
      - junio
      - julio
      - agosto
```

### Varios meses con template

```yaml
condition:
  - condition: template
    value_template: >
      {{ states('sensor.mes_actual') in ['junio', 'julio', 'agosto'] }}
```

### Notificación de inicio de mes

```yaml
automation:
  - alias: "Aviso inicio de mes"
    trigger:
      - platform: state
        entity_id: sensor.mes_actual
    action:
      - service: notify.mobile_app
        data:
          message: "¡Empieza {{ states('sensor.mes_actual') | capitalize }}!"
```

---

## 📝 Changelog

### v1.1.4
- ✨ **Mejora**: Añadido `device_class: enum` y `options` al sensor. Ahora al crear automatizaciones en la interfaz gráfica, Home Assistant **te mostrará un menú desplegable** para seleccionar los meses en lugar de tener que escribirlos a mano.

### v1.1.3
- 🇪🇸 **Cambio**: el estado del sensor ahora es el nombre del mes en **español** en minúsculas (`enero` … `diciembre`), facilitando el uso de `condition: state` en español directamente.

### v1.1.2
- 🔧 Correcciones menores y optimizaciones de estructura.

### v1.1.1
- ⬆️ **Actualización**: Se sube el requisito mínimo de Home Assistant a la versión `2026.2.0`.

### v1.1.0
- 🔄 **Cambio importante**: el estado del sensor ahora es el nombre del mes en inglés en minúsculas (`january` … `december`) en lugar del número (1–12), facilitando el uso de `condition: state` directamente.
- Se elimina el atributo `month_name` (redundante con el estado). Se mantienen `month_name_es`, `month_number` e `year`.

### v1.0.0
- Versión inicial. Estado numérico (1–12).

---

## 📝 Licencia

MIT © [Picholeiro](https://github.com/Picholeiro)
