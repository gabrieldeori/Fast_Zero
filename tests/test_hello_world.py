from fastapi.testclient import TestClient

from fast_zero.hello_world import read_root

assert TestClient(read_root).get('/').json() == {'message': 'Hello World!'}
