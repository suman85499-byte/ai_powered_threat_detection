import os
import sys
import traceback

os.environ["VERCEL"] = "1"

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from web.app import app

except Exception as exc:
    # Save the exception before leaving the except block
    startup_error = str(exc)
    startup_traceback = traceback.format_exc()

    print(f"[Vercel Startup Error] {startup_traceback}")

    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return jsonify({
            "status": "error",
            "message": startup_error,
            "traceback": startup_traceback
        }), 500
