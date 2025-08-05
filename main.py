import pandas as pd
import numpy as np

#Mapeamento de arquivos para seus respectivos rótulos numéricos
file_to_label_map = {
    'benigno.csv': 0,
    'dos_attack.csv': 1,
    'fuzzing_attack.csv': 2,
    'replay.csv': 3,
    'diagnostic.csv': 4
}

#Mapeamento de rótulos para nomes
label_to_name_map = {
    0: 'Benign',
    1: 'DoS_Attack',
    2: 'Fuzzing_Attack',
    3: 'Replay_Attack',
    4: 'Diagnostic_Attack'
}

all_dfs = []

#Carrega cada arquivo e atribui o rótulo correto
for file, label in file_to_label_map.items():
    try:
        df = pd.read_csv(file)
        df['Label'] = label
        all_dfs.append(df)
        print(f"Carregado '{file}' e rotulado como: {label} ({label_to_name_map[label]})")
    except FileNotFoundError:
        print(f"Aviso: Arquivo '{file}' não encontrado.")

#Combina todos os dataframes
combined_df = pd.concat(all_dfs, ignore_index=True)

#Embaralha o dataset para misturar as classes
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)


#Remove colunas desnecessárias para este modelo inicial
features_df = combined_df.drop(columns=['Timestamp', 'IsExtended', 'Data'], errors='ignore')

#Converte a coluna 'ID' (nome correto) de hexadecimal para inteiro
features_df['ID'] = features_df['ID'].apply(lambda x: int(str(x), 16))

#Seleciona as colunas finais
final_df = features_df[['ID', 'DLC', 'Label']]

print("\nDistribuição das Classes no Dataset Final: ")
print(final_df['Label'].map(label_to_name_map).value_counts())

#Salva o dataframe processado
output_filename = 'processed_multiclass_can_data.csv'
final_df.to_csv(output_filename, index=False)

print(f"\n Concluído. Arquivo salvo como '{output_filename}'.")