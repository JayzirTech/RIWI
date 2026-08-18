# Ejercicio 1 — Finanzas
Dataset: `1_finanzas.csv`

**Contexto:** Eres el/la analista financiero de la empresa. El equipo
contable exportó las transacciones del último trimestre desde tres
sistemas distintos, por eso el archivo llegó con inconsistencias.
Antes de responder cualquier pregunta del gerente financiero, necesitas
dejar los datos confiables.

---

## Preguntas de negocio

1. **El gerente financiero pregunta:** "¿Podemos confiar en este
   reporte?" Antes de analizar nada, identifica cuántas transacciones
   están incompletas (con nulos) y cuántas están repetidas por error de
   carga (duplicadas). Elimínalas.

2. Algunas transacciones muestran el monto como texto con símbolo de
   pesos (ej. `"$1,001,829"`), lo que impide sumarlas. Corrige la
   columna `monto` para que todos los valores sean numéricos y se
   puedan sumar correctamente.

3. Contabilidad reporta que la misma cuenta bancaria aparece escrita de
   varias formas ("BANCO BOGOTÁ", "Banco Bogotá ", "Banco Bogotá").
   Unifica los nombres de cuenta para que el reporte por banco no esté
   inflado artificialmente en varias filas.

4. Se detectó una transacción con monto negativo que no corresponde a
   ningún gasto real (fue un error de digitación). Encuéntrala y
   corrígela para que no distorsione el balance.

5. **Pregunta del gerente:** "¿Cuál fue el total de ingresos y el total
   de gastos de la empresa?" Calcula ambos valores.

6. **Pregunta del gerente:** "¿Cuál es nuestro balance neto (ingresos -
   gastos)?" Calcúlalo con los datos ya limpios.

7. El área de compras quiere saber en qué categorías se concentra el
   gasto. Calcula el gasto total por `categoria`, ordenado de mayor a
   menor, y di cuál es la categoría más costosa.

8. Finanzas quiere estandarizar los métodos de pago para negociar mejores
   tarifas bancarias. ¿Qué porcentaje de las transacciones se hicieron
   por transferencia vs. efectivo vs. tarjeta? (rellena antes los nulos
   de `metodo_pago` con `'No especificado'`).

9. El gerente quiere ver la tendencia: ¿cuál fue el balance neto por
   mes? Convierte `fecha` a datetime (hay formatos mixtos) y agrupa por
   mes.

10. Para la auditoría anual, identifica las 5 transacciones de mayor
    monto de todo el trimestre y en qué cuenta se registraron. ¿Hay
    algo que te parezca sospechoso o que valga la pena revisar?

---
*Tip: guarda el resultado limpio con
`df.to_csv('finanzas_limpio.csv', index=False)` para dejarlo listo
como respaldo del reporte.*
