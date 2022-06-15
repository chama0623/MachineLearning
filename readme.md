# MachineLearning Repository

## About
統計学や機械学習に関する実装をまとめたリポジトリです.
一部データについてはファイルサイズ,ライセンスの関係でコミットしていません.

## Directory Structure
.  
├── Bayes  
├── Modeling  
├── MultivariateAnalysis  
├── NLP  
├── QueueingTheory
├── Statistics
├── SupervisedLearning    
├── UnsupervisedLearning  
└── Visualization  

## 実装内容
教師あり学習
- 線形回帰モデル(単回帰分析, 重回帰分析, 多項式回帰, Redge, Lasso, Elastic Net)  
- Logstic回帰, Softmax回帰  
- Support Vector Machine(線形SVM, 非線形SVM, SVM回帰)  
- 決定木  
- kNN  
- Ensemble(ランダムフォレスト, Xgboost, LightBGM)  
- 勾配降下法, SGD  
- ニューラルネットワーク  
  
教師なし学習
- クラスタリング  
- 主成分分析  
- LDA  
  
ベイズ統計
- 分布のベイズ推定(ベルヌーイ, 二項, 正規, ポアソン)
- ポアソン混合分布
- ギブスサンプリング
- 変分推論

モデリング
- データの可視化  
- 特徴量エンジニアリング  
- 評価関数(MSE, MAE, RMSE, 決定係数, Accuracy, Precision, Recall, F-value, ROC, AUC)  
- モデルの評価(HoldOut, K-fold)  

待ち行列理論
- 勉強中

## Reference

scikit-learnとTensorflowによる実践機械学習 Aurelien Geron 著  
ゼロから作るディープラーニング 斎藤康毅 著  
ゼロから作るディープラーニング2 斎藤康毅 著  
機械学習のための特徴量エンジニアリング Alice Zheng, Amanda Casari 著  
Kaggleで勝つデータ分析の技術 門脇大輔, 阪田 隆司 著  
仕事ではじめる機械学習 有賀康顕, 中山心太, 西林孝 著  
多変量解析がわかる 涌井良幸,涌井貞美 著  
図解と数値例で学ぶ多変量解析 野口 博司 著  
統計学入門 東京大学出版会  
現代数理統計学の基礎 久保田達也 著  
ベイズ推論による機械学習入門 須山敦志 著  
待ち行列理論 大石進一 著  