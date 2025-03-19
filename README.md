# README - Projeto de Análise de Dados com PCA, LDA, Fisher e MDC

## Descrição

Este projeto tem como principal objetivo desenvolver classificadores capazes de identificar se um URL está associado ou não a phishing, utilizando técnicas de reconhecimento de padrões.

## Dependências

Para rodar o projeto, é necessário instalar as seguintes bibliotecas:

```bash
pip install pandas numpy matplotlib seaborn plotly scipy scikit-learn statsmodels
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
```

## Estrutura do Código

1. **Carregamento dos dados**: 
   - Os dados são lidos e processados
2. **Normalização**: 
   - Os dados são normalizados
3. **Kolmogorov-Smirnov Test**:
   - KS-Test no dataset completo 
   - KS-Test separado por target
4. **Kruskal Wallis Test**
5. **PCA (Análise de Componentes Principais)**:
6. **LDA (Análise Discriminante Linear)**:
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

## Como Executar o Projeto

1. Abrir o Jupyter Notebook ou um ambiente Python compatível.
2. Certifiquar-se de que todas as dependências estão instaladas.
3. Execute as células do notebook `projeto.ipynb` por ordem.
4. Os resultados e gráficos serão gerados automaticamente.

## Autor

Desenvolvido por Ana Morais e Fernanda Fernandes


