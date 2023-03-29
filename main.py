from flask import Flask
import utils
app = Flask(__name__)

candidate = utils.load_candidate()
@app.route("/")
def page_index():

    str_candidate = ''
    for candidates in candidate.values():
        str_candidate += f"{candidates['name']}<br>{candidates['position']}<br>{candidates['skills']}<br><br>"
    str_candidate += '<pre>'

    return str_candidate

@app.route("/candidate/<int:id>")
def profile(id):
    candidates = candidate[id]
    str_candidate = f"<img src='{candidates['picture']}'><br>{candidates['name']}<br>{candidates['position']}<br>{candidates['skills']}<br>"

    return str_candidate

@app.route("/skills/<skill>")
def skills(skill):

    str_candidate = ''
    for candidates in candidate.values():
        candidates_skills = candidates['skills'].split(', ')
        if skill in candidates_skills:
            str_candidate += f"{candidates['name']}<br>{candidates['position']}<br>{candidates['skills']}<br><br>"

    str_candidate = '<pre>' + str_candidate + '</pre>'
    return str_candidate
app.run(debug=True)

