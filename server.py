from sanic import Sanic
from controllers.user_controller import user_routes
from controllers.mongo_controller import monguito_routes
from sanic_jwt import Initialize
from services.auth_service import authenticate
from config.sentry import init_sentry


app = Sanic(__name__)

init_sentry("https://1ac30326842b4938a01a09360786de49@o4504991838633984.ingest.sentry.io/4504991841845248")

app.config.FALLBACK_ERROR_FORMAT = "html"
app.config.DEBUG = True

#app.middleware('response')(sentry_middleware)

app.blueprint(user_routes)
app.blueprint(monguito_routes)

app.config.JWT_SECRET = "micodigosecreto"

Initialize(app, authenticate=authenticate)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)