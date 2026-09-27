# Contribuir

Gracias por el interés. Es un proyecto pequeño a propósito: dos ficheros, sin dependencias, sin build. La idea es que cualquiera pueda abrirlo, entenderlo y cambiarlo en una tarde. Si vais a aportar algo, intentad que siga siendo así.

## Cómo montártelo en local

```bash
git clone https://github.com/Collanteslu/laya-jev-tester
cd laya-jev-tester
python3 server.py
```

Y abre <http://127.0.0.1:8899>. No hay más pasos: ni `pip install`, ni Node, ni nada que compilar.

Si solo quieres tocar estilos o el HTML, también puedes abrir el `index.html` directamente, pero recuerda que sin el proxy las llamadas a la API las bloquea el navegador (CORS), salvo que tu endpoint lo tenga habilitado.

## Qué tener en cuenta antes de tocar código

- **Cero dependencias**. Si tu cambio necesita un `pip install` o un CDN externo, probablemente no encaja aquí. Hablemos primero en un issue.
- **Todo en un fichero**. `index.html` lleva la interfaz, los estilos y la lógica juntos a propósito. No lo partas en módulos sin pasar antes por un issue comentándolo.
- **Español en la interfaz**, aunque el código (nombres de variables, funciones) va en inglés, como está ahora.
- La página tiene que funcionar en un navegador normal y corriente, sin flags ni extensiones.

## Cómo enviar un pull request

1. Abre primero un issue describiendo qué quieres cambiar y por qué (salvo que sea algo evidente: un typo, un color, un bug pequeño).
2. Haz fork, crea una rama con nombre descriptivo (`fix-barras-score`, `preset-moderacion`...) y commitea ahí.
3. Antes de abrir el PR, prueba tu cambio de verdad: arranca `server.py` y ejecuta una petición contra tu servidor de Laya.
4. Rellena la plantilla del PR: qué cambia, cómo probarlo, y una captura si tocas la interfaz.

Los PR que lleguen sin issue previo (cuando hace falta) o que no se puedan probar igual que arriba se pedirán con calma los cambios que falten. Nada de prisa.

## Reportar bugs

Abre un issue con la plantilla de bug. Lo que más ayuda: qué hiciste, qué esperabas, qué pasó, y qué respondió el servidor (el JSON crudo que se muestra abajo del todo en la página, con el token tapado si aparece).
