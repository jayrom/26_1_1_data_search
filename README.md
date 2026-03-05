# A Busca de Dados: Preparando o Terreno para a Inteligência Cardiológica

Este repositório documenta a etapa de curadoria e investigação de dados para um projeto de Inteligência Artificial aplicado à Cardiologia. O foco desta fase é buscar, identificar e coletar conjuntos de dados cardiológicos, compreender a sua procedência, avaliar a sua integridade, relevância clínica e como diferentes modalidades (numérica, textual e visual) podem ser exploradas por algoritmos de IA.

## 1. Dados numéricos<br><sub>O contexto metabólico e funcional<sub>
Para esta categoria, foram selecionados datasets que representam os sinais vitais e os biomarcadores fundamentais para a saúde cardiovascular.

### Origem e Objetivos dos Datasets

Nesta seção, exploramos a procedência e o impacto dos dados que fundamentam as análises quantitativas.

#### Cardiovascular Disease Dataset
> - **Histórico e Contexto**<br>Este dataset é um clássico da área de saúde, frequentemente utilizado para benchmarking de algoritmos de classificação. Ele foca em exames de rotina para identificar a presença de doenças cardiovasculares em uma fase assintomática.
>
> - **Origem**<br>Dados coletados na Rússia (Mendeley Data / Svetlana Ulianova), com registros consolidados por volta de 2019.
>
> - **Estatísticas (Kaggle)**<br>Possui nota de Usabilidade 10.0, mais de 10.000 upvotes e centenas de milhares de downloads, sendo citado em diversos artigos acadêmicos sobre Random Forest e XGBoost.
>
> - **Licença**<br>Attribution 4.0 International (CC BY 4.0).

#### Heart Failure Prediction Dataset
> - **Histórico e Contexto**<br>Trata-se de um dataset "sintético" resultante da combinação de 5 bases de dados hospitalares independentes (Cleveland, Hungria, Suíça, Long Beach e Stalog). É o dataset mais abrangente disponível publicamente para prever falhas cardíacas com base em sintomas clínicos.
>
> - **Origem**<br>Consolidado em 2021 (Multinacional: EUA, Hungria e Suíça).
>
> - **Estatísticas (Kaggle)**<br>Usabilidade 10.0, cerca de 6.000 upvotes. É reconhecido por não possuir valores nulos, facilitando o treinamento de modelos robustos.
>
> - **Licença**<br>Open Data Commons Attribution License (ODC-By) v1.0.

#### Variáveis relevantes e justificativa clínica

> - **Pressão Arterial Sistólica/Diastólica**<br>Essencial para identificar a hipertensão, o principal preditor de danos vasculares e eventos agudos.<br>
>
> - **Colesterol**<br>Variável crítica para avaliar o risco de aterosclerose e obstrução arterial a longo prazo.
>
> - **Frequência Cardíaca Máxima (MaxHR)**<br>Indica a eficiência do bombeamento cardíaco sob estresse, sendo um marcador vital para a reserva funcional do coração.
>
> - **Depressão de ST (Oldpeak)**<br>Variável derivada do eletrocardiograma (ECG) que indica isquemia miocárdica (falta de oxigenação no músculo cardíaco).
> 

**Relevância para IA** - Para um projeto de saúde, essas variáveis funcionam como "features" de alta correlação, permitindo que modelos de aprendizado de máquina aprendam a distinguir entre padrões de normalidade e estados patológicos com base em evidências fisiológicas concretas.

## 2. Dados Textuais<br><sub>Processamento de Linguagem Natural (NLP)<sub>
A análise de dados não estruturados permite que a IA compreenda a literatura médica e o contexto epidemiológico.

### Fontes Selecionadas

#### Epidemiologia da Insuficiência Cardíaca no Brasil
Artigo científico publicado nos Arquivos Brasileiros de Cardiologia (SBC/SciELO). Link de Referência

#### Diretrizes Brasileiras de Insuficiência Cardíaca
Documento normativo oficial que estabelece os protocolos de diagnóstico e tratamento no Brasil. Link de Referência

#### Exploração dos textos via algoritmos de NLP
Extração de Entidades Nomeadas (NER): Algoritmos podem ser utilizados para identificar automaticamente sintomas (ex: dispneia, fadiga) e medicamentos nos textos, transformando prosa em dados estruturados.

Classificação de Tópicos (Topic Modeling): Permite organizar vastos volumes de literatura, separando discussões sobre "Sintomas" de "Protocolos de Tratamento".

Sumarização Automática: Essencial para extrair pontos-chave de diretrizes extensas, entregando ao profissional de saúde apenas as condutas relevantes para o perfil do paciente em análise.

Justificativa: A análise textual humaniza o projeto de IA, garantindo que o sistema esteja alinhado com as normas médicas vigentes e seja capaz de processar o conhecimento acumulado em décadas de literatura científica.

## 3. Dados Visuais<br><sub>Diagnóstico por Visão Computacional<sub>
Os dados visuais permitem que a IA identifique alterações físicas e estruturais que podem não ser captadas em exames laboratoriais puros.

### Origem e Objetivos do Dataset

#### NIH ChestX-ray14

> - **Histórico e Contexto**<br>
O NIH ChestX-ray14 é um conjunto de dados proveniente do National Institutes of Health (EUA), cujo objetivo é fornecer uma base massiva de radiografias de tórax rotuladas para o treinamento de diagnósticos assistidos por computador. Constitui um marco na Visão Computacional Médica, tendo substituído o antigo ChestX-ray8, expandindo a capacidade de detecção de 8 para 14 patologias diferentes através de mineração de texto em relatórios radiológicos.
>
> - **Origem**<br>
Estados Unidos (NIH Clinical Center), publicado originalmente em 2017.
>
> - **Estatísticas**<br>
É um dos datasets mais citados no Google Scholar na área de radiologia computacional. No Kaggle, a amostra reduzida possui Usabilidade 8.2 e milhares de menções em competições de detecção de pneumonia e cardiomegalia.
>
> - **Licença**<br>
Domínio Público (CC0: Public Domain), permitindo uso irrestrito para pesquisa.





Exploração via Visão Computacional
Detecção de Padrões e Anomalias: Algoritmos podem ser treinados para identificar "infiltrados" ou "edemas" nos pulmões, sinais indiretos de falha cardíaca.

Identificação de Bordas (Segmentação): Utilizada para isolar a silhueta do coração e calcular o Índice Cardiotorácico. Se o coração ocupa mais de 50% da largura do tórax, o sistema sinaliza Cardiomegalia.

Reconhecimento de Dispositivos Implantados: Identificação automática de marca-passos ou stents, fornecendo contexto vital sobre o histórico cirúrgico do paciente.

Importância para IA: A visão computacional atua como um multiplicador de eficiência, permitindo a triagem ultrarrápida de exames em unidades de emergência e reduzindo a variabilidade interpretativa entre diferentes examinadores.

## Conclusão<br><sub>Qualidade, governança e aplicabilidade ao cenário brasileiro<sub>

A fundamentação desta etapa demonstra que a eficácia da Inteligência Artificial não reside apenas no volume, mas na qualidade e procedência do dado. Ao selecionar datasets com índices de usabilidade máximos (10.0 no Kaggle) e reconhecidos globalmente (NIH, Mendeley), garantimos uma base de treinamento validada e livre de ruídos estatísticos.

Embora os dados numéricos e visuais possuam origem internacional (EUA, Rússia e Europa), sua aplicabilidade ao cenário brasileiro é validada pela integração com os Dados Textuais selecionados. Ao cruzar as evidências globais com a Epidemiologia da Insuficiência Cardíaca no Brasil (SciELO) e as Diretrizes da Sociedade Brasileira de Cardiologia, criamos um modelo de "Localização de Dados". Isso garante que os padrões universais de patologia cardiovascular sejam interpretados sob a ótica das particularidades demográficas e dos protocolos de saúde pública do SUS.

A estratégia de downsampling estratificado para 300 amostras complementa essa visão, permitindo um equilíbrio metodológico entre as classes (doença vs. saúde). Com essa tríade de dados (numéricos, textuais e visuais) devidamente licenciados, estabelecemos um ecossistema de dados transparente, ético e — acima de tudo — clinicamente relevante para a realidade da cardiologia brasileira, pronto para sustentar as fases subsequentes de modelagem e arquitetura preditiva.