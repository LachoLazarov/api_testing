Getting Started
To get started with this project, follow the steps below:

Clone the Project

git clone [repository_url]
cd [project_directory]

Set Up Virtual Environment

For Linux:

python3 -m venv venv

For Windows:

python -m venv venv

Activate Virtual Environment

For Linux:

source venv/bin/activate

For Windows:

venv\Scripts\activate

Install Requirements

pip install -r requirements.txt

Testing
To run the tests, make sure you have activated the virtual environment, and then run:

pytest test/test_*.py
