# microcredencialBCBHub
Este repositorio constituye el ejercicio de evaluación final de la Microcredencial Competencias Básicas en Biología Computacional.

# Pipeline Nextflow DSL2 para el análisis de archivos SAM usando Python + uv

Este proyecto implementa un pipeline reproducible en **Nextflow DSL2** para analizar archivos **SAM** mediante un script en **Python** ejecutado con **uv**.

El objetivo del pipeline es:
- Contar el número total de lecturas alineadas en un archivo `.sam`
- Contar cuántas lecturas tienen un valor de calidad **MAPQ = 60**
- Calcular el porcentaje correspondiente
- Generar un fichero de resultados `<nombre_muestra>_MAPQ.txt`

El pipeline ha sido diseñado para ejecutarse **sobre cualquier archivo SAM**, indicado mediante el parámetro `--sam`.

---

## 1. Requisitos

### 🔹 Software
- **Nextflow** ≥ 25.x  
- **uv** (gestor de entornos Python moderno y reproducible)
- **Python** ≥ 3.11 (gestionado por uv)
- **Git** (opcional para clonar este repositorio)

### 🔹 Dependencias Python (en `pyproject.toml`)
- `rich` (formateo de salida con colores)

Estas dependencias se instalan automáticamente mediante uv.

---

## 2. Instalación

### 🔹 Clonar el repositorio

```bash
git clone https://github.com/mcmarquesro/microcredencialBCBHub.git
cd microcredencialBCBHub

## 3. Comprobaciones

### 🔹 Comprobar Nextflow
nextflow -version

### 🔹 Comprobar uv
uv --version

## 4. Uso del pipeline

### 🔹 Ejecución básica
###Desde la carpeta main_project:
nextflow run main.nf --sam /ruta/al/archivo.sam

### 🔹 Ejemplo real
nextflow run main.nf --sam ../WT.sam

## 5. ¿Qué hace cada archivo?
### 🔹 main.py

###   Lee el archivo SAM
###   Cuenta lecturas totales
###   Cuenta lecturas con MAPQ = 60
###   Calcula el porcentaje
###   Imprime resultados usando Rich
###   uv lo ejecuta garantizando las dependencias correctas

### 🔹 main.nf

###   Activa DSL2
###   Recibe el parámetro --sam
###   Crea un canal con ese archivo
###   Ejecuta el proceso ANALYZE_SAM
###   Copia el fichero de salida a main_project/

## 6. Ejemplo de salida
### Si el archivo se llama WT.sam, el pipeline generará:
WT_MAPQ.txt

## Con un contenido similar a:

RESUMEN:
Total de lecturas alineadas:  123456
Lecturas con MAPQ = 60:       87432
Porcentaje:                   70.8%

## 8. Autoría
Mari Carmen Marqués Romero
Proyecto final para la Microcredencial BCBHub de Bioinformática
Año 2026
