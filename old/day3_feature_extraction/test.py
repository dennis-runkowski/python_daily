from main import FeatureExtraction
import os

test_dataset = []
for dirname, subdir, files in os.walk('./test_data/'):
    for file in files:
        temp_path = "{p}{f}".format(p=dirname, f=file)
        with open(temp_path, 'r') as f:
            test_dataset.append(f.read())

print(len(test_dataset))

feature = FeatureExtraction(test_dataset, min_df=25, max_df=0.5, n_grams=3,
                            max_features=25)
feature.clean_data()
# feature.get_features()
# feature.plot_heatmap(doc_end=10)
# f = feature.feature_rank()
# print(type(f))
print(feature.get_features_spacy())