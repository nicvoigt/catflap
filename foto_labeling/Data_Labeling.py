import glob
import os

class Data_Labeler:
    def __init__(self):
        self.unlabeled_dir = "/home/catflap/foto_labeling/static/Unlabeled_photos" # "directory of unlabeled photos"
        self.target_folder = "/home/catflap/foto_labeling/target_dir"
        self.photo_dir = []  # directory to keep photos directories
        self.photo_label = []  # label of each photo
        self.photo_names = []
        self.possible_labels = ["Maus", "Keine Maus", "NA"]

    def fill_photo_dict(self):
        # search for latest pictures taken and fill photo_dict with directories
        os.chdir(self.unlabeled_dir)
        self.photo_dir = [self.unlabeled_dir  + "/" +file for file in glob.glob("*.jpg")]
        self.photo_dir.sort(key=os.path.getctime)
        self.photo_label = [None] * len(self.photo_dir)
        self.photo_names = [file for file in glob.glob("*.jpg")]

    def save_labeled_photos(self):
        # verschieben der photos aus dem ungelabelten in den gelabelten ordner
        target_dir = ""
        # move photos from unlabeled folders to labeled folders

        self.check_if_folder_exist()

        for index, photo in enumerate(self.photo_dir):
            new_link = os.path.join(self.target_folder, self.photo_label[index], self.photo_names[index])
            os.replace(photo, new_link)

    def save_current_photo(self, label):
        self.check_if_folder_exist()
        new_link = os.path.join(self.target_folder, label, self.photo_names[index])
        os.replace(photo, new_link)

    def send_notification(self):
        # later
        return



    def check_if_folder_exist(self):
        for label in self.possible_labels:
            if not os.path.exists(os.path.join(self.target_folder,label)):
                os.mkdir(os.path.join(self.target_folder,label))
