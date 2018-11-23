from flask import Flask, render_template,request
from elasticsearch import Elasticsearch


app = Flask(__name__)
es = Elasticsearch()
HEADERS = {'content-type': 'application/json'}


@app.route('/', methods=["GET","POST"])
def index():
    q = request.form.get("q")

    if q is not None:
        es.transport.connection_pool.connection.headers.update(HEADERS)
        resp = es.search(index="products",doc_type="default",body={"query": {"match": {"name": q}}})
        return render_template("index1.html",q=q,response=resp)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,port=8000)
