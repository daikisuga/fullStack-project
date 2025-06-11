import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app
app = create_app()

if __name__ =='__main__':
    app.run(host='192.168.15.37', port=8000) #ip Pedro
    #app.run(host='192.168.0.0', port=8000) #ip Gustavo
    #app.run(host='192.168.0.0', port=8000) #ip Alan