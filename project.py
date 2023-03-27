import library


def main():
    print(validate_url(get_url()))







def get_url():
    return input("url: ")


def validate_url(url):
    """
    checks if it's a correct url format
    """


    pattern = library.re.compile(r'^(http(s)?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9-]+)*(\?[a-zA-Z0-9-_=]+)?')


    # Use the pattern to match the input URL
  
    if not pattern.match(url):
        validate_url(get_url())

    return True

def verify_url(url):
    """
    Checks if the url actually points to somewhere
    """
    while True:
        if validate_url(url):
            try:
                response = library.requests.head(url)
                return response.status_code == 200
            except:
                return False


def get_title(url):
    # Getting the webpage
    if verify_url(url):
        try:
            r = library.requests.get(url)
            soup = library.BeautifulSoup(r.content, 'html.parser')
        except:
            get_title(url)

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





