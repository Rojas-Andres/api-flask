## Python 3.9.10

### Crear un archivo .env en la raiz del proyecto basandose en el archivo .env-example

# Correr proyecto local windows

- pip install virtualenv 
- virtualenv venv
- .\venv\Scripts\activate
- pip install -r requirements.txt
- python app.py

## Intefaz de swagger

![](images/image_swagger.png)

# Proyecto local corriendo


![](images/proyecto_local_corriendo.png)


### Run Project with docker

- ` docker build -t flask_api -f develop.Dockerfile . `
- ` docker run -p 8000:8000 flask_api `


![](images/run_docker.png)
