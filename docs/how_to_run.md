# Setup & Run

create a folder

# clone the project
git clone https://github.com/Ashikravi/Gym.git

# create virtual environment
python -m venv venv

# activate virtual environment
venv\Scripts\activate

# go into project folder
cd Gym

# install dependencies
pip install -r requirements.txt

# start the server
uvicorn app:app --reload

# open in browser
http://127.0.0.1:8000
