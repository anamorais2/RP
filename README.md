# README - Projeto de Reconhecimento de Padrões

## Descrição

Este projeto tem como principal objetivo desenvolver classificadores capazes de identificar se um URL está associado ou não a phishing, utilizando técnicas de reconhecimento de padrões.

## Dependências

Para rodar o projeto é necessário ter uma versão Python 3.x, Jupyter Notebook (para correr o código) e instalar as seguintes bibliotecas:

```bash
pip install pandas numpy matplotlib seaborn plotly scipy scikit-learn statsmodels pymrmr
```

Ou individualmente:

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install plotly
pip install scipy
pip install scikit-learn
pip install statsmodels
pip install pymrmr
```

## Dataset
Foi utilizado um conjunto de dados PhiUSIIL_Phishing_URL_Dataset.csv.

Este conjunto de dados inclui 134.850 URLs legítimos e 100.945 URLs de phishing. As features foram extraídas tanto do código-fonte da página web associada à URL como da própria estrutura da URL. Além disso, algumas features foram derivadas a partir destas características base (como CharContinuationRate, URLTitleMatchScore, URLCharProb e TLDLegitimateProb), sendo designadas como hyper-features.

No total, o dataset contém 54 features. Para facilitar a análise, consideramos apenas as features não categóricas.


## Estrutura do Código

1. **Carregamento de dados**
2. **Normalização**
3. **Kolmogorov-Smirnov Test**:
   - KS-Test no dataset completo 
   - KS-Test separado por target
4. **Kruskal Wallis Test**
5. **PCA (Análise de Componentes Principais)**
6. **LDA (Análise Discriminante Linear)**
7. **MDC**
   - Euclidian Distance
   - Mahalanobis Distance
8. **Fisher LDA**: Usamos LDA para reduzir as variáveis e aplicamos MDC
9. **LDA + MDC**  
   - Geração de relatórios '.csv' e gráficos de visualização
10. **PCA + MDC**
   - Geração de relatórios '.csv'
11. **PCA + Fisher LDA**
   - Geração de relatórios '.csv'
12. **Bayes Classification**
   - Geração de relatórios '.csv'
13. **KNN Classificador**
   - Geração de relatórios '.csv'
14. **Suport Vector Machine**
   - Geração de relatórios '.csv'
15. **Random Forest**
   - Geração de relatórios '.csv'
   

## Como Executar o Projeto

1. Abrir o Jupyter Notebook ou um ambiente Python compatível.
2. Certifiquar-se de que todas as dependências estão instaladas.
3. Execute as células do notebook `projeto.ipynb` por ordem.
4. Os resultados e gráficos serão gerados automaticamente.

## Autor

Desenvolvido por Ana Morais e Fernanda Fernandes


