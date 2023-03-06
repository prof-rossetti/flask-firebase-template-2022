

# tests for each page:

def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Home</h1>" in response.data

def test_about(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>About</h1>" in response.data

def test_products(test_client):
    response = test_client.get("/products")
    assert response.status_code == 200
    assert b"<h1>Products</h1>" in response.data


    assert b"Textbook" in response.data
    assert b"Cup of Tea" in response.data
    assert b"Strawberries" in response.data
