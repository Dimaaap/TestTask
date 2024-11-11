class URL:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def __truediv__(self, path: str):
        return URL(f"{self.base_url}/{path.strip('/')}")

    def __str__(self) -> str:
        return self.base_url
