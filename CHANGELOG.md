# Changelog

Todo lo notable de este proyecto, con el formato más cercano a [Keep a Changelog](https://keepachangelog.com/es/1.1.0/).

## [0.2.1] - 2026-09-27

### Añadido

- `Dockerfile` (python:3.12-alpine, usuario no root, healthcheck) y `docker-compose.yml` para levantar el tester en un contenedor.
- `server.py` acepta `HOST` y `PORT` por entorno (`127.0.0.1:8899` por defecto; la imagen usa `0.0.0.0:8899`).
- Sección «Con Docker» en los README (es/en).

### Cambiado

- La tarjeta **Petición JSON** (Run + copiar curl) sube al principio de la columna 2, siempre visible sin bajar.
- Las barras de `score` muestran el número de nivel **y** su texto (del formulario o del `legend` de la respuesta).
- Presets bilingües: cuerpo, claves, instructions y criteria en el idioma activo; al cambiar ES/EN el contenido cargado que coincide con un preset se re-localiza (el texto personalizado no se toca).
- Placeholders y altas nuevas localizados (`question_1`, `low/medium/high`, `yes/no`…).

## [0.2.0] - 2026-09-27

### Añadido

- Modelo `jev-1.13-free` (OpenCode Zen) en el selector de checkpoint: el tester ya puede apuntar también a `https://opencode.ai/zen/v1/systemone`.
- Al elegir `jev-1.13-free` la URL de Zen se rellena sola (si estaba vacía), el campo de Bearer se desactiva y la petición sale sin cabecera `Authorization` (esa API es anónima).
- Cabeceras HTTP extra configurables desde la página (proxy, modo directo y `curl` incluidos).
- Sección «Probar Jev gratis (OpenCode Zen)» en los README (es/en).

### Corregido

- El proxy manda un `User-Agent` de navegador: Cloudflare bloqueaba las peticiones de urllib con error 1010.

## [0.1.0] - 2026-09-27

Primera versión publicada.

### Añadido

- Página de pruebas para endpoints `laya-serve` (`POST /v1/systemone`), en HTML/CSS/JS puro sin dependencias.
- Builder de preguntas con los tres tipos del modelo: `choice`, `score` y `noul`, con edición de criterios y niveles.
- Cuatro presets listos para usar: soporte, triaje completo, guardrail y router de modelos.
- Resultados visuales: barras de probabilidad con la opción ganadora destacada, escala con aguja y distribución por nivel para `score`, medidor sí/no para `noul`, badges de `confidence` y `answer_confidence`.
- Metadatos de ejecución: estado HTTP, latencia total e inferencia (`X-Inference-Time-Ms`), checkpoint usado, motivo del routing y tokens consumidos.
- Selector de checkpoint (`auto`, `english`, `multilingual`, `typed-decisions`) y modo JSON a mano para editar el payload completo.
- Servidor local en Python estándar con proxy `POST /proxy` para saltarse el CORS, escuchando solo en `127.0.0.1`.
- Copiar la petición como `curl` e historial de las últimas 10 ejecuciones.
- Token Bearer persistido en `localStorage` (solo en el navegador).
