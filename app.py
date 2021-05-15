from numpy.random import f
import spacy
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text

app = Flask(__name__)

# Loading Model
nlp_model = spacy.load('nlp_ner_model')

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/', methods = ['GET', 'POST'])
def extract():
   
   if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        
        x = extract_text(f.filename)
        doc = nlp_model(x)
        for ent in doc.ents:
            result=f"{ent.label_.upper():{30}}-{ent.text}"
                       
        return render_template('index.html', extracting_text='Result : {}'.format(result))
      
      
if __name__ == "__main__":
    app.run(debug=True)