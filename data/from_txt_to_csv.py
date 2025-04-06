import pandas as pd
from pathlib import Path

def importar_txt_a_dataframe(nombre_archivo, carpeta='data', delimiter=r'\s+'):
    """
    Importa un archivo TXT desde la carpeta 'data' y lo convierte en un DataFrame de pandas.
    
    Args:
        nombre_archivo (str): Nombre del archivo TXT (incluyendo extensión)
        carpeta (str): Nombre de la carpeta donde se encuentra el archivo (por defecto 'data')
        delimiter (str): Delimitador de campos (por defecto '\s+' para espacios variables)
    
    Returns:
        pd.DataFrame: DataFrame con los datos del archivo TXT
    """
    # Construir la ruta completa al archivo
    ruta_completa = Path(carpeta) / nombre_archivo
    
    # Verificar si el archivo existe
    if not ruta_completa.exists():
        raise FileNotFoundError(f"El archivo {ruta_completa} no existe")
    
    try:
        # Leer el archivo TXT con pandas
        # header=None para que no tome la primera línea como encabezado
        # delimiter='\s+' para separar por cualquier cantidad de espacios
        # engine='python' para evitar warnings con regex como delimitador
        df = pd.read_csv(ruta_completa, 
                         delimiter=delimiter, 
                         header=None, 
                         engine='python',
                         skipinitialspace=True)
        
        print(f"Archivo importado correctamente: {ruta_completa}")
        print(f"Dimensiones del DataFrame: {df.shape}")
        
        return df
    
    except Exception as e:
        print(f"Error al importar el archivo: {str(e)}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración
    nombre_txt = "datos.txt"  # Cambia esto por el nombre de tu archivo
    
    # Importar datos
    df_datos = importar_txt_a_dataframe(nombre_txt)
    
    # Mostrar información del DataFrame si la importación fue exitosa
    if df_datos is not None:
        print("\nPrimeras 5 filas del DataFrame:")
        print(df_datos.head())
        
        print("\nInformación del DataFrame:")
        print(df_datos.info())