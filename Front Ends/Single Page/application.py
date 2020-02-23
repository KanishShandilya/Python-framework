from flask import Flask,render_template

app=Flask(__name__)

text=[" hdhvjjeftuy reu gfugfg ry gfg  yfgeu uy uygrurufuur yjf ufg yye g egjhrg ir yrruy gjyg",
    "dg cfycewf yrv gfv  fg uy rfgyurhf yuy i bgfiyvtfyg  jhrf gyuf grfv  ger,rj rvyu3r vfheigrf",
    "eyrgy fyc y ggy4  gy4 g  rgfhr fyg4 r gf 4  j yugyu ti4jn i fgi4jbk 4 y4j4hv 4 kh 4hgf4kj,hr"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first')
def first():
    return text[0]

@app.route('/second')
def second():
    return text[1]

@app.route('/third')
def third():
    return text[2]