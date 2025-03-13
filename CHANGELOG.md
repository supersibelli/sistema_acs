# Changelog
Todas las modificaciones notables del proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2024-03-11

### Adicionado
- Configuración inicial del proyecto Flask
- Sistema de autenticación básico
- Estructura de directorios del proyecto
- Integración de Bootstrap 5 y Font Awesome
- Página de inicio con diseño responsivo
- Menú principal con 3 tipos de formularios
- Sistema de mensajes flash

### Técnico
- Configuración de SQLite para desarrollo
- Implementación de Flask-Login
- Estructura MVC básica
- Sistema de templates con Jinja2

## [0.1.0] - 2024-04-12

### Adicionado
- Implementación inicial del formulario de Cadastro Individual
- Sección "Identificação do Cidadão" con campos básicos
- Validaciones en cliente y servidor para todos los campos
- Sistema de manejo de errores en portugués
- Campos condicionales basados en selecciones del usuario

### Modificado
- Cambio del título de sección de "Identificação do Usuário/Cidadão" a "Identificação do Cidadão"

### Corregido
- Validación de campos de padres cuando están marcados como desconocidos
- Manejo de campos condicionales según nacionalidad
- Limpieza automática de campos no aplicables

### Técnico
- Implementación de validaciones de fechas en formato DD/MM/AAAA
- Mejora en el manejo de errores y mensajes del servidor
- Optimización de la lógica de validación en JavaScript 