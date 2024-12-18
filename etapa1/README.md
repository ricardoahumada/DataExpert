### Reto: **"Construyendo las bases del mantenimiento predictivo"**

#### **Objetivo General**  
Trabajar en equipo para explorar y manipular los datos del entorno de mantenimiento de una planta energética usando Python y SQL. El equipo debe aplicar operaciones básicas para extraer métricas iniciales que permitan entender la frecuencia de mantenimiento, la duración promedio de vida útil de los equipos y las condiciones operativas clave. 

El resultado final será un conjunto de datos enriquecido, listo para la siguiente fase.


#### **Tareas del Reto:**
1. **Carga de datos:**
   - Importar los datasets `Historicos_Ordenes.csv`, `Caracteristicas_Equipos.csv`, y `Registros_Condiciones.csv` usando Python (en memoria).
   - Crear nueva base de datos "data_powergen":
      - Crear tabla de base de datos para datos de mantenimiento (Historicos_Ordenes). Carga los datos Historicos_Ordenes en la tabla correspondiente.
      - Crear tabla de base de datos para generar información combinada (Resultados_join).

2. **Filtrado y agrupamiento:**
   - Contar el número total de órdenes de mantenimiento realizadas para cada equipo (`ID_Equipo`).
   - Calcular la duración promedio de vida útil de los equipos en el dataset `Caracteristicas_Equipos.csv`.
   - Filtrar las órdenes de trabajo para identificar las de tipo "Correctivo" y calcular el costo promedio de estas.

3. **Resúmenes básicos:**
   - Encontrar el equipo con el mayor número de fallos (mantenimiento correctivo).
   - Generar un resumen básico de las temperaturas promedio y máximas registradas para cada equipo.

4. **Consultas básicas:**
   - Listar todas las órdenes de mantenimiento correctivo para un equipo específico, junto con sus costos y tiempos de reparación.
   - Extraer los registros operativos para los días en los que la vibración superó los 3.0 mm/s y la temperatura fue mayor a 60 °C.

5. **Agregaciones y métricas:**
   - Calcular el tiempo promedio entre mantenimientos para cada equipo.
   - Determinar la suma total de horas acumuladas (`Horas_Acumuladas`) por equipo.

6. **Joins y combinaciones:**
   - Crear una tabla combinada que junte los datos de `Historicos_Ordenes` y `Registros_Condiciones` mediante el campo `ID_Equipo`. Esta tabla debe incluir:
     - Número total de órdenes de mantenimiento por equipo.
     - Promedio de condiciones operativas (temperatura, vibración, presión) de cada equipo.

7. **Exporta la tabla derivada:**
   - Exporta la tabla derivada a csv usando Python

Todas las soluciones en Python deben implementarse mediante funciones. Las funciones deben invocarse al final para ejecutar el proceso deseado.

#### **Trabajo en equipo:**  
   - Usar un repositorio común:
      - Un integrante invita a los demás a su repositorio.
      - El resto clona el repositorio compartido
   - Trabajo por pares:
      - Recomendable aboradar las tareas por pares.
   - Dividir las tareas (ejemplo):
      - Tareas relacionadas con los `Historicos_Ordenes.csv`.
      - `Registros_Condiciones.csv` y `Caracteristicas_Equipos.csv`.
      - Consultas básicas y de agregación.
      - Joins y la creación del dataset combinado.

#### **Entregables:**
- Repositorio con los módulos de Python.


### **Duración y Evaluación**
1. **Duración:**  
   - 3 horas


3. **Criterios de Evaluación:**  
   - **Funcionalidad:** Código y consultas sin errores.  
   - **Resultados:** Respuestas correctas a las preguntas planteadas.  
   - **Colaboración:** División clara del trabajo y buena integración de los resultados.


### **Resultados Esperados**
Al finalizar el reto, los participantes habrán logrado:
1. Identificar patrones básicos de mantenimiento y condiciones operativas.
2. Construir un conjunto de datos combinado con métricas clave sobre los equipos.
3. Estar listos para pasar a una etapa más avanzada de modelado y análisis predictivo.