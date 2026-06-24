"""
Simulador de Cajero Automá1co – v2

Contexto del Proyecto

Una entidad financiera llamada TechBank Riwi Digital desea lanzar una versión de
prueba de su nuevo cajero automático en consola como parte de un programa de
formación interna para nuevos desarrolladores.

El objetivo es construir un sistema funcional que simule operaciones básicas de un cajero
automático, respetando reglas de negocio simples pero con validaciones sólidas.

Criterios de Aceptación
1. El sistema debe iniciar con un saldo fijo de $1000.
2. El usuario debe autenticarse con un PIN.
3. Debe existir un límite de intentos de autenticación.
4. El sistema debe permitir:
o Consultar saldo
o Retirar dinero
o Depositar dinero
o Salir
5. No se deben permitir montos negativos.
6. No se deben permitir retiros mayores al saldo disponible.
7. El sistema no debe romperse ante entradas inválidas.
8. Al finalizar, debe mostrarse un mensaje de despedida.
9. El sistema debe ejecutarse completamente desde un archivo principal llamado
main.py.
 
Distribución Funcional
Cada equipo deberá dividir el trabajo en 12 responsabilidades funcionales.
Sugerencia de áreas a cubrir:
1. Configuración inicial del sistema
2. Autenticación
3. Control de intentos
4. Gestión de saldo
5. Lógica de retiro
6. Lógica de depósito
7. Validación de entradas numéricas
8. Validación de reglas de negocio
9. Menú interactivo
10. Registro o historial simple de operaciones
11. Funciones auxiliares
12. Integración general y orquestación (Líder)

Cada integrante debe ser responsable de una funcionalidad concreta.

Flujo Esperado del Sistema
1. Mostrar mensaje de bienvenida.
2. Solicitar autenticación.
3. Validar intentos.
4. Permitir al usuario indicar cuántas operaciones desea realizar.
5. Mostrar menú por cada operación.
6. Ejecutar acción seleccionada.
7. Validar reglas de negocio.
8. Finalizar cuando se completen las operaciones o el usuario decida salir.
9. Mostrar mensaje final:
"Gracias por usar el cajero automático"

Operaciones opcionales
• Agregar límite diario de retiro
• Agregar contador de operaciones exitosas
• Mostrar resumen final de sesión
• Implementar bloqueo definitivo tras 3 intentos fallidos

Entregable Final
• Repositorio funcional en Azure DevOps
• Código ejecutable desde main.py
• Sin errores en ejecución
• Todas las tareas cerradas en Boards
"""
from configuracion_inicial import Mensaje_Bienvenida
from autenticacion import Autenticacion

Mensaje_Bienvenida()
Autenticacion()