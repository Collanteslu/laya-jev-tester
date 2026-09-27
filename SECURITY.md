# Seguridad

Es una herramienta de pruebas que corre en tu máquina (`127.0.0.1`) y no guarda datos en ningún servidor. Aun así, si encuentras algo que no debería estar ahí:

- **No abras un issue público** con detalles de un fallo de seguridad.
- Usa el aviso privado de seguridad del repositorio: pestaña **Security → Report a vulnerability**.

Ten en cuenta a la hora de reportar:

- El Bearer token se guarda en el `localStorage` del navegador por comodidad. Es un comportamiento intencionado y está documentado en el README; si eso no encaja con tu entorno, simplemente borra el campo antes de recargar.
- `server.py` solo escucha en localhost. Si alguien lo expone a la red, el proxy reenviaría peticiones con el token que le lleguen: eso no es un uso previsto.
