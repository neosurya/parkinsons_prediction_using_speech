import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
from sklearn import tree

df = pd.read_csv(r"./readtext.csv")
#print(df)

#drop the first column. It's the voiceID
df.drop('voiceID', inplace = True, axis = 1)

#separate dependent and independent variable
X = df.iloc[:, :-1]
df_X = df.iloc[:, :-1].values
df_Y = df.iloc[:,-1].values


#print(df_X)

# Split the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(df_X, df_Y, test_size = 0.3, random_state = 0)
print(y_train)

# Scale
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Feature selection
""" sel = SelectFromModel(RandomForestClassifier(n_estimators = 100))
sel.fit(X_train, y_train)
print(sel.get_support())
selected_feat= X.columns[(sel.get_support())]
print(len(selected_feat))
print(selected_feat) """


# Fit classifier to the Training set
#KNN
model_knn = KNeighborsClassifier(n_neighbors = 10)
model_knn.fit(X_train, y_train)

#SVM
""" model_svm = svm.SVC()
model_svm.fit(X_train, y_train)

#RF
model_rf = RandomForestClassifier(max_depth=15, random_state=0)
model_rf.fit(X_train, y_train)

#Gradient Boosting
model_gb = GradientBoostingClassifier(random_state=0)
model_gb = model_gb.fit(X_train, y_train)

#Decision Tree
model_dt = tree.DecisionTreeClassifier()
model_dt = model_dt.fit(X_train, y_train)

#Logistic Regression
model_lr = LogisticRegression(random_state=0)
model_lr = model_lr.fit(X_train, y_train)

#Naive Bayes
model_nb = GaussianNB()
model_nb = model_nb.fit(X_train, y_train) """


#predict
y_pred_knn = model_knn.predict(X_test)
# y_pred_svm = model_svm.predict(X_test)
# y_pred_rf = model_rf.predict(X_test)
# y_pred_gb = model_gb.predict(X_test)
# y_pred_dt = model_dt.predict(X_test)
# y_pred_lr = model_lr.predict(X_test)
# y_pred_nb = model_nb.predict(X_test)


#confusion matrix
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)
# conf_matrix_svm = confusion_matrix(y_test, y_pred_svm)
# conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
# conf_matrix_gb = confusion_matrix(y_test, y_pred_gb)
# conf_matrix_dt = confusion_matrix(y_test, y_pred_dt)
# conf_matrix_lr = confusion_matrix(y_test, y_pred_lr)
# conf_matrix_nb = confusion_matrix(y_test, y_pred_nb)
print(conf_matrix_knn)
# print(conf_matrix_svm)
# print(conf_matrix_rf)
# print(conf_matrix_gb)
# print(conf_matrix_dt)
# print(conf_matrix_lr)
# print(conf_matrix_nb)

#accuracy
accuracy_knn = ((conf_matrix_knn[0,0] + conf_matrix_knn[1,1])/(conf_matrix_knn[0,0] +conf_matrix_knn[0,1]+conf_matrix_knn[1,0]+conf_matrix_knn[1,1]))*100
# accuracy_svm = ((conf_matrix_svm[0,0] + conf_matrix_svm[1,1])/(conf_matrix_svm[0,0] +conf_matrix_svm[0,1]+conf_matrix_svm[1,0]+conf_matrix_svm[1,1]))*100
# accuracy_rf = ((conf_matrix_rf[0,0] + conf_matrix_rf[1,1])/(conf_matrix_rf[0,0] +conf_matrix_rf[0,1]+conf_matrix_rf[1,0]+conf_matrix_rf[1,1]))*100
# accuracy_gb = ((conf_matrix_gb[0,0] + conf_matrix_gb[1,1])/(conf_matrix_gb[0,0] +conf_matrix_gb[0,1]+conf_matrix_gb[1,0]+conf_matrix_gb[1,1]))*100
# accuracy_dt = ((conf_matrix_dt[0,0] + conf_matrix_dt[1,1])/(conf_matrix_dt[0,0] +conf_matrix_dt[0,1]+conf_matrix_dt[1,0]+conf_matrix_dt[1,1]))*100
# accuracy_lr = ((conf_matrix_lr[0,0] + conf_matrix_lr[1,1])/(conf_matrix_lr[0,0] +conf_matrix_lr[0,1]+conf_matrix_lr[1,0]+conf_matrix_lr[1,1]))*100
# accuracy_nb = ((conf_matrix_nb[0,0] + conf_matrix_nb[1,1])/(conf_matrix_nb[0,0] +conf_matrix_nb[0,1]+conf_matrix_nb[1,0]+conf_matrix_nb[1,1]))*100


print(accuracy_knn)
# print(accuracy_svm)
# print(accuracy_rf)
# print(accuracy_gb)
# print(accuracy_dt)
# print(accuracy_lr)
# print(accuracy_nb)

################ applying cross validation using scikit learn################
df_X = sc.fit_transform(df_X)
k_fold = KFold(n_splits=37)
#KNN
model_knn_kfold = KNeighborsClassifier(n_neighbors = 10)
y_pred_kfold_knn = cross_val_predict(model_knn_kfold, df_X, df_Y, cv=k_fold)
print(df_Y)
print(y_pred_kfold_knn)
conf_matrix_knn_kfold = confusion_matrix(df_Y, y_pred_kfold_knn)
print("Confusion Matrix for KNN using k-fold (leave one out)")
print(conf_matrix_knn_kfold)

# #SVM
# model_svm = svm.SVC()
# y_pred_kfold_svm = cross_val_predict(model_svm, df_X, df_Y, cv=k_fold)
# conf_matrix_svm_kfold = confusion_matrix(df_Y, y_pred_kfold_svm)
# print("Confusion Matrix for SVM using k-fold (leave one out)")
# print(conf_matrix_svm_kfold)

# #RF
# model_rf = RandomForestClassifier(max_depth=15, random_state=0)
# y_pred_kfold_rf = cross_val_predict(model_rf, df_X, df_Y, cv=k_fold)
# conf_matrix_rf_kfold = confusion_matrix(df_Y, y_pred_kfold_rf)
# print("Confusion Matrix for RF using k-fold (leave one out)")
# print(conf_matrix_rf_kfold)

# #Gradient Boosting
# model_gb = GradientBoostingClassifier(random_state=0)
# y_pred_kfold_gb = cross_val_predict(model_gb, df_X, df_Y, cv=k_fold)
# conf_matrix_gb_kfold = confusion_matrix(df_Y, y_pred_kfold_gb)
# print("Confusion Matrix for Gradient Boosting using k-fold (leave one out)")
# print(conf_matrix_gb_kfold)

# #Decision Tree
# model_dt_1 = tree.DecisionTreeClassifier()
# y_pred_kfold_dt = cross_val_predict(model_dt_1, df_X, df_Y, cv=k_fold)
# conf_matrix_dt_kfold = confusion_matrix(df_Y, y_pred_kfold_dt)
# print("Confusion Matrix for Decision Tree using k-fold (leave one out)")
# print(conf_matrix_dt_kfold)

# #Logistic Regression
# #model_lr_1 = LogisticRegression()
# y_pred_kfold_lr = cross_val_predict(model_lr, df_X, df_Y, cv=k_fold)
# conf_matrix_lr_kfold = confusion_matrix(df_Y,y_pred_kfold_lr)
# print("Confusion Matrix for Logistic Regression using k-fold (leave one out)")
# print(conf_matrix_lr_kfold)

# #Naives Bayes
# model_nb_1 = GaussianNB()
# y_pred_kfold_nb = cross_val_predict(model_nb_1, df_X, df_Y, cv=k_fold)
# conf_matrix_nb_kfold = confusion_matrix(df_Y,y_pred_kfold_nb)
# print("Confusion Matrix for Naive Bayes using k-fold (leave one out)")
# print(conf_matrix_nb_kfold)

