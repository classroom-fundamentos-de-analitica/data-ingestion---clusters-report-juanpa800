"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():

    file = open('clusters_report.txt','r')
    columnas = file.readline()
    columnas = columnas.split(' ')
    columnas2 = [
    columnas[0].lower(), #Cluster
    columnas[2].lower()+'_'+columnas[3]+'_'+columnas[13]+'_'+columnas[14],  # Cantidad de palabras clave
    columnas[8].lower()+'_'+columnas[9]+'_'+columnas[13]+'_'+columnas[14], # Procentaje de palabras clave
    columnas[12].lower()+'_'+columnas[13]+'_'+columnas[14] # Palabras clave
    ]
    rows = []
    row = []
    file.readline()
    file.readline()
    file.readline()
    for line in file:
        contenido = line.split('\n')
        contenido = contenido
        if len(contenido[0]) < 3:
            continue

        if contenido[0][3] in ['1','2','3','4','5','6','7','8','9']:
            col5 = contenido[0][40:]
            col1to4 = contenido[0][:40]
            col1to4 = col1to4.strip().replace('              ','**')
            col1to4 = col1to4.strip().replace('             ','**')
            col1to4 = col1to4.strip().replace('            ','**')
            col1to4 = col1to4.strip().replace('           ','**')
            col1to4 = col1to4.strip().replace('          ','**')
            col1to4 = col1to4.strip().replace('         ','**')
            col1to4 = col1to4.strip().replace('        ','**')
            col1to4 = col1to4.strip().replace('       ','**')
            col1to4 = col1to4.strip().replace('      ','**')
            col1to4 = col1to4.strip().replace('     ','**')
            col1to4 = col1to4.strip().replace('    ','**')
            col1to4 = col1to4.strip().replace('   ','**')
            col1to4 = col1to4.strip().replace('  ','**')
            contenido = col1to4.strip().split('**')
            contenido[0] = int(contenido[0])
            contenido[1] = int(contenido[1])
            contenido[2] = contenido[2].replace(",",".")
            contenido[2] = float(contenido[2].replace(" %",""))
            rows.append(row.copy())
            row = contenido + [col5.strip()]
        else:
            claves = row[3]+' '+contenido[0].strip()
            claves = claves.replace('    ',' ')
            claves = claves.replace('   ',' ')
            claves = claves.replace('  ',' ')
            row[3] = claves.strip().replace('.',"")
    rows.append(row.copy())

    # for i in rows[1:]:
    #     print(i)

    df = pd.DataFrame(rows[1:])
    df.columns = columnas2
    return df