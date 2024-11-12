from locust import HttpUser, TaskSet, task, between

class ExploreTasks(TaskSet):
    @task
    def explore_page(self):
        self.client.get("/explore")

class ExploreUser(HttpUser):
    tasks = [ExploreTasks]
    wait_time = between(1, 5)