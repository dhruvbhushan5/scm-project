from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_drawing', methods=['POST'])
def save_drawing():
    data = request.get_json()
    image_data = data['imageData']
    tool = data['tool']

    # Handle the drawing data as needed (save to a file, database, etc.)
    # For simplicity, let's just print the tool and length of image_data
    print(f"Tool: {tool}, Image Data Length: {len(image_data)}")

    return 'Drawing saved successfully'

if __name__ == '__main__':
    app.run(debug=True)
