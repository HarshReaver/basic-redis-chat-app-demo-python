import eventlet
eventlet.monkey_patch()

from chat.app import app, run_app  # noqa


if __name__ == "__main__":
    run_app()
