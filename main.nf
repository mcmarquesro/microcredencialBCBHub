#!/usr/bin/env nextflow
nextflow.enable.dsl=2
// He tenido que instalar de nuevo Nextflow y la nueva versión es DSL2
// Me ha costado muchos errores ver las diferencias con la anterior

///////////////////////////////////////////////////////
// Pipeline para ejecutar main.py sobre un archivo SAM
// usando uv
////////////////////////////////////////////////////


// Parámetro recibido desde la línea de comandos
params.sam = null

process ANALYZE_SAM {

    publishDir "$HOME/dia9/nf/main/", mode: 'copy'

    input:
        path sam_file

    output:
        path "${sam_file.baseName}_MAPQ.txt"

    script:
    """
    uv run $HOME/dia9/nf/main/main_project/main.py ${sam_file} > ${sam_file.baseName}_MAPQ.txt
    """
}

workflow {

    // Creamos un canal usando la ruta absoluta del parámetro
    sam_channel = Channel.fromPath(params.sam)

    // Ejecutamos el proceso con ese canal
    ANALYZE_SAM(sam_channel)
}



