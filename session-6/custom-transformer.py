import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# TODO: Modify this list to include the numerical columns
NUMERICAL_VARS = ['pclass', 'age', 'sibsp', 'parch', 'fare']

# Crear custom transformer


class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables):
        if not isinstance(variables, list):
            # self.variables = [variables]+"_nan"
            print("not isinstance")
        else:
            self.variables = variables
            print("isinstance")

    def fit(self, X, y):
        return self

    def transform(self, X):
        # TODO: Put your code here
        for var in self.variables:
            if pd.api.types.is_numeric_dtype(X[var]):
                new_var = var + "_nan"
                X[new_var] = pd.isna(X[var]).astype("int8")
             #   X[new_var] = X[new_var].astype("bool")
        return X


# Leer el csv sin aplicar transformaciones
df = pd.read_csv("module-2/session-6/activity/raw-data.csv")

# Imprimir los primeros datos
print(df.head(10))

mi = MissingIndicator(variables=NUMERICAL_VARS)
# Aplicar las transformaciones
df_mi = mi.transform(df)

# Imprimir resultados despues de las transformaciones
print(df_mi.head(20))
