# Makefile
# DSCI 310 Group 12, Mar 2024

# This driver script completes the predictive analysis of
# credit default risk for a German bank
# and creates figures and a final report.

all: reports/credit_risk_report.html reports/credit_risk_report.pdf

# Define PHONY targets: dats, edav, prep, model
.PHONY: dats edav prep model


# 1) Download the Data
# Input NA
# Output is just german.csv
dats: data/german.csv

data/german.csv: scripts/download_data.py
	python scripts/download_data.py \
        data/german.csv

# 2) Exploratory Data Analysis and Visualizations
# Input is german.csv
# Outputs are german_clean.csv and all img (except random forest & roc)
edav: data/german_clean.csv \
		img/age.png \
		img/credit_amount.png \
		img/credit_risk.png \
		img/duration.png \
		img/existing_credits.png \
		img/liable_people.png \
		img/rate.png \
		img/residence.png \
		img/heatmap.png

data/german_clean.csv img/age.png img/credit_amount.png img/credit_risk.png img/duration.png img/existing_credits.png img/liable_people.png img/rate.png img/residence.png img/heatmap.png: data/german.csv scripts/cleaning_and_eda.py
	python scripts/cleaning_and_eda.py \
		data/german.csv \
		img \
		data/german_clean.csv
		

# 3) Data Preprocessing 
# Input is german_clean.csv
# Outputs are x train & test, y train & test, column_names
prep: data/x_test.csv \
		data/x_train.csv \
		data/y_test.csv \
		data/y_train.csv \
		data/column_names.csv

data/x_test.csv data/x_train.csv data/y_test.csv data/y_train.csv data/column_names.csv: scripts/preprocessing.py  
	python scripts/preprocessing.py \
		data/german_clean.csv \
		data

# 4) Data Modelling
# Input is x train & test, y train & test, column_names
# Outputs are: cross_validation_scores.csv, linear-reg_coefficients.csv, logistic_regression_C_optimization.csv, test_scores.csv, random forests and roc plot
model: data/cross_validation_scores.csv \
	data/linear-reg_coefficients.csv \
	data/logistic_regression_C_optimization.csv \
	data/test_scores.csv \
	img/0_random_forest_tree.png \
	img/1_random_forest_tree.png \
	img/2_random_forest_tree.png \
	img/roc_plot.png

data/cross_validation_scores.csv data/linear-reg_coefficients.csv data/logistic_regression_C_optimization.csv data/test_scores.csv img/0_random_forest_tree.png img/1_random_forest_tree.png img/2_random_forest_tree.png img/roc_plot.png: scripts/model.py
	python scripts/model.py \
	data/column_names.csv \
	data/x_train.csv \
	data/y_train.csv \
	data/x_test.csv \
	data/y_test.csv \
	img \
	data

# 5) Write and Render Quarto report in HTML and PDF
# Input is credit_risk_report.qmd
# Output is credit_risk_report.html, credit_risk_report.pdf
reports/credit_risk_report.html: reports/credit_risk_report.qmd edav prep model
	quarto render reports/credit_risk_report.qmd --to html

reports/credit_risk_report.pdf: reports/credit_risk_report.qmd edav prep model
	quarto render reports/credit_risk_report.qmd --to pdf

# Clean 

clean-dats:
	rm -f data/german.csv

clean-edav: 
	rm -f data/german_clean.csv \
		img/age.png \
		"img/Credit amount.png" \
		"img/Credit risk.png" \
		img/duration.png \
		"img/Existing credits.png" \
		"img/Liable people.png" \
		img/rate.png \
		img/residence.png \
		img/heatmap.png

clean-prep: 
	rm -f data/x_test.csv \
		data/x_train.csv \
		data/y_test.csv \
		data/y_train.csv \
		data/column_names.csv

clean-model: 
	rm -f data/cross_validation_scores.csv \
	data/linear-reg_coefficients.csv \
	data/logistic_regression_C_optimization.csv \
	data/test_scores.csv \
	img/0_random_forest_tree.png \
	img/1_random_forest_tree.png \
	img/2_random_forest_tree.png \
	img/roc_plot.png

clean-all: clean-dats clean-edav clean-prep clean-model
	rm -f reports/credit_risk_report.html reports/credit_risk_report.pdf
	rm -r reports/credit_risk_report_files