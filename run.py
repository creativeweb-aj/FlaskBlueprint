from App import create_app
import os

# App Run by this this
DEBUG = os.environ.get("DEBUG")

if __name__ == "__main__":
    create_app().run(debug=DEBUG)