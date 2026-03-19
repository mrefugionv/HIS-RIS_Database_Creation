# EDA - Analisis exploratorio
- ¿que campos tengo?
- ¿que tipo de datos tengo? (char, str, int, float, datetime, list, )
- ¿son coherentes con la información que tengo? (ex. id-str,no operaciones matematica, o edad en entero no float)
- ¿Todos estan standarizados (mismo formato en títulos de campos y registros)? - ex. str todos mayusculas o minusculas o tipo oración. espacios, guiones bajos, etc...

# Preporcesamiento
- ¿hay valores duplicados? - 
  * Explicitos - Asegurate que sea exactamente el mismo registro en todos los campos (sino tal vez solo sea info parecida del paciente)
  * Implicitos - En un campo que una misma opción se escriba diferente (hip, hop, hip-hop...)
- ¿hay valores auscentes? ¿que proporción? ¿los campos en los que hay auscentes son cruciales para la investigación?
- ¿por que hay esas incosistencias? - entre sistemas 
- ¿como podemos menejarla información faltante?
   * No cruciales - rellenar con valor prefdetrminado como 'unknown' o 0.
   * Afectan - buscar las razones por las cuales hay datos ausentes e intentar recuperarlos.
* Sort values-  maximo, minimo, 
* describe - media, mediana, moda, desviacon estandar, min, max

# Procesamiento
 * merge tables
 * Pivotaje de tablas
     pivot_calls = calls.pivot_table (  #Utilizamos tablas dinámicas para agrupar
index = 'user_id',                 #User id sera el indice que correpoonde a los valores de las filas     
columns = 'call_month',            # Queremos una columna por cada mes del año
values = 'id',                     # En cada celda queremos que se coloque el número de llamada que hizo ...
aggfunc = 'count'                  #... el usuario ese mes por eso contamos el numero de id de llamadas
)

 * Agrupación de cohortes -
 * Matriz de correlación 


# Visualización
 * barras
 * histogramas -   Medias , medianas, valores atipicos...
 * lineas
 * scatter /dispersion
 * circulo /pastel
 * heatmaps



# Conclusiones - o Pruebas de hipotesis stadísticas 
  * medias, medianas, 
 * caja bigotes, campana de Gauss..
 * Pruebas estadísticas como -  taylor test, tstudent , levene

 * KPIS :
  - LTV Valor del ciclo de vida del cliente
  - CAC Costo de adquisición de clientes
  - ROMI = LTV / CAC
* Pruebas A/B
  -  ICE = (Impacto * Confinza) / Esfuerzo
* Embudos

* Matricas acumuladas  - para evitar peeking 
* Valores atipicos, percentiles 5%


# Machine learning
 * clustering , dendograma