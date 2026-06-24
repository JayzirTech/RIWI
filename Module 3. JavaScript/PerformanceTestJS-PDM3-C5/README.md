# Guía para el README del Proyecto

> **Importante:** Este documento está escrito en español como guía para los coders. El archivo `README.md` que entreguen en su proyecto debe estar redactado completamente en inglés.

---

# Project Canvas

## Nombre sugerido del proyecto

**Workspace Reservation System SPA**

## Descripción general

Este proyecto consiste en desarrollar una Single Page Application (SPA) utilizando JavaScript, Vite, TailwindCSS y JSON Server.

La aplicación simula un sistema de reservas de espacios de trabajo donde los usuarios pueden autenticarse, navegar por rutas protegidas y gestionar información consumida desde una API simulada.

El objetivo principal es evaluar conocimientos relacionados con:

- Arquitectura SPA
- Autenticación
- Manejo de roles
- Protección de rutas
- Persistencia de sesión
- Consumo de APIs
- Manipulación del DOM
- Modularización del código
- Buenas prácticas de desarrollo

---

## Contexto del problema

Una empresa dispone de diferentes espacios de trabajo compartidos:

- Salas de reuniones
- Oficinas privadas
- Espacios de coworking
- Auditorios

Para evitar conflictos de horarios y mejorar la organización interna, se requiere una plataforma que permita administrar reservas de dichos espacios.

La aplicación debe contemplar dos roles:

### Administrador (admin)

Puede:

- Ver todas las reservas
- Crear reservas
- Editar reservas
- Eliminar reservas
- Aprobar o rechazar reservas
- Gestionar espacios de trabajo
- Acceder a módulos administrativos

### Usuario (user)

Puede:

- Consultar espacios disponibles
- Crear reservas
- Ver únicamente sus reservas
- Modificar reservas pendientes
- Cancelar sus propias reservas

---

## Tecnologías utilizadas

- JavaScript ES6+
- Vite
- TailwindCSS
- JSON Server
- Concurrently
- HTML5
- CSS3

---

## Estructura base entregada

```txt
src
├── assets
├── components
│   └── Sidebar.js
├── controllers
│   └── login.controller.js
├── router
│   └── router.js
├── views
│   ├── loginView.js
│   ├── homeView.js
│   └── notFound.js
├── utils.js
├── main.js
└── style.css
```

---

## Explicación de la arquitectura

### Components

Contiene componentes reutilizables de interfaz.

Ejemplo:

```txt
components/
└── Sidebar.js
```

El Sidebar puede reutilizarse en distintas vistas y centraliza la navegación principal del sistema.

### Controllers

Contienen la lógica de negocio y los eventos de la aplicación.

Ejemplo:

```txt
controllers/
└── login.controller.js
```

Responsabilidades:

- Capturar eventos del formulario
- Validar credenciales
- Consumir la API
- Gestionar el inicio de sesión
- Redireccionar usuarios

### Views

Representan las pantallas de la aplicación.

Actualmente:

- Login
- Home
- Not Found (404)

Cada vista retorna una plantilla HTML que es renderizada dinámicamente dentro del contenedor principal.

### Router

Administra la navegación interna de la SPA.

Responsabilidades:

- Renderizar vistas
- Gestionar rutas
- Proteger vistas privadas
- Redireccionar usuarios
- Mostrar páginas 404

### Utils

Contiene funciones auxiliares reutilizables.

Actualmente:

- Guardar sesión
- Obtener sesión
- Eliminar sesión
- Validar autenticación

---

## API simulada

La aplicación utiliza JSON Server para simular una API REST.

Ejemplo de usuario administrador:

```json
{
  "id": 1,
  "email": "admin@test.com",
  "password": "123456",
  "role": "admin"
}
```

Ejemplo de usuario estándar:

```json
{
  "id": 2,
  "email": "user@test.com",
  "password": "123456",
  "role": "user"
}
```

---

## Configuración del entorno

Instalar dependencias:

```bash
npm install
```

Ejecutar proyecto:

```bash
npm run dev
```

Este comando levanta simultáneamente:

- Vite
- JSON Server

gracias al uso de Concurrently.

---

## Scripts sugeridos

```json
{
  "scripts": {
    "client": "vite",
    "server": "json-server --watch db.json --port 3000",
    "dev": "concurrently \"npm run client\" \"npm run server\""
  }
}
```

---

## Credenciales de prueba

Administrador:

```txt
admin@test.com
A123456 
```

Usuario:

```txt
user@test.com
A123456
```

---

## Funcionalidades base incluidas

- Login funcional
- Consumo de API mediante JSON Server
- Persistencia de sesión con LocalStorage
- Logout
- Router SPA
- Protección básica de rutas
- Sidebar reutilizable
- Página 404 personalizada
- Configuración de TailwindCSS
- Configuración de Vite

---

## Módulos pendientes para desarrollar

Los coders deberán implementar:

- CRUD de reservas
- CRUD de espacios
- Gestión de roles
- Guards avanzados
- Validaciones de permisos
- Dashboard administrativo
- Estadísticas
- Filtros y búsquedas
- Notificaciones
- Reglas de negocio

---

## Nota para los coders

Aunque esta guía está escrita en español para facilitar la comprensión del proyecto, el archivo README.md entregado como evidencia debe estar redactado completamente en inglés.
