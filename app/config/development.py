from config.default import Config

class DevelopmentConfig(Config):
    #SERVER_NAME = 'DEVELOPMENT'
    DEVELOPMENT = True
    TESTING = True
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = False
    TEMPLATE_DEBUG = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    HEFENG_API = {
                "HELP_FILE": "static/help.txt",
                "WEATHER_INFO_JSON_FILE": "static/weather_info.json",
                "API_KEY": "742459bcd8b54244b1979cb30a4a4ac7",
                "BASE_URL_NOW":"https://free-api.heweather.com/v5/now?city=%s&key=",
                "BASE_URL_CITY":"https://free-api.heweather.com/v5/search?city=%s&key="
                }
    SQLITE_DB = {
                "DB_NAME": "my_weather.db",
                "TABLE_NAME_WEATHER": "weather_info",
                "TABLE_NAME_USER": "user",
    }

    SQLALCHEMY_DATABASE_URI = "sqlite:///my_weather_alchemy.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
