from locust import HttpUser, task

class firstLocust(HttpUser):
    
    @task
    def hello_world(self):
        self.client.get('/hello')