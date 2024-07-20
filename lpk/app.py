from flask import Flask, render_template, request, redirect, url_for
from models import db, Applicant
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourpassword@localhost/datalpk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    training_programs = [
        {"name": "Pelatihan Web Developer", "description": "Deskripsi Web Developer", "image": "https://picsum.photos/200"},
        {"name": "Data Scientist", "description": "Deskripsi Data Scientist", "image": "https://picsum.photos/200"},
        {"name": "Android Developer", "description": "Deskripsi Android Developer", "image": "https://picsum.photos/200"},
        {"name": "Video Editor", "description": "Deskripsi Video Editor", "image": "https://picsum.photos/200"},
        {"name": "Animator", "description": "Deskripsi Animator", "image": "https://picsum.photos/200"},
        {"name": "Content Creator", "description": "Deskripsi Content Creator", "image": "https://picsum.photos/200"},
        {"name": "Enterprise Resource Planning", "description": "Deskripsi ERP", "image": "https://picsum.photos/200"},
        {"name": "Desainer Grafis", "description": "Deskripsi Desainer Grafis", "image": "https://picsum.photos/200"},
        {"name": "Teknisi Jaringan", "description": "Deskripsi Teknisi Jaringan", "image": "https://picsum.photos/200"}
    ]
    return render_template('home.html', training_programs=training_programs)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        nik = request.form['nik']
        whatsapp_number = request.form['whatsapp_number']
        email = request.form['email']
        training_program = request.form['training_program']

        new_applicant = Applicant(
            full_name=full_name, 
            nik=nik, 
            whatsapp_number=whatsapp_number, 
            email=email, 
            training_program=training_program
        )
        db.session.add(new_applicant)
        db.session.commit()
        return redirect(url_for('applicants'))

    return render_template('register.html')

@app.route('/applicants')
def applicants():
    all_applicants = Applicant.query.all()
    return render_template('applicants.html', applicants=all_applicants)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_applicant(id):
    applicant = Applicant.query.get_or_404(id)

    if request.method == 'POST':
        applicant.full_name = request.form['full_name']
        applicant.nik = request.form['nik']
        applicant.whatsapp_number = request.form['whatsapp_number']
        applicant.email = request.form['email']
        applicant.training_program = request.form['training_program']
        
        db.session.commit()
        return redirect(url_for('applicants'))

    return render_template('edit_applicant.html', applicant=applicant)

@app.route('/delete/<int:id>')
def delete_applicant(id):
    applicant = Applicant.query.get_or_404(id)
    db.session.delete(applicant)
    db.session.commit()
    return redirect(url_for('applicants'))

if __name__ == '__main__':
    app.run(debug=True)
