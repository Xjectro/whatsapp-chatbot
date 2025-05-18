from .whatsapp import bp as whatsapp_bp


def register_routes(app):
    app.register_blueprint(whatsapp_bp)
