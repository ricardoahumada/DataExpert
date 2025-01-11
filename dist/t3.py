# %% [markdown]
# ## Resúmenes básicos:

# %%
import data_utils as du

# %%
# Encontrar el equipo con el mayor número de fallos (mantenimiento correctivo).



def obtener_fallos_por_equipo():

    SQL = "SELECT id_equipo, COUNT(id_equipo) AS num_ap FROM historicos_ordenes WHERE tipo_mantenimiento='Correctivo' GROUP BY id_equipo ORDER BY  num_ap"

    d_num_equipo_correctivo = du.get_data_for_sql(SQL)
    # print(d_num_equipo_correctivo)
    return d_num_equipo_correctivo[0][0]


def obtener_datos_de_equipo(id_e):
    fcaract = '../data/Caracteristicas_Equipos.csv'
    dcaract = du.read_csv(fcaract)
    dequipo = tuple(filter(lambda aE: aE[0] == id_e, dcaract[1]))
    # print(dcaract[0][0], dequipo[0])
    data = dict(zip(dcaract[0][0],dequipo[0]))
    # print(data)
    return data


id_equipo = obtener_fallos_por_equipo()

equipo = obtener_datos_de_equipo(id_equipo)

print('El equipo con  más fallos es: {0}'.format(equipo))

# %%
# Generar un resumen básico de las temperaturas promedio y máximas registradas para cada equipo.

import statistics as st

fregistro = '../data/Registros_Condiciones.csv'
dregistro = du.read_csv(fregistro)
# print(dregistro)


def obtener_temperaturas_por_equipo(registros):
    new_data = {}

    for registro in registros:
        if len(registro) >= 4:
            id_e = registro[0]
            temp = registro[3]

            if id_e not in new_data:
                new_data[id_e] = []

        new_data[id_e].append(temp)

    return new_data


def obtener_promedio_y_maximo_por_equipo(data_temps_x_equipo):
    new_data = {}

    for eq_id,eq_temps in data_temps_x_equipo.items():
        media = st.mean(map(lambda aT:float(aT), eq_temps))
        maximo = max(eq_temps)
        new_data[eq_id]={'maximo':maximo, 'media': round(media,2)}

    return new_data


temperaturas_x_equipo = obtener_temperaturas_por_equipo(dregistro[1])

max_meida_x_equipo = obtener_promedio_y_maximo_por_equipo(temperaturas_x_equipo)

print('Resumen básico: {0}'.format(max_meida_x_equipo))




