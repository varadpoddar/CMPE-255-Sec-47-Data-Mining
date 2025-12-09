# Assignment 4 — Summary (CRISP-DM, SEMMA, KDD)

Three methodologies applied to distinct tabular problems with executed notebooks, figures, and video scripts.

## CRISP-DM — House Prices (Regression)
- **Data**: 1,460 rows, 79 features; target `SalePrice` (right-skewed).  
- **Best model**: Log-target GradientBoosting (hold-out RMSE 27,626; MAE 16,654; R² 0.900). CV-tuned candidate: n_estimators=200, lr=0.125, depth=3 (CV RMSE ≈ 26,457).  
- **Key drivers**: Overall quality, living area, garage, basement, year built/remodeled (stable across permutation, SHAP, PDP).  
- **Artifacts**: `CRISP-DM/house_prices_crispdm_executed.ipynb`, embedded figures, `CRISP-DM/assignment.script`.  
- **Notes**: Log target improves metrics; slice MAE highlights higher errors on expensive homes and certain neighborhoods (e.g., NridgHt); monitor slices and drift if deploying.

## SEMMA — Adult Income (Classification)
- **Data**: 32,561 rows, 14 features; target income (<=50K/>50K), ~24% positive.  
- **Best model**: Tuned GradientBoostingClassifier; validation ROC-AUC ~0.93 (CV best ~0.929).  
- **Key drivers**: Capital gain, education level/num, hours per week, age, marital status, occupation (confirmed by SHAP).  
- **Artifacts**: `SEMMA/adult_income_semma_executed.ipynb`, embedded figures, `SEMMA/assignment.script`.  
- **Notes**: Class weighting/SMOTE explored; tree ensemble wins. Fairness/slice metrics (sex, marital status) should be monitored; calibration and drift checks recommended for deployment.

## KDD — Wine Quality (Regression)
- **Data**: 1,599 rows (red), 11 numeric chemistry features; target `quality`.  
- **Best model**: Tuned GradientBoostingRegressor; base RF RMSE ~0.55 (R² ~0.53); tuned GB CV RMSE ≈ 0.63 with params (n_estimators=400, depth=4, lr=0.05).  
- **Key drivers**: Alcohol, sulphates, volatile acidity (negative), density, sulfur dioxide (via SHAP).  
- **Artifacts**: `KDD/wine_quality_kdd_executed.ipynb`, embedded figures, `KDD/assignment.script`.  
- **Notes**: PCA shows ~80% variance in first ~5 components; residuals centered with modest spread; refit tuned GB on full train/hold-out for final numbers if serving.

## What we learned
- Methodologies guide structure but converge on similar best practices: solid preprocessing, baselines, tuned ensembles, and thorough interpretability (SHAP, PDP).
- Log transforms (CRISP-DM) and class-handling strategies (SEMMA) materially affect performance; slice analysis is key for fairness and monitoring.
- Even small datasets benefit from tuning and diagnostics (residuals/ROC/PR/SHAP/PDP); embedding figures in READMEs improves clarity for review and presentation.

## Video scripts
- See `CRISP-DM/assignment.script`, `SEMMA/assignment.script`, `KDD/assignment.script` for ready narration to walk through each notebook and figures.
