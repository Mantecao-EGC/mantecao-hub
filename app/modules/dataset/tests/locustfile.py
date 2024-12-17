from locust import HttpUser, TaskSet, task
from core.locust.common import get_csrf_token
from core.environment.host import get_host_for_locust_testing


class DatasetBehavior(TaskSet):
    def on_start(self):
        self.dataset()

    @task
    def dataset(self):
        response = self.client.get("/dataset/upload")
        get_csrf_token(response)


class DownloadBehavior(TaskSet):
    def on_start(self):
        self.download()

    @task
    def download(self):
        with self.client.get("/dataset/download/4", stream=True, catch_response=True) as response:
            if response.status_code == 200:
                # Opcional: valida el tamaño del archivo.
                file_size = int(response.headers.get("Content-Length", 0))
                if file_size > 0:
                    response.success()  # Marca la respuesta como exitosa.
                else:
                    response.failure("Archivo vacio o tamaño desconocido.")
            else:
                response.failure("Fallo al descargar")


class DatasetUser(HttpUser):
    tasks = [DatasetBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()


class Download(HttpUser):
    tasks = [DownloadBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
