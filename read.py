from google.colab import auth
import pandas as pd
import gspread
from google.auth import default

class Read:
    def __init__(self):
        # Autentica o usuário
        auth.authenticate_user()
        creds, _ = default()
        self.gc = gspread.authorize(creds)

    def sheet(self, url):
        # Abre a planilha especificada pelo URL e lê os dados
        planilha = self.gc.open_by_url(url)
        aba = planilha.sheet1
        valores = aba.get_all_values(value_render_option='FORMATTED_VALUE')

        # Transforma os valores em um DataFrame do Pandas
        df = pd.DataFrame(valores)
        df.columns = df.iloc[0] # Define a primeira linha como cabeçalho
        df = df.drop(0) # Remove a primeira linha de dados
        return df.head()

# Uso da classe
#url_da_planilha = 'https://docs.google.com/spreadsheets/d/...'
#read = Read()
#df = read.sheet(url_da_planilha)
#print(df)
