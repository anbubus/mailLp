from flask import Flask, render_template, request, redirect
import aspose.pdf as ap


app = Flask(__name__)


@app.route("/")
def loginPage():
    return render_template("login.html")


@app.route("/", methods=["POST", "GET"])
def login():
    f = open("logUsers.txt")
    f.seek(0)
    if request.method == "POST":
        nome = request.form.get("name")
        senha = request.form.get("pass")

        pato = f.readlines()
        if nome + ' - ' + senha + "\n" in pato:
            return redirect("/mail/" + nome)
        else:
            #f.close()
            #f = open("logUsers.txt", 'a')
            #f.write(nome+" - "+senha+"\n")
            return redirect("/")
            
            
        f.close()

        
@app.route("/mail/<user_name>")
def homemail(user_name):
    return render_template("mail.html", user_name = user_name)

@app.route("/mail/<user_name>",  methods=["POST", "GET"])

def mail(user_name):

    if request.method == "POST":
        date = (str)(request.form.get("date"))
        dest = request.form.get("destinatario")
        text = request.form.get("text")
        rem = request.form.get("remetente")
        mail = date + "\n" + dest + "\n" + text + "\n" + rem

    document = ap.Document()
    page=document.pages.add()
    text_fragment = ap.text.TextFragment(mail)
    page.paragraphs.add(text_fragment)
    document.save(user_name + "mail.pdf")

    return render_template("mail.html", user_name = user_name)



if __name__ == "__main__":
    app.run(debug=True)