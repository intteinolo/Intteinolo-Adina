
# # Información sobre instalación de ambiente python

# # En ubuntu 21.04

sudo apt-get update

sudo apt-get upgrad

sudo apt-get install -y build-essential openssl openssl-dev* wget curl


# # Instalación de Python3.7

cd /opt

wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz

tar -xvf Python-3.7.8.tgz

cd Python-3.7.8

sudo ./configure --enable-shared

sudo make

sudo make test

sudo make install

cd /usr/local/lib/
sudo mkdir /usr/lib64/
sudo cp libpython3.so /usr/lib64/
sudo cp libpython3.so /usr/lib
sudo cp libpython3.7m.so.1.0 /usr/lib64/
sudo cp libpython3.7m.so.1.0 /usr/lib/
cd /usr/lib64
sudo ln -s libpython3.7m.so.1.0 libpython3.7m.so
cd /usr/lib
sudo ln -s libpython3.7m.so.1.0 libpython3.7m.so

# # Instalación de Python3.8

cd /opt

wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz

tar xzf Python-3.8.7.tgz

cd Python-3.8.7
sudo ./configure --enable-optimizations
sudo make altinstall


# # Instalación de herramientas necesarías para instalar las bibliotecas de python

sudo apt install libffi-dev

sudo apt install python3-pip

sudo apt install python3-venv

sudo apt-get install libhdf5-dev

# # Construcción de ambiente en Visual Studio Code

python3.8 -m venv .env

virtualenv -p python3.8 .my-env-name (clona ambiente)

source .env/bin/activate

# # En caso de querer dessactivar el ambiente

deactivate

# # Una vez ingresado en el entorno identificado por "(nombre ambiente) $"

pip install --upgrade pip 

# # En caso de tener un archivo de requerimientos para las librerias del ambiente

# #instalar todo lo que se pide:
pip install -r requirements.txt

pip list

# # En caso de no tener archivo de requerimientos

pip install --upgrade pip setuptools wheel

pip install tensorflow

pip install keras

pip install sklearn_export

pip install scikit-mlm

pip install sklearn

pip install scikit-learn

pip install pandas

pip install pymongo

pip install "pymongo[srv]"

pip install dnspython

pip install certifi

pip install request

# # Se recomienda generar un archivo de requerimientos del ambiente
# # Crear copia de requerimientos de entorno


pip freeze > requirements.txt







