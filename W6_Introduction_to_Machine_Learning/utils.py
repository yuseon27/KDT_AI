import sys
assert sys.version_info >= (3, 5)

import sklearn
assert sklearn.__version__ >= "0.20"

import numpy as np
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

PROJECT_ROOT_DIR = "."
CHAPTER_ID       = 'end_to_end_project'
IMAGE_PATH       = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGE_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300) : #{
    path = os.path.join(IMAGE_PATH, fig_id + "." + fig_extension)
    if tight_layout : plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
#}

# Ignore useless warnigs (see SciPy issue #5998)
import warnings
warnings.filterwarnings(action="ignore", message="^interal gelsd")

import os
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master"
HOUSING_PATH  = os.path.join("datasets", "housing")
HOUSING_URL   = DOWNLOAD_ROOT + "/datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH) : #{
    if not os.path.isdir(housing_path) :
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
#}

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH) :
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)



from sklearn.base import BaseEstimator, TransformerMixin

# column index
rooms_ix, bedromms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin) : #{
    def __init__(self, add_bedrooms_per_room = True) : #{  # no *args or **kwargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    #}
    
    def fit(self, X, y=None) : #{
        return self  # nothing else to do
    #}
    
    def transform(self, X) : #{
        rooms_per_household      = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        
        if self.add_bedrooms_per_room :
            bedrooms_per_room = X[:, bedromms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else :
            return np.c_[X, rooms_per_household, population_per_household]
    #}
#}


def display_scores(scores) : #{
    print("Scores :", scores)
    print("Mean :", scores.mean())
    print("Standard Deviation :", scores.std())
#}