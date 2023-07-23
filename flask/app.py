from flask import Flask,render_template
import requests
app=Flask(__name__)
@app.route('/')
def hii():
    return render_template('tourism.html')
if __name__=='__main__':
    app.run(debug=True)