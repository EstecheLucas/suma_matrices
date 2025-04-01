🚀 Cómo ejecutar los servidores
1️⃣ Servidor en Node.js
Este servidor usa el módulo http de Node.js para servir archivos estáticos desde la carpeta public.

Pasos para ejecutar:
Asegúrate de tener Node.js instalado. Puedes verificar con:


Copiar
Editar
node -v
Guarda el archivo como server.js en tu proyecto.

Abre una terminal y ejecuta:


Copiar
Editar
node server.js
El servidor se ejecutará en http://localhost:4500/.

Si quieres detenerlo, presiona CTRL + C en la terminal.

2️⃣ Aplicación en Flask (Python)
Esta app web en Flask renderiza páginas HTML y maneja peticiones.

Pasos para ejecutar:
Asegúrate de tener Python 3 instalado. Puedes verificar con:


Copiar
Editar
python --version
Instala Flask si no lo tienes:


Copiar
Editar
pip install flask
Guarda el archivo como app.py.

En la terminal, ejecuta:


Copiar
Editar
python app.py
El servidor se ejecutará en http://127.0.0.1:5000/.

Para detenerlo, presiona CTRL + C en la terminal.

📌 Notas
El servidor de Node.js sirve archivos desde la carpeta public.

La aplicación en Flask busca archivos en una carpeta templates/.

Si tienes dudas, dime. 🚀
