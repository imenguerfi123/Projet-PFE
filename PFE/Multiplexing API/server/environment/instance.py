import os

env = os.environ.get("PYTHON_ENV", "development")
port = os.environ.get("PORT", 8080)

all_environments = {
    "development": { "port": 5000, "debug": True, "host": "0.0.0.0", "swagger-url": "/" },
    "production": { "port": port, "debug": False, "swagger-url": None  }
}

environment_config = all_environments[env]
