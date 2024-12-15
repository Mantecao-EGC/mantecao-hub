from locust import HttpUser, TaskSet, task, between  # type: ignore
from core.locust.common import get_csrf_token


class ExploreTasks(TaskSet):
    @task
    def explore_page(self):
        self.client.get("/explore")

    @task
    def search_features_only(self):
        response = self.client.get("/explore")
        csrf_token = get_csrf_token(response)

        response = self.client.post("/explore", data={
            "csrf_token": csrf_token,
            "query": "",
            "publication_type": "any",
            "sorting": "newest",
            "config_number": "",
            "core_features": str(between(1, 100))
        })
        if response.status_code != 200:
            print(f"Filter failed: {response.status_code}")

    @task
    def search_configs_only(self):
        response = self.client.get("/explore")
        csrf_token = get_csrf_token(response)

        response = self.client.post("/explore", data={
            "csrf_token": csrf_token,
            "query": "",
            "publication_type": "any",
            "sorting": "newest",
            "config_number": str(between(1, 100)),
            "core_features": ""
        })
        if response.status_code != 200:
            print(f"Filter failed: {response.status_code}")

    @task
    def search_configs_and_features(self):
        response = self.client.get("/explore")
        csrf_token = get_csrf_token(response)

        response = self.client.post("/explore", data={
            "csrf_token": csrf_token,
            "query": "",
            "publication_type": "any",
            "sorting": "newest",
            "config_number": str(between(1, 100)),
            "core_features": str(between(1, 100))
        })
        if response.status_code != 200:
            print(f"Filter failed: {response.status_code}")


class ExploreUser(HttpUser):
    tasks = [ExploreTasks]
    wait_time = between(1, 5)
