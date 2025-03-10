import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import kstest, kruskal, norm


DATA_PATH = 'PhiUSIIL_Phishing_URL_Dataset.csv'

def load_data(data_path=DATA_PATH):
    data = pd.read_csv(data_path)
    
    print("\nInformações do Dataset:")
    print(data.info())
    
    print("\nPrimeiras linhas do Dataset:")
    print(data.head(10))
    
    print("\nEstatísticas do Dataset:")
    print(data.describe())
    
    print("\nValores nulos no Dataset:")
    print(data.isnull().sum())
    
    # Modificar a a coluna label para target, para ser de fácil perceção ??
    data.rename(columns={'label': 'target'}, inplace=True)
    
    # Remover colunas categóricas
    categorical_columns = data.select_dtypes(include=['object']).columns
    data.drop(categorical_columns, axis=1, inplace=True)
    
    #Vai apresentar o nome das colunas
    #print("Columns: " + ", ".join(list(map(str, data.columns))))
    
    return data

def separar_features_target(data):
    X = data.copy()
    X.drop('target', axis=1,inplace=True)
    y = data['target'].copy()
    
    return X,y


def normalizar_features(X): # 
    scaler = StandardScaler() # É o mesmo que usar Z_score, pois a média é 0 e o desvio padrão é 1
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    return X


data = load_data()
X, y  = separar_features_target(data)
X = normalizar_features(X)

def plot_class_distribution(data):
    
    values = data['target'].value_counts()
    keys = ['Legítimo', 'Phishing']
    
    fig_pie = px.pie(names=keys, values=values, title='Distribuição das classes (%)')
    
    fig_bar = px.bar(x = keys, y=values, labels={'x': 'Classe', 'y': 'Contagem'},
                     title="Distribuição das Classes (Phishing vs. Legítimo)")
    
    fig_pie.show()
    fig_bar.show()
    
    print("\nPerc. of class 1 (Legítimo): " + str(data['target'].sum() / data.shape[0] * 100) + " %")

    #São muitos features, como simplificar aqui para verificar a matriz de correlação?
    
    # Com matplotlib
    corr = data.corr()
    
    plt.figure(figsize=(40, 40))
    sns.heatmap(corr, annot=True, vmin=-1.0, cmap='mako')
    plt.title("Matriz de Correlação")
    plt.show()
    
    ''' 
    # Com plotly
    fig_corr = px.imshow(corr, title="Matriz de Correlação",
                     color_continuous_scale= 'blues',
                     labels={'x': 'Features', 'y': 'Features', 'color': 'Correlação'})
    fig_corr.show()
    '''

    
    
#plot_class_distribution(data)


def KW_test(data, features):
    Hs = {}
    
    # Índices das classes
    ix_legitimo = np.where(y == 1)[0]
    ix_phishing = np.where(y == 0)[0]
    
    # Aplicar Kruskal-Wallis para cada feature
    for i in range(X.shape[1]):
        stat = kruskal(X.iloc[ix_legitimo, i], X.iloc[ix_phishing, i]) # iloc trabalha com pandas, flatten trabalha com numpy
        Hs[features[i]] = stat  
 
    Hs_sorted = sorted(Hs.items(), key=lambda x: x[1], reverse=True)
    
    return Hs_sorted

Hs_sorted = KW_test(data, X.columns)
print(Hs_sorted)

def plot_features(X, y, top_features):
    data = X.copy()
    data['Class'] = y.map({0: 'Phishing', 1:'Legítimo'})
    
    color_discrete_map = {'Legítimo': 'lightskyblue', 'Phishing': 'hotpink'}
    
    for feature in top_features:
        fig = px.violin(data, y=feature, x='Class', box=True, points="all", 
                        title=f'Violin plot for {feature}', color='Class', 
                        color_discrete_map=color_discrete_map)
        fig.show()
        
plot_features(X, y, [x[0] for x in Hs_sorted[:1]])