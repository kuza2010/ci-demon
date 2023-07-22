import sys

from src import create_app

config_path = sys.argv[1]
app = create_app(configfile=config_path)
app.run(host='0.0.0.0', port=5000)
