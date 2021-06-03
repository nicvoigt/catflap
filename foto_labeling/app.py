from flask import Flask, render_template, request
import os
import Data_Labeling
PEOPLE_FOLDER = os.path.join('static', "Unlabeled_photos")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
global Labeler
Labeler = Data_Labeling.Data_Labeler()
Labeler.unlabeled_dir = "/home/catflap/foto_labeling/static/Unlabeled_photos/"
Labeler.fill_photo_dict()
photo = Labeler.photo_names[0]
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], photo)
global counter
counter = 0

@app.route('/')
@app.route('/index')
@app.route("/send", methods=["GET", "POST"])
def show_index():
    global counter
    global Labeler
    for index, pic in enumerate(Labeler.photo_names):

        if request.method == "GET":
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'],
                                         Labeler.photo_names[min(counter, len(Labeler.photo_names))])
            return render_template("index.html", user_image = full_filename)

        if request.method == "POST":
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'],
                                         (Labeler.photo_names[min(counter + 1, len(Labeler.photo_names)-1)]))
            if request.form.get("Maus"):
                Labeler.photo_label[counter] = "Maus"

            elif request.form.get("Keine Maus"):
                Labeler.photo_label[counter] = "Keine Maus"

            elif request.form.get("NA"):
                Labeler.photo_label[counter] = "NA"

            elif (counter >= len(Labeler.photo_names)-1) or (request.form.get("Ende")):
                Labeler.save_labeled_photos()
                exit()
            counter += 1

            return render_template("index.html", user_image=full_filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port =5000)
