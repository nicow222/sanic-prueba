from sanic import Sanic
from controllers.user_controller import user_routes
from sanic_jwt import Initialize
from services.auth_service import authenticate

app = Sanic(__name__)

app.blueprint(user_routes)

app.config.JWT_SECRET = "micodigosecreto"

Initialize(app, authenticate=authenticate)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)