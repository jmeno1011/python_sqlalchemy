from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
data = sns.load_dataset("titanic")

data.head()
# data.head() 결과값
# => titanic 데이터를 일단 봄
# survived : IF the passenger survived (0-No, 1-Yes), pclass: passenger Class (1=1nd, 2=2nd, 3=3nd)
# sex(male, female), age, sibsp : No of siblings/spouese aboard(형제, 배우자 탑승중),
# parch: No of parents/children aboard(부모/자녀 탑승중), fare: passenger fare
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
# 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
# 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
# 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
# 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
# 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True

# feature가 될 값으로 feature_names 설정 후
feature_names = ["pclass", "age", "sex"]
# feature 추출
dfX = data[feature_names].copy()
#    pclass   age     sex
# 0       3  22.0    male
# 1       1  38.0  female
# 2       3  26.0  female
# 문자열로 되어있는 "sex"를 숫자로 변경해줌 male : 1 , female : 0
dfX["sex"] = LabelEncoder().fit_transform(dfX["sex"])
#    pclass   age  sex
# 0       3  22.0    1
# 1       1  38.0    0
# 2       3  26.0    0
# dfX.columns.tolist() => feature_names = ["pclass", "age", "sex"] 와 같다

# NaN 값이 들어있음
# print(dfX.tail())
#      pclass   age  sex
# 886       2  27.0    1
# 887       1  19.0    0
# 888       3   NaN    0
# fillna를 통해 값을 채움
dfX["age"].fillna(dfX["age"].mean(), inplace=True)
# DataFrame을 numpy array로 변환
feature_data = dfX.to_numpy()

# 타겟용 데이터 추출 / 타겟은 survived 가 됨
dfy = data["survived"].copy()
# DataFrame을 numpy array로 변환
target_data = dfy.to_numpy()

# train_test_split로 테스트 데이터와 트레인 데이터 분리 , test_size=0.3은 트레인 : 테스트 = 7 : 3 이다
# stratify은 default가 None이지만 타겟으로 설정해주면 class의 비율을 유지해준다.
# 여기서 class란 현재 타겟데이터의 경우 0과 1로 이루어져있는데 이것들을 클래스라고 함
X_train, X_test, y_train, y_test = train_test_split(
    feature_data, target_data, stratify=target_data, random_state=0, test_size=0.3)

# 의사결정트리 - DecisionTreeClassifier 를 이용함
clf = tree.DecisionTreeClassifier(random_state=0)
# fit은 모델에 맞게 데이터를 넣어서 피팅을 함
clf = clf.fit(feature_data, target_data)

print("훈련 세트 정확도: {:.3f}".format(clf.score(X_train, y_train)))
# 훈련 세트 정확도: 0.876
print("테스트 세트 정확도: {:.3f}".format(clf.score(X_test, y_test)))
# 테스트 세트 정확도: 0.888
print(clf.get_depth())
# clf.get_depth() 결과는 깊이 17가 나옴

# ===>>> 정확도가 0.888 좋게 나오지 않는다.
# 가지치기랑 데이터 선별하는 것도 필요
