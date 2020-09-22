from googletrans import Translator
from flask import Flask,render_template,request



app=Flask(__name__)
app.secret_key = 'dont tell anyone'

@app.route("/translate_lang",methods=["post"])
def translate_lang():
    if request.method == "POST":
        sentence = str(request.form["sentence"])
        code = str(request.form["code"])
        
        print(sentence)
        translator=Translator()

        translated_sentence = translator.translate(sentence,src="en",dest=code)
        translated=translated_sentence.text

    return render_template("index2.html",language_selected=code,sentence=sentence,translated_res=translated)



@app.route("/")
def index():
    lang=[{"name":"Afrikaans","code":"af"},{"name":"Irish","code":"ga"},{"name":"Albanian","code":"sq"},{"name":"Italian","code":"it"},{"name":"Arabic","code":"ar"},{"name":"Japanese","code":"ja"},{"name":"kannada","code":"kn"},{"name":"Basque","code":"eu"},{"name":"English","code":"en"},{"name":"Russian","code":"ru"},{"name":"French","code":"fr"},{"name":"Swedish","code":"sv"},
    {"name":"German","code":"de"},{"name":"Telugu","code":"te"},{"name":"Greek","code":"el"},{"name":"Tamil","code":"ta"},{"name":"Hindi","code":"hi"},
    {"name":"Gujrathi","code":"gu"},{"name":"urdu","code":"ur"},{"name":"Turkish","code":"tr"},{"name":"Georgian","code":"ka"}]
    
  
  
    return render_template("index2.html",languages=lang)

if __name__=="__main__":
    app.run(debug=True)
