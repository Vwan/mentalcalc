# coding: UTF-8
def load_config(env):
    if env == 'PRODUCTION':
        from .production import ProductionConfig
        return ProductionConfig
    elif env == 'DEVELOPMENT':
        from .development import DevelopmentConfig
        return DevelopmentConfig
    else:
        from .default import Config
        return Config
