from project import get_url, validate_url, verify_url, get_title, convert_html_to_pdf
def test_get_url():
    # Test that function returns the correct URL
    url = "https://www.test.com"
    user_input = lambda: url
    assert get_url(input_function=user_input) == url



def test_validate_url():
    ...

def test_verify_url():
    ...

def test_get_title():
    ...

def test_convert_html_to_pdf():
    ...