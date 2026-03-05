# A Busca de Dados: Preparando o Terreno para a Inteligência Cardiológica

Este repositório documenta a etapa de curadoria e investigação de dados para um projeto de Inteligência Artificial aplicado à Cardiologia. O foco desta fase é buscar, identificar e coletar conjuntos de dados cardiológicos, compreender a sua procedência, avaliar a sua integridade, relevância clínica e como diferentes modalidades (numérica, textual e visual) podem ser exploradas por algoritmos de IA.

## 1. Dados Nnuméricos: o contexto metabólico e funcional
Para esta categoria, foram selecionados datasets que representam os sinais vitais e os biomarcadores fundamentais para a saúde cardiovascular.

### Origem e Objetivos dos Datasets

#### Cardiovascular Disease Dataset
Originário de estudos clínicos com cerca de 70.000 pacientes. O objetivo é fornecer uma base estatística robusta sobre o perfil de saúde sistêmica.

#### Heart Failure Prediction Dataset
Um dataset consolidado que une cinco conjuntos de dados hospitalares distintos. O objetivo é identificar padrões que precedem a insuficiência cardíaca.

#### Variáveis relevantes e justificativa clínica

> - **Pressão Arterial Sistólica/Diastólica**<br>Essencial para identificar a hipertensão, o principal preditor de danos vasculares e eventos agudos.<br>
>
> - **Colesterol**<br>Variável crítica para avaliar o risco de aterosclerose e obstrução arterial a longo prazo.
>
> - **Frequência Cardíaca Máxima (MaxHR)**<br>Indica a eficiência do bombeamento cardíaco sob estresse, sendo um marcador vital para a reserva funcional do coração.
>
> - **Depressão de ST (Oldpeak)**<br>Variável derivada do eletrocardiograma (ECG) que indica isquemia miocárdica (falta de oxigenação no músculo cardíaco).
> 

**Relevância para IA**<br>
Para um projeto de saúde, essas variáveis funcionam como "features" de alta correlação, permitindo que modelos de aprendizado de máquina aprendam a distinguir entre padrões de normalidade e estados patológicos com base em evidências fisiológicas concretas.

2. Dados Textuais: Processamento de Linguagem Natural (NLP)
A análise de dados não estruturados permite que a IA compreenda a literatura médica e o contexto epidemiológico.

Fontes Selecionadas
Epidemiologia da Insuficiência Cardíaca no Brasil: Artigo científico publicado nos Arquivos Brasileiros de Cardiologia (SBC/SciELO). Link de Referência

Diretrizes Brasileiras de Insuficiência Cardíaca: Documento normativo oficial que estabelece os protocolos de diagnóstico e tratamento no Brasil. Link de Referência

Exploração via Algoritmos de NLP
Extração de Entidades Nomeadas (NER): Algoritmos podem ser utilizados para identificar automaticamente sintomas (ex: dispneia, fadiga) e medicamentos nos textos, transformando prosa em dados estruturados.

Classificação de Tópicos (Topic Modeling): Permite organizar vastos volumes de literatura, separando discussões sobre "Sintomas" de "Protocolos de Tratamento".

Sumarização Automática: Essencial para extrair pontos-chave de diretrizes extensas, entregando ao profissional de saúde apenas as condutas relevantes para o perfil do paciente em análise.

Justificativa: A análise textual humaniza o projeto de IA, garantindo que o sistema esteja alinhado com as normas médicas vigentes e seja capaz de processar o conhecimento acumulado em décadas de literatura científica.

3. Dados Visuais: Diagnóstico por Visão Computacional
Os dados visuais permitem que a IA identifique alterações físicas e estruturais que podem não ser captadas em exames laboratoriais puros.

Origem e Objetivos dos Datasets
NIH ChestX-ray14: Conjunto de dados proveniente do National Institutes of Health (EUA). O objetivo é fornecer uma base massiva de radiografias de tórax rotuladas para o treinamento de diagnósticos assistidos por computador.

Exploração via Visão Computacional
Detecção de Padrões e Anomalias: Algoritmos podem ser treinados para identificar "infiltrados" ou "edemas" nos pulmões, sinais indiretos de falha cardíaca.

Identificação de Bordas (Segmentação): Utilizada para isolar a silhueta do coração e calcular o Índice Cardiotorácico. Se o coração ocupa mais de 50% da largura do tórax, o sistema sinaliza Cardiomegalia.

Reconhecimento de Dispositivos Implantados: Identificação automática de marca-passos ou stents, fornecendo contexto vital sobre o histórico cirúrgico do paciente.

Importância para IA: A visão computacional atua como um multiplicador de eficiência, permitindo a triagem ultrarrápida de exames em unidades de emergência e reduzindo a variabilidade interpretativa entre diferentes examinadores.

Conclusão da Etapa
Esta fase de pesquisa demonstra que um projeto de IA em saúde bem-sucedido depende da integração de múltiplas fontes de dados. Ao dominar a origem e o potencial de dados numéricos, textuais e visuais, estabelecemos uma base sólida para o desenvolvimento de soluções que são tecnicamente precisas e clinicamente relevantes.