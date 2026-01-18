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
Inside the project root (Gym/), create a file named .env

    DB_HOST=aws-************************.com
    DB_PORT=5432
    DB_NAME=postgres
    DB_USER=postgres.***********
    DB_PASSWORD=***********
    SUPABASE_URL=https:*************.co
    SUPABASE_KEY=sb_***************vyeLe

replace with real values

# install dependencies
pip install -r requirements.txt

# start the server
uvicorn app:app --reload

# open in browser
http://127.0.0.1:8000
