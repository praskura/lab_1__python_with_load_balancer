from locust import HttpUser, task

class HealthCheckUser(HttpUser):
    @task
    def load_health_check(self):
        self.client.get("/health_check")
