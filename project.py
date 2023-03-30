import library


def main():
    while True:
        url = get_url()
        if validate_url(url) and verify_url(url):
            break
        else:
            url = get_url()
            

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

def get_url():
    return input("url: ")


def validate_url(url):
    """
    checks if it's a correct url format
    """


    pattern = library.re.compile(r'^(http(s)?)?://(www)?\.[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9-]+)*(\?[a-zA-Z0-9-_=]+)?')


    # Use the pattern to match the input URL
  
    return bool(pattern.match(url))
       

def verify_url(url):
    """
    Checks if the url actually points to somewhere
    """
   
    response = library.requests.head(url)
    return response.status_code == 200
           

def get_title(url):
    # Getting the webpage

    r = library.requests.get(url)
    soup = library.BeautifulSoup(r.content, 'html.parser')
    
    try:
        output_path = soup.title.string.replace(" ", "_") + ".pdf"
    except AttributeError:
        output_path = "file.pdf"
    
    return output_path

        


if __name__=='__main__':
    main()





