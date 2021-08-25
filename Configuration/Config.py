import os


class Config:
    REPORT_TITLE = "Startup Jobs API Checks"
    BASE_URLS = {
        "dev": None,
        "staging": None,
        "prod": "https://startupjobs.cz"
    }

    @classmethod
    def env(cls):
        return os.environ.get("SHARK_ENV") or "dev"

    @classmethod
    def base_url(cls):
        return cls.BASE_URLS[cls.env()]
