import os
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
#from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk.integrations.pymongo import PyMongoIntegration
from sentry_sdk.integrations.sanic import SanicIntegration

sentry_logging = LoggingIntegration(
    level=os.environ.get('SENTRY_LOGGING_LEVEL', 'WARNING'),
    event_level=os.environ.get('SENTRY_EVENT_LEVEL', 'ERROR')
)

def init_sentry(dsn):
    sentry_sdk.init(
        dsn=dsn,
        integrations=[
            sentry_logging,
            SanicIntegration(),
            PyMongoIntegration(),
        ],

        traces_sample_rate=1.0,
    )