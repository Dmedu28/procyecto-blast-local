import sys  # Para leer el nombre del archivo de entrada
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML
import io

# --- 1. CONFIGURACIÓN DEL ARCHIVO ---
# El nombre de tu secuencia desconocida
try:
    archivo_desconocido = sys.argv[1]
except IndexError:
    print("Error: ¡Olvidaste pasar el nombre del archivo FASTA!")
    print("Uso: python identificar.py tu_archivo.fasta")
    sys.exit()  # Termina el script

# El nombre de la base de datos
# IMPORTANTE: Usa el nombre del .fasta original (enserio)
db_hongos = "hongos_db.fasta"

print(f"Buscando {archivo_desconocido} en la base de datos local...")

# --- 2. CONSTRUIR EL COMANDO BLAST ---
# Esto crea el comando de terminal: "blastn -query X -db Y -outfmt 5"
cline = NcbiblastnCommandline(
    query=archivo_desconocido,
    db=db_hongos,
    outfmt=5,  # Formato de salida XML (fácil de leer para Biopython, recuerda aza)
    task="blastn",
    evalue=0.001,
)

# --- 3. EJECUTAR BLAST Y CAPTURAR LA SALIDA ---
stdout, stderr = cline()

# Si stdout está vacío, no hubo resultados
if not stdout:
    print("\nNo se encontraron coincidencias significativas en la base de datos.")
    sys.exit()

blast_results = NCBIXML.read(io.StringIO(stdout))

# --- 4. ANALIZAR Y MOSTRAR EL MEJOR RESULTADO ---
if blast_results.alignments:
    # Obtiene el primer (y mejor) alineamientoo
    mejor_hit = blast_results.alignments[0]

    # Obtiene la información de ese hit
    titulo = mejor_hit.title
    e_value = mejor_hit.hsps[0].expect
    identidad = (mejor_hit.hsps[0].identities / mejor_hit.hsps[0].align_length) * 100

    print("\n¡Resultados encontrados!")
    print(f"  Mejor Coincidencia: {titulo}")
    print(f"  Identidad: {identidad:.2f} %")  # .2f = redondear a 2 decimales
    print(f"  E-value: {e_value}")

else:
    print("\nNo se encontraron coincidencias significativas en la base de datos.")
