**Panel vs Pooled Data**

Panel data and pooled data are two types of data commonly used in statistics and econometrics, particularly in longitudinal studies and regression analysis.

1. Panel Data:
   - Panel data, also known as longitudinal data or cross-sectional time-series data, is a type of dataset where observations are made on the same units (e.g., individuals, firms, countries) over multiple time periods.
   - Each unit in the dataset is observed repeatedly over time, allowing researchers to analyze changes within units over time as well as differences between units.
   - Panel data typically consists of both cross-sectional and time-series dimensions, making it valuable for studying both individual and temporal variations.
   - Panel data analysis methods include fixed effects models, random effects models, and pooled ordinary least squares (OLS) regression.

2. Pooled Data:
   - Pooled data refers to a dataset that combines observations from different units (e.g., individuals, firms) without any specific organization or structure based on time or individual units.
   - Unlike panel data, pooled data does not have repeated observations for the same units over multiple time periods. Instead, it consists of independent observations from different units.
   - Pooled data can be used for cross-sectional analysis, where each observation is treated as independent and no consideration is given to time-related effects or individual heterogeneity.
   - Pooled data can also be used in pooled OLS regression, where all observations are pooled together to estimate the coefficients of the regression equation, assuming no individual-specific effects or time trends.

Since our data consists of repeated observations on the same units over time, it allows for the analysis of both individual and temporal variations in our data. 

**Regression Analysis for Panel Data**

1.	**Fixed Effects Model:**
This model accounts for individual-specific effects by including dummy variables for each individual or entity in the regression equation. Fixed effects models are suitable when there are time-invariant unobserved heterogeneity among entities.
Since there are individual-specific effects (e.g., company-specific characteristics) that are time-invariant or slowly changing over time in our data, we will use a fixed effects model. This model allows us to control for these individual effects. Fixed effects models are suitable when you want to estimate the effect of changes in independent variables within each company while controlling for time-invariant factors.

2.	**Random Effects Model:**
Random effects models assume that individual-specific effects are random variables. These models estimate the variance components of the random effects and use them to correct standard errors. Random effects models are appropriate when individual-specific effects are assumed to be uncorrelated with the independent variables.

**3. Pooled OLS Regression:**
This is the simplest form of panel data regression. Pooled OLS regression pools the data across all companies and time periods and estimates a single regression equation. However, this approach ignores individual-specific effects and potential correlation across time for the same company, which may lead to biased and inefficient estimates if there are unobserved individual effects.

Given the nature of our data—entries for multiple companies over a period of 10 years—fixed effects or random effects models are commonly used due to their ability to account for individual-specific effects. Conducting diagnostic tests and sensitivity analyses can help guide and validate our decision and ensure the robustness of our results.


References
- https://www.reed.edu/economics/parker/s10/312/notes/Notes8.pdf
- https://towardsdatascience.com/fixed-effect-regression-simply-explained-ab690bd885cf