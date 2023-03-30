from project import get_url, validate_url, verify_url, get_title
def test_get_url(monkeypatch):
    # Test that function returns the correct URL
    url = "https://www.example.com"
    monkeypatch.setattr('builtins.input', lambda _:url)
    assert get_url() == url



def test_validate_url():
    assert validate_url("example.com") == False
    assert validate_url("www.example.com") == False
    assert validate_url("http://www.example.com") == True
    assert validate_url("https://www.example.com") == True
    assert validate_url(".example.com") == False
    

def test_verify_url():
    assert verify_url("http://www.example.com") == True


def test_get_title():
    assert get_title("http://www.example.com") == "Example_Domain.pdf"
