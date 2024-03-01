Stop-Process -Name "uvicorn"

Make sure you're in the same directory as the main file
uvicorn main:app --reload

Default when started should be
http://127.0.0.1:8000/