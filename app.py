from flask import Flask, request
from utils import*
import user, diary, notice, survey
app = Flask(__name__)

@app.route('/')
def main():
    return 'home_page'

if __name__ == '__main__':
    app.run(debug=True)
    
