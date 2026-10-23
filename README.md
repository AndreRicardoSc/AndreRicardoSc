<!--
  GitHub Profile README — André Ricardo Schultz (@AndreRicardoSc)
  Idioma: Português (BR). Todos os dados foram verificados nos repositórios.
  Itens que dependem de você estão marcados com [PREENCHER].
-->

<h1 align="center">André Ricardo Schultz</h1>

<h3 align="center">Full Stack Developer</h3>

<p align="center">
  <em>"Transformo problemas reais em aplicações completas — do modelo de dados ao pixel final."</em>
</p>

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1200&color=3FB950&center=true&vCenter=true&width=600&lines=Desenvolvimento+Full+Stack;Django+%2B+DRF+%7C+Vue+3+%2B+Vite;APIs+REST+e+WebSockets;Aprendendo+todos+os+dias"
    alt="Full Stack Developer — Django, DRF, Vue 3, Vite, APIs REST e WebSockets"
    width="600"
  />
</p>

<p align="center">
  <a href="https://github.com/AndreRicardoSc?tab=followers">
    <img src="https://img.shields.io/github/followers/AndreRicardoSc?label=Seguidores&style=flat-square&color=3FB950&logo=github" alt="Seguidores no GitHub" />
  </a>
  <img src="https://img.shields.io/badge/Localiza%C3%A7%C3%A3o-Santa%20Catarina%2C%20Brasil-2F81F7?style=flat-square&logo=googlemaps&logoColor=white" alt="Santa Catarina, Brasil" />
  <img src="https://komarev.com/ghpvc/?username=AndreRicardoSc&label=Visualiza%C3%A7%C3%B5es&color=3FB950&style=flat-square" alt="Visualizações do perfil" />
</p>

---

## Sobre mim

Sou estudante do **terceiro ano do ensino médio integrado ao curso técnico em Informática para a Internet**, no **IFC — Campus Araquari** (Santa Catarina, Brasil).

Trabalho principalmente no desenvolvimento de aplicações **full stack**: defino as regras de negócio, modelo os dados, construo a **API REST** no backend e desenvolvo a interface no frontend, cuidando também de autenticação, integração e experiência de uso. Meu foco atual está em **Python/Django com Django REST Framework** no servidor e **Vue.js 3 com Vite e Pinia** no cliente.

Gosto de entender o problema antes de escrever código, de organizar o projeto em camadas claras e de aprender novas ferramentas resolvendo problemas concretos. A maior parte do que sei veio de projetos reais — dois deles em equipe, um deles com contexto de pesquisa educacional.

**Interesses:** desenvolvimento web, APIs REST, arquitetura de software, bancos de dados, automação, interfaces modernas, acessibilidade e experiência do usuário.

---

## Tecnologias e ferramentas

### Usadas em projetos

**Linguagens**

<p>
  <img src="https://skillicons.dev/icons?i=python,js,html,css" alt="Python, JavaScript, HTML e CSS" />
</p>

**Frontend**

<p>
  <img src="https://skillicons.dev/icons?i=vue,vite,pinia,tailwind" alt="Vue.js, Vite, Pinia e Tailwind CSS" />
</p>

<p>
  <img src="https://img.shields.io/badge/GSAP-88CE02?style=flat-square&logo=greensock&logoColor=black" alt="GSAP" />
  <img src="https://img.shields.io/badge/Vue_Router-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white" alt="Vue Router" />
  <img src="https://img.shields.io/badge/Axios-5A29E4?style=flat-square&logo=axios&logoColor=white" alt="Axios" />
</p>

**Backend e banco de dados**

<p>
  <img src="https://skillicons.dev/icons?i=django,postgres,sqlite,redis" alt="Django, PostgreSQL, SQLite e Redis" />
</p>

<p>
  <img src="https://img.shields.io/badge/Django_REST_Framework-A30000?style=flat-square&logo=django&logoColor=white" alt="Django REST Framework" />
  <img src="https://img.shields.io/badge/Django_Channels-092E20?style=flat-square&logo=django&logoColor=white" alt="Django Channels" />
  <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="SimpleJWT" />
  <img src="https://img.shields.io/badge/OpenAPI_3-6BA539?style=flat-square&logo=swagger&logoColor=white" alt="drf-spectacular e OpenAPI 3" />
  <img src="https://img.shields.io/badge/MapLibre_GL-295DAA?style=flat-square&logo=maplibre&logoColor=white" alt="MapLibre GL JS" />
  <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="WebSockets" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL" />
</p>

**Ferramentas**

<p>
  <img src="https://skillicons.dev/icons?i=git,github,githubactions,vscode,vercel" alt="Git, GitHub, GitHub Actions, VS Code e Vercel" />
</p>

PDM · Ruff · ESLint · Prettier · Oxlint · Figma

### Estudando e explorando

<p>
  <img src="https://skillicons.dev/icons?i=docker,typescript,linux" alt="Docker, TypeScript e Linux" />
</p>

> Os ícones representam tecnologias presentes nos meus repositórios. As ferramentas listadas em "estudando e explorando" ainda não aparecem em projetos concluídos.

---

## Projetos em destaque

### 🐕 DOGGO — Dog Service

Marketplace que conecta tutores de cães a prestadores de serviços de **Dog Walking**, **Dog Sitting** e **Dog Boarding**.

**Problema:** hoje a contratação desses serviços acontece de forma descentralizada, via mensagens pessoais — sem agenda clara, preços transparentes nem registro do que aconteceu durante o atendimento.

**O que está implementado**

- Autenticação e autorização com JWT (SimpleJWT) e perfis separados para cliente e prestador
- API REST com ViewSets para usuários, pets, prestadores, serviços, tipos de serviço, pagamentos e avaliações
- Cadastro de pets com características relevantes para a busca de prestadores
- Acompanhamento de passeio em **tempo real via WebSocket** (Django Channels + Redis), com geolocalização e desenho da rota percorrida no mapa (MapLibre GL JS)
- Sincronização automática da localização do usuário autenticado durante o serviço em andamento
- Documentação da API com OpenAPI 3 (Swagger e Redoc)
- Busca global e filtragem de prestadores
- Upload de imagens com validação de conteúdo
- Interface responsiva *mobile first* com Vue 3, Pinia e Tailwind CSS
- PWA instalável no frontend

**Tecnologias**

<p>
  <img src="https://skillicons.dev/icons?i=django,python,postgres,redis,vue,vite,pinia,tailwind" alt="Django, Python, PostgreSQL, Redis, Vue, Vite, Pinia e Tailwind CSS" />
</p>

Django REST Framework · Django Channels · SimpleJWT · drf-spectacular · WebSockets · MapLibre GL JS · GSAP

**Repositórios:** [doggo-backend](https://github.com/Doggo-Dog-Service/doggo-backend) · [doggo-frontend](https://github.com/Doggo-Dog-Service/doggo-frontend)

**Demonstração:** [doggo-frontend.vercel.app](https://doggo-frontend.vercel.app)

Projeto desenvolvido em equipe de três pessoas no contexto do Projeto Integrador do curso técnico no IFC — Campus Araquari.

---

### 💰 FinTrack (em desenvolvimento)

Aplicação de **planejamento e controle financeiro pessoal**, sendo construída como uma aplicação Saas.

**Problema:** acompanhar para onde o dinheiro vai exige uma visão organizada de receitas, despesas, categorias, metas e orçamentos — algo difícil de manter em anotações soltas.

**O que está implementado no backend**

- Modelo de dados com usuário customizado e autenticação por JWT
- CRUD completo de **transações** (receitas e despesas), **categorias** (com ícone, cor e tipo), **orçamentos** e **metas** com data limite e status
- Relatórios financeiros que agregam transações, orçamentos e metas por categoria
- Owner-based querysets: cada usuário acessa apenas os próprios dados
- API REST documentada com OpenAPI 3 (Swagger/Redoc) via drf-spectacular
- Endpoints de registro, login, refresh e verificação de token
- Ambiente de desenvolvimento com PDM, variáveis de ambiente via `.env` e lint/format com Ruff
- Deploy preparado com `gunicorn`, `whitenoise` e `dj-database-url`

**Tecnologias**

<p>
  <img src="https://skillicons.dev/icons?i=django,python,postgres,sqlite" alt="Django, Python, PostgreSQL e SQLite" />
</p>

Django REST Framework · SimpleJWT · drf-spectacular · PDM · Ruff

> Status: backend funcional e em desenvolvimento ativo. O frontend web ainda não foi publicado em repositório público.

---

### 🧩 Mosaico — Aventura dos Padrões (PC Lúdico)

Recurso educacional interativo para trabalhar **Pensamento Computacional** e **Reconhecimento de Padrões** com estudantes da Educação Básica.

**Problema:** conteúdos de Pensamento Computacional costumam ser apresentados de forma abstrata para crianças e adolescentes. O projeto traduz um dos quatro pilares — o reconhecimento de padrões — em atividades jogáveis, com progressão e recompensas.

**O que está implementado**

- Três modos de jogo, cada um explorando um tipo diferente de padrão: **Formas**, **Números** e **Sons**
- Progressão estruturada em **três fases** por modo, cada uma disponível em três níveis de **dificuldade** (fácil, médio e difícil)
- Fluxo completo de jogo: introdução → atividade → feedback → desbloqueio da próxima fase
- Sistema de **conquistas** com desbloqueio progressivo
- Progresso da campanha **persistido localmente** no navegador (Pinia + `localStorage`)
- Trilha sonora, efeitos sonoros e recursos de acessibilidade para tamanho de fonte e uso de áudio
- Interface lúdica, animada e responsiva com Vue 3, Tailwind CSS e GSAP

**Tecnologias**

<p>
  <img src="https://skillicons.dev/icons?i=vue,vite,pinia,tailwind" alt="Vue, Vite, Pinia e Tailwind CSS" />
</p>

GSAP · Vue Router · persistência local com Pinia + `localStorage`

**Repositório:** [projetopcludico/PCLudico](https://github.com/projetopcludico/PCLudico)

**Demonstração:** [pc-ludico.vercel.app](https://pc-ludico.vercel.app)

Projeto de pesquisa e desenvolvimento educacional desenvolvido em equipe, com foco em jogos digitais para o ensino de Pensamento Computacional na Educação Básica.

---

### 🎬 Portal Ghibli

Uma aplicação web inspirada no universo do Studio Ghibli, desenvolvida para explorar e apresentar conteúdos cinematográficos por meio de uma interface moderna, interativa e visualmente envolvente. O projeto utiliza a **API do TMDB** para obter dados sobre filmes, combinando desenvolvimento frontend e animações para proporcionar uma experiência de navegação mais dinâmica.

**✨ Destaques**
- 🎥 **Integração com a API do TMDB:** consumo de dados cinematográficos por meio de uma API externa.
- 🖼️ **Interface moderna:** componentes desenvolvidos com Vue.js e estilizados com Tailwind CSS.
- 🎞️ **Animações interativas:** utilização do Motion.js para criar transições e movimentos na interface.
- 📱 **Experiência de navegação:** organização visual voltada à apresentação de conteúdo cinematográfico.

**🛠️ Tecnologias utilizadas**

![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Motion](https://img.shields.io/badge/Motion-FFFFFF?style=for-the-badge&logo=framer&logoColor=black)
![TMDB](https://img.shields.io/badge/TMDB-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white)

🔗 **[Acessar projeto online](https://portal-ghibli.vercel.app/)**



## Estatísticas do GitHub

<p align="center">
  <img
    src="https://github-readme-stats.vercel.app/api?username=AndreRicardoSc&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&locale=pt-br&bg_color=0D1117&title_color=3FB950&icon_color=3FB950&text_color=C9D1D9&border_color=30363D"
    alt="Estatísticas do GitHub de André Ricardo Schultz"
    height="165"
  />
  <img
    src="https://github-readme-stats.vercel.app/api/top-langs/?username=AndreRicardoSc&layout=compact&hide_border=true&langs_count=8&locale=pt-br&bg_color=0D1117&title_color=3FB950&text_color=C9D1D9&border_color=30363D"
    alt="Linguagens mais utilizadas nos repositórios de André Ricardo Schultz"
    height="165"
  />
</p>

<p align="center">
  <img
    src="https://streak-stats.demolab.com?user=AndreRicardoSc&locale=pt_BR&hide_border=true&background=0D1117&border=30363D&stroke=30363D&ring=3FB950&fire=3FB950&currStreakLabel=3FB950&sideLabels=C9D1D9&dates=8B949E&currStreakNum=C9D1D9&sideNums=C9D1D9"
    alt="Sequência de contribuições de André Ricardo Schultz"
  />
</p>

<p align="center">
  <sub>
    Cards gerados dinamicamente por
    <a href="https://github.com/anuraghazra/github-readme-stats">GitHub Readme Stats</a> e
    <a href="https://github.com/DenverCoder1/github-readme-streak-stats">GitHub Streak Stats</a>.
    Se algum serviço estiver fora do ar, os dados continuam disponíveis diretamente no
    <a href="https://github.com/AndreRicardoSc">meu perfil do GitHub</a>.
  </sub>
</p>



## Contato

<p align="center">
  <a href="https://github.com/AndreRicardoSc">
    <img src="https://img.shields.io/badge/GitHub-AndreRicardoSc-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="mailto:schultzandrericardo@gmail.com">
    <img src="https://img.shields.io/badge/E--mail-schultzandrericardo@gmail.com-2F81F7?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" />
  </a>
  <a href="https://www.linkedin.com/in/andré-ricardo-schultz-5656532b8/">
    <img src="https://img.shields.io/badge/LinkedIn-André Ricardo Schultz-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
</p>


<p align="center">
  <sub>
    André Ricardo Schultz · IFC Campus Araquari · Santa Catarina, Brasil
  </sub>
</p>
