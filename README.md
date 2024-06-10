# resflow-v2




## Features

- Users can upload resumes without authentication.
- Supported file formats: PDF, DOCX, TXT.
- Drag-and-drop functionality for file upload.
- Detailed error messages for validation and upload failures.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Axios, React Dropzone

## Setup and Installation

### Backend Setup (Django)

1. **Clone the repository**:

    ```bash
    https://github.com/arfazkhan/resflow-v2.git
    cd resflow-v2.git
    ```

2. **Set up a virtual environment and activate it**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```



5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

### Frontend Setup (React)

1. **Navigate to the frontend directory**:

    ```bash
    cd frontend
    ```

2. **Install the dependencies**:

    ```bash
    npm install
    ```

3. **Start the React development server**:

    ```bash
    npm start
    ```

## Running the Project Locally

### Running the Backend

Ensure your virtual environment is activated and run:

```bash
python manage.py runserver
```

The backend should now be running at `http://127.0.0.1:8000`.

### Running the Frontend

Navigate to the `frontend` directory and run:

```bash
npm start
```

The frontend should now be running at `http://localhost:3000`.

## Usage

- Visit `http://localhost:3000` to access the resume upload form.
- Fill in your name, email, and upload a resume file (PDF, DOCX, or TXT).
- Submit the form to upload the resume.

