# companio-backend

### Setup:

    python -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Run the development server:

    uvicorn main:app --reload

### Deploy on Railway

- Connect to your project using `railway link`
- Run locally using `uvicorn main:app --reload`
- Deploy using `railway run` or just by pushing to the main branch

### Docker

- Build the image using `docker build -t companio-backend .`
- The image contains both the FastAPI server and the PostgreSQL database.
