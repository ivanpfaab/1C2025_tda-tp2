#!/bin/bash

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
# En Linux / macOS
source venv/bin/activate
# En Windows (comentado, activar manualmente después)
# venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

