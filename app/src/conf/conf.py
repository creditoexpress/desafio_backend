import os

def init_app(app):
    app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    if __name__ == "__main__":
        ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
        ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
        app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)