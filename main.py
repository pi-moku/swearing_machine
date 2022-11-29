import pandas as pd
from sklearn import tree
import sys

#データ読み込み
df = pd.read_csv('main.csv')

#特徴量
xcol = ['性格','容姿']
x = df[xcol]
t = df['言葉']

# モデル
model = tree.DecisionTreeClassifier(random_state=0)
model.fit(x,t)


# 予測
print("悪口マシーン")
seikaku = input('性格 1,良い（優しい）2,ふつう 3,悪い> ')
try:
    seikaku = int(seikaku)
except:
    print('文字などでは入力しないでください')
    sys.exit()

if seikaku:
    #入力してるか
    if seikaku == 1 or seikaku == 2 or seikaku == 3:
        yousi = input('容姿(性格と同じ)> ')
        try:
            yousi = int(yousi)
        except:
            print('文字などは入力しないでください')
            sys.exit()

        if yousi:
            if yousi == 1 or yousi == 2 or yousi == 3:
                nai = [[seikaku,yousi]]
                print(model.predict(nai))
            else:
                print("容姿は1か2か3かでお願い")
        else:
            print("容姿を入力して")
    else:
        print("性格は1か2か3")
else:
    print('しっかり入力して')
    sys.exit()
