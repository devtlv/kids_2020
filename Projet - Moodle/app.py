import flask
from flask import request, render_template, redirect, url_for
import flask_login
import flask_sqlalchemy
import flask_migrate
from wtforms import fields

"""
Premiere fois que vous creez la base de donnees:
    flask db init

A chaque fois que vous modifiez/ajoutez une colonne/une classe:
    flask db migrate
    flask db upgrade
"""

app = flask.Flask("Moodle")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SECRET_KEY'] = 'aerhdqaiwhdficauhsdficuhiufhwisdhfishfiuhef'

login_manager = flask_login.LoginManager(app)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


# name=db.Column(db.Text)

class Exercice(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    titre       = db.Column(db.String(64))
    description = db.Column(db.String(300))
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))

    commentaires = db.relationship('Commentaire', backref='exercice')


class Commentaire(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    contenu     = db.Column(db.Text())

    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercice_id = db.Column(db.Integer, db.ForeignKey('exercice.id'))

class User(db.Model, flask_login.UserMixin):
    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(64))
    password    = db.Column(db.String(64))
    exercices   = db.relationship('Exercice', backref='user')

    commentaires = db.relationship('Commentaire', backref='user')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    print("test")
    print(flask_login.current_user)
    # print(flask_login.user_logged_in())

    return flask.render_template("home.html",
                                class_name="Les tigres"
                                )

# AJOUTER_EXERCICE
# Fonction
# Template


# Creer un compte
@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    # request.method == GET : Ca load le form pour la premiere fois
    # request.method == POST : l'utilisateur a appuyé sur le boutton submit.

    if request.method == "POST":
        req = request.form

        username = req.get("username")
        password = req.get("password")
        confirm_password = req.get("confirm-password")

        if not password == confirm_password:
            # faire des choses si les passwords sont differents
            password_different = True

            return render_template("signUp.html", password_different=password_different)


        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('projets'))

    return flask.render_template("signUp.html")

# Se connecter
@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():

    if request.method == "POST":
        req = request.form

        username = req.get("username")
        password = req.get("password")

        user = User.query.filter_by(username=username).first()
        # Check si l'utilisateur existe
        if user is None:
            return flask.render_template("signIn.html", fail=True)

        # Check si le mot de passe est le bon
        if user.password != password:
            return flask.render_template("signIn.html", fail=True)

        flask_login.login_user(user)

        return redirect(url_for('projets'))

    return flask.render_template("signIn.html")


@app.route('/projets')
def projets():
    projets = ["Space Invaders", "Memory", "Snake"]
    return flask.render_template("projets.html", projets=projets)


@app.route('/add-exercise', methods=['GET', 'POST'])
def add_exercise():
    if request.method == "POST":
        req = request.form

        titre = req.get("titre")
        description = req.get("description")

        # Pour sauvegarder un exercice
        exercice = Exercice(titre=titre, description=description)
        db.session.add(exercice)
        db.session.commit()

        return redirect(url_for('projets'))

    return flask.render_template("add_exercise.html")

@app.route('/exercises')
def exercises():
    exercices = Exercice.query.all()

    return flask.render_template("exercises.html", exercices=exercices)

@app.route('/exercice/<exercice_id>', methods=('GET', 'POST'))
def exercice(exercice_id):
    exercice = Exercice.query.get(exercice_id)

    if request.method == "POST":
        contenu = request.form.get("commentaire")
        commentaire = Commentaire(contenu=contenu)
        commentaire.user_id = flask_login.current_user.id
        commentaire.exercice_id = exercice_id

        # Sauvegarde:
        db.session.add(commentaire)
        db.session.commit()

    return flask.render_template('exercice_details.html', exercice=exercice)


@app.route('/logout')
def logout():
    flask_login.logout_user()

    return redirect(url_for('projets'))



app.run(port=5000, debug=True)
