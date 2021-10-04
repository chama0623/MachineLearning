from sklearn.model_selection import KFold

class KFold_validation:
    def __init__(self,n_split=5,shuffle=True,random_state=0): # コンストラクタ
        self.__n_split = n_split
        self.__shuffle = shuffle
        self.__random_state=random_state

    def fit(self,model,X,y,loss_func):
        self.models = []
        self.evals = []
        self.K_fold = KFold(n_splits=self.__n_split,shuffle=self.__shuffle,random_state=self.__random_state)
        self.row_num_list = list(range(len(y)))
        for train_cv_num,eval_cv_num in self.K_fold.split(self.row_num_list,y):
            # 学習データ生成
            X_train_cv = X.iloc[train_cv_num,:]
            y_train_cv = y.iloc[train_cv_num]
            # 検証データ生成
            X_eval_cv = X.iloc[eval_cv_num,:]
            y_eval_cv = y.iloc[eval_cv_num]
            # 学習
            model.fit(X_train_cv,y_train_cv)
            self.models.append(model)
            # 検証
            y_pred_eval = model.predict(X_eval_cv)
            score = loss_func(y_eval_cv,y_pred_eval)
            self.evals.append(score)
            print("score= ",score)

    def predict(self,X):
        predictions = []
        for model in self.models:
            pred = model.predict(X)
            predictions.append(pred)

        return sum(predictions)/self.__n_split

    @property
    def n_split(self): # インスタンス名.n_splitで呼び出し
        return self.__n_split

    @n_split.setter
    def n_split(self,n_split): # インスタンス名.n_split = valueで呼び出し
        self.__n_split = n_split

    @property
    def shuffle(self):
        return self.__shuffle

    @shuffle.setter
    def shuffle(self,shuffle):
        self.__shuffle = shuffle

    @property
    def random_state(self):
        return self.__random_state

    @random_state.setter
    def random_state(self,random_state):
        self.__random_state = random_state
