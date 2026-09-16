from app.scraper.parser import parse_books

def test_parse_books():
    html = """
        <article class="product_pod">
            <h3>
                <a 
                    href="catalogue/a-light-in-the-attic_1000/index.html" 
                    title="A Light in the Attic"
                >
                    A Light in the Attic
                </a>
            </h3>

            <p class="price_color">£51.77</p>
            <p class="instock availability">
                In stock
            </p>
            <p class="star-rating Three"></p>
        </article>
    """
    books = parse_books(html)
    assert len(books) == 1
    book = books[0]
    assert book.title == "A Light in the Attic"
    assert book.price == 51.77
    assert book.availability == "In stock"
    assert book.rating == 3