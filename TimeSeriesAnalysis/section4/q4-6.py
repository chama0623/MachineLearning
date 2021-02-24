import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("../Data/msci_day.xls")
df["Date"] = pd.to_datetime(df["Date"],format="%Y-%m-%d")

# 問題(1)
# 対数差分を計算
data = pd.DataFrame(index=df.index)
data["jp"] = np.log(df["jp"]) - np.log(df["jp"].shift(1))
data["fr"] = np.log(df["fr"]) - np.log(df["fr"].shift(1))
data["ca"] = np.log(df["ca"]) - np.log(df["ca"].shift(1))
data = data.dropna()

# 問題(2)
"""
日本,フランス,カナダの順番に並べると,日本の市場が開き終了した後にフランスの市場が開く,そして最後にカナダの市場が開く.
つまり日次のデータでは日本の外生性(モデルで説明できない要因)なる.さらに,日本市場は他の2つの市場が開く前に終了するため
他の2つの市場からは影響を受けない.同様に,フランスの市場はカナダの市場よりも外生性が高くなることが予想される.したがって
日次データの場合は,日本,フランス,カナダの順に並べることが再帰的構造の仮定の下では最も自然な順序になる.
"""

# 問題(3)
"""
週次,月次の場合は,日次のように時差が及ぼす影響は大きくない.したがって,株式市場の影響力を考える必要がある.しかし,日本,
フランス,カナダの外生性の大小を考えることは難しい.ここでは2019年の国別の時価総額(https://www.globalnote.jp/post-3751.html)
を参考にする.時価総額を参考にすると日本,フランス,カナダの順番に並べるとよさそうである.
"""

# 問題(4)
# VAR(0)~VAR(10)から,AICを参考に最適なモデルを選択
from statsmodels.tsa.api import VAR
model = VAR(data)
print(model.select_order(10))
# VAR(2)モデルを選択
results = model.fit(maxlags=15, ic='aic')

# 問題(5)
import statsmodels.api as sm
# フランスに対する日本のグレンジャー因果性検定
test_results = results.test_causality(causing=0, caused=1)
pvalue = test_results.pvalue
print(test_results)
print(pvalue)

# 問題(6)
# インパルス応答関数をプロット
irf = results.irf(10)
irf.plot(orth=False)
plt.show()

# 問題(7)
# プロット
FEVD = results.fevd(10)
FEVD.plot()
plt.show()
# 標準出力
print(FEVD.summary())