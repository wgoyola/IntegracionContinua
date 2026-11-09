from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    visitas = r.incr("visitas")
    return f"Hola desde el contenedor WEB. Visitas guardadas en REDIS: {visitas}"

app.run(host="0.0.0.0", port=5000)