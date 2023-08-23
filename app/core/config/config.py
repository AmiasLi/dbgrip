from typing import Dict, Type
from functools import lru_cache

from app.core.config.base import Settings, Envs
from app.core.config.development import DevSettings
from app.core.config.production import PrdSettings

settings: Dict[Envs, Type[Settings]] = {
    Envs.dev: DevSettings,
    Envs.prod: PrdSettings,
}


@lru_cache()
def get_settings() -> Settings:
    return settings[Settings().APP_ENV]()
