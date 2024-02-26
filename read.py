from google.colab import auth
import pandas as pd
import gspread
from google.auth import default
import re

class Read:
    def __init__(self):
        # Autentica o usuário
        auth.authenticate_user()
        creds, _ = default()
        self.gc = gspread.authorize(creds)

    def name_sheet(self, spreadsheet_name, sheet_name=None):
        planilha = self.gc.open(spreadsheet_name)
        # Escolhe a aba especificada pelo nome ou ID, ou a primeira aba por padrão
        if sheet_name:
            try:
                # Tenta abrir a aba pelo nome
                aba = planilha.worksheet(sheet_name)
            except gspread.exceptions.WorksheetNotFound:
                # Se não encontrada pelo nome, tenta pelo ID (como string)
                aba = planilha.get_worksheet_by_id(int(sheet_name))
        else:
            # Se nenhum nome ou ID for fornecido, abre a primeira aba
            aba = planilha.sheet1

        # Lê os dados da aba selecionada
        valores = aba.get_all_values(value_render_option='FORMATTED_VALUE')

        # Transforma os valores em um DataFrame do Pandas
        df = pd.DataFrame(valores)
        df.columns = df.iloc[0] # Define a primeira linha como cabeçalho
        df = df.drop(0) # Remove a primeira linha de dados
        return df
