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

4. **Create environment file**
   Create a copy of .env.template file and replace the placeholders with you variables values.

5. **Install dependencies:**
    - `pip install -r requirements.txt`
6. **Apply database migrations:**
    - `python manage.py migrate`
7. **Run the development server:**
    - `python manage.py runserver`
