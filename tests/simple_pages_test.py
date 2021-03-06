"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data



def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Branches" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b" What is Pytest & Flask? " in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Continuous Delivery / CD: " in response.data


def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"Pylint: " in response.data


def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"Arrange: " in response.data

def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"Instantiation: " in response.data

def test_request_page8(client):
    """This makes the index page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"Simple Calculator: " in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page9")
    assert response.status_code == 404
