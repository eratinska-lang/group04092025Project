from fastapi import FastAPI


def get_application() -> FastAPI:
    app = FastAPI(debug=True)
    return app


app = get_application()
