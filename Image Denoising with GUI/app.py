import os
from matplotlib import pyplot as plt
from skimage import io
from medpy.filter.smoothing import anisotropic_diffusion
from skimage import img_as_float
from flask import Flask, render_template, request
from flask_dropzone import Dropzone
import webbrowser
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH= os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*60*1000)

dropzone = Dropzone(app)
@app.route('/',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.filename="Noisy_Image.png"


        f.save(os.path.join(app.config['UPLOADED_PATH'],f.filename))
        img_url=os.path.join(app.config['UPLOADED_PATH'],"Noisy_Image.png")
        f.filename = img_as_float(io.imread(img_url, as_gray=True))
        
        img_aniso_filtered = anisotropic_diffusion(f.filename, niter=50, kappa=50, gamma=0.2, option=2) 
        cln_img_url=os.path.join(app.config['UPLOADED_PATH'],"Clean_Image.png")
        plt.imsave(cln_img_url, img_aniso_filtered, cmap='gray')

    return render_template('index.html')

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)