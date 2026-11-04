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

Trabalho principalmente no desenvolvimento de aplicações **full stack**: defino as regras de negócio, modelo os dados, construo a **API REST** no backend e desenvolvo a interface no frontend, cuidando também de autenticação, integração e experiência de uso. Meu foco atual está em **Python/Django com Django REST Framework** no servidor e **Vue.js 3 com Vite e Pinia** no cliente.

Entre os projetos em equipe que já construí estão uma plataforma de gestão de projetos (**Fluxo**, hackathon), um marketplace de serviços para cães (**Doggo**) e um recurso educacional de Pensamento Computacional (**Mosaico**).

**Interesses:** desenvolvimento web, APIs REST, arquitetura de software, bancos de dados, automação, interfaces modernas, acessibilidade e experiência do usuário.

### Formação
- **Último ano** do Técnico em Informática para Internet - IFC - Campus Araquari
- **Prestando vestibular para** Bacharelado em Sistema de Informação (BSI) - IFC - Campus Araquari

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

## Projetos em destaque

> ✅ As demos abaixo estavam **no ar** na verificação de 04/11/2026.

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

**Demonstração:** [doggo-frontend.vercel.app](https://doggo-frontend.vercel.app) <img src="https://img.shields.io/badge/Demo-No%20ar-3FB950?style=flat-square&logo=vercel&logoColor=white" alt="Demo no ar (verificada em 04/11/2026)" />

Projeto desenvolvido em equipe de três pessoas no contexto do Projeto Integrador do curso técnico no IFC — Campus Araquari.

---

### 🚀 Fluxo — Gestão de Projetos em Equipe

Plataforma full stack de gestão de projetos em equipe, desenvolvida no **hackathon de 2026** pela equipe [DreamTeam-2k26](https://github.com/DreamTeam-2k26).

**Problema:** projetos de equipe dependem de informação espalhada entre conversas, pastas e planilhas. O Fluxo centraliza tarefas, conversas, arquivos e decisões em um só lugar.

**O que está implementado**

- Quadro **Kanban** com tarefas: responsável, descrição, comentários e anexos movidos entre colunas
- **Chat e chamadas em tempo real** via WebSocket
- Pastas e arquivos do projeto (upload)
- **Brainstorm** por tópicos
- Dashboard, calendário, atividades e links do projeto
- Criação de projetos, membros e convites por link
- Autenticação com **JWT e login com Google**
- Perfil de usuário com foto

**Tecnologias**

<p>
  <img src="https://skillicons.dev/icons?i=vue,vite,pinia,js,django,python" alt="Vue, Vite, Pinia, JavaScript, Django e Python" />
</p>

Vue Router · Axios · GSAP e Motion · WebSocket · Django REST Framework · SimpleJWT · PDM · Ruff · Vercel

**Repositórios:** [frontend](https://github.com/DreamTeam-2k26/frontend) · [backend](https://github.com/DreamTeam-2k26/backend)

**Demonstração:** [fluxo-beige-three.vercel.app](https://fluxo-beige-three.vercel.app) <img src="https://img.shields.io/badge/Demo-No%20ar-3FB950?style=flat-square&logo=vercel&logoColor=white" alt="Demo no ar (verificada em 04/11/2026)" />

---

### 🧩 Outros projetos finalizados

| Projeto | Repositório (código) | Demo |
|---|---|---|
| **Mosaico — Aventura dos Padrões** · jogo educacional de Pensamento Computacional com três modos (Formas, Números, Sons), fases, conquistas e progresso persistido | [projetopcludico/PCLudico](https://github.com/projetopcludico/PCLudico) | [🟢 No ar](https://pc-ludico.vercel.app) |
| **Portal Ghibli** · explorador cinematográfico com dados da API do TMDB, interface em Vue 3 + Tailwind e animações | [AndreRicardoSc/portal-ghibli](https://github.com/AndreRicardoSc/portal-ghibli) | [🟢 No ar](https://portal-ghibli.vercel.app) |

---

### 💰 FinTrack (em desenvolvimento)

Aplicação de **planejamento e controle financeiro pessoal** (SaaS), construída com Django REST Framework.

**O que está implementado no backend**

- Modelo de dados com usuário customizado e autenticação por JWT
- CRUD completo de **transações** (receitas e despesas), **categorias** (com ícone, cor e tipo), **orçamentos** e **metas** com data limite e status
- Relatórios financeiros por categoria agregando transações, orçamentos e metas
- Owner-based querysets: cada usuário acessa apenas os próprios dados
- API documentada com OpenAPI 3 (Swagger/Redoc) via drf-spectacular

> Status: backend funcional e em desenvolvimento ativo. O frontend web ainda não foi publicado em repositório público.


## Estatísticas do GitHub

<ul style="
  list-style: none; 
  margin: 0; 
  padding: 0;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px
">
  <li>
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=AndreRicardoSc&theme=github_dark" alt="Estatísticas de André Ricardo Schultz" width="100%"/>
  </li>
  <li>
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=AndreRicardoSc&theme=github_dark" alt="Linguagens por repositório de André Ricardo Schultz" width="100%"/>
  </li>
  <li>
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=AndreRicardoSc&theme=github_dark" alt="Horários produtivos de André Ricardo Schultz" width="100%"/>
  </li>
  <li style="
    grid-column: span 3 / span 3;
  ">
    <img src="https://streak-stats.demolab.com?user=AndreRicardoSc&locale=pt_BR&hide_border=true&background=0D1117&border=30363D&ring=3FB950&fire=3FB950&currStreakLabel=3FB950&sideLabels=C9D1D9&dates=8B949E&currStreakNum=C9D1D9&sideNums=C9D1D9" alt="Sequência de contribuições de André Ricardo Schultz" width="100%"/>
  </li>
</ul>

<div style="
  margin-top: 20px;
  border-radius: 10px;
  border: solid 1px;
  background: black;
  padding-bottom: 20px;
">
  <img src="https://raw.githubusercontent.com/AndreRicardoSc/AndreRicardoSc/output/github-contribution-grid-snake-dark.svg" alt="Animação da cobra percorrendo as contribuições" width="100%" />
</div>

<p align="center">
  <sub>
    Cards gerados por
    <a href="https://github.com/vn7n24fzkq/github-profile-summary-cards">GitHub Profile Summary Cards</a>,
    <a href="https://github.com/DenverCoder1/github-readme-streak-stats">GitHub Streak Stats</a> e
    <a href="https://github.com/Platane/snk">GitHub Snake</a>.
  </sub>
</p>

---

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
