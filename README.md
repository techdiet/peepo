# peepo
hr management platform

### Steps for the application set up
1. **Clone the repository:**
    - `git clone https://github.com/techdiet/peepo.git`
2. **Navigate to the project directory:**
    - `cd peepo`
3. **Create and activate a Virtual Environment:** Isolate your project dependencies from the global Python environment by creating and activating a virtual environment.
    - Create a virtual environment `python -m venv .venv`
    - Activate the virtual environment
        - On Windows `source .venv\Scripts\activate`
        - On macOS/Linux `source .venv/bin/activate`
4. **Install dependencies:**
    - `pip install -r requirements.txt`
5. **Apply database migrations:**
    - `python manage.py migrate`
6. **Run the development server:**
    - `python manage.py runserver`
