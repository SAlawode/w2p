import library


def main():
    convert_html_to_pdf(get_url())







def get_url():
    return input("url: ")


def validate_url(url):
    """
    Use regex to verify the url given by the user
    return: a bool. True or False
    """
    pattern = llibrary.re.compile(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w]*\??(?:[-\w.&=]+)?')

    # Use the pattern to match the input URL
    match = pattern.match(url)

    # Return True if the URL matches the pattern, False otherwise
    return bool(match)

def verify_url(url):
    if validate_url:
        response = library.requests.head(url)
        return response.status_code == 200


def get_title(url):
    # Getting the webpage
    if verify_url:
        r = library.requests.get(url)
        soup = library.BeautifulSoup(r.content, 'html.parser')

    try:
        output_path = soup.title.string + ".pdf"
    except AttributeError:
        output_path = "file.pdf"
    
    return output_path

        
def convert_html_to_pdf(url):
    output_path = get_title(url)

    options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    }

    # Convert the website to a PDF file using pdfkit
    library.pdfkit.from_url(url, output_path, options=options)



if __name__=='__main__':
    main()





