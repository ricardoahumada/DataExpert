# %% [markdown]
# ## Agregaciones y métricas:

# %%
import data_utils as du

# %%
# Calcular el tiempo promedio entre mantenimientos para cada equipo.
import statistics as st


def obtener_mantenimiento_x_equipos():

    SQL = "SELECT id_equipo, fecha FROM historicos_ordenes ORDER BY id_equipo ASC,  fecha ASC"
    data = du.get_data_for_sql(SQL)

    grouped_data = {}

    for id_eq, fecha in data:
        if id_eq not in grouped_data: grouped_data[id_eq] = []

        grouped_data[id_eq].append(fecha)

    return grouped_data


def calcula_promedio_entre_mantenimientos(fechas_mantenimiento):
    new_data = {}

    for id_eq, fechas in fechas_mantenimiento.items():
        restas = [f2 - f1 for f1, f2 in zip(fechas, fechas[1:])]
        restas_int = list(map(lambda aF:aF.days, restas))
        # print(id_eq, st.mean(restas_int))
        new_data[id_eq] = round(st.mean(restas_int),2)

    return new_data

equipos_y_fechas = obtener_mantenimiento_x_equipos()

promedio_entre_mantenimientos = calcula_promedio_entre_mantenimientos(equipos_y_fechas)

print('Tiempo promedio entre mantenimientos para cada equipo (en días):\n {0}'.format(promedio_entre_mantenimientos))

# %%
# Determinar la suma total de horas acumuladas (Horas_Acumuladas) por equipo.

import statistics as st

fregistro = '../data/Registros_Condiciones.csv'
dregistro = du.read_csv(fregistro)
# print(dregistro)


def obtener_horas_acumuladas_x_equipo(registros):
    new_data = {}

    for registro in registros:
        id_eq = registro[0]
        if len(registro) >= 7:
            if id_eq not in new_data:
                new_data[id_eq] = 0

            new_data[id_eq] += int(registro[6])

    return new_data


horas_acumuladas_x_equipo = obtener_horas_acumuladas_x_equipo(dregistro[1])

print('Suma total de horas acumuladas (Horas_Acumuladas) por equipo.:\n {0}'.format(horas_acumuladas_x_equipo))




