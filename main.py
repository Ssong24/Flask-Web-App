from venv import create
from website import create_app   # when having __init__.py in folder, python recognize the folder as package

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)