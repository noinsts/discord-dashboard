import asyncio
import threading

from flask import Flask, redirect, render_template, jsonify

from config import Config


class FlaskServer:
    def __init__(self, discord_client):
        self.app = Flask(
            __name__,
            template_folder=Config.TEMPLATE_DIR,
            static_folder=Config.STATIC_DIR
        )
        self.port = Config.FLASK_PORT
        self.host = Config.FLASK_HOST
        self.debug = Config.FLASK_DEBUG
        self.dc = discord_client

        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/")
        def home():
            return redirect("/dashboard")

        @self.app.route("/dashboard")
        def dashboard():
            return render_template('dashboard.html')

        @self.app.route("/api/stats")
        def stats():
            if not self.dc.is_ready():
                return jsonify({"error": "Discord bot is not ready yet"}), 503

            return jsonify(self.dc.stats)

        @self.app.route("/api/refresh_stats", methods=["POST"])
        def refresh_stats():
            if not self.dc.is_ready():
                return jsonify({"error": "Discord bot is not ready yet"}), 503

            # Запускаємо оновлення у фоновому потоці
            def run_async_update():
                coro = self.dc.update_data()
                asyncio.run(coro)

            threading.Thread(target=run_async_update, daemon=True).start()
            return jsonify({"status": "refresh started"})

    def run(self):
        self.app.run(port=self.port, host=self.host, debug=self.debug)

    def get_app(self):
        return self.app
