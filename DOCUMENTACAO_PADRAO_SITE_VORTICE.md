# Documentação Oficial & Padrão de Duplicação — Portal Vórtice Mídia

Este documento registra toda a arquitetura visual, técnica, estrutura de seções (`100vh` por dobra), motor de física 3D do vórtice e especificações de ativos do **Portal Oficial Vórtice Mídia**, servindo como manual padrão para manutenção ou duplicação futura do site para novos projetos do grupo.

---

## 1. Visão Geral da Arquitetura

- **Diretório Raiz do Projeto:** `C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA\`
- **Script Gerador Mestre:** `build_sites.py` (gera automaticamente `index.html` e `index_transparente.html`).
- **Regra de Ouro de Layout:**
  1. **Fundo Fixo Contínuo (`#cinema-stage`):** O furacão/tornado 8K no deserto gira ininterruptamente no `<canvas id="vortex-canvas">` com 380 destroços e partículas de poeira.
  2. **Transparência de Vidro em Todas as Seções:** Todas as seções de rolagem possuem fundos translúcidos (`rgba(...)` entre `0.22` e `0.64`) para que o tornado girando ao fundo seja sempre visível através das seções.
  3. **1 Seção = 1 Tela Inteira (`min-height: 100vh`):** Cada seção foi calibrada para caber 100% dentro de uma única tela de notebook/desktop sem cortar os blocos inferiores.
  4. **Zero Emojis:** Proibido o uso de emojis em qualquer texto ou botão. Todos os ícones utilizam SVGs vetoriais oficiais em 3D.

---

## 2. Componentes Fixos Globais

### 2.1. Logo Vórtice Mídia (Canto Superior Esquerdo da Dobra 1)
- **Arquivo:** `./assets/ui/vortice_midia_official_logo.png`
- **Posicionamento:** Livre e solta no céu no canto superior esquerdo (`top: 18px; left: 34px; height: clamp(142px, 19.5vh, 205px)`), **sem bloco ou moldura ao redor**.

### 2.2. Rádio Vórtice Music (Player Fixo no Canto Superior Direito)
- **Elemento:** `#vortice-radio-widget` (`position: fixed; top: 18px; right: 28px; z-index: 260;`)
- **Funcionalidade:**
  - Toca automaticamente em sequência contínua (`loop` de rádio) todas as músicas de todos os estilos da Vórtice Mídia (Rock, Gospel Épico, Dark/Noir, Gospel Acústico, Emoção/Pets).
  - Possui ícone de alto-falante com **ondas sonoras animadas** e **barras de equalizador em movimento** quando a música está tocando.
  - Controles diretos de **Play/Pause** e **Próxima Faixa (`⏭`)**.

---

## 3. Mapa Completo das Seções (Ordem de Rolagem)

### Dobra 1 (Hero): Vórtice 3D + 10 Placas de Trânsito do Código de Trânsito (CTB)
- **Container:** `<section id="hero-stage">` + `<div id="vortex-orbit-stage">`
- **Comportamento 3D das 10 Placas:**
  - **Placas Padrão CTB com Brilho e Textura de Tempestade:** Placas horizontais largas (`assets/signs/sign_01_rock.png` a `sign_10_aquario.png`) com alto brilho reflexivo de esmalte metálico e marcas de desgaste do vento.
  - **Órbita Desalinhada (Sem Fila Indiana e Sem Sobreposição):** Cada placa orbita em uma altura diferente (`altitudeOffset` de `-210px` a `+215px`), com raio próprio e sistema anticolisão em tempo real para que nenhuma placa apague ou fique amontoada sobre outra.
  - **Rotação no Próprio Eixo + Translação:** Enquanto giram no sentido horário ao redor do funil do tornado, as placas também giram/inclinam no próprio eixo (`rotateZ`, `rotateX`, `rotateY`).
  - **Profundidade 3D Real:** Na frente do tornado ficam grandes, brilhantes e nítidas; apenas ao passar exatamente por trás da coluna central do funil diminuem e se misturam à poeira.
  - **Pausa Individual no Hover:** Ao passar o mouse sobre uma placa, **somente aquela placa para** e fica 100% reta na frente para clique, enquanto as outras 9 continuam girando.
  - **Conteúdo Interno da Placa:** Apenas o **Nome do Canal em fonte grande** e a barra de **Botões 3D de Apertar** (Spotify, Deezer, Apple Music com a maçã oficial, Amazon Music com o `a` + sorriso oficial, YouTube e Saiba Mais).

---

### Seção 1 do Scroll: "Escolha Sua Sintonia Agora" (`#momentos`)
- **Estilo:** Fundo escuro super translúcido (`rgba(4, 5, 8, 0.24)`) revelando o vórtice atrás + Título gigante branco (`Escolha Sua Sintonia Agora`).
- **Grade:** 8 cards fotográficos (`4 colunas x 2 linhas`) representando os momentos do público:
  1. *Dormir & Orar em Paz* (Águas de Descanso) — Botões: `▶ Assistir no YouTube` | `Página`
  2. *Deus Falar Comigo* (Iago Cordeiro — `@IagoCordeiroMusic`) — Botões: `▶ Ouvir Agora` (toca a música direto no site!) | `Página`
  3. *Gospel Épico & Fé* (Sacronia) — Botões: `▶ Ouvir Agora` | `Página`
  4. *Crítica & Indignação* (Rock Incorruptível) — Botões: `▶ Ouvir Agora` | `Página`
  5. *Noite, Estrada & Treino* (Neon Asher) — Botões: `▶ Ouvir Agora` | `Página`
  6. *Amor por Cães & Gatos* (Patinhas & Canções) — Botões: `▶ Ouvir Agora` | `Página`
  7. *Mistérios & Investigação* (Aliens da Bíblia • Incorruptível) — Botões: `▶ Assistir Série` | `Página`
  8. *Diversão para Crianças* (Trono da Promessa • Felinos) — Botões: `▶ Assistir Série` | `App Kids`

---

### Seção 2 do Scroll: "As Mais Tocadas" (`#top5`)
- **Estilo:** Atmosfera vinho/roxa translúcida (`rgba(34, 6, 26, 0.28)`) com o vórtice visível ao fundo.
- **5 Faixas em Linhas Horizontais:**
  - As faixas em espera ficam em roxo translúcido (`rgba(58, 14, 42, 0.44)`), deixando ver o furacão atrás.
  - A faixa que está **tocando no momento** recebe destaque escuro sólido (`rgba(78, 14, 54, 0.92)`) e borda branca brilhante.
  - Exibe: Capa 8K + **Nome da Música** + **Nome da Banda na Frente** + Botão `▶ OUVIR / ❚❚ TOCANDO`.

---

### Seção 3 do Scroll: "Últimos Vídeos Longos do YouTube" (`#universos`)
- **Estilo:** Fundo escuro translúcido (`rgba(5, 6, 9, 0.25)`) + Grade `5 colunas x 2 linhas` com todos os **10 canais**.
- **Automação RSS YouTube:** Possui função `syncLatestYouTubeVideos()` que busca automaticamente a miniatura e o link do último vídeo publicado assim que os `channel_id` são preenchidos.
- **Canais e Handles Oficiais:**
  - Águas de Descanso: `@AguasDeDescanso`
  - Rock Incorruptível: `@RockIncorruptivel`
  - Sacronia: `@Sacronia`
  - Neon Asher: `@NeonAsher`
  - Iago Cordeiro: `@IagoCordeiroMusic`
  - Patinhas & Canções: `@PatinhaseCancoes`
  - Trono da Promessa: `@TronoDaPromessa`
  - Incorruptível: `@IncorruptivelOficial`
  - Aliens da Bíblia: `@AliensDaBiblia`
  - Aquário dos Felinos: `@AquarioDosFelinos`

---

### Seção 4 do Scroll: "Siga a Vórtice" (`.section-platforms-3d`)
- **Estilo:** Fundo translúcido (`rgba(4, 5, 8, 0.22)`) com **9 Placas de Trânsito em Movimento 3D** (`YouTube`, `Spotify`, `Instagram`, `TikTok`, `Facebook`, `Deezer`, `YT Music`, `Amazon Music`, `Apple Music`).
- Cada placa traz cravado o botão 3D oficial da respectiva plataforma/rede social.

---

### Seção 5 do Scroll: "Receba os Lançamentos" (`.section-ivory-vip`)
- **Estilo:** Contraste claro em **Branco/Marfim Translúcido** (`rgba(248, 245, 238, 0.64)`) que mantém a leitura limpa de revista editorial mas permite enxergar o tornado girando ao fundo.
- **Campos:** Nome, WhatsApp/E-mail, Canal de Aviso Preferido e Canal Favorito.

---

### Seção 6A do Scroll: "Personalize Sua Música & Comerciais Sob Encomenda" (`#personalize-sua-musica`)
- **Estilo:** Seção exclusiva e dedicada somente ao Estúdio Musical & Audiovisual da Vórtice Mídia, com fundo translúcido para ver o vórtice.
- **Estrutura:**
  - **Banner 8K Estúdio Musical (`./assets/ui/banner_estudio_vortice.jpg`)** com chamada principal e botão direto de WhatsApp.
  - **3 Blocos de Serviços Musicais:**
    1. *Músicas para Homenagens, Casamentos & Família*
    2. *Jingles Políticos & Campanhas Eleitorais*
    3. *Comerciais 3D & Trilhas para Empresas*

---

### Seção 6B do Scroll: "Aplicativos de EBD & Gestão para Igrejas" (`#aplicativos-ebd-igrejas`)
- **Estilo:** Seção exclusiva logo abaixo da seção de música, dedicada às soluções de tecnologia cristã e aplicativos da Vórtice Mídia.
- **Estrutura:**
  - **Banner 8K Aplicativos & Igrejas (`./assets/ui/banner_apps_vortice.jpg`)** mostrando tablets e celulares com o App Kids e painel da igreja.
  - **3 Blocos de Soluções em Aplicativos:**
    1. *Aplicativo de EBD & Revistinha Digital Infantil*
    2. *Aplicativo da Igreja, Rol de Membros & Transmissão de Lives*
    3. *Demonstração Interativa: App Trono da Promessa Kids*

---

### Seção 7 do Scroll: "A Essência da Vórtice Mídia — Missão, Visão e Valores" (`#missao-visao-valores`)
- **Estilo:** Bloco institucional translúcido (`rgba(8, 10, 15, 0.42)`) com o vórtice girando ao fundo, apresentando a história da empresa **Vórtice Mídia** seguida pelos **3 Pilares Corporativos Clássicos**:
  1. **NOSSA MISSÃO**
  2. **NOSSA VISÃO**
  3. **NOSSOS VALORES**
- Inclui no rodapé os links institucionais (`Voltar ao Topo`, `Propriedade Intelectual` e `Política de Privacidade LGPD`).

---

## 4. Página Exclusiva de Cada Canal (`#channel-portal-overlay`)

Ao clicar no nome de qualquer canal nas placas do tornado, no botão `Saiba Mais` ou no botão `Página`:
1. **Botão de Retorno Integrado com a Logo Vórtice Mídia:** No topo da página do canal, exibe o **Símbolo do Tornado da Vórtice Mídia integrado à escrita "VOLTAR AO PORTAL VÓRTICE MÍDIA"** — clicando em qualquer parte da logo ou do texto, o usuário retorna imediatamente à tela inicial.
2. **Cabeçalho Limpo:** Exibe apenas a **Logo Oficial do Canal**, o **Nome do Canal** na sua fonte temática e a sinopse (sem pílulas de URL ou etiquetas alaranjadas extras).
3. **Plataformas Oficiais em Placas de Trânsito 3D:** Na seção *"Acesse o Canal nas Plataformas Oficiais"*, exibe as **Placas de Trânsito 3D animadas** (`YouTube`, `Spotify`, `Deezer`, `Apple Music`, `Amazon Music`, `YouTube Music`, `Instagram`, `TikTok`, `Facebook`).

---

## 5. Como Duplicar Este Site para um Novo Projeto

1. Copie a pasta `C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA` para o novo diretório desejado.
2. Substitua os arquivos de mídia em `assets/channels/`, `assets/logos/`, `assets/signs/`, `assets/audio/` e `assets/ui/`.
3. Edite o array `VORTICE_CHANNELS` dentro de `build_sites.py` com os nomes, cores, fontes e links dos novos canais/projetos.
4. Execute `python build_sites.py` para regerar `index.html` e `index_transparente.html`.
