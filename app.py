import time
import redis
from flask import Flask

app = Flask(__name__)
# Connect to Redis (the hostname will be 'db')
cache = redis.Redis(host='db', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello World! I have been seen {count} times.\n'

Print ("hello vasuki")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
