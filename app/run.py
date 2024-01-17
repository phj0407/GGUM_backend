import sys
import os

# 현재 파일의 경로를 가져와서 프로젝트 폴더를 sys.path에 추가
project_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_folder)

from app import app

if __name__ == '__main__':
    app.run(debug=True)