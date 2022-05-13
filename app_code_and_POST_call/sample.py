from flask import Flask,request
from FinalMatrixAssessmentCode import ImageProcessing
import json, ast

app = Flask(__name__)

@app.route("/imageProcessingWeb", methods=['POST'])
def homepage():
    if request.method == 'POST':
        

        rows = request.json.get('row')
        columns = request.json.get('col')
        corner_coordinates = request.json.get('lst')
        corner_coordinates = ast.literal_eval(corner_coordinates)

        result = ImageProcessing.fillGridSpaceWithEdgePoints(corner_coordinates,rows,columns)
    return json.dumps({'result': result})












if __name__ == " __main__":
    app.run(debug=True)
