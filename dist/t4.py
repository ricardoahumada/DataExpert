# %% [markdown]
# ## Consultas básicas:

# %%
import data_utils as du

# %%
# Listar todas las órdenes de mantenimiento correctivo para un equipo específico, junto con sus costos y tiempos de reparación.

def obtener_correctivo_x_equipo(id_equipo):
    SQL = "SELECT id_orden, tiempo_reparacion_horas, costo_mantenimiento FROM historicos_ordenes WHERE id_equipo = '{0}' AND tipo_mantenimiento='Correctivo'".format(id_equipo)
    correctivo_x_equipo = du.get_data_for_sql(SQL)
    return correctivo_x_equipo

id_equipo='E016'

ordenes = obtener_correctivo_x_equipo(id_equipo)

print('Órdenes de mantenimiento correctivo para {0}:\n {1}'.format(id_equipo, ordenes))

# %%
# Extraer los registros operativos para los días en los que la vibración superó los 3.0 mm/s y la temperatura fue mayor a 60 °C.

import statistics as st

fregistro = '../data/Registros_Condiciones.csv'
dregistro = du.read_csv(fregistro)
# print(dregistro)


def obtener_registros_x_condiciones(registros):
    new_data = []

    for registro in registros:
        if len(registro) >= 5:
            vib = registro[4]
            temp = registro[3]

            if float(vib)>=3 and float(temp) > 60:
                new_data.append(registro)

    return new_data


registros_x_condiciones = obtener_registros_x_condiciones(dregistro[1])

print('registros operativos para los días en los que la vibración superó los 3.0 mm/s y la temperatura fue mayor a 60 °C:\n {0}'.format(registros_x_condiciones))




