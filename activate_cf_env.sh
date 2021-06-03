#!/bin/bash
cd /home/catflap/

source env/bin/activate

python3 main2.py

cd /home/catflap/foto_labeling
python3 app.py
