from app import app, seed
with app.app_context():
    seed()
if __name__ == "__main__":
    app.run()
