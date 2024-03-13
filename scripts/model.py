
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import click
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz

@click.command()
@click.argument('column_name_path', type=str)
@click.argument('x_train_path', type=str)
@click.argument('y_train_path', type=str)
@click.argument('x_test_path', type=str)
@click.argument('y_test_path', type=str)
@click.argument('fig_output_folder', type=str)
@click.argument('data_output_folder', type=str)

def main(column_name_path, x_train_path,y_train_path,x_test_path,y_test_path,fig_output_folder,data_output_folder):
    X_train = pd.read_csv(x_train_path)
    X_test = pd.read_csv(x_test_path)
    y_train = pd.read_csv(y_train_path).values.ravel()
    y_test = pd.read_csv(y_test_path)
    column_names = pd.read_csv(column_name_path).iloc[:, 0].to_list()
    #Creating a results dictionary
    results = {}
    
    #Create a dummy classifier object
    dummy = DummyClassifier(random_state = 69)
    
    #Assessing dummy classifier scores
    scores = cross_validate(dummy, X_train, y_train, return_train_score=True)
    scores_df = pd.DataFrame(scores)
    scores_df
    
    #Creating model score dataframe
    mean_scores = scores_df.mean()
    
    results["Dummy"] = mean_scores
    
    
    #Creating a LogisticRegression object
    lr = LogisticRegression(random_state = 69)
    
    #Assessing model scores
    scores = cross_validate(lr, X_train, y_train, return_train_score=True)
    pd.DataFrame(scores)
    
    # Hyperparameter optimization
    
    scores_dict = {
        "C": 10.0 ** np.arange(-4, 6, 1),
        "mean_train_scores": list(),
        "mean_cv_scores": list(),
    }
    for C in scores_dict["C"]:
        lr = LogisticRegression(C=C, random_state = 69)
        scores = cross_validate(lr, X_train, y_train, return_train_score=True)
        scores_dict["mean_train_scores"].append(scores["train_score"].mean())
        scores_dict["mean_cv_scores"].append(scores["test_score"].mean())
    
    results_df = pd.DataFrame(scores_dict)
    results_df.to_csv(f'{data_output_folder}/logistic_regression_C_optimization.csv', index = False)
    
    # Extracting the best parameter
    highest_mean_cv_score_index = results_df['mean_cv_scores'].idxmax()
    highest_mean_cv_score_c_value = results_df.loc[highest_mean_cv_score_index, 'C']
    
    # Creating a LogisticRegression object with the best parameter and assessing scores
    lr_parameterised = LogisticRegression(C = 0.1, random_state = 69)
    scores_updated = cross_validate(lr_parameterised, X_train, y_train, return_train_score=True)
    
    #Fitting the model
    lr_parameterised.fit(X_train,y_train)
    
    #Accessing the coefficients of the variables. 
    pd.DataFrame({"columns":column_names, "coefs":list(lr_parameterised.coef_[0])}).sort_values("coefs").to_csv(f'{data_output_folder}/linear-reg_coefficients.csv', index = False)
    
    #Predicting on test set
    y_pred = lr_parameterised.predict(X_test)
    
    # Evaluate the model performance on the test set
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    test_results = {}
    test_results['Logistic Regression'] = [accuracy,precision,recall,f1]
    
    
    # Map label values from 1 and 2 to 0 and 1
    y_test_binary = y_test.copy()  # Create a copy to avoid modifying the original array
    y_test_binary[y_test_binary == 1] = 0
    y_test_binary[y_test_binary == 2] = 1
    
    #ROC curve plot
    fpr, tpr, thresholds = roc_curve(y_test_binary, lr_parameterised.predict_proba(X_test)[:, 1])
    plt.plot(fpr, tpr, label="ROC Curve")
    plt.xlabel("FPR")
    plt.ylabel("TPR (recall)")
    
    default_threshold = np.argmin(np.abs(thresholds - 0.5))
    
    plt.plot(
        fpr[default_threshold],
        tpr[default_threshold],
        "or",
        markersize=10,
        label="threshold 0.5",
    )
    plt.legend(loc="best");

    plt.savefig(f'{fig_output_folder}/roc_plot.png')
    
    
    # Creating a dataframe of the results of different models
    
    results["Logistic Regression"] = pd.DataFrame(scores_updated).mean()
    
    X_train_df = pd.DataFrame(X_train, columns=column_names)
    
    
    
    #Create a Random Forest Classifier object and assessing model scores
    rf_classifier = RandomForestClassifier(
            n_jobs=-1,
            random_state=123)
    
    scores_rf =cross_validate(rf_classifier, X_train, y_train, return_train_score=True)
    
    
    # Define the hyperparameters to tune
    param_grid = {
        'n_estimators': [100, 150, 200, 250, 300],  # Number of trees in the forest
        'max_depth': [1, 5, 10, 15, 20],    # Maximum depth of the trees
    }
    
    # Perform Grid Search with cross-validation
    grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    
    # Get the best hyperparameters
    best_params = grid_search.best_params_
    
    # Get the best model
    best_model = grid_search.best_estimator_
    
    # Creating the model with best hyperparameter and assessing scores
    rf_parameterised = RandomForestClassifier(
            n_estimators = best_params['n_estimators'],
            max_depth = best_params['max_depth'],
            n_jobs=-1,
            random_state=123)
    
    scores_rf_parameterised =cross_validate(rf_parameterised, X_train, y_train, return_train_score=True)
    
    #Fit the model 
    rf_parameterised.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = rf_parameterised.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    test_results['Random Forest'] = [accuracy,precision,recall,f1]
    
    test_results = pd.DataFrame(test_results)
    test_results['Measures'] = ['Accuracy', 'Precision','Recall','F1 Score']
    test_results.to_csv(f'{data_output_folder}/test_scores.csv')
    
    feature_names = (
      X_train_df.columns.tolist()
    )
    feature_names[:10]
    
    #Create 3 trees for visualization
    
    for i in range(3):
        tree = rf_parameterised.estimators_[i]
        dot_data = export_graphviz(tree,
                                   feature_names=feature_names,  
                                   filled=True,  
                                   max_depth=2, 
                                   impurity=False, 
                                   proportion=True)
        graph = graphviz.Source(dot_data)
        graph.render(f'{fig_output_folder}/{i}_random_forest_tree', format = 'png', cleanup = True)
    
    #Assessing model performance of different models
    results["Random Forest"] = pd.DataFrame(scores_rf_parameterised).mean()
    results_df = pd.DataFrame(results).T
    results_df.to_csv(f'{data_output_folder}/cross_validation_scores.csv')

if __name__ == '__main__':
    main()