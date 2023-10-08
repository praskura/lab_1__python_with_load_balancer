from locust import HttpUser, task

class HealthCheckUser(HttpUser):
    @task
    def load_health_check(self):
        self.client.get("/health_check")

class DatabaseUser(HttpUser):
    @task
    def load_get_entities(self):
        self.client.get("/get_entities")
