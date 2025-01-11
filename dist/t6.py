# %% [markdown]
# ## Datos derivados:

# %%
import data_utils as du

# %%
# Crear una tabla combinada que una los datos de Historicos_Ordenes y Registros_Condiciones mediante el campo ID_Equipo en la tabla Resultados_join
fregistros_condiciones = '../data/Registros_Condiciones.csv'
dregistros_condiciones = du.read_csv(fregistros_condiciones)

fhistorico_ordenes = '../data/Historicos_Ordenes.csv'
dhistorico_ordenes = du.read_csv(fhistorico_ordenes)

# print(dregistros_condiciones )
# print(dhistorico_ordenes)


def group_by_position(data, position):
    new_data = {}

    for anElem in data:
        if (len(anElem) > position):
            clave = anElem[position]
            if clave not in new_data:
                new_data[clave] = []
            new_data[clave].append(anElem)

    return new_data


dregistros_condiciones_x_id_equipo = group_by_position(
    dregistros_condiciones[1], 0)
# print(dregistros_condiciones_x_id_equipo)

dhistorico_ordenes_x_id_equipo = group_by_position(dhistorico_ordenes[1], 1)
# print(dhistorico_ordenes_x_id_equipo)

# %%
def join_registros_ordenes(registros, ordenes):
    claves_registro = list(registros.keys())
    claves_ordenes = list(ordenes.keys())
    equipos = set(filter(None, claves_registro + claves_ordenes))
    # print(equipos)

    resultados_join_data = []

    for equipo in equipos:
        registros_x_equipo = registros[equipo]
        ordenes_x_equipo = ordenes[equipo]
        # print(len(registros_x_equipo), len(ordenes_x_equipo))

        for registro in registros_x_equipo:
            for orden in ordenes_x_equipo:
                resultado = {
                    'ID_Equipo': equipo,
                    'Fecha_Orden': orden[2],
                    'Tipo_Mantenimiento': orden[3],
                    'Costo_Mantenimiento': float(orden[5]),
                    'Ubicacion': orden[6],
                    'Fecha_Condicion': registro[1],
                    'Horas_Operativas': int(registro[2]),
                    'Temperatura_C': float(registro[3]),
                    'Vibracion_mm_s': float(registro[4]),
                    'Presion_Bar': float(registro[5]),
                    'Horas_Acumuladas': int(registro[6])
                }

                resultados_join_data.append(resultado)

    return resultados_join_data


resultados_join = join_registros_ordenes(dregistros_condiciones_x_id_equipo, dhistorico_ordenes_x_id_equipo)

# print('resultados_join:', len(resultados_join) ,resultados_join[:100])

# %%
def insert_join(registro):
    sql = """INSERT INTO Resultados_Join (ID_Equipo, Fecha_Orden, Tipo_Mantenimiento, Costo_Mantenimiento, Ubicacion, Fecha_Condicion, Horas_Operativas, Temperatura_C, Vibracion_mm_s, Presion_Bar, Horas_Acumuladas) 
    VALUES ('{0}', '{1}', '{2}', {3}, '{4}', '{5}', {6}, {7}, {8}, {9}, {10})""".format(registro['ID_Equipo'],
                                                                              registro['Fecha_Orden'],
                                                                              registro['Tipo_Mantenimiento'],
                                                                              registro['Costo_Mantenimiento'],
                                                                              registro['Ubicacion'],
                                                                              registro['Fecha_Condicion'],
                                                                              registro['Horas_Operativas'],
                                                                              registro['Temperatura_C'],
                                                                              registro['Vibracion_mm_s'],
                                                                              registro['Presion_Bar'],
                                                                              registro['Horas_Acumuladas'])

    du.insert_data_sql(sql)

# Insertamos los 100 primeros registros
for resultado in resultados_join[0:100]:
    insert_join(resultado)


print("REGISTROS INSERTADOS!!")


