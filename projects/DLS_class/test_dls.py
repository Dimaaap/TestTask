from dls import URL

SITE_PATH_ROOT = "https://mysite.com"


class TestURL:

    def test_urs_creation(self):
        url = URL(SITE_PATH_ROOT)
        assert str(url) == SITE_PATH_ROOT, "Failed in class creation"

    def test_url_concatenation(self):
        url = URL(SITE_PATH_ROOT) / 'static' / 'js' / 'main.js'
        assert str(url) == f"{SITE_PATH_ROOT}/static/js/main.js"

    def test_url_no_trailing_slashes(self):
        url = URL(SITE_PATH_ROOT)
        url_with_trailing_slash = URL(f"{SITE_PATH_ROOT}/")
        assert str(url) == str(url_with_trailing_slash), "Trailing slash has not been removed"

    def test_url_multiple_concatenate(self):
        url = URL(SITE_PATH_ROOT) / 'a' / 'b' / 'c'
        assert str(url) == f"{SITE_PATH_ROOT}/a/b/c"

    def test_url_edge_case(self):
        url = URL(f"{SITE_PATH_ROOT}//") / '/static/' / '/js/' / '/main.js'
        assert str(url) == 'https://mysite.com/static/js/main.js'