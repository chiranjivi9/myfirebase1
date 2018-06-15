from firebase import firebase
from flask import Flask, render_template, request
from form import FirePut

app= Flask(__name__)
app.config['SECRET_KEY'] = 'abc'

firebase= firebase.FirebaseApplication('https://dbone-7da37.firebaseio.com/', None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testing')
def testing():
    return "<h2>this is another page </h2>"

if __name__=='__main__':
 app.run(debug=True)

count = 0
@app.route('/api/put', methods=['GET', 'POST'])
def fireput():
    form = FirePut()
    if form.validate_on_submit():
        global count
        count += 1
        putData = {'Title': form.title.data, 'Year' : form.year.data, 'Rating' : form.rating.data}
        firebase.put('/films', 'film' + str(count), putData)
        return render_template('result.html', form=form, putData=putData)
    return render_template('myform.html', form=form)
