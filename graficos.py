import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
file_path = './assets/Sales Dataset.csv'
data = pd.read_csv(file_path)

# Gráfico de Barras: Vendas totais por Categoria
category_sales = data.groupby('Category')['Amount'].sum().sort_values(ascending=False)

# Plotando o gráfico de barras
plt.figure(figsize=(10,6))
category_sales.plot(kind='bar', color='pink')
plt.title('Vendas Totais por Categoria', fontsize=14)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Vendas Totais (Amount)', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Gráfico de Linhas: Vendas por Mês (Year-Month)
monthly_sales = data.groupby('Year-Month')['Amount'].sum()

# Plotando o gráfico de linhas
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line', color='pink', marker='o')
plt.title('Vendas Mensais (Year-Month)', fontsize=14)
plt.xlabel('Ano-Mês', fontsize=12)
plt.ylabel('Vendas Totais (Amount)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Gráfico de Pizza: Distribuição de Vendas por Modo de Pagamento
payment_sales = data.groupby('PaymentMode')['Amount'].sum()

# Plotando o gráfico de pizza
plt.figure(figsize=(8,8))
payment_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3', n_colors=len(payment_sales)))
plt.title('Distribuição das Vendas por Modo de Pagamento', fontsize=14)
plt.ylabel('')  # Remove the ylabel to make it cleaner
plt.show()

# Heatmap: Correlação entre as variáveis numéricas (Amount, Profit, Quantity)
correlation_matrix = data[['Amount', 'Profit', 'Quantity']].corr()

# Plotando o heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Correlação entre Amount, Profit e Quantity', fontsize=14)
plt.show()
