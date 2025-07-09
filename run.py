from src import create_app
"""
This script initializes and runs the Image Server application.

- Imports the `create_app` factory function from the `src` package.
- Creates an instance of the application using `create_app()`.
- If executed as the main program, starts the application server on host `0.0.0.0` and port `8000`.

Usage:
    python run.py

The server will be accessible on all network interfaces at port 8000.
"""

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
