from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/<int:num_boxes>/<color>')
def play(num_boxes, color):
    return render_template('play.html', num_boxes=num_boxes, color=color)

if __name__ == '__main__':
    app.run(debug=True)