from flask import Flask, render_template, redirect, request,session, url_for,flash
from markupsafe import escape
# import requests
# import json
# from turtle import st
import ibm_db





conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=pgw62994;PWD=rxrMsd0egpHDdyvI",'','')
print(conn)
print("connection successful...")


app = Flask(__name__)
app.secret_key = 'gtvhfryj123#@%'

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/myaccount')
def myaccount():
    return render_template('my-account.html')

@app.route('/shop-list')
def shoplist():
    return render_template('shop-list.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/single-product')
def singleproduct():
    return render_template('single-product.html')

@app.route('/thank-you')
def thankyou():
    return render_template('thank-you.html')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phonenumber = request.form['phonenumber']


        sql = "SELECT * FROM SFRA WHERE email = ?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            return render_template('index.html', msg="already members")
        else:
            insert_sql = "INSERT INTO SFRA VALUES (?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.bind_param(prep_stmt, 4, phonenumber)
            ibm_db.execute(prep_stmt)
            
            return render_template('index.html', msg="saved successfully")

@app.route('/login', methods=['GET', 'POST'])
def loginagent():
    app.secret_key = 'praveenkumhesbf/.[[.;;ar'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email,password)

        sql = f"SELECT * FROM sfra WHERE email='{escape(email)}' and password='{escape(password)}'"
        stmt = ibm_db.exec_immediate(conn, sql)
        data = ibm_db.fetch_both(stmt)
            
        if data:
            session["mail"] = escape(email)
            session["password"] = escape(password)
            return redirect(url_for('home'))

        else:
            return render_template('login.html', msg="Account does not exist or invalid Credentials")

    return "NOT WORKING!!??"
            
            



# url = "https://jsearch.p.rapidapi.com/search"

# querystring = {"query":" Web Developer , USA","num_pages":"1"}

# headers = {
# 	"X-RapidAPI-Key": "d118e88785mshb0e33767fd34476p166ed9jsna896a9c9e5da",
# 	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
# }



# @app.route("/api", methods=['GET'])
# def api():
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     data = json.loads(response.text)
#     return render_template('job-list.html',data=data)



# @app.route('/signup', methods =['GET', 'POST'])
# def signup():
#     return render_template('sign-up.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/bookmark')
# def bookmark():
#     return render_template('bookmark-jobs.html')

# @app.route('/candidatedetails')
# def candidatedetails():
#     return render_template('candidate-details.html')

# @app.route('/candidategird')
# def candidategird():
#     return render_template('candidate-gird.html')

# @app.route('/candidatelist')
# def candidatelist():
#     return render_template('candidate-list.html')

# @app.route('/companydetails')
# def companydetails():
#     return render_template('company-details.html')

# @app.route('/companylist')
# def companylist():
#     return render_template('company-list.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/faqs')
# def faqs():
#     return render_template('faqs.html')

# @app.route('/jobcategories')
# def jobcategories():
#     return render_template('job-categories.html')

# @app.route('/jobdetails')
# def jobdetails():
#     return render_template('job-details.html')

# @app.route('/jobgrid')
# def jobgrid():
#     return render_template('job-gird.html')

# @app.route('/joblist')
# def joblist():
#     return render_template('job-list.html')

# @app.route('/managejobpost')
# def managejobpost():
#     return render_template('manage-jobs-post.html')

# @app.route('/managejobs')
# def managejobs():
#     return render_template('manage-jobs.html')

# @app.route('/privacypolicy')
# def privacypolicy():
#     return render_template('privacy-policy.html')

# @app.route('/profile')
# def profile():
#     return render_template('profile.html')

# @app.route('/resetpassword')
# def resetpassword():
#     return render_template('reset-password.html')

# @app.route('/services')
# def services():
#     return render_template('services.html')

# @app.route('/signin')
# def signin():
#     return render_template('sign-in.html')

# @app.route('/signout')
# def signout():
#     return render_template('sign-out.html')

# @app.route('/team')
# def team():
#     return render_template('team.html')



# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         phonenumber = request.form['phonenumber']


#         sql = "SELECT * FROM users WHERE email = ?"
#         stmt = ibm_db.prepare(conn, sql)
#         ibm_db.bind_param(stmt,1,email)'

#         ibm_db.execute(stmt)
#         account = ibm_db.fetch_assoc(stmt)
        
#         if account:
#             return render_template('about.html', msg="already members")
#         else:
#             insert_sql = "INSERT INTO users VALUES (?,?,?,?)"
#             prep_stmt = ibm_db.prepare(conn, insert_sql)
#             ibm_db.bind_param(prep_stmt, 1, username)
#             ibm_db.bind_param(prep_stmt, 2, email)
#             ibm_db.bind_param(prep_stmt, 3, password)
#             ibm_db.bind_param(prep_stmt, 4, phonenumber)
#             ibm_db.execute(prep_stmt)

#             return "hello"
            
               






if __name__ == "__main__":
    app.run(debug=True)