# Sistema de Detecção de Intrusão (IDS) para Redes CAN Automotivas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-PSGS-blue?style=for-the-badge&logo=linkedin&link=URL_DO_SEU_LINKEDIN)](https://www.linkedin.com/in/paulo-souza-862a67292/)

> **Contexto do Projeto:** Este repositório contém o desenvolvimento do projeto final da disciplina de Redes Automotivas (IF747) do Centro de Informática (CIn) da Universidade Federal de Pernambuco (UFPE). O projeto foi desenvolvido em Julho/Agosto de 2025.

---

## 📖 Sobre o Projeto

[cite_start]O objetivo central deste projeto é **coletar datasets com dados maliciosos e benignos e propor, implementar e validar experimentalmente sistemas de detecção de intrusão baseados em Machine Learning para uma rede veicular CAN (Controller Area Network)**[cite: 54].

A segurança em redes automotivas é uma área crítica, especialmente com o aumento da conectividade dos veículos. [cite_start]Este trabalho explora a implementação de um Sistema de Detecção de Intrusão (IDS) de baixo custo, utilizando uma Raspberry Pi, para monitorar o tráfego da rede CAN e identificar atividades maliciosas em tempo real, como as que ganharam notoriedade em reportagens sobre hacks em veículos[cite: 15, 18].

---

## ✨ Principais Funcionalidades

-   **Coleta de Dados:** Scripts para captura e registro de tráfego em tempo real do barramento CAN.
-   **Simulação de Ataques Cibernéticos:** Implementação de quatro tipos distintos de ataques veiculares para geração de datasets realistas:
    -   Denial of Service (DoS)
    -   Message Spoofing
    -   Replay Attack
    -   Fuzzing Attack
-   **Detecção de Intrusão:** Desenvolvimento de um sistema baseado em Machine Learning para classificar o tráfego da rede como "Benigno" ou "Malicioso".
-   [cite_start]**Ambiente de Baixo Custo:** Validação do conceito utilizando hardware acessível, como a Raspberry Pi [cite: 86] [cite_start]e um módulo CAN MCP2515[cite: 87].

---

## 🛠️ Tecnologias Utilizadas

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=white" alt="Raspberry Pi" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</div>

---
---

## ⚙️ Configuração do Ambiente

### Hardware
* [cite_start]Raspberry Pi Model 3 ou 4 [cite: 86]
* [cite_start]Módulo CAN MCP2515 com transceptor TJA1050 [cite: 87]
* Cabos para conexão com o barramento CAN

### Software
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-NOME-DE-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-NOME-DE-USUARIO/NOME-DO-REPOSITORIO.git)
    cd NOME-DO-REPOSITORIO
    ```
2.  **Instale as dependências do Python:**
    ```bash
    pip install python-can pandas scikit-learn
    ```
3.  **Configure a interface CAN na Raspberry Pi:**
    Antes de executar qualquer script, ative a interface `can0` no terminal.
    ```bash
    sudo ip link set can0 down
    sudo ip link set can0 up type can bitrate 500000
    ```

---

## 🚀 Modo de Uso

A coleta de dados para cada cenário de ataque é realizada utilizando dois terminais simultaneamente.

### Passo 1: Coleta de Dados

1.  **Abra dois terminais** na sua Raspberry Pi.

2.  **No Terminal 1 (Ouvinte):** Inicie o script de logging. Lembre-se de alterar a variável `OUTPUT_FILENAME` dentro do `can_logger.py` para um nome descritivo (ex: `log_benigno.csv`, `log_dos_attack.csv`).
    ```bash
    # Navegue até a pasta correta
    cd 2_data_collection/
    # Execute o logger
    python can_logger.py
    ```

3.  **No Terminal 2 (Atacante):** Inicie o script do ataque desejado.
    ```bash
    # Navegue até a pasta correta
    cd 1_scripts_ataque/
    # Exemplo para o ataque de DoS
    python dos_attack.py
    ```
4.  Aguarde a finalização dos scripts. O arquivo CSV com os dados capturados estará salvo na pasta `2_data_collection/`. Mova-o para a pasta `3_datasets/` para manter a organização.

### Passo 2: Treinamento do Modelo (Próximas Etapas)
Com os datasets coletados, a próxima fase do projeto envolve:
1.  Carregar os dados com Pandas.
2.  Realizar a extração de *features* (engenharia de características).
3.  Treinar um modelo de Machine Learning (ex: Isolation Forest, Random Forest) com Scikit-learn.
4.  Validar a eficácia do modelo na detecção dos ataques.

---

## ⚔️ Ataques Implementados

* **Denial of Service (DoS):** Inunda o barramento CAN com mensagens de alta prioridade para impedir a comunicação legítima dos ECUs.
* **Message Spoofing:** Personifica um ECU legítimo para injetar dados falsos ou comandos maliciosos na rede de forma periódica.
* **Replay Attack:** Grava uma sequência de mensagens de uma ação legítima (ex: destravar portas) e a reenvia posteriormente para executar o comando de forma não autorizada.
* **Fuzzing Attack:** Envia dados e/ou IDs completamente aleatórios para o barramento, com o objetivo de causar falhas e descobrir vulnerabilidades nos ECUs.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Feito com ❤️ por **[PSGS] e [DABN]**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-SEU_NOME-blue?style=flat&logo=linkedin&link=URL_DO_SEU_LINKEDIN)](https://www.linkedin.com/in/paulo-souza-862a67292/)
[![GitHub](https://img.shields.io/badge/GitHub-SEU_USUARIO-black?style=flat&logo=github&link=https://github.com/SEU_USUARIO)](https://github.com/paulosouza-ec)

