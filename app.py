from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# import Methods of ontology
from Onto_methods import Methods


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Ontology():

	requet = ""
	if request.method == 'POST':
			requet = request.form['requet']
	if requet == "":
		requet = "Sports"
	onto = Methods.main(requet)

	Termes = onto[1]
	Concepts = onto[0]
	

	ontcon_term = []
	for m in onto[0]:
		ontcon_term.append(m)
	for m in onto[1]:
		ontcon_term.append(m)
	
	requet_after=  '+'.join(ontcon_term)

	
	context = {
		'concepts' : Concepts,
		'termes'   : Termes,
		'requet_befor_reformulation': requet,
		'requet_after_reformulation': requet_after
	}

	return render_template('bas1.html', context=context)


@app.route('/All_class/')
def All_class():

	classes = Methods.All_class()

	context = {

		'all_class' : classes,

	}

	return render_template('All_class.html', context=context)


#========================== main Function ==============================#


if __name__ == "__main__":
    app.run(debug=True)