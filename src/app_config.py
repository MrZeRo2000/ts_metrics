
from app import AppContext
from config import Configuration
from log import Logger
from oracle_interface import OracleInterface


class AppConfig:
    @staticmethod
    def execute():
        context = AppContext.get_context()
        context.register_singleton_component(Configuration())
        context.register_singleton_component(Logger("ts_metrics").logger)
        context.register_singleton_component(OracleInterface())