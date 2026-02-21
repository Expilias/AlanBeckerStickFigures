from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return render_template('home.html')

@app.route('/AnimationVersusMinecraft')
def AVM() -> str:
    return render_template('AVM.html')
@app.route('/AnimationVersusMinecraft/season1')
def AVM_season1() -> str:
    return render_template('avm_season1.html')
@app.route('/AnimationVersusMinecraft/season2')
def AVM_season2() -> str:
    return render_template('avm_season2.html')
@app.route('/AnimationVersusMinecraft/season3')
def AVM_season3() -> str:
    return render_template('avm_season3.html')
@app.route('/AnimationVersusMinecraft/season4')
def AVM_season4() -> str:
    return render_template('avm_season4.html')
@app.route('/AnimationVersusMinecraft/season5')
def AVM_season5() -> str:
    return render_template('avm_season5.html')

@app.route('/AnimationVersusAnimator')
def AVA() -> str:
    return render_template('AVA.html')
@app.route('/AnimationVersusAnimator/season1')
def AVA_season1() -> str:
    return render_template('ava_season1.html')
@app.route('/AnimationVersusAnimator/season2')
def AVA_season2() -> str:
    return render_template('ava_season2.html')
@app.route('/AnimationVersusAnimator/season3')
def AVA_season3() -> str:
    return render_template('ava_season3.html')

@app.route('/AnimationVersusEducation')
def AVE() -> str:
    return render_template('AVE.html')

@app.route('/AnimationVersusSeries')
def AVS() -> str:
    return render_template('AVS.html')

@app.route('/TheJourneyOfSpiritedAway')
def JSA() -> str:
    return render_template('JSA.html')

@app.route('/AnimationTutorialSeries')
def ATS() -> str:
    return render_template('ATS.html')
@app.route('/AnimationTutorialSeries/Flash')
def ATS_Flash() -> str:
    return render_template('ats_Flash.html')
@app.route('/AnimationTutorialSeries/Photoshop')
def ATS_Photoshop() -> str:
    return render_template('ats_Photoshop.html')

@app.route('/TheTwelvePrinciplesOfAnimation')
def TPA() -> str:
    return render_template('TPA.html')
if __name__ == '__main__':
    app.run()