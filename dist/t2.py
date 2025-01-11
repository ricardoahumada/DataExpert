# %% [markdown]
# ## Filtrado y agrupamiento:

# %%
import data_utils as du

# %%
# Contar el número total de órdenes de mantenimiento realizadas para cada equipo (ID_Equipo).
fhistorico = '../data/Historicos_Ordenes.csv'
dhistorico = du.read_csv(fhistorico)
# print(dhistorico)


def contar_ordenes_por_equipo(data, t_mant):
    if not data:
        return None

    mant_x_equipo = {}

    for row in data:
        if len(row) > 1:
            equipo = row[1]
            tipo_mant = row[3]
            if tipo_mant == t_mant:
                if equipo not in mant_x_equipo:
                    mant_x_equipo[equipo] = 0

                mant_x_equipo[equipo] += 1

    return mant_x_equipo


contar_ordenes_por_equipo(dhistorico[1], 'Correctivo')

# %%
# Calcular la duración promedio de vida útil de los equipos en el dataset Caracteristicas_Equipos.csv.

import statistics as st

fcaract = '../data/Caracteristicas_Equipos.csv'
dcaract = du.read_csv(fcaract)

vida_util = map(lambda aD:int(aD[4]),dcaract[1])

promedio_vida_util = st.mean(vida_util)
print('El promedio de vida útil de equipos es: {0}'.format(promedio_vida_util) )






# %%
# Filtrar las órdenes de trabajo para identificar las de tipo "Correctivo" y calcular el costo promedio de estas.

import statistics as st


SQL = "SELECT costo_mantenimiento FROM historicos_ordenes WHERE tipo_mantenimiento='Correctivo'"

dhistorico_correctivo = du.get_data_for_sql(SQL)

costo_correctivo = map(lambda aD: aD[0], dhistorico_correctivo)

promedio_costo_correctivo = round(st.mean(costo_correctivo), 2)


print('El coste promoedio de ordenes de tipo correctivo es: {0}'.format(promedio_costo_correctivo))


