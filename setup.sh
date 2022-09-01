#!/bin/sh

conda install -c conda-forge montreal-forced-aligner -y
pip install -r requirements.txt
pip install PyAudio
python setup_install/huaweicloud-python-sdk-sis-1.7.1/setup.py install
7z x misc_7z/misc.7z.001
