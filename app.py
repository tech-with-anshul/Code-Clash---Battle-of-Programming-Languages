import os
from flask import Flask, render_template, request, jsonify
from config import Config
from models import db
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_session import Session

migrate = Migrate()
login_manager = LoginManager()
sess = Session()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    sess.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/select')
    def select():
        languages = [
            {"id": "python", "name": "Python", "creator": "Guido van Rossum", "year": 1991, "difficulty": "Easy", "popularity": "Very High", "icon": "devicon-python-plain"},
            {"id": "java", "name": "Java", "creator": "James Gosling", "year": 1995, "difficulty": "Medium", "popularity": "Very High", "icon": "devicon-java-plain"},
            {"id": "javascript", "name": "JavaScript", "creator": "Brendan Eich", "year": 1995, "difficulty": "Medium", "popularity": "Extremely High", "icon": "devicon-javascript-plain"},
            {"id": "typescript", "name": "TypeScript", "creator": "Anders Hejlsberg", "year": 2012, "difficulty": "Medium", "popularity": "High", "icon": "devicon-typescript-plain"},
            {"id": "c", "name": "C", "creator": "Dennis Ritchie", "year": 1972, "difficulty": "Hard", "popularity": "High", "icon": "devicon-c-plain"},
            {"id": "cpp", "name": "C++", "creator": "Bjarne Stroustrup", "year": 1985, "difficulty": "Very Hard", "popularity": "High", "icon": "devicon-cplusplus-plain"},
            {"id": "csharp", "name": "C#", "creator": "Anders Hejlsberg", "year": 2000, "difficulty": "Medium", "popularity": "High", "icon": "devicon-csharp-plain"},
            {"id": "go", "name": "Go", "creator": "Robert Griesemer, Rob Pike, Ken Thompson", "year": 2009, "difficulty": "Medium", "popularity": "High", "icon": "devicon-go-original-wordmark"},
            {"id": "rust", "name": "Rust", "creator": "Graydon Hoare", "year": 2010, "difficulty": "Hard", "popularity": "Medium", "icon": "devicon-rust-plain"},
            {"id": "ruby", "name": "Ruby", "creator": "Yukihiro Matsumoto", "year": 1995, "difficulty": "Easy", "popularity": "Medium", "icon": "devicon-ruby-plain"},
            {"id": "php", "name": "PHP", "creator": "Rasmus Lerdorf", "year": 1995, "difficulty": "Easy", "popularity": "High", "icon": "devicon-php-plain"},
            {"id": "swift", "name": "Swift", "creator": "Chris Lattner", "year": 2014, "difficulty": "Medium", "popularity": "Medium", "icon": "devicon-swift-plain"}
        ]
        return render_template('select.html', languages=languages)

    @app.route('/arena')
    def arena():
        lang1 = request.args.get('lang1')
        lang2 = request.args.get('lang2')
        if not lang1 or not lang2:
            return "Please select two languages.", 400
            
        domains = [
            {"id": "ai", "name": "Artificial Intelligence", "icon": "fas fa-brain", "desc": "Math, performance, and data processing are key."},
            {"id": "web", "name": "Web Development", "icon": "fas fa-globe", "desc": "DOM manipulation, async tasks, and frameworks matter."},
            {"id": "systems", "name": "Systems Programming", "icon": "fas fa-microchip", "desc": "Memory management and raw speed rule here."},
            {"id": "enterprise", "name": "Enterprise Software", "icon": "fas fa-building", "desc": "Stability, architecture, and object orientation."}
        ]
        return render_template('arena.html', lang1=lang1, lang2=lang2, domains=domains)

    @app.route('/battle')
    def battle():
        lang1 = request.args.get('lang1')
        lang2 = request.args.get('lang2')
        domain = request.args.get('domain')
        if not lang1 or not lang2 or not domain:
            return "Missing parameters", 400
            
        return render_template('battle.html', lang1=lang1, lang2=lang2, domain=domain)

    @app.route('/api/simulate')
    def api_simulate():
        lang1 = request.args.get('lang1')
        lang2 = request.args.get('lang2')
        domain = request.args.get('domain')
        
        import sys
        sys.path.append(os.path.join(os.path.dirname(__file__), 'services'))
        from battle_engine import simulate_battle
        
        result = simulate_battle(lang1, lang2, domain)
        return jsonify(result)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
