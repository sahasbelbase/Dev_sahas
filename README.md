**Create a Virtual Environment (Optional but Recommended)**

python -m venv venv

**Activate the Virtual Environment**


**On Windows:**

venv\Scripts\activate

**On Unix or MacOS:**

source venv/bin/activate

**Install Dependencies**

pip install -r requirements.txt

**Database Initialization**

flask db init

flask db migrate

flask db upgrade


**This initializes the database and applies the initial migration.**


**Run Flask Application**

flask run

**Frontend Setup (Angular)**


**Navigate to the Frontend Folder**

cd frontend

**Install Node Modules**

npm install


**Run Angular Application**

ng serve


The Angular application should be running on http://localhost:4200.


