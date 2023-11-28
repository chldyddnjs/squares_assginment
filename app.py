from flask import Flask, render_template,redirect
import os
app = Flask(__name__)
root = os.getcwd()
samples = os.listdir(os.path.join(root,'templates\GeneratedWeb'))
@app.route('/')
def home():
    return render_template('index.html',samples=samples)

@app.route('/<page_id>')
def generated_page(page_id):
    if 'sample' in page_id:
        return render_template(f'GeneratedWeb/{page_id}/index.html')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    