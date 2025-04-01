// Servidor mínimo con Node.js
const http = require('http'); // Importar el modulo http
const fs = require('fs'); // Importar el modulo fs para leer y servvir archivos
const path = require('path'); // Importar el modulo path para manejos de rutas de archivos

// Crear servidor
const server = http.createServer((req, res) => { // Función que se ejecuta cuando se recibe una petición
  console.log(`Petición: ${req.url}`);// Muestra en la consola la petición
 
  // Determinar qué archivo servir
  let filePath; // Variable para almacenar la ruta del archivo
  if (req.url === '/' || req.url === '') { 
    filePath = path.join(__dirname, 'public', 'index.html'); // Ruta del archivo de inicio
  } else {
    filePath = path.join(__dirname, 'public', req.url); // Ruta del archivo solicitado
  }
 
  // Leer y servir el archivo
  fs.readFile(filePath, (err, content) => { // Función que se ejecuta cuando se lee el archivo
    res.writeHead(200, { 'Content-Type': 'text/html' }); // Encabezado de la petición
    res.end(content); // Enviar el contenido del archivo
  });
});

// Iniciar servidor
const PORT = 4500;
server.listen(PORT, '0.0.0.0',  () => {
  console.log(`Servidor iniciado en puerto ${PORT}`);
});