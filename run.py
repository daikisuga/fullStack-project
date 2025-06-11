import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app
app = create_app()

if __name__ =='__main__':
<<<<<<< Updated upstream
    app.run(host='192.168.00.00', port=8000) #ip Pedro
=======
    app.run(host='192.168.15.12', port=8000)
>>>>>>> Stashed changes
