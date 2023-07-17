import numpy as np


class GaussianNB:
    """
    # Gaussian Naive Bayes (GaussianNB)
    ---

    ## Deskripsi
    Gaussian Naive Bayes merupakan salah satu metode di dalam supervised
    learning.
    gaussian Naive Bayes digunakan klasifikasi data yang berguna untuk mencari tahu
    menebak data `label` tersebut
    """

    def __init__(self) :
        self.features = []
        self.likelihoods = {}
        self.class_priors = {}
        self.pred_priors = {}
        self.X = None
        self.Y = None

    def __kalkulasi_probability_class(self, panjang_data):
        """
        menghitung peluang dari nilai unique class
        """
        for unique_value in np.unique(self.Y):
            value_outcome = sum(self.Y == unique_value)
            self.class_priors[unique_value] = value_outcome / panjang_data

    def __kalkulasi_kemiripan(self):
        for fitur in self.features:
            for outcome in np.unique(self.Y):
                outcome_count = sum(self.Y == outcome)
                feat_kemiripan = self.X[fitur][self.Y[self.Y == outcome].index.values]
                feat_kemiripan = feat_kemiripan.value_counts().to_dict()
                for feat_val, count in feat_kemiripan.item():
                    self.likelihoods[fitur][feat_val + "_" + outcome] = count
                    self.likelihoods[fitur][feat_val + "_" + outcome] /= outcome_count

    def __kalkulasi_predictor_prior(self):
        for fitur in self.features:
            feat_vals = X[fitur].value_counts().to_dict()
            for feat_val, count in feat_vals.items():
                self.pred_priors[fitur][feat_val] = count / self.X[0]

    def fit(self, x: np.array,
            y: np.array) -> None:
        self.X = np.array(x)
        self.Y = np.array(y)
        panjang_data, _ = self.X.shape
        for fitur in self.features:
            self.likelihoods[fitur] = {}
            self.pred_priors[fitur] = {}
            for feat_val in np.unique(self.X[fitur]):
                self.pred_priors[fitur].update({feat_val: 0})
                for outcome in np.unique(self.Y):
                    self.likelihoods[fitur].update({feat_val + "_" + outcome: 0})
                    self.class_priors.update({outcome: 0})
        self.__kalkulasi_probability_class(panjang_data)
        self.__kalkulasi_kemiripan()
        self.__kalkulasi_predictor_prior()

    def predict(self, x: np.array):
        X = np.array(x)
        results = []
        for query in X:
            probs_outcome = {}
            for outcome in np.unique(self.Y):
                prior = self.class_priors[outcome]
                likelihood = 1
                evidence = 1
                for feat, feat_val in zip(self.features, query):
                    likelihood *= self.likelihoods[feat][feat_val + "_" + outcome]
                    evidence *= self.pred_priors[feat][feat_val]

                posterior = (likelihood * prior) / evidence
                probs_outcome[outcome] = posterior

            result = max(probs_outcome, key=lambda x: probs_outcome[x])
            results.append(result)

        return np.array(results)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    clf = GaussianNB()
    clf.fit(X, Y)
    print(clf.predict([[-0.8, -1]]))
