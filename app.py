from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

app.secret_key = 'secret_key'


@app.route("/")
def index():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from school")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/add",methods=['POST','GET'])
def add():
    if request.method=='POST':
        data=request.form['data']
        subject=request.form['subject']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("insert into school(DATA,SUBJECT) values (?,?)",(data,subject))
        con.commit()
        flash('Створенно','success')
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<string:uid>",methods=['POST','GET'])
def edit(uid):
    if request.method=='POST':
        data=request.form['data']
        subject=request.form['subject']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("update school set DATA=?,SUBJECT=? where UID=?",(data,subject,uid))
        con.commit()
        flash('Вдачно зміненно','success')
        return redirect(url_for("index"))
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from school where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("edit.html",datas=data)
    
@app.route("/delete/<string:uid>",methods=['GET'])
def delete(uid):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("delete from school where UID=?",(uid,))
    con.commit()
    flash('Видаленно','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.run(debug=True)
    