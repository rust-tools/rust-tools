import sys
import os

path = '/app.py'
if path not in sys.path:
   sys.path.insert(0, path)

from app import app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)