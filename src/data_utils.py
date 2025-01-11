# %% [markdown]
# ## LEER DATOS DE DISTINTAS FUENTES

# %% [markdown]
# ### CSVS

# %%
import my_sql_module as msm
import os
import sys

# %%


def read_csv(file_path):
    head = None
    data = None
    try:
        texto = open(file_path, 'r').read()
        filas = texto.split('\n')
        head = list(map(lambda aF: tuple(aF.split(',')), filas[:1]))
        data = list(map(lambda aF: tuple(aF.split(',')), filas[1:]))

    except Exception as err:
        print('problema con acceso al archivo', err)

    return head, data

# %%
# caract = '../data/Caracteristicas_Equipos.csv'
# print(read_csv(caract))

# # %%
# historico = '../data/Historicos_Ordenes.csv'
# print(read_csv(historico))

# # %%
# registro = '../data/Registros_Condiciones.csv'
# print(read_csv(registro))

# %% [markdown]
# ### BBDD


# %%

# Do not expose your Neon credentials to the browser

PGHOST = 'ep-super-meadow-a2w5lasv.eu-central-1.aws.neon.tech'
PGDATABASE = 'data_powergen'
PGUSER = 'datafundamentasl_owner'
PGPASSWORD = 'yPDtEpT5R6mI'

# %%


def get_data_for_sql(sql):

    if not sql:
        return None

    conn = None
    cur = None

    data = None

    # print('SQL:', sql)

    try:
        conn = msm.create_server_connection(
            PGHOST, PGDATABASE, PGUSER, PGPASSWORD)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return data


# resultado = get_data_for_sql('SELECT * FROM historicos_ordenes LIMIT 10')
# print(resultado[1:10])


def insert_data_sql(sql):
    if not sql:
        return None

    conn = None
    cur = None

    # print('SQL:', sql)

    try:
        conn = msm.create_server_connection(
            PGHOST, PGDATABASE, PGUSER, PGPASSWORD)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as err:
        print(f"Error: '{err}'")
        conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return True