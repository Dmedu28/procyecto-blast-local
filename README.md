## 🍄 Identificador de Hongos con BLAST Local

Este es un pipeline de bioinformática simple que utiliza **Python**, **Biopython** y **BLAST+** local para identificar 
secuencias de ADN desconocidas (en formato FASTA) comparándolas contra una base de datos local de secuencias 
de hongos (región ITS).

---

## 💡 Estatus del Proyecto: Micro-proyecto
Este es un **micro-proyecto de aprendizaje** (learning project). 
El objetivo principal fue demostrar la capacidad de instalar, configurar y conectar 
herramientas clave de bioinformática (`BLAST+`, `Biopython`) en un entorno Linux 
para crear un *pipeline* automatizado funcional.

---

## 1. 🎯 Objetivo del Proyecto

El objetivo es automatizar el proceso de identificación de secuencias. 
En lugar de usar el sitio web de NCBI manualmente, este script permite al usuario ejecutar un BLAST local
contra una base de datos curada, obteniendo resultados de identificación de forma instantánea en la terminal.

---

## 2. ⚙️ Cómo Usarlo

Este proyecto fue diseñado para correr en un entorno Linux (Ubuntu).

### A. Instalación
Primero, instala las dependencias necesarias
```bash
sudo apt update
sudo apt install python3-biopython ncbi-blast+
```
Clona este repositorio y navega a la carpeta:
```bash
git clone https://github.com/Dmedu28/proyecto-blast-local.git
cd proyecto-blast-local
```

### B. Ejecución

La base de datos `hongos_db.fasta` (y sus archivos de índice `.nhr`, `.nin`, etc.) ya están incluidos en este repositorio.

Para identificar una secuencia, simplemente ejecuta el script `identificar.py` seguido del archivo FASTA que quieres probar:
```bash
python3 identificar.py test.fasta
```
Esto arrojará un resultado similar al siguiente:
  Buscando test.fasta en la base de datos local...
  
  ¡Resultados encontrados!
  Mejor Coincidencia: gnl|BL_ORD_ID|1 Secuencia2_AB121666.2 Penicillium chrysoge...
  Identidad: 100.00 %
  E-value: 0.0


### C. Limitaciones Importantes

**Esta no es una herramienta de diagnóstico completa.** La base de datos (`hongos_db.fasta`) incluida 
es una **base de datos de demostración** y es muy pequeña.

* **Solo puede leer las secuencias específicas** que fueron añadidas manualmente.
* Si la secuencia de prueba no está en esta mini-base de datos, el script reportará "No se encontraron coincidencias".* 
