# -*- coding: utf-8 -*-
import os

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>VÓRTICE MÍDIA — __MODEL_TITLE__</title>
  <link rel="icon" type="image/png" sizes="192x192" href="/assets/ui/favicon.png?v=3">
  <link rel="icon" type="image/png" sizes="64x64" href="/favicon.png?v=3">
  <link rel="shortcut icon" href="/favicon.ico?v=3">
  <link rel="apple-touch-icon" href="/assets/ui/favicon.png?v=3">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="image" href="./assets/tornado/tornado_dunes_8k.jpg" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/ui/vortice_midia_official_logo.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_01_rock.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_02_sacronia.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_03_neon.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_04_iago.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_05_patinhas.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_06_aguas.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_07_trono.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_08_incorruptivel.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_09_aliens.png" fetchpriority="high">
  <link rel="preload" as="image" href="./assets/signs/sign_10_aquario.png" fetchpriority="high">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Black+Ops+One&family=Chakra+Petch:wght@600;700&family=Cinzel:wght@700;800;900&family=Fredoka:wght@600;700&family=Inter:wght@400;500;600;700;800&family=Orbitron:wght@700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&display=swap" rel="stylesheet">
  <style>
    :root {
      --gold-accent: #e5b85c;
      --gold-bright: #f7d07a;
      --ivory-bg: #f4efe6;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    html {
      scroll-behavior: smooth;
      background-color: #000000;
      color: #ffffff;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    body {
      width: 100%;
      min-height: 100vh;
      overflow-x: hidden;
      overflow-y: auto;
      background-color: #000000;
      color: #ffffff;
    }

    /* ==========================================================================
       CAMADA FIXA DO TORNADO 8K NO DESERTO
       ========================================================================== */
    #cinema-stage {
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      z-index: 1;
      background: #000000 url('./assets/tornado/tornado_dunes_8k.jpg') center center / cover no-repeat;
      pointer-events: none;
    }

    #vortex-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 2;
    }

    .cinema-vignette {
      position: absolute;
      inset: 0;
      z-index: 3;
      pointer-events: none;
      background:
        radial-gradient(circle at 48% 48%, rgba(0,0,0,0.0) 0%, rgba(0,0,0,0.18) 62%, rgba(0,0,0,0.82) 100%),
        linear-gradient(180deg, rgba(0,0,0,0.28) 0%, rgba(0,0,0,0.0) 25%, rgba(0,0,0,0.0) 75%, rgba(0,0,0,0.95) 100%);
    }

    /* ==========================================================================
       DOBRA 1 (HERO):
       - LOGO VÓRTICE MÍDIA GRANDONA NO CANTO SUPERIOR ESQUERDO (LIVRE, SEM BLOCO!)
       - AS 10 PLACAS DE TRÂNSITO GIRANDO EM ÓRBITA 3D SENTIDO HORÁRIO AO REDOR DO TORNADO!
       - QUANDO VÃO PARA TRÁS DO TORNADO: DIMINUEM E PRATICAMENTE APAGAM JUNTO AOS DESTROÇOS!
       - QUANDO VOLTAM PELA FRENTE: FICAM GRANDONAS, COLORIDAS E 100% NÍTIDAS!
       ========================================================================== */
    #hero-stage {
      position: relative;
      z-index: 20;
      width: 100%;
      height: 100vh;
      min-height: 100vh;
      padding: 18px 34px;
      perspective: 1400px;
      overflow: hidden;
    }

    /* Canto Superior Esquerdo: Logo Vórtice Mídia transformada em Botão Interativo para Alinhar/Desalinhar as 10 Placas! */
    .hero-left-wing {
      position: absolute;
      top: 16px;
      left: 32px;
      z-index: 180;
      pointer-events: auto;
    }

    .vortice-logo-btn-wrap {
      background: transparent;
      border: none;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      user-select: none;
      outline: none;
    }

    .vortice-logo-free {
      pointer-events: auto;
      height: clamp(136px, 18.5vh, 194px);
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 14px 34px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 22px rgba(0, 0, 0, 0.85));
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), filter 0.28s ease;
    }

    .vortice-logo-btn-wrap:hover .vortice-logo-free {
      transform: scale(1.05);
      filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.98)) drop-shadow(0 0 26px rgba(247, 208, 122, 0.55));
    }

    .vortice-logo-btn-wrap:active .vortice-logo-free {
      transform: scale(0.97);
    }

    .logo-align-hint-pill {
      display: inline-block;
      margin-top: -4px;
      padding: 0;
      background: transparent;
      border: none;
      color: rgba(247, 208, 122, 0.72);
      font-family: 'Orbitron', sans-serif;
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.26em;
      text-transform: uppercase;
      text-shadow: 0 2px 6px rgba(0, 0, 0, 0.95), 0 0 12px rgba(0, 0, 0, 0.9);
      transition: color 0.22s ease, opacity 0.22s ease;
    }

    .vortice-logo-btn-wrap:hover .logo-align-hint-pill {
      color: #ffffff;
    }

    /* ==========================================================================
    /* ==========================================================================
       PLACA MERCOSUL "RÁDIO VÓRTICE" FIXA NO CANTO SUPERIOR DIREITO
       - Estilizada como uma autêntica Placa de Carro Padrão Mercosul (Faixa Azul Maior + Cruzeiro do Sul + BRASIL + Bandeira Maior)!
       - Fixa na tela durante o scroll (position: fixed) e continua balançando no vento o tempo todo!
       ========================================================================== */
    @keyframes mercosulWindSway {
      0%   { transform: perspective(900px) translate3d(0px, 0px, 0px) rotateZ(-1.8deg) rotateY(-4deg) rotateX(2deg); }
      25%  { transform: perspective(900px) translate3d(-3px, 4px, 6px) rotateZ(1.4deg) rotateY(3.5deg) rotateX(-1.5deg); }
      50%  { transform: perspective(900px) translate3d(2px, -3px, 2px) rotateZ(-2.2deg) rotateY(-2.5deg) rotateX(2.5deg); }
      75%  { transform: perspective(900px) translate3d(-2px, 3px, 5px) rotateZ(1.9deg) rotateY(4deg) rotateX(-2deg); }
      100% { transform: perspective(900px) translate3d(0px, 0px, 0px) rotateZ(-1.8deg) rotateY(-4deg) rotateX(2deg); }
    }

    #vortice-radio-widget {
      position: fixed;
      top: 8px;
      right: 14px;
      z-index: 320;
      display: flex;
      flex-direction: column;
      width: 238px;
      min-width: 238px;
      max-width: 238px;
      height: 64px;
      border-radius: 8px;
      background:
        linear-gradient(135deg, rgba(255,255,255,0.97) 0%, rgba(232,237,244,0.97) 48%, rgba(214,222,233,0.97) 100%);
      border: 2.5px solid #1a202c;
      box-shadow:
        0 0 0 1px rgba(255, 255, 255, 0.75),
        0 5px 0 #0b0e14,
        0 12px 24px rgba(0, 0, 0, 0.90),
        inset 0 0 8px rgba(0, 0, 0, 0.16);
      overflow: hidden;
      user-select: none;
      animation: mercosulWindSway 5.2s ease-in-out infinite;
      transform-origin: center top;
      transition: box-shadow 0.25s ease, filter 0.25s ease;
    }

    #vortice-radio-widget:hover {
      animation-play-state: paused;
      transform: perspective(900px) translate3d(0px, -1px, 10px) rotateZ(0deg) rotateY(0deg) rotateX(0deg) scale(1.04);
      box-shadow:
        0 0 0 1.5px #ffffff,
        0 6px 0 #0b0e14,
        0 16px 32px rgba(0, 0, 0, 0.96),
        0 0 18px rgba(0, 200, 83, 0.45);
    }

    /* Faixa Superior Azul Oficial Padrão Mercosul (#003399) — Compacta e nítida! */
    .mercosul-top-bar {
      width: 100%;
      height: 19px;
      background: linear-gradient(180deg, #0044cc 0%, #002b80 100%);
      border-bottom: 1px solid rgba(0, 18, 56, 0.9);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 8px;
      color: #ffffff;
    }

    .mercosul-left-emblem {
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }

    .mercosul-left-emblem svg {
      width: 18px;
      height: 14px;
      overflow: visible;
      filter: drop-shadow(0 1px 1px rgba(0, 0, 0, 0.55));
    }

    .mercosul-country-title {
      font-family: 'Orbitron', 'Inter', sans-serif;
      font-size: 8.5px;
      font-weight: 900;
      letter-spacing: 0.18em;
      color: #ffffff;
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.65);
    }

    .mercosul-br-flag {
      width: 18px;
      height: 13px;
      border-radius: 2px;
      border: 1px solid rgba(255, 255, 255, 0.78);
      overflow: hidden;
      display: inline-flex;
      flex-shrink: 0;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
    }

    /* Corpo Principal da Placa Mercosul Compacta */
    .mercosul-plate-body {
      position: relative;
      flex: 1;
      display: flex;
      align-items: center;
      gap: 7px;
      padding: 4px 8px 5px 8px;
      background:
        repeating-linear-gradient(115deg, rgba(255,255,255,0.0) 0px, rgba(255,255,255,0.0) 6px, rgba(0,51,153,0.025) 6px, rgba(0,51,153,0.025) 12px);
    }

    @keyframes radioBtnBreathe {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.08); }
    }

    .radio-speaker-btn {
      position: relative;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      border: 1.5px solid #0b1324;
      background: linear-gradient(180deg, #162238 0%, #090e18 100%);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 2px 0 #05080e, 0 3px 7px rgba(0, 0, 0, 0.35);
      animation: radioBtnBreathe 2.2s ease-in-out infinite;
      transition: transform 0.2s ease, background 0.2s ease;
      flex-shrink: 0;
    }

    #vortice-radio-widget.is-playing .radio-speaker-btn {
      border-color: #05692b;
      background: linear-gradient(180deg, #00e660 0%, #008a38 100%);
      box-shadow: 0 2px 0 #03471d, 0 0 10px rgba(0, 230, 96, 0.65);
      animation: radioBtnBreathe 1.25s ease-in-out infinite;
    }

    .radio-speaker-btn:hover {
      transform: scale(1.12);
    }

    .radio-speaker-btn svg {
      width: 14px;
      height: 14px;
      fill: #00e660;
      transition: fill 0.2s ease;
    }

    #vortice-radio-widget.is-playing .radio-speaker-btn svg {
      fill: #ffffff;
    }

    /* Ondas sonoras saindo do ícone continuamente */
    @keyframes soundWavePulse {
      0% { transform: scale(0.88); opacity: 0.75; }
      75% { transform: scale(1.48); opacity: 0; }
      100% { transform: scale(1.58); opacity: 0; }
    }

    .radio-wave-ring {
      position: absolute;
      inset: -2px;
      border-radius: 50%;
      border: 1.5px solid rgba(0, 200, 83, 0.65);
      opacity: 0;
      pointer-events: none;
      animation: soundWavePulse 2.2s ease-out infinite;
    }

    .radio-wave-ring.r2 {
      animation-delay: 1.1s;
    }

    #vortice-radio-widget.is-playing .radio-wave-ring.r1 {
      border-color: #00c853;
      animation: soundWavePulse 1.35s ease-out infinite;
    }

    #vortice-radio-widget.is-playing .radio-wave-ring.r2 {
      border-color: #00c853;
      animation: soundWavePulse 1.35s ease-out 0.67s infinite;
    }

    .radio-info-col {
      display: flex;
      flex-direction: column;
      justify-content: center;
      flex: 1;
      min-width: 0;
      cursor: pointer;
    }

    .radio-brand-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 5px;
      margin-bottom: 1px;
    }

    /* Tipografia estampada em alto-relevo estilo Placa Mercosul */
    .radio-title-badge {
      font-family: 'Orbitron', 'Chakra Petch', sans-serif;
      font-size: 10.5px;
      font-weight: 900;
      letter-spacing: 0.05em;
      color: #090e1a;
      text-transform: uppercase;
      text-shadow: 0 1px 0 rgba(255, 255, 255, 0.9), 0 -1px 0 rgba(0, 0, 0, 0.25);
      line-height: 1.05;
      white-space: nowrap;
    }

    /* Equalizador com 12 barras verdes pulsando continuamente dentro da Placa! */
    .radio-eq-bars {
      display: inline-flex;
      align-items: flex-end;
      gap: 1.5px;
      height: 14px;
      padding: 1.5px 3.5px;
      border-radius: 4px;
      background: rgba(9, 14, 26, 0.90);
      box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.8);
      flex-shrink: 0;
    }

    .radio-eq-bars span {
      width: 2px;
      height: 4px;
      background: linear-gradient(180deg, #69f0ae 0%, #00e676 55%, #00a152 100%);
      border-radius: 999px;
      box-shadow: 0 0 4px rgba(0, 230, 118, 0.7);
      transition: height 0.15s ease;
    }

    /* Movimento vivo mesmo em standby (pulsando suave) */
    @keyframes eqIdleWave {
      0%, 100% { height: 3px; opacity: 0.8; }
      50% { height: 9px; opacity: 1; }
    }

    .radio-eq-bars span:nth-child(1)  { animation: eqIdleWave 1.10s ease-in-out 0.00s infinite; }
    .radio-eq-bars span:nth-child(2)  { animation: eqIdleWave 0.95s ease-in-out 0.12s infinite; }
    .radio-eq-bars span:nth-child(3)  { animation: eqIdleWave 1.25s ease-in-out 0.24s infinite; }
    .radio-eq-bars span:nth-child(4)  { animation: eqIdleWave 0.88s ease-in-out 0.36s infinite; }
    .radio-eq-bars span:nth-child(5)  { animation: eqIdleWave 1.15s ease-in-out 0.18s infinite; }
    .radio-eq-bars span:nth-child(6)  { animation: eqIdleWave 0.92s ease-in-out 0.42s infinite; }
    .radio-eq-bars span:nth-child(7)  { animation: eqIdleWave 1.05s ease-in-out 0.08s infinite; }
    .radio-eq-bars span:nth-child(8)  { animation: eqIdleWave 1.20s ease-in-out 0.28s infinite; }
    .radio-eq-bars span:nth-child(9)  { animation: eqIdleWave 0.90s ease-in-out 0.15s infinite; }
    .radio-eq-bars span:nth-child(10) { animation: eqIdleWave 1.12s ease-in-out 0.32s infinite; }
    .radio-eq-bars span:nth-child(11) { animation: eqIdleWave 0.98s ease-in-out 0.20s infinite; }
    .radio-eq-bars span:nth-child(12) { animation: eqIdleWave 1.18s ease-in-out 0.05s infinite; }

    /* Movimento intenso quando a música está tocando! */
    @keyframes eqBounce1 { 0%, 100% { height: 3px; } 50% { height: 11px; } }
    @keyframes eqBounce2 { 0%, 100% { height: 10px; } 40% { height: 3px; } 80% { height: 11px; } }
    @keyframes eqBounce3 { 0%, 100% { height: 5px; } 30% { height: 11px; } 70% { height: 3px; } }
    @keyframes eqBounce4 { 0%, 100% { height: 9px; } 25% { height: 3px; } 65% { height: 11px; } }

    #vortice-radio-widget.is-playing .radio-eq-bars span {
      box-shadow: 0 0 7px rgba(56, 255, 128, 0.95);
    }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(1)  { animation: eqBounce1 0.46s ease-in-out infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(2)  { animation: eqBounce2 0.39s ease-in-out 0.05s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(3)  { animation: eqBounce3 0.52s ease-in-out 0.11s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(4)  { animation: eqBounce4 0.42s ease-in-out 0.07s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(5)  { animation: eqBounce1 0.49s ease-in-out 0.16s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(6)  { animation: eqBounce2 0.37s ease-in-out 0.03s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(7)  { animation: eqBounce3 0.45s ease-in-out 0.14s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(8)  { animation: eqBounce4 0.51s ease-in-out 0.09s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(9)  { animation: eqBounce1 0.40s ease-in-out 0.19s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(10) { animation: eqBounce2 0.48s ease-in-out 0.06s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(11) { animation: eqBounce3 0.43s ease-in-out 0.12s infinite; }
    #vortice-radio-widget.is-playing .radio-eq-bars span:nth-child(12) { animation: eqBounce4 0.47s ease-in-out 0.02s infinite; }

    .radio-now-playing {
      font-family: 'Inter', sans-serif;
      font-size: 9.5px;
      font-weight: 800;
      color: #1e293b;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 145px;
    }

    #vortice-radio-widget.is-playing .radio-now-playing {
      color: #047857;
    }

    .radio-next-btn {
      width: 20px;
      height: 20px;
      border-radius: 5px;
      border: 1px solid #0f172a;
      background: #0f172a;
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 9.5px;
      box-shadow: 0 1.5px 0 #020617;
      transition: transform 0.18s ease, background 0.18s ease;
      flex-shrink: 0;
    }

    .radio-next-btn:hover {
      background: #003399;
      border-color: #003399;
      transform: scale(1.1);
    }

    /* Palco 3D de Tela Inteira onde as 10 Placas giram ao redor do Tornado (e NÃO em cima da logo!) */
    #vortex-orbit-stage {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      transform-style: preserve-3d;
      z-index: 35;
    }

    /* ==========================================================================
       AS 10 PLACAS DE SINALIZAÇÃO / TRÂNSITO (PADRÃO CTB COM PROPORÇÃO EXATA 1260x590!)
       - Proporção exata da placa (268px x 125px com background-size: 100% 100%)
         para NENHUM botão jamais sair para fora da placa!
       - Contém a Logo Oficial + Escrita Original de cada canal!
       ========================================================================== */
    .vortice-channel-btn {
      position: absolute;
      top: 0;
      left: 0;
      width: 268px;
      height: 125px;
      pointer-events: auto;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background-size: 100% 100%;
      background-repeat: no-repeat;
      background-position: center;
      background-color: transparent;
      border: none;
      transform-style: preserve-3d;
      backface-visibility: visible;
      will-change: transform, opacity;
      filter: drop-shadow(0 14px 22px rgba(0, 0, 0, 0.88));
      cursor: pointer;
      user-select: none;
    }

    /* Camada interna estampada diretamente no metal da placa (100% dentro da moldura da placa!) */
    .sign-stamped-surface {
      position: relative;
      z-index: 2;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      transform: translateZ(2px);
    }

    /* Logo + Escrita Oficial do Canal Cravada na Placa */
    .channel-name-row {
      width: 100%;
      height: 54px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      margin-bottom: 4px;
    }

    .sign-channel-lockup-img {
      max-width: 210px;
      max-height: 52px;
      width: auto;
      height: auto;
      object-fit: contain;
      pointer-events: none;
      display: block;
    }

    /* Barra de Botões 3D de Apertar Cravados na Placa (100% dentro das bordas da placa!) */
    .btn-actions-bar {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 3.5px;
      width: 100%;
    }

    .streaming-icons-group {
      display: flex;
      align-items: center;
      gap: 3px;
    }

    /* Botãozinho 3D Estilizado de Apertar para as 5 Plataformas (Spotify, Deezer, Apple, Amazon e YouTube) */
    .platform-icon-link {
      width: 19.5px;
      height: 19.5px;
      border-radius: 4.5px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      text-decoration: none;
      border: 1px solid rgba(255, 255, 255, 0.58);
      box-shadow:
        0 2px 0 rgba(0, 0, 0, 0.88),
        0 3px 6px rgba(0, 0, 0, 0.72),
        inset 0 1px 1px rgba(255, 255, 255, 0.72);
      transition: transform 0.14s ease, filter 0.14s ease, box-shadow 0.14s ease;
      flex-shrink: 0;
    }

    .platform-icon-link svg {
      width: 11.5px;
      height: 11.5px;
      fill: #ffffff;
      filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.55));
    }

    .platform-icon-link.spotify { background: linear-gradient(180deg, #24e06a 0%, #108a3e 100%); }
    .platform-icon-link.deezer  { background: linear-gradient(180deg, #a855f7 0%, #6b21a8 100%); }
    .platform-icon-link.apple   { background: linear-gradient(180deg, #ff3b5c 0%, #be123c 100%); }
    .platform-icon-link.amazon  { background: linear-gradient(180deg, #00b4f5 0%, #006699 100%); }
    .platform-icon-link.youtube { background: linear-gradient(180deg, #ff2a2a 0%, #b30000 100%); }

    .platform-icon-link:hover {
      transform: translateY(-2px) scale(1.14);
      filter: brightness(1.15);
      box-shadow:
        0 4px 0 rgba(0, 0, 0, 0.85),
        0 6px 10px rgba(0, 0, 0, 0.75),
        inset 0 1px 2px rgba(255, 255, 255, 0.85);
    }

    .right-links-group {
      display: flex;
      align-items: center;
      gap: 3.5px;
    }

    /* Botão 3D Preto Estilizado da Vórtice Mídia (Funil Vórtice + "Página") */
    .vortice-pagina-btn {
      height: 19.5px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 3.5px;
      padding: 0 6px;
      border-radius: 4.5px;
      background: linear-gradient(180deg, #262b38 0%, #07090e 100%);
      border: 1px solid rgba(247, 208, 122, 0.82);
      color: #ffffff;
      font-family: 'Chakra Petch', sans-serif;
      font-size: 9px;
      font-weight: 800;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      cursor: pointer;
      box-shadow:
        0 2px 0 rgba(0, 0, 0, 0.95),
        0 3px 7px rgba(0, 0, 0, 0.82),
        inset 0 1px 1px rgba(255, 255, 255, 0.32);
      transition: transform 0.14s ease, filter 0.14s ease, border-color 0.14s ease, box-shadow 0.14s ease;
      flex-shrink: 0;
    }

    .vortice-pagina-btn svg {
      width: 11px;
      height: 11px;
      fill: #f7d07a;
      filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.85));
      flex-shrink: 0;
    }

    .vortice-pagina-btn:hover {
      transform: translateY(-2px) scale(1.08);
      filter: brightness(1.16);
      border-color: #ffffff;
      box-shadow:
        0 4px 0 rgba(0, 0, 0, 0.95),
        0 6px 12px rgba(247, 208, 122, 0.35),
        inset 0 1px 2px rgba(255, 255, 255, 0.55);
    }

    /* ==========================================================================
       ESTRUTURA DE ROLAGEM — CADA SESSÃO CABE 100% INTEIRA NA MESMA TELA (100VH)
       E TODAS TÊM TRANSPARÊNCIA PARA VER O VÓRTICE GIRANDO LÁ ATRÁS!
       ========================================================================== */
    .scroll-universe {
      position: relative;
      z-index: 25;
      width: 100%;
    }

    /* --------------------------------------------------------------------------
       PADRÃO UNIFICADO DE TODAS AS SEÇÕES DO PORTAL:
       - Mesma transparência limpa da Seção 1 e 2 (sem lente colorida e sem linha divisória!)
       - Mesmo tamanho/altura ampla da Loja Oficial (min-height: 108vh; padding: 104px 36px 64px)
       - Todos os títulos FORA dos blocos, na mesma fonte imponente ('Cinzel'), mesmo tamanho e cor branca!
       -------------------------------------------------------------------------- */
    .section-momentos {
      min-height: 108vh;
      padding: 104px 36px 64px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .container-wide {
      max-width: 1380px;
      width: 100%;
      margin: 0 auto;
    }

    .editorial-header {
      text-align: center;
      margin-top: 0;
      margin-bottom: 36px;
    }

    .editorial-giant-title,
    .top5-serif-heading {
      font-family: 'Cinzel', Georgia, serif;
      font-size: clamp(30px, 3.3vw, 44px);
      font-weight: 900;
      letter-spacing: 0.04em;
      line-height: 1.15;
      text-transform: uppercase;
      color: #ffffff;
      text-align: center;
      text-shadow:
        0 3px 0 rgba(0, 0, 0, 0.90),
        0 12px 32px rgba(0, 0, 0, 0.95);
      margin: 0;
    }

    .momentos-photo-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
    }

    .momento-photo-card {
      border-radius: 15px;
      overflow: hidden;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.20);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      display: flex;
      flex-direction: column;
      transition: transform 0.26s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.26s ease, background 0.26s ease, box-shadow 0.26s ease;
    }

    .momento-photo-card:hover {
      transform: translateY(-6px);
      background: rgba(16, 19, 28, 0.84);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 18px rgba(255, 255, 255, 0.28);
    }

    .momento-img-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      height: auto;
      overflow: hidden;
      background: #050608;
    }

    .momento-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }

    .momento-photo-card:hover .momento-img-wrap img {
      transform: scale(1.06);
    }

    .momento-card-body {
      padding: 13px 14px 15px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .momento-kicker {
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: #ffffff;
      margin-bottom: 4px;
    }

    .momento-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 12px;
      line-height: 1.2;
    }

    /* Botões Ouvir Agora e Página com EXATAMENTE o mesmo tamanho (1fr 1fr)! */
    .momento-btn-row {
      margin-top: auto;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      width: 100%;
    }

    .momento-pill-btn,
    .momento-page-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      width: 100%;
      min-height: 36px;
      padding: 8px 6px;
      border-radius: 10px;
      background: rgba(10, 12, 18, 0.56);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      color: #ffffff;
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.02em;
      text-decoration: none;
      white-space: nowrap;
      cursor: pointer;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.60);
      transition: all 0.22s ease;
    }

    .momento-pill-btn:hover,
    .momento-pill-btn.active-playing,
    .momento-page-btn:hover {
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      color: #ffffff;
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.88), 0 0 16px rgba(255, 255, 255, 0.30);
      transform: translateY(-2px);
    }

    /* --------------------------------------------------------------------------
       SESSÃO 2 DO SCROLL: "AS MAIS TOCADAS" (MESMO FUNDO TRANSPARENTE DA SEÇÃO 1,
       SEM LENTE BRANCA E SEM LINHA DIVISÓRIA!)
       -------------------------------------------------------------------------- */
    .section-top5 {
      min-height: 108vh;
      padding: 104px 36px 64px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .top5-narrow-container {
      max-width: 920px;
      width: 100%;
      margin: 0 auto;
    }

    .top5-serif-heading {
      margin-bottom: 36px;
    }

    .top5-cards-stack {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    /* Mesma transparência escura limpa da Seção 1 para ver o vórtice lá atrás */
    .top5-wine-card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 12px 22px;
      border-radius: 14px;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 14px 34px rgba(0, 0, 0, 0.72);
      transition: all 0.25s ease;
    }

    .top5-wine-card:hover, .top5-wine-card.playing {
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow: 0 18px 42px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
      transform: translateY(-2px);
    }

    .top5-left-group {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .top5-cover-thumb {
      width: 52px;
      height: 52px;
      border-radius: 9px;
      object-fit: cover;
      border: 1px solid rgba(255, 255, 255, 0.35);
      flex-shrink: 0;
    }

    .top5-song-and-band {
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      gap: 10px;
    }

    .top5-song-name {
      font-family: 'Inter', sans-serif;
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      text-shadow: 0 2px 6px rgba(0, 0, 0, 0.85);
    }

    .top5-band-front {
      font-family: 'Inter', sans-serif;
      font-size: 14px;
      font-weight: 600;
      color: rgba(255, 255, 255, 0.90);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .top5-band-front::before {
      content: "•";
      color: #ff3b3b;
      font-size: 16px;
    }

    .top5-right-controls {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .top5-play-action {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: none;
      border: none;
      color: #ffffff;
      cursor: pointer;
      font-family: 'Inter', sans-serif;
      font-size: 9.5px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      gap: 2px;
    }

    .top5-play-action span.tri {
      font-size: 16px;
      transition: transform 0.2s ease;
    }

    .top5-play-action:hover span.tri {
      transform: scale(1.25);
    }

    /* --------------------------------------------------------------------------
       SESSÃO 3 DO SCROLL: "ÚLTIMOS VÍDEOS LONGOS DO YOUTUBE"
       - Mesmo padrão de altura, fundo transparente e título de todas as seções!
       -------------------------------------------------------------------------- */
    .section-universos {
      min-height: 108vh;
      padding: 104px 36px 64px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .section-universos .editorial-header {
      margin-bottom: 36px;
    }

    .universos-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
    }

    .universo-poster-card {
      border-radius: 15px;
      overflow: hidden;
      background: rgba(10, 12, 18, 0.50);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.20);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.68);
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: #ffffff;
      transition: transform 0.26s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.26s ease, background 0.26s ease, box-shadow 0.26s ease;
    }

    .universo-poster-card:hover {
      transform: translateY(-6px);
      background: rgba(16, 19, 28, 0.84);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 18px rgba(255, 255, 255, 0.28);
    }

    .universo-thumb-box {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      height: auto;
      overflow: hidden;
      background: #040507;
    }

    .universo-thumb-box img.bg-art {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.45s ease;
    }

    .universo-poster-card:hover .universo-thumb-box img.bg-art {
      transform: scale(1.06);
    }

    .universo-duration-badge {
      position: absolute;
      top: 8px;
      left: 8px;
      padding: 3px 8px;
      border-radius: 999px;
      background: rgba(0, 0, 0, 0.78);
      border: 1px solid rgba(255, 255, 255, 0.28);
      color: #ffffff;
      font-size: 8.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }

    .floating-yt-circle {
      position: absolute;
      bottom: 8px;
      right: 8px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: linear-gradient(180deg, #ff2a2a 0%, #cc0000 100%);
      border: 2px solid rgba(255, 255, 255, 0.55);
      color: #ffffff;
      font-size: 11px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 8px 18px rgba(255, 0, 0, 0.55), inset 0 1px 2px rgba(255, 255, 255, 0.45);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .universo-poster-card:hover .floating-yt-circle {
      transform: scale(1.15);
    }

    .universo-body {
      padding: 8px 11px 10px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .universo-style-tag {
      font-size: 8.5px;
      font-weight: 800;
      letter-spacing: 0.13em;
      text-transform: uppercase;
      color: #f7d07a;
      margin-bottom: 2px;
    }

    .universo-channel-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 15.5px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 7px;
      line-height: 1.15;
    }

    .section-universos .momento-pill-btn,
    .section-universos .momento-page-btn {
      min-height: 30px;
      padding: 5px 6px;
      font-size: 10.5px;
    }

    /* --------------------------------------------------------------------------
       SESSÃO 4 DO SCROLL: "QUAL É O SEU MOMENTO AGORA?"
       - Mesmo padrão de altura, fundo transparente e sem linha divisória!
       -------------------------------------------------------------------------- */
    .section-platforms-3d {
      min-height: 108vh;
      padding: 104px 36px 64px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      background: rgba(4, 5, 8, 0.22);
      border: none;
      text-align: center;
      perspective: 1200px;
    }

    .flying-signs-platforms-grid {
      max-width: 1220px;
      margin: 36px auto 0;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px 34px;
      align-items: center;
      justify-items: center;
    }

    /* Movimento Vigoroso de Vendaval 3D para as Placas de "Siga a Vórtice" e Páginas dos Canais */
    @keyframes signWindFloat {
      0% {
        transform: translate3d(calc(var(--s-dx, 14px) * -1), -12px, -18px) rotateZ(var(--s-tilt, -6.5deg)) rotateY(var(--s-roty, 16deg)) rotateX(8deg) scale(0.95);
      }
      25% {
        transform: translate3d(calc(var(--s-dx, 14px) * 0.6), 9px, 24px) rotateZ(calc(var(--s-tilt, -6.5deg) * -0.65)) rotateY(calc(var(--s-roty, 16deg) * -0.5)) rotateX(-7deg) scale(1.03);
      }
      50% {
        transform: translate3d(var(--s-dx, 14px), -14px, 32px) rotateZ(calc(var(--s-tilt, -6.5deg) * -1.15)) rotateY(calc(var(--s-roty, 16deg) * -1.1)) rotateX(9deg) scale(1.05);
      }
      75% {
        transform: translate3d(calc(var(--s-dx, 14px) * -0.5), 11px, 10px) rotateZ(calc(var(--s-tilt, -6.5deg) * 0.55)) rotateY(calc(var(--s-roty, 16deg) * 0.45)) rotateX(-6deg) scale(0.98);
      }
      100% {
        transform: translate3d(calc(var(--s-dx, 14px) * -1), -12px, -18px) rotateZ(var(--s-tilt, -6.5deg)) rotateY(var(--s-roty, 16deg)) rotateX(8deg) scale(0.95);
      }
    }

    .social-road-sign {
      width: 100%;
      max-width: 345px;
      min-height: 116px;
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 18px 28px;
      text-decoration: none;
      transform-style: preserve-3d;
      animation: signWindFloat 3.4s ease-in-out infinite;
      animation-delay: var(--s-delay, 0s);
      filter: drop-shadow(0 18px 28px rgba(0, 0, 0, 0.92));
      transition: transform 0.25s ease, filter 0.25s ease;
    }

    .social-road-sign:hover {
      animation-play-state: paused;
      transform: translate3d(0, -6px, 36px) scale(1.10) rotateZ(0deg) rotateY(0deg) rotateX(0deg) !important;
      filter: drop-shadow(0 24px 38px rgba(0, 0, 0, 0.98)) brightness(1.12);
      z-index: 20;
    }

    /* Botão 3D Oficial da Rede Social Cravado Dentro da Placa de Trânsito */
    .social-official-3d-badge {
      display: inline-flex;
      align-items: center;
      gap: 11px;
      padding: 10px 20px;
      border-radius: 13px;
      color: #ffffff;
      font-family: 'Chakra Petch', sans-serif;
      font-size: 14.5px;
      font-weight: 800;
      letter-spacing: 0.07em;
      text-transform: uppercase;
      box-shadow:
        0 5px 0 rgba(0, 0, 0, 0.80),
        0 12px 24px rgba(0, 0, 0, 0.68),
        inset 0 2px 3px rgba(255, 255, 255, 0.62);
      border: 1px solid rgba(255, 255, 255, 0.52);
    }

    .social-official-3d-badge svg {
      width: 22px;
      height: 22px;
      fill: #ffffff;
      flex-shrink: 0;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.45));
    }

    .social-badge-col {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
      line-height: 1.1;
    }

    .social-badge-sub {
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.14em;
      color: rgba(255, 255, 255, 0.86);
      margin-top: 2px;
    }

    .badge-yt { background: linear-gradient(180deg, #ff2626 0%, #a80000 100%); }
    .badge-sp { background: linear-gradient(180deg, #1ed760 0%, #0d7a35 100%); }
    .badge-ig { background: linear-gradient(145deg, #f9ce34 0%, #ee2a7b 52%, #6228d7 100%); }
    .badge-tk { background: linear-gradient(180deg, #161922 0%, #050608 100%); border-color: #00f2fe; }
    .badge-fb { background: linear-gradient(180deg, #1877f2 0%, #0a4699 100%); }
    .badge-dz { background: linear-gradient(180deg, #a855f7 0%, #581c87 100%); }
    .badge-ym { background: linear-gradient(180deg, #e11d48 0%, #881337 100%); }
    .badge-am { background: linear-gradient(180deg, #00b4f5 0%, #005f80 100%); }
    .badge-ap { background: linear-gradient(180deg, #fa243c 0%, #9f1222 100%); }

    /* --------------------------------------------------------------------------
       SESSÃO 5 DO SCROLL: "RECEBA OS LANÇAMENTOS"
       - Mesmo fundo transparente das Seções 1 e 2 (sem lente branca!)
       - Título FORA do bloco em cima e bloco escuro translúcido embaixo!
       -------------------------------------------------------------------------- */
    .section-ivory-vip {
      min-height: 108vh;
      padding: 104px 36px 64px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      background: rgba(4, 5, 8, 0.22);
      color: #ffffff;
      border: none;
    }

    .ivory-form-container {
      max-width: 860px;
      width: 100%;
      margin: 0 auto;
      padding: 36px 42px;
      border-radius: 22px;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 22px 54px rgba(0, 0, 0, 0.72);
      text-align: center;
    }

    .ivory-sub {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 20px;
      color: #ffffff;
      font-weight: 700;
      margin-bottom: 26px;
      line-height: 1.4;
    }

    .ivory-grid-inputs {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      text-align: left;
      margin-bottom: 22px;
    }

    .ivory-field label {
      display: block;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #f7d07a;
      margin-bottom: 6px;
    }

    .ivory-field input, .ivory-field select {
      width: 100%;
      padding: 14px 16px;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.28);
      background: rgba(16, 19, 28, 0.78);
      color: #ffffff;
      font-family: 'Inter', sans-serif;
      font-size: 14.5px;
      outline: none;
      box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.45);
    }

    .ivory-field input::placeholder {
      color: rgba(255, 255, 255, 0.55);
    }

    .ivory-field select option {
      background: #0d1017;
      color: #ffffff;
    }

    .ivory-submit-btn {
      width: 100%;
      padding: 15px 28px;
      border-radius: 12px;
      border: 1.5px solid rgba(255, 255, 255, 0.24);
      background: rgba(10, 12, 18, 0.62);
      color: #ffffff;
      font-family: 'Chakra Petch', 'Inter', sans-serif;
      font-size: 14.5px;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      cursor: pointer;
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.68);
      transition: all 0.22s ease;
    }

    .ivory-submit-btn:hover {
      transform: translateY(-2px);
      background: rgba(18, 22, 32, 0.90);
      border-color: #ffffff;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
    }

    /* --------------------------------------------------------------------------
       SESSÕES 6A E 6B DO SCROLL:
       - 6A: PERSONALIZE SUA MÚSICA & COMERCIAIS
       - 6B: APLICATIVOS PARA EBD & IGREJAS
       - Título FORA em cima + Banner e 3 Blocos embaixo!
       -------------------------------------------------------------------------- */
    .section-studio-loja {
      min-height: 108vh;
      padding: 104px 36px 64px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .studio-hero-banner {
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      min-height: 190px;
      margin-bottom: 18px;
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 22px 54px rgba(0, 0, 0, 0.80);
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      align-items: center;
      padding: 24px 34px;
      gap: 20px;
    }

    .studio-hero-banner img.studio-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 1;
    }

    .studio-banner-mask {
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, rgba(5, 6, 9, 0.84) 0%, rgba(5, 6, 9, 0.62) 55%, rgba(5, 6, 9, 0.12) 100%);
      z-index: 2;
    }

    .studio-banner-content {
      position: relative;
      z-index: 5;
    }

    .studio-banner-desc {
      font-size: 14.5px;
      color: rgba(255, 255, 255, 0.90);
      line-height: 1.55;
      margin-bottom: 16px;
      max-width: 650px;
    }

    .studio-cards-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }

    /* Bloquinhos no mesmo padrão cinza-escuro translúcido de Escolha Sua Sintonia e As Mais Tocadas */
    .gold-showcase-card {
      border-radius: 16px;
      padding: 20px 22px;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }

    .gold-showcase-card:hover {
      transform: translateY(-5px);
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
    }

    .gold-card-tag {
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #f7d07a;
      margin-bottom: 6px;
    }

    .gold-card-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 20.5px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .gold-card-text {
      font-size: 13.5px;
      color: rgba(255, 255, 255, 0.88);
      line-height: 1.5;
      margin-bottom: 16px;
    }

    /* Botão padronizado igual ao Card/Botão de As Mais Tocadas (discreto + margem branca forte no hover) */
    .emerald-action-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      padding: 11px 18px;
      border-radius: 10px;
      background: rgba(10, 12, 18, 0.62);
      color: #ffffff;
      font-family: 'Chakra Petch', 'Inter', sans-serif;
      font-size: 12.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      text-decoration: none;
      cursor: pointer;
      border: 1.5px solid rgba(255, 255, 255, 0.24);
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.65);
      transition: all 0.22s ease;
    }

    .emerald-action-btn:hover {
      transform: translateY(-2px);
      background: rgba(18, 22, 32, 0.90);
      border-color: #ffffff;
      color: #ffffff;
      box-shadow: 0 14px 32px rgba(0, 0, 0, 0.88), 0 0 18px rgba(255, 255, 255, 0.28);
    }

    /* --------------------------------------------------------------------------
       SESSÃO 7 DO SCROLL: FORÇA CRIATIVA VÓRTICE MÍDIA
       - Todos os cards com EXATAMENTE a mesma transparência (rgba(10, 12, 18, 0.56))
         e borda de Escolha Sua Sintonia e As Mais Tocadas!
       -------------------------------------------------------------------------- */
    .section-story-editorial {
      min-height: 108vh;
      padding: 104px 36px 28px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .story-chapter-box {
      max-width: 1380px;
      width: 100%;
      margin: 0 auto 18px;
      padding: 24px 32px;
      border-radius: 16px;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      text-align: center;
      transition: all 0.25s ease;
    }

    .story-chapter-box:hover {
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
    }

    .story-chapter-p {
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      line-height: 1.65;
      color: rgba(255, 255, 255, 0.92);
      margin: 0 auto;
      max-width: 1120px;
    }

    .mvv-corporate-grid {
      max-width: 1380px;
      width: 100%;
      margin: 0 auto 24px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
      text-align: left;
    }

    .mvv-card-3d {
      padding: 20px 22px;
      border-radius: 16px;
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      transition: all 0.25s ease;
    }

    .mvv-card-3d:hover {
      transform: translateY(-5px);
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
    }

    .mvv-tag {
      font-family: 'Orbitron', sans-serif;
      font-size: 10.5px;
      font-weight: 900;
      letter-spacing: 0.16em;
      color: #f7d07a;
      margin-bottom: 4px;
      display: block;
      text-transform: uppercase;
    }

    .mvv-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 19.5px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 6px;
    }

    .mvv-text {
      font-size: 12.8px;
      color: rgba(255, 255, 255, 0.88);
      line-height: 1.48;
    }

    /* Rodapé Institucional Limpo */
    .vortice-clean-footer {
      max-width: 1380px;
      width: 100%;
      margin: 0 auto;
      padding: 18px 0 10px;
      border-top: 1px solid rgba(255, 255, 255, 0.16);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      font-size: 13px;
      color: rgba(255, 255, 255, 0.70);
    }

    .footer-links-inline {
      display: flex;
      align-items: center;
      gap: 24px;
      flex-wrap: nowrap;
    }

    .footer-links-inline a {
      color: rgba(255, 255, 255, 0.88);
      text-decoration: none;
      white-space: nowrap;
      font-weight: 600;
      transition: color 0.2s ease;
    }

    .footer-links-inline a:hover {
      color: var(--gold-accent);
    }

    /* ==========================================================================
       PÁGINA EXCLUSIVA DE CADA CANAL (#channel-portal-overlay)
       - Padronizada em todas as 10 páginas com o contraste Noir-Neon de alto impacto
         (Preto Profundo #050811 + Ciano Elétrico #00f5d4 + Roxo/Magenta Neon #a855f7 / #ff2a6d)
       - O que muda de um canal para outro são o Banner Full-Bleed, a Logo Oficial,
         as 6 Imagens Cruas das Músicas/Episódios e os Textos/Áudios exclusivos!
       - Sem botões de seção no topo, sem bordas amarelas, sem caixas fechando seções
         e sem etiquetas "SEÇÃO 02", "FAIXA 01" ou "IDENTIDADE OFICIAL DO YOUTUBE".
       ========================================================================== */
    .channel-dedicated-page {
      --ch-bg: transparent;
      --ch-accent: #34d399;
      --ch-secondary: #10b981;
      --ch-tertiary: #059669;
      --ch-glow-a: rgba(52, 211, 153, 0.30);
      --ch-glow-b: rgba(16, 185, 129, 0.26);
      --ch-font: 'Orbitron', sans-serif;
      position: fixed;
      inset: 0;
      z-index: 300;
      width: 100vw;
      height: 100vh;
      overflow-y: auto;
      overflow-x: hidden;
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.32s ease, visibility 0.32s ease;
      background: transparent;
      color: #ffffff;
      scroll-behavior: smooth;
    }

    body.channel-view-active #hero-stage,
    body.channel-view-active .scroll-universe {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }

    .channel-dedicated-page.open {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }

    .channel-dedicated-page:not(.open) .ch-vortice-logo-return,
    .platform-claim-overlay:not(.open) .ch-vortice-logo-return {
      pointer-events: none !important;
      visibility: hidden !important;
    }

    /* ==========================================================================
       PLACA AMARELA "VÓRTICE MÍDIA • VOLTAR AO PORTAL" NO CANTO SUPERIOR ESQUERDO
       - Apenas a Placa Amarela limpa (sem texto de cuidado/perigo/radiação, sem símbolo de perigo e sem bolinha preta)!
       - Com a Logo Oficial Vórtice Mídia (funil + escrita oficial estática do print) maior direto no fundo amarelo
         + a informação "← VOLTAR AO PORTAL" direto na placa!
       ========================================================================== */
    @keyframes hazardWindSway {
      0%   { transform: perspective(900px) translate3d(0px, 0px, 0px) rotateZ(1.6deg) rotateY(4deg) rotateX(2deg); }
      25%  { transform: perspective(900px) translate3d(3px, 4px, 6px) rotateZ(-1.4deg) rotateY(-3.5deg) rotateX(-1.5deg); }
      50%  { transform: perspective(900px) translate3d(-2px, -3px, 2px) rotateZ(2.1deg) rotateY(2.5deg) rotateX(2.5deg); }
      75%  { transform: perspective(900px) translate3d(2px, 3px, 5px) rotateZ(-1.8deg) rotateY(-4deg) rotateX(-2deg); }
      100% { transform: perspective(900px) translate3d(0px, 0px, 0px) rotateZ(1.6deg) rotateY(4deg) rotateX(2deg); }
    }

    .ch-sticky-navbar {
      position: fixed;
      top: 8px;
      left: 14px;
      z-index: 330;
      background: none;
      backdrop-filter: none;
      border: none;
      padding: 0;
      pointer-events: none;
    }

    .ch-page-topbar {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      margin: 0;
    }

    .ch-vortice-logo-return {
      pointer-events: auto;
      display: flex;
      flex-direction: column;
      align-items: stretch;
      justify-content: space-between;
      width: 238px;
      min-width: 238px;
      max-width: 238px;
      height: 64px;
      padding: 0;
      border-radius: 8px;
      background:
        linear-gradient(135deg, #fde047 0%, #facc15 50%, #eab308 100%);
      border: 2.5px solid #18181b;
      box-shadow:
        0 0 0 1px rgba(254, 240, 138, 0.82),
        0 5px 0 #09090b,
        0 12px 24px rgba(0, 0, 0, 0.90),
        inset 0 0 10px rgba(161, 98, 7, 0.25);
      overflow: hidden;
      cursor: pointer;
      user-select: none;
      text-decoration: none;
      animation: hazardWindSway 5.4s ease-in-out infinite;
      transform-origin: center top;
      transition: box-shadow 0.25s ease, filter 0.25s ease;
    }

    .ch-vortice-logo-return:hover {
      animation-play-state: paused;
      transform: perspective(900px) translate3d(0px, -1px, 10px) rotateZ(0deg) rotateY(0deg) rotateX(0deg) scale(1.04);
      filter: brightness(1.05);
      box-shadow:
        0 0 0 1.5px #fef08a,
        0 6px 0 #09090b,
        0 16px 32px rgba(0, 0, 0, 0.96),
        0 0 20px rgba(250, 204, 21, 0.55);
    }

    /* Faixas Zebradas Superior e Inferior (Amarelo e Preto Diagonal — sem texto de radiação!) */
    .hazard-zebra-bar {
      width: 100%;
      height: 6.5px;
      flex-shrink: 0;
      background: repeating-linear-gradient(
        -45deg,
        #111827 0px,
        #111827 7px,
        #facc15 7px,
        #facc15 14px
      );
    }

    .hazard-zebra-bar.top {
      border-bottom: 1.5px solid #111827;
    }

    .hazard-zebra-bar.bottom {
      border-top: 1.5px solid #111827;
    }

    /* Corpo Central Retangular em Colunas Lado a Lado:
       [Funil + VÓRTICE MÍDIA (Logo Oficial)] | [← VOLTAR / AO PORTAL] */
    .hazard-plate-middle {
      flex: 1;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 7px 0 6px;
      gap: 5px;
      min-height: 0;
    }

    /* Logo Oficial Vórtice Mídia (Funil + Escrita 3D Oficial do Print) direto no fundo amarelo! */
    .ch-yellow-plate-official-logo {
      height: 40px;
      width: auto;
      max-width: 146px;
      object-fit: contain;
      display: block;
      background: transparent;
      flex-shrink: 0;
      filter:
        drop-shadow(0 1.5px 2.5px rgba(0, 0, 0, 0.82))
        drop-shadow(0 0 1px rgba(0, 0, 0, 0.95));
    }

    .hazard-col-divider {
      width: 1.5px;
      height: 28px;
      background: rgba(17, 24, 39, 0.32);
      border-radius: 2px;
      flex-shrink: 0;
    }

    /* Coluna da Direita: "← VOLTAR" em cima e "AO PORTAL" embaixo direto no fundo amarelo! */
    .hazard-return-col {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 2px;
      flex: 1;
      min-width: 0;
    }

    .hazard-return-line1 {
      font-family: 'Chakra Petch', 'Inter', sans-serif;
      font-size: 10px;
      font-weight: 900;
      letter-spacing: 0.06em;
      color: #111827;
      text-transform: uppercase;
      text-shadow: 0 1px 0 rgba(255, 255, 255, 0.78);
      line-height: 1.05;
      white-space: nowrap;
    }

    .hazard-return-line2 {
      font-family: 'Chakra Petch', 'Inter', sans-serif;
      font-size: 9px;
      font-weight: 900;
      letter-spacing: 0.05em;
      color: #111827;
      text-transform: uppercase;
      text-shadow: 0 1px 0 rgba(255, 255, 255, 0.78);
      line-height: 1.05;
      white-space: nowrap;
    }

    /* ==========================================================================
       SEÇÃO 1 DA PÁGINA DO CANAL: FULL-BLEED BANNER EM 1 ÚNICA ROLAGEM (100VH EXATO)
       - Sem logo escrita dentro da arte do banner!
       - Cabe 100% na primeira tela (100vh) sem invadir a Seção 2!
       ========================================================================== */
    .ch-page-hero {
      position: relative;
      width: 100%;
      height: 100vh;
      min-height: 680px;
      max-height: 100vh;
      margin-top: 0;
      margin-bottom: 140px;
      padding: 84px 48px 92px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      overflow: hidden;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .ch-hero-fullbleed-art {
      position: absolute;
      inset: 0;
      z-index: 1;
      overflow: hidden;
      pointer-events: none;
    }

    .ch-hero-fullbleed-art img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 24%;
      filter: saturate(1.12) contrast(1.06) brightness(0.95);
      transform: scale(1.01);
    }

    /* Degradê suave nas bordas superior, laterais e inferior fundindo na transparência do vórtice */
    .ch-hero-fullbleed-art::after {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(180deg,
          rgba(4, 5, 8, 0.68) 0%,
          rgba(4, 5, 8, 0.14) 22%,
          rgba(4, 5, 8, 0.10) 54%,
          rgba(4, 5, 8, 0.78) 84%,
          rgba(4, 5, 8, 0.92) 100%),
        radial-gradient(ellipse at 50% 42%,
          transparent 52%,
          rgba(4, 5, 8, 0.64) 88%,
          rgba(4, 5, 8, 0.90) 100%);
    }

    .ch-page-hero-content {
      position: relative;
      z-index: 5;
      max-width: 1380px;
      width: 100%;
      margin: 0 auto;
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: flex-end;
      gap: 28px;
    }

    /* Quadradinho da Foto de Perfil com a Logo Oficial do Canal em Proporção 1:1 Sem Margens */
    .ch-page-logo {
      width: 128px;
      height: 128px;
      object-fit: cover;
      border-radius: 22px;
      background: rgba(10, 12, 18, 0.85);
      border: 1.5px solid rgba(255, 255, 255, 0.35);
      padding: 0;
      box-shadow:
        0 20px 46px rgba(0, 0, 0, 0.95),
        0 0 24px rgba(255, 255, 255, 0.18);
      flex-shrink: 0;
    }

    .ch-page-title-block h1 {
      font-family: 'Cinzel', Georgia, serif;
      font-size: clamp(32px, 3.8vw, 50px);
      font-weight: 900;
      letter-spacing: 0.04em;
      color: #ffffff;
      text-shadow:
        0 3px 0 rgba(0, 0, 0, 0.90),
        0 12px 32px rgba(0, 0, 0, 0.95);
      margin: 0 0 6px;
      line-height: 1.1;
      text-transform: uppercase;
    }

    .ch-slogan-line {
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      font-size: 18.5px;
      color: #f7d07a;
      margin-bottom: 8px;
      text-shadow: 0 4px 16px rgba(0, 0, 0, 0.95);
    }

    .ch-hero-cta-col {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 10px;
    }

    /* ==========================================================================
       BOTÕES 3D PUROS DE ÍCONE DAS PLATAFORMAS (O PRÓPRIO SÍMBOLO É O BOTÃO!)
       - Igualzinho ao conceito das Placas da primeira página, porém em escala de destaque
         para os cards de música e para o Hero do canal!
       - Sem retângulo de texto "Spotify", "Deezer", etc. O ícone 3D É o botão!
       ========================================================================== */
    .ch-pure-icons-row {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      gap: 12px;
      flex-wrap: wrap;
    }

    .ch-plat-icon-3d {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      text-decoration: none;
      border: 1.5px solid rgba(255, 255, 255, 0.68);
      box-shadow:
        0 4px 0 rgba(0, 0, 0, 0.92),
        0 8px 18px rgba(0, 0, 0, 0.78),
        inset 0 2px 2px rgba(255, 255, 255, 0.72);
      transition: transform 0.18s cubic-bezier(0.16, 1, 0.3, 1), filter 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
      flex-shrink: 0;
      cursor: pointer;
    }

    .ch-plat-icon-3d svg {
      width: 23px;
      height: 23px;
      fill: #ffffff;
      filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.55));
    }

    .ch-plat-icon-3d.spotify { background: linear-gradient(180deg, #24e06a 0%, #108a3e 100%); }
    .ch-plat-icon-3d.deezer  { background: linear-gradient(180deg, #a855f7 0%, #6b21a8 100%); }
    .ch-plat-icon-3d.apple   { background: linear-gradient(180deg, #ff3b5c 0%, #be123c 100%); }
    .ch-plat-icon-3d.amazon  { background: linear-gradient(180deg, #00b4f5 0%, #006699 100%); }
    .ch-plat-icon-3d.youtube { background: linear-gradient(180deg, #ff2a2a 0%, #b30000 100%); }

    .ch-plat-icon-3d:hover {
      transform: translateY(-4px) scale(1.14);
      filter: brightness(1.16);
      border-color: #ffffff;
      box-shadow:
        0 7px 0 rgba(0, 0, 0, 0.92),
        0 14px 26px rgba(0, 0, 0, 0.88),
        0 0 18px rgba(255, 255, 255, 0.35),
        inset 0 2px 3px rgba(255, 255, 255, 0.9);
    }

    .ch-plat-icon-3d:active {
      transform: translateY(1px) scale(0.98);
    }

    /* ==========================================================================
       CORPO DE SEÇÕES DA PÁGINA DO CANAL (SEÇÕES 2 A 7)
       - Padronizado 100% com a Página Principal (vorticemidia.com.br):
         * Espaçamento/suspiro padronizado e generoso entre TODAS as seções (padding: 150px 36px 150px),
           sem espaço minúsculo após Músicas e sem espaço exagerado desigual após a Loja!
         * Fundo cinza escuro transparente uniforme (background: rgba(4, 5, 8, 0.22))
         * ZERO linhas separando as seções (border: none)
         * Títulos centralizados com a mesma fonte ('Cinzel') da Home!
       ========================================================================== */
    .ch-page-body {
      width: 100%;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      gap: 0;
    }

    .ch-section-block {
      width: 100%;
      min-height: 0;
      padding: 150px 36px 150px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      position: relative;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .ch-sec-inner {
      max-width: 1380px;
      width: 100%;
      margin: 0 auto;
    }

    /* Identidade Visual Unificada Cinza Escuro Translúcido para TODAS as Seções de TODOS os 10 Canais (Seções 2 a 7):
       - Exatamente igual à primeira página (sem verde, sem roxo e sem linhas divisórias!) */
    #ch-sec-historia,
    #ch-sec-repertorio,
    #ch-sec-loja,
    #ch-sec-cronicas,
    #ch-sec-bastidores,
    #ch-sec-guia,
    #ch-sec-plataformas {
      --sec-accent: #f7d07a;
      --sec-accent-soft: rgba(255, 255, 255, 0.22);
      --sec-card-bg: rgba(10, 12, 18, 0.56);
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    #ch-sec-plataformas {
      padding-bottom: 160px;
    }

    .ch-sec-header {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 20px;
      margin-top: 0;
      margin-bottom: 44px;
      border: none;
      padding-bottom: 0;
    }

    .ch-sec-title {
      font-family: 'Cinzel', Georgia, serif;
      font-size: clamp(30px, 3.3vw, 44px);
      font-weight: 900;
      letter-spacing: 0.04em;
      line-height: 1.15;
      text-transform: uppercase;
      color: #ffffff;
      text-align: center;
      margin: 0;
      text-shadow:
        0 3px 0 rgba(0, 0, 0, 0.90),
        0 12px 32px rgba(0, 0, 0, 0.95);
    }

    .ch-sec-subtitle {
      font-size: 15px;
      color: rgba(226, 232, 240, 0.88);
      margin: 8px 0 0;
      text-align: center;
    }

    /* ==========================================================================
       SEÇÃO 2: SOBRE O CANAL, PROPÓSITO & IDENTIDADE CANÔNICA
       - Ambos os lados (História à esquerda e Identidade à direita) dentro de cards
         cinza escuro translúcido padronizados igual à Força Criativa da Home!
       ========================================================================== */
    .ch-story-editorial-grid {
      display: grid;
      grid-template-columns: 1.35fr 0.85fr;
      gap: 24px;
      align-items: stretch;
    }

    #portal-story-left {
      border-radius: 18px;
      padding: 28px 32px;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      display: flex;
      flex-direction: column;
      justify-content: center;
      transition: all 0.25s ease;
    }

    #portal-story-left:hover {
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
    }

    .ch-story-lead {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 21px;
      font-weight: 700;
      line-height: 1.50;
      color: #f7d07a;
      margin-bottom: 16px;
    }

    .ch-story-p {
      font-size: 15.2px;
      line-height: 1.72;
      color: rgba(255, 255, 255, 0.92);
      margin-bottom: 14px;
    }

    .ch-story-p:last-child {
      margin-bottom: 0;
    }

    .ch-persona-dossier-box {
      border-radius: 18px;
      padding: 28px 30px;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      display: flex;
      flex-direction: column;
      justify-content: center;
      transition: all 0.25s ease;
    }

    .ch-persona-dossier-box:hover {
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
    }

    .ch-persona-tag {
      font-family: 'Orbitron', sans-serif;
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #f7d07a;
      margin-bottom: 6px;
    }

    .ch-persona-quote {
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      font-size: 18px;
      line-height: 1.58;
      color: #ffffff;
      margin: 14px 0;
      padding-left: 16px;
      border-left: 3px solid #f7d07a;
    }

    /* ==========================================================================
       SEÇÃO 3: CATÁLOGO DE MÚSICAS / EPISÓDIOS COM IMAGEM CRUA (SEM TEXTO)
       + ÍCONES 3D PUROS DAS PLATAFORMAS (MESMO CINZA ESCURO TRANSLÚCIDO DA HOME!)
       ========================================================================== */
    .ch-tracks-grid {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 24px;
    }

    .ch-track-card {
      width: min(100%, 420px);
      flex: 0 1 420px;
      border-radius: 16px;
      overflow: hidden;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }

    .ch-tracks-grid.single-card-mode .ch-track-card {
      width: min(100%, 560px);
      flex: 0 1 560px;
    }

    .ch-validation-status-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 14px;
      border-radius: 10px;
      background: rgba(247, 208, 122, 0.12);
      border: 1px solid rgba(247, 208, 122, 0.45);
      color: #f7d07a;
      font-family: 'Chakra Petch', sans-serif;
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .ch-track-card:hover {
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow:
        0 22px 46px rgba(0, 0, 0, 0.88),
        0 0 20px rgba(255, 255, 255, 0.28);
      transform: translateY(-5px);
    }

    .ch-track-raw-thumb-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      overflow: hidden;
      background: #04060c;
      border-bottom: 1px solid rgba(255, 255, 255, 0.16);
    }

    .ch-track-raw-thumb-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.55s ease, filter 0.35s ease;
    }

    .ch-track-card:hover .ch-track-raw-thumb-wrap img {
      transform: scale(1.06);
      filter: brightness(1.08) contrast(1.05);
    }

    .ch-track-style-chip {
      position: absolute;
      bottom: 10px;
      left: 12px;
      padding: 4px 11px;
      border-radius: 999px;
      background: rgba(10, 12, 18, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.35);
      color: #f7d07a;
      font-family: 'Chakra Petch', sans-serif;
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      backdrop-filter: blur(6px);
    }

    .ch-track-body {
      padding: 18px 20px 20px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
      gap: 14px;
    }

    .ch-track-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 20.5px;
      font-weight: 800;
      color: #ffffff;
      margin: 0 0 6px;
      line-height: 1.22;
    }

    .ch-track-story {
      font-size: 13.5px;
      line-height: 1.58;
      color: rgba(255, 255, 255, 0.88);
      margin: 0;
    }

    .ch-track-actions-stack {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      padding-top: 10px;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }

    /* ==========================================================================
       SEÇÕES 4, 5 E 6: PILARES DO UNIVERSO, BASTIDORES DE PRODUÇÃO & GUIA DO PÚBLICO
       (Mesmo card cinza escuro translúcido + borda branca no hover da Página Principal!)
       ========================================================================== */
    .ch-chronicles-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }

    .ch-neon-pillar-card {
      border-radius: 16px;
      padding: 24px 26px;
      background: rgba(10, 12, 18, 0.56);
      backdrop-filter: blur(4px);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 16px 38px rgba(0, 0, 0, 0.72);
      transition: all 0.25s ease;
    }

    .ch-neon-pillar-card:hover {
      transform: translateY(-5px);
      background: rgba(18, 22, 32, 0.88);
      border-color: #ffffff;
      box-shadow: 0 22px 46px rgba(0, 0, 0, 0.88), 0 0 20px rgba(255, 255, 255, 0.28);
    }

    .ch-neon-pillar-tag {
      font-family: 'Orbitron', sans-serif;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #f7d07a;
      margin-bottom: 8px;
    }

    .ch-neon-pillar-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 20.5px;
      font-weight: 800;
      color: #ffffff;
      margin: 0 0 10px;
    }

    .ch-neon-pillar-text {
      font-size: 13.8px;
      line-height: 1.62;
      color: rgba(255, 255, 255, 0.88);
      margin: 0;
    }

    .ch-faq-grid-2col {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }

    /* ==========================================================================
       LOJA OFICIAL VÓRTICE MÍDIA (HOME) + LOJA EXCLUSIVA DE CADA CANAL (#ch-sec-loja)
       - Cor Invertida com "As Mais Tocadas": Vinho / Roxo / Rubi Translúcido!
       - Esteira ampliada + cards dimensionados (268px) para caberem 4 blocos inteiros lado a lado!
       - Botões sem verde e sem azul (Ouro/Âmbar Imperial e Vinho/Rubi Imperial)!
       ========================================================================== */
    .section-vortice-store {
      --store-aligned-width: min(1220px, calc(100vw - 156px));
      position: relative;
      width: 100%;
      min-height: 108vh;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      padding: 104px 16px 64px;
      background: rgba(4, 5, 8, 0.22);
      border: none;
    }

    .section-vortice-store .container-wide {
      max-width: 1460px;
      width: 100%;
    }

    .section-vortice-store .editorial-header {
      text-align: center;
      margin-top: 0;
      margin-bottom: 36px;
    }

    /* Grade de 5 colunas x 2 linhas para os 10 Botões das Lojas dos Canais (Formato Placa Retangular, Sem Logo) */
    .store-channels-nav-bar {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 12px;
      width: var(--store-aligned-width);
      max-width: var(--store-aligned-width);
      margin: 0 auto 30px;
    }

    .store-channel-ShortcutBtn {
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      min-height: 46px;
      padding: 10px 10px;
      border-radius: 10px;
      background: rgba(10, 12, 18, 0.56);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      color: #ffffff;
      font-family: 'Orbitron', 'Chakra Petch', sans-serif;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      cursor: pointer;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(6px);
      transition: all 0.2s ease;
    }

    .store-channel-ShortcutBtn:hover,
    .store-channel-ShortcutBtn:active {
      background: rgba(18, 22, 32, 0.90);
      border-color: #ffffff;
      color: #ffffff;
      box-shadow:
        0 12px 26px rgba(0, 0, 0, 0.88),
        0 0 16px rgba(255, 255, 255, 0.30);
      transform: translateY(-2px);
    }

    /* Container da Esteira Horizontal Alinhado 100% com a Largura dos 10 Botões Acima
       e com os Botões de Seta (< e >) Posicionados do Lado de Fora! */
    .store-conveyor-outer {
      position: relative;
      width: var(--store-aligned-width);
      max-width: var(--store-aligned-width);
      margin: 0 auto;
      display: block;
    }

    .store-conveyor-arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 46px;
      height: 46px;
      border-radius: 12px;
      background: rgba(10, 12, 18, 0.62);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      color: #ffffff;
      font-size: 20px;
      font-weight: 900;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(6px);
      transition: all 0.2s ease;
      z-index: 10;
      user-select: none;
    }

    .store-conveyor-arrow.prev {
      left: -58px;
    }

    .store-conveyor-arrow.next {
      right: -58px;
    }

    .store-conveyor-arrow:hover {
      background: rgba(18, 22, 32, 0.92);
      border-color: #ffffff;
      box-shadow:
        0 14px 28px rgba(0, 0, 0, 0.90),
        0 0 16px rgba(255, 255, 255, 0.30);
      transform: translateY(calc(-50% - 2px)) scale(1.05);
    }

    .store-conveyor-arrow:active {
      transform: translateY(calc(-50% + 1px));
    }

    .store-conveyor-viewport {
      width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      scrollbar-width: none;
      -ms-overflow-style: none;
      padding: 10px 0 16px;
      scroll-behavior: auto;
    }

    .store-conveyor-viewport::-webkit-scrollbar {
      display: none;
    }

    .store-conveyor-track {
      display: flex;
      align-items: stretch;
      gap: 12px;
      width: max-content;
    }

    /* Grade de 1 linha (4 cards) dentro da página de cada canal */
    .vortice-store-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }

    /* Card de Produto em Cinza Escuro Translúcido Padronizado alinhado exatamente com as 5 colunas da barra superior */
    .store-product-card {
      width: calc((var(--store-aligned-width) - 48px) / 5);
      min-width: calc((var(--store-aligned-width) - 48px) / 5);
      max-width: calc((var(--store-aligned-width) - 48px) / 5);
      border-radius: 16px;
      overflow: hidden;
      background: rgba(10, 12, 18, 0.65);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 14px 32px rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(6px);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.24s ease, border-color 0.24s ease, box-shadow 0.24s ease, background 0.24s ease;
    }

    .vortice-store-grid .store-product-card {
      width: 100%;
      min-width: 0;
      max-width: none;
    }

    .store-product-card:hover {
      transform: translateY(-6px);
      background: rgba(16, 20, 28, 0.88);
      border-color: #ffffff;
      box-shadow:
        0 20px 44px rgba(0, 0, 0, 0.92),
        0 0 22px rgba(255, 255, 255, 0.24);
    }

    /* Vitrine Oficial de Produtos Reais Amazon no Fundo Branco Original 100% Nítido (vorticemidia-20) */
    .store-prod-visual {
      position: relative;
      width: 100%;
      height: 168px;
      overflow: hidden;
      background: #ffffff;
      border-bottom: 1.5px solid rgba(255, 255, 255, 0.16);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 10px;
      text-align: center;
      cursor: pointer;
    }

    .store-prod-real-img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.26s ease;
    }

    .store-product-card:hover .store-prod-real-img {
      transform: scale(1.06);
    }

    .store-coming-soon-stamp {
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 10px 18px;
      border-radius: 12px;
      background: rgba(10, 12, 18, 0.65);
      border: 1.5px solid rgba(255, 255, 255, 0.38);
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.75);
      transition: transform 0.24s ease, border-color 0.24s ease, box-shadow 0.24s ease;
    }

    .store-product-card:hover .store-coming-soon-stamp {
      transform: scale(1.05);
      border-color: #ffffff;
      box-shadow:
        0 14px 28px rgba(0, 0, 0, 0.88),
        0 0 18px rgba(255, 255, 255, 0.28);
    }

    .store-coming-soon-word {
      font-family: 'Orbitron', sans-serif;
      font-size: 18px;
      font-weight: 900;
      letter-spacing: 0.14em;
      color: #ffffff;
      text-transform: uppercase;
      text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95);
    }

    .store-prod-body {
      padding: 14px 12px 10px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      flex: 1;
      text-align: center;
    }

    .store-prod-title {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.32;
      margin: 0;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .store-prod-actions {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 0 10px 14px;
    }

    /* Botão "Quero Este Item" Padronizado (Cinza Escuro Translúcido + Borda Branca no Hover) */
    .store-btn-buy {
      flex: 1;
      padding: 8px 6px;
      border-radius: 9px;
      background: rgba(10, 12, 18, 0.62);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      color: #ffffff;
      font-family: 'Chakra Petch', sans-serif;
      font-size: 10px;
      font-weight: 900;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      cursor: pointer;
      text-align: center;
      text-decoration: none;
      box-shadow: 0 6px 14px rgba(0, 0, 0, 0.65);
      transition: all 0.2s ease;
    }

    .store-btn-buy:hover,
    .store-btn-buy:active {
      background: rgba(18, 22, 32, 0.92);
      border-color: #ffffff;
      color: #ffffff;
      box-shadow:
        0 10px 22px rgba(0, 0, 0, 0.88),
        0 0 14px rgba(255, 255, 255, 0.30);
      transform: translateY(-2px);
    }

    /* Botão "Loja do Canal" Padronizado (Cinza Escuro Translúcido + Borda Branca no Hover) */
    .store-btn-channel {
      padding: 8px 8px;
      border-radius: 9px;
      background: rgba(10, 12, 18, 0.62);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      color: #ffffff;
      font-family: 'Chakra Petch', sans-serif;
      font-size: 9.5px;
      font-weight: 900;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      white-space: nowrap;
      cursor: pointer;
      box-shadow: 0 6px 14px rgba(0, 0, 0, 0.65);
      transition: all 0.2s ease;
    }

    .store-btn-channel:hover,
    .store-btn-channel:active {
      background: rgba(18, 22, 32, 0.92);
      border-color: #ffffff;
      color: #ffffff;
      box-shadow:
        0 10px 22px rgba(0, 0, 0, 0.88),
        0 0 14px rgba(255, 255, 255, 0.30);
      transform: translateY(-2px);
    }

    /* Na seção "Qual É o Seu Momento Agora?", o badge tem 1 frase emocional centralizada e maior */
    #destinos-vortice .social-official-3d-badge {
      padding: 11px 18px;
      justify-content: center;
    }

    #destinos-vortice .social-badge-col span:first-child {
      font-size: 14px;
      letter-spacing: 0.09em;
    }

    /* ==========================================================================
       PÁGINA INSTITUCIONAL DE PERFIL OFICIAL EM REIVINDICAÇÃO & HOMOLOGAÇÃO
       (#platform-claim-overlay)
       - Abre dentro do próprio site sempre que o visitante clica em uma plataforma
         musical/social cujo perfil de artista ainda está em processo de reivindicação!
       - Mantém o vórtice girando ao fundo com a mesma estética Cinza Escuro Translúcido!
       ========================================================================== */
    .platform-claim-overlay {
      position: fixed;
      inset: 0;
      z-index: 420;
      width: 100vw;
      height: 100vh;
      overflow-y: auto;
      overflow-x: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 90px 24px 36px;
      background: rgba(4, 5, 8, 0.72);
      backdrop-filter: blur(8px);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.28s ease, visibility 0.28s ease;
    }

    .platform-claim-overlay.open {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }

    .claim-dossier-card {
      position: relative;
      max-width: 780px;
      width: 100%;
      border-radius: 22px;
      padding: 38px 42px;
      background: rgba(10, 12, 18, 0.78);
      backdrop-filter: blur(8px);
      border: 1.5px solid rgba(255, 255, 255, 0.26);
      box-shadow:
        0 28px 70px rgba(0, 0, 0, 0.92),
        0 0 28px rgba(255, 255, 255, 0.14);
      text-align: center;
      color: #ffffff;
    }

    .claim-status-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 999px;
      background: rgba(16, 20, 30, 0.85);
      border: 1px solid rgba(247, 208, 122, 0.55);
      color: #f7d07a;
      font-family: 'Orbitron', sans-serif;
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      margin-bottom: 22px;
      box-shadow: 0 0 18px rgba(0, 0, 0, 0.65);
    }

    .claim-status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #f7d07a;
      box-shadow: 0 0 10px #f7d07a;
      animation: radioBtnBreathe 1.4s ease-in-out infinite;
    }

    .claim-bridge-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      margin-bottom: 22px;
    }

    .claim-ch-avatar {
      width: 82px;
      height: 82px;
      border-radius: 18px;
      object-fit: cover;
      border: 2px solid rgba(255, 255, 255, 0.45);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.85);
      background: #000000;
    }

    .claim-bridge-connector {
      display: flex;
      align-items: center;
      gap: 6px;
      color: #f7d07a;
      font-family: 'Orbitron', sans-serif;
      font-size: 12px;
      font-weight: 900;
      letter-spacing: 0.2em;
    }

    .claim-plat-badge-big {
      width: 82px;
      height: 82px;
      border-radius: 18px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border: 2px solid rgba(255, 255, 255, 0.72);
      box-shadow:
        0 6px 0 rgba(0, 0, 0, 0.88),
        0 14px 30px rgba(0, 0, 0, 0.82),
        inset 0 2px 3px rgba(255, 255, 255, 0.7);
    }

    .claim-plat-badge-big svg {
      width: 40px;
      height: 40px;
      fill: #ffffff;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.55));
    }

    .claim-main-title {
      font-family: 'Cinzel', Georgia, serif;
      font-size: clamp(22px, 2.8vw, 32px);
      font-weight: 900;
      color: #ffffff;
      line-height: 1.18;
      margin: 0 0 8px;
      text-transform: uppercase;
    }

    .claim-sub-headline {
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      font-size: 18px;
      color: #f7d07a;
      margin-bottom: 18px;
    }

    .claim-desc-box {
      background: rgba(10, 12, 18, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.20);
      border-radius: 16px;
      padding: 18px 22px;
      font-size: 14.8px;
      line-height: 1.68;
      color: rgba(241, 245, 249, 0.94);
      margin-bottom: 22px;
      text-align: left;
    }

    .claim-steps-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 26px;
      text-align: left;
    }

    .claim-step-item {
      padding: 12px 14px;
      border-radius: 12px;
      background: rgba(10, 12, 18, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.20);
    }

    .claim-step-item.active-step {
      background: rgba(18, 22, 32, 0.88);
      border-color: rgba(255, 255, 255, 0.65);
    }

    .claim-step-tag {
      font-family: 'Orbitron', sans-serif;
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #f7d07a;
      margin-bottom: 4px;
      display: block;
    }

    .claim-step-item.active-step .claim-step-tag {
      color: #ffffff;
    }

    .claim-step-title {
      font-size: 12.5px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
    }

    .claim-actions-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      flex-wrap: wrap;
    }

    .claim-btn-primary,
    .claim-btn-secondary,
    .claim-btn-back {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 9px;
      padding: 13px 22px;
      border-radius: 12px;
      background: rgba(10, 12, 18, 0.68);
      border: 1.5px solid rgba(255, 255, 255, 0.26);
      color: #ffffff;
      font-family: 'Chakra Petch', sans-serif;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      text-decoration: none;
      cursor: pointer;
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.72);
      transition: all 0.2s ease;
    }

    .claim-btn-primary:hover,
    .claim-btn-secondary:hover,
    .claim-btn-back:hover {
      transform: translateY(-2px);
      background: rgba(18, 22, 32, 0.92);
      border-color: #ffffff;
      box-shadow: 0 14px 32px rgba(0, 0, 0, 0.88), 0 0 18px rgba(255, 255, 255, 0.28);
    }

    .claim-btn-PrimarySvg {
      width: 18px;
      height: 18px;
      fill: #ffffff;
    }

    @media (max-width: 1180px) {
      .momentos-photo-grid, .universos-grid, .studio-cards-3col, .mvv-corporate-grid, .flying-signs-platforms-grid, .ch-chronicles-grid, .ch-tracks-grid, .vortice-store-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .studio-hero-banner, .ch-page-hero-content, .ch-story-editorial-grid, .ch-faq-grid-2col, .claim-steps-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 720px) {
      .momentos-photo-grid, .universos-grid, .studio-cards-3col, .ivory-grid-inputs, .mvv-corporate-grid, .flying-signs-platforms-grid, .ch-chronicles-grid, .ch-tracks-grid, .ch-faq-grid-2col, .vortice-store-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>

  <!-- =========================================================================
       CAMADA FIXA DO TORNADO 8K GIRANDO NO DESERTO COM DESTROÇOS VOANDO
       ========================================================================= -->
  <div id="cinema-stage">
    <canvas id="vortex-canvas"></canvas>
    <div class="cinema-vignette"></div>
  </div>

  <!-- =========================================================================
       PLACA MERCOSUL "RÁDIO VÓRTICE" FIXA NO CANTO SUPERIOR DIREITO
       (Fica fixa na tela durante todo o scroll e continua balançando no vento!)
       ========================================================================= -->
  <div id="vortice-radio-widget" title="Placa Mercosul Rádio Vórtice — Clique para Tocar ou Pausar">
    <div class="mercosul-top-bar">
      <span class="mercosul-left-emblem" aria-hidden="true">
        <!-- Emblema Cruzeiro do Sul + Linha Orbital Curva (Maior e sem texto MERCOSUL) -->
        <svg viewBox="0 0 36 26">
          <!-- Arco / Linha curva orbital do Cruzeiro -->
          <path d="M2 21 Q18 12 34 19" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" fill="none"/>
          <!-- 4 Estrelas do Cruzeiro do Sul -->
          <polygon points="18,2 19.1,4.8 22,5.1 19.8,6.9 20.5,9.7 18,8.1 15.5,9.7 16.2,6.9 14,5.1 16.9,4.8" fill="#ffffff"/>
          <polygon points="18,14 19.1,16.8 22,17.1 19.8,18.9 20.5,21.7 18,20.1 15.5,21.7 16.2,18.9 14,17.1 16.9,16.8" fill="#ffffff"/>
          <polygon points="10,8 10.9,10.3 13.4,10.6 11.5,12.1 12.1,14.5 10,13.1 7.9,14.5 8.5,12.1 6.6,10.6 9.1,10.3" fill="#ffffff"/>
          <polygon points="26,7.5 26.9,9.8 29.4,10.1 27.5,11.6 28.1,14 26,12.6 23.9,14 24.5,11.6 22.6,10.1 25.1,9.8" fill="#ffffff"/>
        </svg>
      </span>
      <span class="mercosul-country-title">BRASIL</span>
      <span class="mercosul-br-flag" aria-hidden="true">
        <svg viewBox="0 0 28 20" width="100%" height="100%">
          <rect width="28" height="20" fill="#009b3a"/>
          <polygon points="14,2 26,10 14,18 2,10" fill="#fedf00"/>
          <circle cx="14" cy="10" r="4.6" fill="#002776"/>
          <path d="M10 9.5 Q14 7.8 18 10.8" stroke="#ffffff" stroke-width="1.2" fill="none"/>
        </svg>
      </span>
    </div>
    <div class="mercosul-plate-body">
      <button type="button" class="radio-speaker-btn" id="radio-toggle-btn" onclick="toggleVorticeRadio()">
        <span class="radio-wave-ring r1"></span>
        <span class="radio-wave-ring r2"></span>
        <svg viewBox="0 0 24 24" id="radio-speaker-svg">
          <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
        </svg>
      </button>
      <div class="radio-info-col" onclick="toggleVorticeRadio()">
        <div class="radio-brand-row">
          <span class="radio-title-badge">RÁDIO VÓRTICE</span>
          <div class="radio-eq-bars">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
        </div>
        <div class="radio-now-playing" id="radio-track-label">Clique para Sintonizar ▶</div>
      </div>
      <button type="button" class="radio-next-btn" onclick="nextVorticeRadioTrack(event)" title="Próxima Música">⏭</button>
    </div>
  </div>

  <!-- =========================================================================
       DOBRA 1 (HERO):
       - LOGO VÓRTICE MÍDIA COMO BOTÃO INTERATIVO: CLICOU ALINHA AS 10 PLACAS DE FRENTE,
         CLICOU DE NOVO ELAS VOLTAM A GIRAR EM ÓRBITA 3D NO TORNADO!
       ========================================================================= -->
  <section id="hero-stage">
    <div class="hero-left-wing">
      <button type="button" class="vortice-logo-btn-wrap" id="vortice-logo-toggle-btn" onclick="toggleHeroSignsAlignment()" title="Clique na Logo da Vórtice Mídia">
        <img class="vortice-logo-free" src="./assets/ui/vortice_midia_official_logo.png" alt="Vórtice Mídia">
        <span class="logo-align-hint-pill" id="logo-align-hint-text">Clique na Logo</span>
      </button>
    </div>

    <!-- Palco 3D de Tela Inteira onde as 10 Placas giram ao redor do Tornado -->
    <div id="vortex-orbit-stage"></div>
  </section>

  <!-- =========================================================================
       UNIVERSO DE ROLAGEM — CADA SESSÃO TEM TRANSPARÊNCIA PARA VER O VÓRTICE ATRÁS!
       ========================================================================= -->
  <div class="scroll-universe">

    <!-- SESSÃO 1: ESCOLHA SUA SINTONIA AGORA (SOMENTE OS 5 CANAIS DE MÚSICA + BOTÕES DO MESMO TAMANHO!) -->
    <section class="section-momentos" id="momentos">
      <div class="container-wide">
        <div class="editorial-header">
          <h2 class="editorial-giant-title">Escolha Sua Sintonia Agora</h2>
        </div>

        <div class="momentos-photo-grid">
          <!-- Card 1: Rock Incorruptível -->
          <div class="momento-photo-card">
            <div class="momento-img-wrap">
              <img src="./assets/banners/rock_youtube_banner.jpg" alt="Rock Incorruptível" loading="lazy">
            </div>
            <div class="momento-card-body">
              <span class="momento-kicker">ROCK INCORRUPTÍVEL</span>
              <h3 class="momento-title">Crítica Política</h3>
              <div class="momento-btn-row">
                <button type="button" class="momento-pill-btn sintonia-play-music-btn" data-sintonia-channel="rock-incorruptivel" onclick="playChannelMusicById('rock-incorruptivel')">▶ Ouvir Agora</button>
                <button type="button" class="momento-page-btn" onclick="openChannelById('rock-incorruptivel')">Página</button>
              </div>
            </div>
          </div>

          <!-- Card 2: Sacronia -->
          <div class="momento-photo-card">
            <div class="momento-img-wrap">
              <img src="./assets/banners/sacronia_youtube_banner.jpg" alt="Sacronia" loading="lazy">
            </div>
            <div class="momento-card-body">
              <span class="momento-kicker">SACRONIA</span>
              <h3 class="momento-title">Gospel Sacro Contemporâneo</h3>
              <div class="momento-btn-row">
                <button type="button" class="momento-pill-btn sintonia-play-music-btn" data-sintonia-channel="sacronia" onclick="playChannelMusicById('sacronia')">▶ Ouvir Agora</button>
                <button type="button" class="momento-page-btn" onclick="openChannelById('sacronia')">Página</button>
              </div>
            </div>
          </div>

          <!-- Card 3: Neon Asher -->
          <div class="momento-photo-card">
            <div class="momento-img-wrap">
              <img src="./assets/banners/neon_youtube_banner.jpg" alt="Neon Asher" loading="lazy">
            </div>
            <div class="momento-card-body">
              <span class="momento-kicker">NEON ASHER</span>
              <h3 class="momento-title">Rock Gótico</h3>
              <div class="momento-btn-row">
                <button type="button" class="momento-pill-btn sintonia-play-music-btn" data-sintonia-channel="neon-asher" onclick="playChannelMusicById('neon-asher')">▶ Ouvir Agora</button>
                <button type="button" class="momento-page-btn" onclick="openChannelById('neon-asher')">Página</button>
              </div>
            </div>
          </div>

          <!-- Card 4: Iago Cordeiro -->
          <div class="momento-photo-card">
            <div class="momento-img-wrap">
              <img src="./assets/banners/iago_youtube_banner.jpg" alt="Iago Cordeiro" loading="lazy">
            </div>
            <div class="momento-card-body">
              <span class="momento-kicker">IAGO CORDEIRO</span>
              <h3 class="momento-title">Louvor Congregacional</h3>
              <div class="momento-btn-row">
                <button type="button" class="momento-pill-btn sintonia-play-music-btn" data-sintonia-channel="iago-cordeiro" onclick="playChannelMusicById('iago-cordeiro')">▶ Ouvir Agora</button>
                <button type="button" class="momento-page-btn" onclick="openChannelById('iago-cordeiro')">Página</button>
              </div>
            </div>
          </div>

          <!-- Card 5: Patinhas & Canções -->
          <div class="momento-photo-card">
            <div class="momento-img-wrap">
              <img src="./assets/banners/patinhas_youtube_banner.jpg" alt="Patinhas e Canções" loading="lazy">
            </div>
            <div class="momento-card-body">
              <span class="momento-kicker">PATINHAS &amp; CANÇÕES</span>
              <h3 class="momento-title">Amor por Pets</h3>
              <div class="momento-btn-row">
                <button type="button" class="momento-pill-btn sintonia-play-music-btn" data-sintonia-channel="patinhas-e-cancoes" onclick="playChannelMusicById('patinhas-e-cancoes')">▶ Ouvir Agora</button>
                <button type="button" class="momento-page-btn" onclick="openChannelById('patinhas-e-cancoes')">Página</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SESSÃO 2: AS MAIS TOCADAS (ROXO TRANSLÚCIDO VENDO O VÓRTICE ATRÁS) -->
    <section class="section-top5" id="top5">
      <div class="top5-narrow-container">
        <h2 class="top5-serif-heading">As Mais Tocadas</h2>
        <div class="top5-cards-stack" id="top5-list-container"></div>
        <audio id="vortice-inline-audio" preload="none"></audio>
      </div>
    </section>

    <!-- SESSÃO 3: ÚLTIMOS VÍDEOS LONGOS DO YOUTUBE
         - Mesma estrutura de Escolha Sua Sintonia Agora (borda branquinha no hover + botões do mesmo tamanho)!
         - Sem textos "Clique para assistir..."!
         - Com os Banners Oficiais do YouTube de todos os 10 canais! -->
    <section class="section-universos" id="universos">
      <div class="container-wide">
        <div class="editorial-header">
          <h2 class="editorial-giant-title">Últimos Vídeos Longos do YouTube</h2>
        </div>

        <div class="universos-grid" id="latest-yt-videos-grid">
          <!-- 1. Águas de Descanso -->
          <div class="universo-poster-card" data-yt-handle="AguasDeDescanso">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/aguas_youtube_banner.jpg" alt="Águas de Descanso" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Leitura da Bíblia &amp; Descanso com Chuva</span>
              <h3 class="universo-channel-title">Águas de Descanso</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@AguasDeDescanso/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('aguas-de-descanso')">Página</button>
              </div>
            </div>
          </div>

          <!-- 2. Rock Incorruptível -->
          <div class="universo-poster-card" data-yt-handle="RockIncorruptivel">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/rock_youtube_banner.jpg" alt="Rock Incorruptível" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Crítica Política</span>
              <h3 class="universo-channel-title">Rock Incorruptível</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@RockIncorruptivel/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('rock-incorruptivel')">Página</button>
              </div>
            </div>
          </div>

          <!-- 3. Sacronia -->
          <div class="universo-poster-card" data-yt-handle="SacroniaMusic">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/sacronia_youtube_banner.jpg" alt="Sacronia" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Gospel Sacro Contemporâneo</span>
              <h3 class="universo-channel-title">Sacronia</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@SacroniaMusic/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('sacronia')">Página</button>
              </div>
            </div>
          </div>

          <!-- 4. Neon Asher -->
          <div class="universo-poster-card" data-yt-handle="NeonAsherDarkRock">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/neon_youtube_banner.jpg" alt="Neon Asher" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Rock Gótico</span>
              <h3 class="universo-channel-title">Neon Asher</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@NeonAsherDarkRock/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('neon-asher')">Página</button>
              </div>
            </div>
          </div>

          <!-- 5. Iago Cordeiro -->
          <div class="universo-poster-card" data-yt-handle="iagocordeiromusic">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/iago_youtube_banner.jpg" alt="Iago Cordeiro" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Louvor Congregacional</span>
              <h3 class="universo-channel-title">Iago Cordeiro</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@iagocordeiromusic/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('iago-cordeiro')">Página</button>
              </div>
            </div>
          </div>

          <!-- 6. Patinhas & Canções -->
          <div class="universo-poster-card" data-yt-handle="patinhasecancoes">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/patinhas_youtube_banner.jpg" alt="Patinhas e Canções" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Amor por Pets</span>
              <h3 class="universo-channel-title">Patinhas &amp; Canções</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@patinhasecancoes/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('patinhas-e-cancoes')">Página</button>
              </div>
            </div>
          </div>

          <!-- 7. Trono da Promessa -->
          <div class="universo-poster-card" data-yt-handle="TronoDaPromessa">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/trono_youtube_banner.jpg" alt="Trono da Promessa" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Série Bíblica Kids</span>
              <h3 class="universo-channel-title">Trono da Promessa</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@TronoDaPromessa/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('trono-da-promessa')">Página</button>
              </div>
            </div>
          </div>

          <!-- 8. Incorruptível -->
          <div class="universo-poster-card" data-yt-handle="CanalIncorruptivel">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/incorruptivel_youtube_banner.jpg" alt="Incorruptível" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Crítica Política</span>
              <h3 class="universo-channel-title">Incorruptível</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@CanalIncorruptivel/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('incorruptivel')">Página</button>
              </div>
            </div>
          </div>

          <!-- 9. Aliens da Bíblia -->
          <div class="universo-poster-card" data-yt-handle="AliensDaBiblia">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/aliens_youtube_banner.jpg" alt="Aliens da Bíblia" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Mistérios da Bíblia</span>
              <h3 class="universo-channel-title">Aliens da Bíblia</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@AliensDaBiblia/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('aliens-da-biblia')">Página</button>
              </div>
            </div>
          </div>

          <!-- 10. Aquário dos Felinos -->
          <div class="universo-poster-card" data-yt-handle="AquarioDosFelinos">
            <div class="universo-thumb-box">
              <img class="bg-art yt-auto-thumb" src="./assets/banners/aquario_youtube_banner.jpg" alt="Aquário dos Felinos" loading="lazy">
            </div>
            <div class="universo-body">
              <span class="universo-style-tag">Aventura Pet Infantil</span>
              <h3 class="universo-channel-title">Aquário dos Felinos</h3>
              <div class="momento-btn-row">
                <a href="https://www.youtube.com/@AquarioDosFelinos/videos" target="_blank" rel="noopener" class="momento-pill-btn yt-auto-link">▶ Assistir</a>
                <button type="button" class="momento-page-btn" onclick="openChannelById('aquario-dos-felinos')">Página</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SESSÃO 4: QUAL É O SEU MOMENTO AGORA? (PLACAS DE TRÂNSITO 3D FLUTUANDO NO VENTO COM RESPOSTAS DE SENTIMENTO/EMOÇÃO!) -->
    <section class="section-platforms-3d" id="destinos-vortice">
      <div class="container-wide">
        <h2 class="editorial-giant-title">Qual É o Seu Momento Agora?</h2>

        <div class="flying-signs-platforms-grid">
          <!-- 1. Voz de Protesto -> Rock Incorruptível -->
          <a href="#/rock-incorruptivel" onclick="event.preventDefault(); openChannelById('rock-incorruptivel');" class="social-road-sign" style="background-image:url('./assets/signs/sign_01_rock.png');--s-tilt:-7.5deg;--s-roty:18deg;--s-dx:16px;--s-delay:0s;">
            <div class="social-official-3d-badge badge-yt">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>VOZ DE PROTESTO</span>
              </div>
            </div>
          </a>

          <!-- 2. Emoção Sinfônica -> Sacronia -->
          <a href="#/sacronia" onclick="event.preventDefault(); openChannelById('sacronia');" class="social-road-sign" style="background-image:url('./assets/signs/sign_02_sacronia.png');--s-tilt:7.2deg;--s-roty:-16deg;--s-dx:-15px;--s-delay:0.35s;">
            <div class="social-official-3d-badge badge-dz">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>EMOÇÃO SINFÔNICA</span>
              </div>
            </div>
          </a>

          <!-- 3. Superando a Dor -> Neon Asher -->
          <a href="#/neon-asher" onclick="event.preventDefault(); openChannelById('neon-asher');" class="social-road-sign" style="background-image:url('./assets/signs/sign_03_neon.png');--s-tilt:-6.8deg;--s-roty:19deg;--s-dx:17px;--s-delay:0.75s;">
            <div class="social-official-3d-badge badge-tk">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>SUPERANDO A DOR</span>
              </div>
            </div>
          </a>

          <!-- 4. Paz & Gratidão -> Iago Cordeiro -->
          <a href="#/iago-cordeiro" onclick="event.preventDefault(); openChannelById('iago-cordeiro');" class="social-road-sign" style="background-image:url('./assets/signs/sign_04_iago.png');--s-tilt:7.6deg;--s-roty:-17deg;--s-dx:-16px;--s-delay:0.2s;">
            <div class="social-official-3d-badge badge-sp">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>PAZ &amp; GRATIDÃO</span>
              </div>
            </div>
          </a>

          <!-- 5. Carinho & Afeto -> Patinhas & Canções -->
          <a href="#/patinhas-e-cancoes" onclick="event.preventDefault(); openChannelById('patinhas-e-cancoes');" class="social-road-sign" style="background-image:url('./assets/signs/sign_05_patinhas.png');--s-tilt:-7.2deg;--s-roty:16deg;--s-dx:15px;--s-delay:0.55s;">
            <div class="social-official-3d-badge badge-ig">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>CARINHO &amp; AFETO</span>
              </div>
            </div>
          </a>

          <!-- 6. Sono & Descanso -> Águas de Descanso -->
          <a href="#/aguas-de-descanso" onclick="event.preventDefault(); openChannelById('aguas-de-descanso');" class="social-road-sign" style="background-image:url('./assets/signs/sign_06_aguas.png');--s-tilt:8.0deg;--s-roty:-19deg;--s-dx:-18px;--s-delay:0.95s;">
            <div class="social-official-3d-badge badge-am">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>SONO &amp; DESCANSO</span>
              </div>
            </div>
          </a>

          <!-- 7. Fé em Família -> Trono da Promessa -->
          <a href="#/trono-da-promessa" onclick="event.preventDefault(); openChannelById('trono-da-promessa');" class="social-road-sign" style="background-image:url('./assets/signs/sign_07_trono.png');--s-tilt:-7.4deg;--s-roty:18deg;--s-dx:16px;--s-delay:0.3s;">
            <div class="social-official-3d-badge badge-fb">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>FÉ EM FAMÍLIA</span>
              </div>
            </div>
          </a>

          <!-- 8. Sede de Mistério -> Aliens da Bíblia -->
          <a href="#/aliens-da-biblia" onclick="event.preventDefault(); openChannelById('aliens-da-biblia');" class="social-road-sign" style="background-image:url('./assets/signs/sign_09_aliens.png');--s-tilt:6.9deg;--s-roty:-16deg;--s-dx:-15px;--s-delay:0.7s;">
            <div class="social-official-3d-badge badge-ym">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>SEDE DE MISTÉRIO</span>
              </div>
            </div>
          </a>

          <!-- 9. Alegria em Casa -> Aquário dos Felinos -->
          <a href="#/aquario-dos-felinos" onclick="event.preventDefault(); openChannelById('aquario-dos-felinos');" class="social-road-sign" style="background-image:url('./assets/signs/sign_10_aquario.png');--s-tilt:-7.5deg;--s-roty:18deg;--s-dx:16px;--s-delay:1.1s;">
            <div class="social-official-3d-badge badge-ap">
              <div class="social-badge-col" style="align-items:center;text-align:center;">
                <span>ALEGRIA EM CASA</span>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- SESSÃO 4B: LOJA OFICIAL VÓRTICE MÍDIA (1 ÚNICA ESTEIRA HORIZONTAL AUTOMÁTICA + BOTÕES PARA AS LOJAS DOS 10 CANAIS!) -->
    <section class="section-vortice-store" id="loja-vortice">
      <div class="container-wide">
        <div class="editorial-header">
          <h2 class="editorial-giant-title">Loja Oficial Vórtice Mídia</h2>
        </div>

        <!-- Botões diretos para a Loja Oficial de cada um dos 10 Canais -->
        <div class="store-channels-nav-bar" id="home-store-channels-bar"></div>

        <!-- Esteira Horizontal Única com Rolagem Automática Infinita + Botões Esquerda/Direita -->
        <div class="store-conveyor-outer" id="home-store-conveyor-wrap">
          <button type="button" class="store-conveyor-arrow prev" onclick="scrollStoreConveyor(-1)" title="Passar para a Esquerda">&#10094;</button>
          <div class="store-conveyor-viewport" id="home-store-conveyor-viewport">
            <div class="store-conveyor-track" id="vortice-home-store-track"></div>
          </div>
          <button type="button" class="store-conveyor-arrow next" onclick="scrollStoreConveyor(1)" title="Passar para a Direita">&#10095;</button>
        </div>
      </div>
    </section>

    <!-- SESSÃO 5: RECEBA OS LANÇAMENTOS (TÍTULO FORA EM CIMA + BLOCO TRANSPARENTE EMBAIXO!) -->
    <section class="section-ivory-vip">
      <div class="container-wide">
        <div class="editorial-header">
          <h2 class="editorial-giant-title">Receba os Lançamentos</h2>
        </div>

        <div class="ivory-form-container">
          <p class="ivory-sub">Cadastre-se para receber os avisos sempre que uma música, clipe ou episódio novo estrear.</p>

          <form onsubmit="event.preventDefault(); alert('Cadastro confirmado! Você receberá os novos lançamentos da Vórtice Mídia no seu WhatsApp.');">
            <div class="ivory-grid-inputs">
              <div class="ivory-field">
                <label>SEU NOME</label>
                <input type="text" placeholder="Como te chamamos?" required>
              </div>
              <div class="ivory-field">
                <label>SEU WHATSAPP (COM DDD)</label>
                <input type="tel" placeholder="(00) 90000-0000" required>
              </div>
              <div class="ivory-field" style="grid-column: 1 / -1;">
                <label>CANAL FAVORITO</label>
                <select>
                  <option>Todos os 10 Canais da Vórtice Mídia</option>
                  <option>Rock Incorruptível</option>
                  <option>Sacronia</option>
                  <option>Neon Asher</option>
                  <option>Iago Cordeiro</option>
                  <option>Patinhas &amp; Canções</option>
                  <option>Águas de Descanso</option>
                  <option>Trono da Promessa</option>
                  <option>Incorruptível</option>
                  <option>Aliens da Bíblia</option>
                  <option>Aquário dos Felinos</option>
                </select>
              </div>
            </div>
            <button type="submit" class="ivory-submit-btn">Quero Receber no WhatsApp</button>
          </form>
        </div>
      </div>
    </section>

    <!-- SESSÃO 6A (PARTE 1): PRODUÇÕES SOB ENCOMENDA (TÍTULO CURTO EM 1 LINHA + BANNER E BLOCOS EMBAIXO!) -->
    <section class="section-studio-loja" id="personalize-sua-musica">
      <div class="container-wide">
        <div class="editorial-header">
          <h2 class="editorial-giant-title">Produções Sob Encomenda</h2>
        </div>

        <div class="studio-hero-banner">
          <img class="studio-bg" src="./assets/ui/banner_estudio_vortice.jpg" alt="Vórtice Mídia — Produções Sob Encomenda" loading="lazy">
          <div class="studio-banner-mask"></div>
          <div class="studio-banner-content">
            <p class="studio-banner-desc" style="font-size:16.5px;font-weight:600;margin-bottom:18px;">
              Transformamos sua história, homenagem familiar, casamento, aniversário, campanha política ou marca empresarial em uma produção musical exclusiva de estúdio com qualidade cinematográfica.
            </p>
            <button type="button" class="emerald-action-btn" style="max-width:360px;" onclick="alert('Em breve! O atendimento para produções sob encomenda estará disponível em breve.')">
              Em Breve
            </button>
          </div>
        </div>

        <div class="studio-cards-3col">
          <!-- Música 1 -->
          <div class="gold-showcase-card">
            <div>
              <div class="gold-card-tag">HOMENAGENS &amp; FAMÍLIA</div>
              <h3 class="gold-card-title">Casamentos, Aniversários &amp; Histórias</h3>
              <p class="gold-card-text">
                Eternize a história de quem você ama com uma letra emocionante e arranjo profissional no estilo musical que sua família mais gosta.
              </p>
            </div>
            <button type="button" class="emerald-action-btn" onclick="alert('Em breve! Este serviço estará disponível em breve.')">Em Breve</button>
          </div>

          <!-- Música 2 -->
          <div class="gold-showcase-card">
            <div>
              <div class="gold-card-tag">IMPACTO &amp; MEMORIZAÇÃO</div>
              <h3 class="gold-card-title">Jingles Políticos &amp; Campanhas</h3>
              <p class="gold-card-text">
                Produção rápida e marcante de jingles de campanha, hinos de mobilização e trilhas de alto impacto para redes sociais e carros de som.
              </p>
            </div>
            <button type="button" class="emerald-action-btn" onclick="alert('Em breve! Este serviço estará disponível em breve.')">Em Breve</button>
          </div>

          <!-- Música 3 -->
          <div class="gold-showcase-card">
            <div>
              <div class="gold-card-tag">EMPRESAS &amp; MARCAS</div>
              <h3 class="gold-card-title">Comerciais 3D &amp; Jingles</h3>
              <p class="gold-card-text">
                Identidade sonora, música oficial da sua empresa e comerciais animados em 3D que destacam o seu negócio da concorrência.
              </p>
            </div>
            <button type="button" class="emerald-action-btn" onclick="alert('Em breve! Este serviço estará disponível em breve.')">Em Breve</button>
          </div>
        </div>
      </div>
    </section>

    <!-- SESSÃO 6B (PARTE 2): APLICATIVOS PARA IGREJAS (TÍTULO CURTO EM 1 LINHA + BANNER E BLOCOS EMBAIXO!) -->
    <section class="section-studio-loja" id="aplicativos-ebd-igrejas">
      <div class="container-wide">
        <div class="editorial-header">
          <h2 class="editorial-giant-title">Aplicativos para Igrejas</h2>
        </div>

        <div class="studio-hero-banner">
          <img class="studio-bg" src="./assets/ui/banner_apps_vortice.jpg" alt="Vórtice Mídia — Aplicativos para EBD e Igrejas" loading="lazy">
          <div class="studio-banner-mask"></div>
          <div class="studio-banner-content">
            <p class="studio-banner-desc" style="font-size:16.5px;font-weight:600;margin-bottom:18px;">
              Desenvolvemos aplicativos modernos para igrejas e ministérios infantis: revistinhas digitais interativas da Escola Bíblica Dominical (EBD) e plataformas completas de membros, lives e estudos bíblicos.
            </p>
            <button type="button" class="emerald-action-btn" style="max-width:360px;" onclick="alert('Em breve! Os aplicativos interativos estarão disponíveis em breve.')">
              Em Breve
            </button>
          </div>
        </div>

        <div class="studio-cards-3col">
          <!-- App 1 -->
          <div class="gold-showcase-card">
            <div>
              <div class="gold-card-tag">MINISTÉRIO INFANTIL &amp; EBD</div>
              <h3 class="gold-card-title">Aplicativo de EBD &amp; Revistinha Digital</h3>
              <p class="gold-card-text">
                Criamos a revistinha digital interativa da Escola Bíblica Dominical da sua igreja, com lições bíblicas, quiz, oficina de pintura e jogos educativos sem anúncios.
              </p>
            </div>
            <button type="button" class="emerald-action-btn" onclick="alert('Em breve! Este aplicativo estará disponível em breve.')">Em Breve</button>
          </div>

          <!-- App 2 -->
          <div class="gold-showcase-card">
            <div>
              <div class="gold-card-tag">COMUNIDADE &amp; GESTÃO</div>
              <h3 class="gold-card-title">Aplicativo da Igreja &amp; Rol de Membros</h3>
              <p class="gold-card-text">
                Aplicativo próprio da igreja no celular dos membros: cadastro e rol de membros, transmissão ao vivo dos cultos, estudos bíblicos, devocionais e pedidos de oração.
              </p>
            </div>
            <button type="button" class="emerald-action-btn" onclick="alert('Em breve! Este aplicativo estará disponível em breve.')">Em Breve</button>
          </div>

          <!-- App 3 -->
          <div class="gold-showcase-card">
            <div>
              <div class="gold-card-tag">PROJETO MODELO NO AR</div>
              <h3 class="gold-card-title">App Trono da Promessa Kids</h3>
              <p class="gold-card-text">
                Plataforma infantil interativa com episódios em 3D, Quebra-Cabeça Bíblico, Pintura Mágica, Quiz do Vovô Nésio, Álbum da Fé e Cantinho de Dormir.
              </p>
            </div>
            <button type="button" class="emerald-action-btn" onclick="alert('Em breve! O aplicativo Trono da Promessa Kids estará disponível em breve.')">Em Breve</button>
          </div>
        </div>
      </div>
    </section>

    <!-- SESSÃO 7: A FORÇA CRIATIVA DA VÓRTICE MÍDIA (TÍTULO FORA EM CIMA + BLOCO E 3 CARDS EMBAIXO COM MESMA TRANSPARÊNCIA!) -->
    <section class="section-story-editorial" id="missao-visao-valores">
      <div class="container-wide">
        <div class="editorial-header">
          <h2 class="editorial-giant-title">A Força Criativa da Vórtice Mídia</h2>
        </div>

        <div class="story-chapter-box">
          <p class="story-chapter-p">
            A Vórtice Mídia nasceu da convicção de que a arte digital, a música e o audiovisual não existem apenas para preencher o tempo, mas para despertar consciências, consolar corações e reunir gerações em torno daquilo que realmente importa. Em um cenário digital cada vez mais descartável e ruidoso, escolhemos o caminho do trabalho autoral cuidadoso: construir dez universos temáticos independentes que dialogam com os diferentes momentos da vida — da reflexão cidadã ao louvor congregacional, da emoção de quem ama os animais ao ensino bíblico para as crianças e ao descanso profundo no fim do dia.
          </p>
        </div>

        <div class="mvv-corporate-grid">
          <div class="mvv-card-3d">
            <span class="mvv-tag">01 &bull; ESSÊNCIA CRIATIVA</span>
            <h3 class="mvv-title">Arte Com Propósito</h3>
            <p class="mvv-text">
              Cada canal da Vórtice Mídia possui identidade visual, direção musical e linha editorial próprias. Não produzimos conteúdo em série sem alma: cada letra é escrita para contar uma história verdadeira, cada arranjo sonoro é desenhado para transmitir emoção real e cada cenário visual é lapidado com estética cinematográfica.<br><br>
              Do peso das guitarras de protesto no <strong>Rock Incorruptível</strong> e da solenidade épica do <strong>Sacronia</strong> à doçura acústica de <strong>Iago Cordeiro</strong>, da melancolia noturna de <strong>Neon Asher</strong> à ternura em 3D de <strong>Patinhas &amp; Canções</strong>, unimos tecnologia de ponta e sensibilidade humana para entregar obras que permanecem na memória.
            </p>
          </div>
          <div class="mvv-card-3d">
            <span class="mvv-tag">02 &bull; PRINCÍPIOS &amp; VALORES</span>
            <h3 class="mvv-title">Verdade, Fé &amp; Família</h3>
            <p class="mvv-text">
              Nossa fundação repousa sobre pilares inegociáveis: a fé cristã reverente às Escrituras, a defesa da família como porto seguro, a proteção da infância contra conteúdos vazios, o amor e a compaixão pelos animais e a coragem cidadã diante dos fatos.<br><br>
              Nos canais infantis <strong>Trono da Promessa</strong> e <strong>Aquário dos Felinos</strong>, os pais encontram um ambiente 100% confiável, educativo e acolhedor para seus filhos. Na crônica analítica do <strong>Incorruptível</strong>, nos documentários de <strong>Aliens da Bíblia</strong> e na leitura bíblica serena de <strong>Águas de Descanso</strong>, honramos a inteligência, a fé e a paz de quem nos acompanha.
            </p>
          </div>
          <div class="mvv-card-3d">
            <span class="mvv-tag">03 &bull; CAMINHO &amp; FUTURO</span>
            <h3 class="mvv-title">Evolução Constante</h3>
            <p class="mvv-text">
              A Vórtice Mídia é um ecossistema vivo em expansão contínua. Além da presença diária no YouTube e nas principais plataformas globais de streaming musical — Spotify, Deezer, Apple Music, Amazon Music e YouTube Music —, caminhamos para integrar música sob encomenda, séries animadas e aplicativos interativos para igrejas e famílias.<br><br>
              Nosso compromisso com o futuro é claro: continuar inovando na linguagem visual e sonora sem jamais abrir mão da autenticidade, levando mensagens de coragem, esperança, beleza e fé para lares em todo o Brasil e no mundo.
            </p>
          </div>
        </div>
      </div>

      <footer class="vortice-clean-footer">
        <div>&copy; 2026 Vórtice Mídia Produções e Tecnologia Digital &bull; Todos os direitos reservados.</div>
        <div class="footer-links-inline">
          <a href="#hero-stage">Voltar ao Topo</a>
          <a href="./politica_privacidade.html">Propriedade Intelectual</a>
          <a href="./politica_privacidade.html" target="_blank">Política de Privacidade (LGPD)</a>
        </div>
      </footer>
    </section>

  </div>

  <!-- =========================================================================
       PÁGINA EXCLUSIVA DE CADA CANAL (#channel-portal-overlay)
       - Padronizada em todas as 10 páginas com o contraste Noir-Neon (Preto + Ciano + Roxo/Magenta)!
       - Sem botões de navegação de seção no topo, sem bordas amarelas e sem caixas fechando seções!
       - 7 Seções Completas com Imagens Cruas nos cards e Botões Grandes das Plataformas!
       ========================================================================= -->
  <div class="channel-dedicated-page" id="channel-portal-overlay">
    <!-- PLACA AMARELA NO CANTO SUPERIOR ESQUERDO
         Contém APENAS a Logo Oficial Vórtice Mídia (do print) direto no fundo amarelo
         + a informação "← VOLTAR AO PORTAL" (sem texto de cuidado/radiação, sem símbolo de perigo e sem bolinha preta!) -->
    <div class="ch-sticky-navbar">
      <div class="ch-page-topbar">
        <button type="button" class="ch-vortice-logo-return" onclick="closeChannelPortal()" title="Clique na Placa para Voltar ao Portal Vórtice Mídia">
          <span class="hazard-zebra-bar top" aria-hidden="true"></span>
          <span class="hazard-plate-middle">
            <img class="ch-yellow-plate-official-logo" src="./assets/ui/vortice_midia_official_logo.png" alt="Vórtice Mídia">
            <span class="hazard-col-divider" aria-hidden="true"></span>
            <span class="hazard-return-col">
              <span class="hazard-return-line1">&larr; VOLTAR</span>
              <span class="hazard-return-line2">AO PORTAL</span>
            </span>
          </span>
          <span class="hazard-zebra-bar bottom" aria-hidden="true"></span>
        </button>
      </div>
    </div>

    <!-- SEÇÃO 1: BANNER OFICIAL FULL-BLEED EM 1 ÚNICA ROLAGEM (100VH EXATO) -->
    <div class="ch-page-hero" id="ch-sec-identidade">
      <div class="ch-hero-fullbleed-art">
        <img id="ch-page-bg" src="" alt="Banner Oficial do Canal">
      </div>

      <div class="ch-page-hero-content">
        <img class="ch-page-logo" id="ch-page-logo" src="" alt="Logo Oficial do Canal">
        <div class="ch-page-title-block">
          <h1 id="portal-title-text">Canal</h1>
          <div class="ch-slogan-line" id="portal-slogan-text"></div>
          <p id="portal-desc-text" style="max-width:780px;font-size:15.5px;line-height:1.64;color:rgba(241,245,249,0.94);margin:0;text-shadow:0 4px 16px rgba(0,0,0,0.95);"></p>
        </div>
        <div class="ch-hero-cta-col" id="portal-hero-ctas"></div>
      </div>
    </div>

    <!-- CORPO COM AS SEÇÕES 2 A 7 (CADA SEÇÃO COM AMPLO RESPIRO E IDENTIDADE DE COR PRÓPRIA!) -->
    <div class="ch-page-body">

      <!-- SEÇÃO 2: SOBRE O CANAL, PROPÓSITO & HISTÓRIA -->
      <section class="ch-section-block" id="ch-sec-historia">
        <div class="ch-sec-inner">
          <div class="ch-sec-header">
            <div>
              <h2 class="ch-sec-title" id="portal-story-heading">Sobre o Canal &amp; Sua Essência</h2>
            </div>
          </div>
          <div class="ch-story-editorial-grid">
            <div id="portal-story-left"></div>
            <div class="ch-persona-dossier-box" id="portal-story-right"></div>
          </div>
        </div>
      </section>

      <!-- SEÇÃO 3: CATÁLOGO DE MÚSICAS / EPISÓDIOS COM IMAGEM CRUA E ÍCONES 3D PUROS DAS PLATAFORMAS -->
      <section class="ch-section-block" id="ch-sec-repertorio">
        <div class="ch-sec-inner">
          <div class="ch-sec-header">
            <div>
              <h2 class="ch-sec-title" id="portal-rep-title">Músicas &amp; Clipes Oficiais</h2>
            </div>
            <div id="portal-rep-right-action"></div>
          </div>
          <div class="ch-tracks-grid" id="portal-tracks-container"></div>
        </div>
      </section>

      <!-- SEÇÃO 3B: LOJA OFICIAL EXCLUSIVA DESTE CANAL (#ch-sec-loja) -->
      <section class="ch-section-block" id="ch-sec-loja">
        <div class="ch-sec-inner">
          <div class="ch-sec-header">
            <div>
              <h2 class="ch-sec-title" id="portal-store-title">Loja Oficial do Canal</h2>
            </div>
          </div>
          <div class="vortice-store-grid" id="portal-store-container"></div>
        </div>
      </section>

      <!-- SEÇÃO 4: O QUE MOVIMENTA ESTE UNIVERSO -->
      <section class="ch-section-block" id="ch-sec-cronicas">
        <div class="ch-sec-inner">
          <div class="ch-sec-header">
            <div>
              <h2 class="ch-sec-title">O Que Movimenta Este Universo</h2>
            </div>
          </div>
          <div class="ch-chronicles-grid" id="portal-lore-container"></div>
        </div>
      </section>

      <!-- SEÇÃO 5: BASTIDORES DE PRODUÇÃO, DIREÇÃO MUSICAL & EXPERIÊNCIA VISUAL -->
      <section class="ch-section-block" id="ch-sec-bastidores">
        <div class="ch-sec-inner">
          <div class="ch-sec-header">
            <div>
              <h2 class="ch-sec-title">Produção de Estúdio, Estética Visual &amp; Experiência</h2>
            </div>
          </div>
          <div class="ch-chronicles-grid" id="portal-production-container"></div>
        </div>
      </section>

      <!-- SEÇÃO 6: GUIA DO PÚBLICO & PERGUNTAS FREQUENTES -->
      <section class="ch-section-block" id="ch-sec-guia">
        <div class="ch-sec-inner">
          <div class="ch-sec-header">
            <div>
              <h2 class="ch-sec-title">Guia do Público &amp; Perguntas Frequentes</h2>
            </div>
          </div>
          <div class="ch-faq-grid-2col" id="portal-faq-container"></div>
        </div>
      </section>

      <!-- SEÇÃO 7: ACESSE O CANAL NAS PLATAFORMAS OFICIAIS (PLACAS 3D EM MOVIMENTO) -->
      <section class="ch-section-block" id="ch-sec-plataformas">
        <div class="ch-sec-inner">
          <div class="ch-sec-header">
            <div>
              <h2 class="ch-sec-title">Acesse o Canal nas Plataformas Oficiais</h2>
            </div>
          </div>
          <div class="flying-signs-platforms-grid" id="portal-actions-container" style="margin-top:8px;"></div>
        </div>
      </section>

    </div>
  </div>

  <!-- =========================================================================
       PÁGINA INSTITUCIONAL INTERNA: PERFIL OFICIAL EM REIVINDICAÇÃO & HOMOLOGAÇÃO
       (#platform-claim-overlay)
       - Abre sempre que o visitante clica em uma plataforma que ainda está em
         processo oficial de reivindicação de conta de artista (evitando links genéricos).
       ========================================================================= -->
  <div class="platform-claim-overlay" id="platform-claim-overlay">
    <div class="ch-sticky-navbar" style="z-index:440;">
      <div class="ch-page-topbar">
        <button type="button" class="ch-vortice-logo-return" onclick="closePlatformClaimPage()" title="Clique na Placa para Voltar">
          <span class="hazard-zebra-bar top" aria-hidden="true"></span>
          <span class="hazard-plate-middle">
            <img class="ch-yellow-plate-official-logo" src="./assets/ui/vortice_midia_official_logo.png" alt="Vórtice Mídia">
            <span class="hazard-col-divider" aria-hidden="true"></span>
            <span class="hazard-return-col">
              <span class="hazard-return-line1">&larr; VOLTAR</span>
              <span class="hazard-return-line2">AGORA</span>
            </span>
          </span>
          <span class="hazard-zebra-bar bottom" aria-hidden="true"></span>
        </button>
      </div>
    </div>

    <div class="claim-dossier-card">
      <div class="claim-status-pill">
        <span class="claim-status-dot"></span>
        <span id="claim-pill-text">CONTA OFICIAL EM PROCESSO DE REIVINDICAÇÃO</span>
      </div>

      <div class="claim-bridge-row">
        <img class="claim-ch-avatar" id="claim-channel-logo" src="./assets/logos_color/rock_color.jpg" alt="Logo do Canal">
        <div class="claim-bridge-connector">&bull; &bull; &bull; &#10142; &bull; &bull; &bull;</div>
        <div class="claim-plat-badge-big ch-plat-icon-3d spotify" id="claim-platform-badge"></div>
      </div>

      <h2 class="claim-main-title" id="claim-title-heading">Canal Oficial em Homologação</h2>
      <div class="claim-sub-headline" id="claim-sub-heading">
        Perfil Oficial de Artista em Fase Final de Reivindicação e Verificação
      </div>

      <div class="claim-desc-box" id="claim-desc-text"></div>

      <div class="claim-steps-grid">
        <div class="claim-step-item">
          <span class="claim-step-tag">&#10004; ETAPA 01 &bull; CONCLUÍDA</span>
          <div class="claim-step-title">Produção &amp; Distribuição Oficial Vórtice Mídia</div>
        </div>
        <div class="claim-step-item active-step">
          <span class="claim-step-tag">&#9203; ETAPA 02 &bull; EM ANDAMENTO</span>
          <div class="claim-step-title" id="claim-step2-text">Reivindicação e Verificação da Conta de Artista</div>
        </div>
        <div class="claim-step-item">
          <span class="claim-step-tag">&#128274; ETAPA 03 &bull; EM BREVE</span>
          <div class="claim-step-title">Liberação do Acesso Direto Verificado no Portal</div>
        </div>
      </div>

      <div class="claim-actions-row" id="claim-actions-container"></div>
    </div>
  </div>

  <script>
    const SVG_ICONS = {
      spotify: `<svg viewBox="0 0 24 24"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/></svg>`,
      deezer: `<svg viewBox="0 0 24 24"><path d="M18.81 4.16v3.03H24V4.16h-5.19zM6.27 8.38v3.027h5.189V8.38h-5.19zm12.54 0v3.027H24V8.38h-5.19zM6.27 12.594v3.027h5.189v-3.027h-5.19zm6.271 0v3.027h5.19v-3.027h-5.19zm6.269 0v3.027H24v-3.027h-5.19zM0 16.81v3.029h5.19v-3.03H0zm6.27 0v3.029h5.189v-3.03h-5.19zm6.271 0v3.029h5.19v-3.03h-5.19zm6.269 0v3.029H24v-3.03h-5.19z"/></svg>`,
      apple: `<svg viewBox="0 0 24 24"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.96 6.33c.67-.81 1.12-1.94 1-3.08-.96.04-2.13.64-2.82 1.45-.61.7-.15 1.85-1.01 2.97 1.08.08 2.16-.53 2.83-1.34z"/></svg>`,
      amazon: `<svg viewBox="0 0 24 24"><path d="M13.958 9.09c0 1.132.029 2.056-.591 3.051-.502.791-1.301 1.238-2.186 1.238-1.214 0-1.922-.824-1.922-2.092 0-2.492 2.415-2.882 4.7-2.882v.685zm3.186 6.705c-.209.189-.512.201-.745.074-1.052-.872-1.238-1.276-1.819-2.106-1.734 1.767-2.962 2.297-5.209 2.297-2.66 0-4.731-1.641-4.731-4.625 0-2.365 1.391-4.009 3.37-4.764 1.715-.654 4.11-.791 5.942-.995v-.41c0-.753.06-1.542-.383-2.094-.385-.479-1.124-.72-1.775-.72-1.205 0-2.277.618-2.54 1.797-.054.285-.261.567-.549.582l-3.061-.333c-.259-.056-.548-.266-.472-.66C5.9 1.362 9.077.3 12.153.3c1.992 0 4.596.53 6.165 1.841 1.992 1.667 1.804 3.954 1.804 6.463v5.805c0 1.726.8 2.471 1.554 3.412.263.367.321.805-.013 1.077-.838.699-2.327 1.802-3.149 2.43l-1.37-5.533zM2.2 19.2c4.4 3.1 10.6 3.8 16.5 1.2.4-.2.8.2.5.6-2.9 3.1-9.9 3.8-17.3-.9-.4-.3-.1-.9.3-.9zm18.4 1.8c-.4-.5-2.5-.3-3.5-.1-.3.1-.4-.2-.1-.4 1.7-1.2 4.5-.9 4.8-.5.3.4-.1 3.3-1.7 4.7-.2.2-.5.1-.4-.2.4-.9 1.3-3 .9-3.5z"/></svg>`,
      youtube: `<svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>`,
      ytmusic: `<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 14.5c-2.49 0-4.5-2.01-4.5-4.5S9.51 7.5 12 7.5s4.5 2.01 4.5 4.5-2.01 4.5-4.5 4.5zm-1.5-6.75v4.5l4-2.25-4-2.25z"/></svg>`,
      vorticeFunnel: `<svg viewBox="0 0 24 24"><path d="M2 4.5C2 3.12 6.48 2 12 2s10 1.12 10 2.5S17.52 7 12 7 2 5.88 2 4.5zm2.5 5.2c0-1.05 3.36-1.9 7.5-1.9s7.5.85 7.5 1.9-3.36 1.9-7.5 1.9-7.5-.85-7.5-1.9zm3.2 4.8c0-.88 2.15-1.6 4.8-1.6s4.8.72 4.8 1.6-2.15 1.6-4.8 1.6-4.8-.72-4.8-1.6zm2.6 4.3c0-.66 1.25-1.2 2.8-1.2s2.8.54 2.8 1.2-1.25 1.2-2.8 1.2-2.8-.54-2.8-1.2zm1.4 3.2a1.3 1.3 0 1 1 2.6 0 1.3 1.3 0 0 1-2.6 0z"/></svg>`,
      instagram: `<svg viewBox="0 0 24 24"><path d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2zm-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4H7.6zm9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8 1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25zM12 7a5 5 0 0 1 5 5 5 5 0 0 1-5 5 5 5 0 0 1-5-5 5 5 0 0 1 5-5z"/></svg>`,
      tiktok: `<svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"/></svg>`,
      facebook: `<svg viewBox="0 0 24 24"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.326-.043-1.557-.14-2.857-.14C11.928 2 10 3.657 10 6.7v2.8H7v4h3V22h4v-8.5z"/></svg>`
    };

    /* =========================================================================
       OS 10 CANAIS COM BANNERS OFICIAIS FULL-BLEED (100% SEM LOGO/TEXTO),
       LOGOS DE PERFIL 1:1 EM FUNDO PRETO, 6 MÚSICAS/EPISÓDIOS COM IMAGENS CRUAS
       E BÍBLIA EDITORIAL COMPLETA!
       ========================================================================= */
    const VORTICE_CHANNELS = [
      {
        id: 'rock-incorruptivel',
        slug: 'vortice.media/rock-incorruptivel',
        name: 'ROCK INCORRUPTÍVEL',
        bandFrontName: 'Rock Incorruptível',
        hasMusic: true,
        hasApp: false,
        sampleSongTitle: 'O Barulho Vai Começar',
        sampleAudioUrl: './assets/audio/rock_incorruptivel_barulho.mp3',
        bannerImg: './assets/banners/rock_youtube_banner.jpg',
        coverImg: './assets/banners/rock_youtube_banner.jpg',
        logoImg: './assets/logos_color/rock_color.jpg',
        badgeText: 'Crítica Política',
        slogan: '"Quando a verdade é silenciada nos palácios, ela grita nos amplificadores."',
        description: 'Crítica política e indignação cidadã transformadas em hinos explosivos de guitarra, bateria pesada e animações 3D viscerais no coração de Brasília.',
        playlist: [
          {
            title: 'O Barulho Vai Começar — "Acabou o Silêncio dos Corruptos!"',
            style: 'MÚSICA & CLIPE NO AR • EPISÓDIO 01',
            rawImg: './assets/episodes/rock_real_ep01.jpg',
            audioUrl: './assets/audio/rock_incorruptivel_barulho.mp3',
            youtubeUrl: 'https://www.youtube.com/watch?v=bbGKuAcQ-aw',
            story: 'O hino de abertura do canal: guitarras rasgadas diante do Congresso anunciando que o cidadão comum acordou e não aceita mais discursos vazios.'
          },
          {
            title: 'A Fábrica de Promessas — "As Mesmas Promessas de 4 em 4 Anos"',
            style: 'MÚSICA & CLIPE NO AR • EPISÓDIO 02',
            rawImg: './assets/episodes/rock_real_ep02.jpg',
            audioUrl: './assets/audio/rock_fabrica_de_promessas.mp3',
            youtubeUrl: 'https://www.youtube.com/watch?v=4bPfRBxFmZE',
            story: 'Retrata os bastidores eleitorais onde promessas milagrosas são produzidas em série a cada quatro anos e esquecidas no dia seguinte.'
          },
          {
            title: 'Próximos Hinos em Processo de Validação & Reivindicação',
            style: 'EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/banners/rock_youtube_banner.jpg',
            audioUrl: './assets/audio/rock_vai_incomodar.mp3',
            isValidationCard: true,
            story: 'Novas músicas e videoclipes oficiais de Rock Incorruptível já estão em processo de validação e distribuição nas plataformas. Aguarde mais músicas dentro desta seção!'
          }
        ],
        storyHeading: 'O Palco da Indignação: Quando o Rock Encontra a Crônica Política',
        storyLead: 'Nascido da urgência de transformar a revolta silenciosa do trabalhador brasileiro em arte visceral, o Rock Incorruptível une o peso do Hard Rock de arena à sátira afiada sobre os bastidores do poder.',
        storyParagraphs: [
          'Em cada clipe e composição, a Esplanada dos Ministérios e os salões atapetados deixam de ser cenários distantes e passam a ser palco de um julgamento musical. Aqui não há espaço para meias-palavras: os riffs de guitarra traduzem o cansaço de quem paga impostos e exige respeito.',
          'Mais do que entretenimento, cada faixa é construída como uma crônica histórica cantada — unindo vocais rasgados, bateria pulsante e direção de arte cinematográfica em 3D.'
        ],
        personaTitle: 'A VOZ DA ARENA • O VOCALISTA DA VERDADE',
        personaQuote: 'Eles acharam que o povo ia se acostumar com o teatro. Mas esqueceram que uma verdade cantada no último volume atravessa qualquer parede blindada.',
        personaDetails: 'Direção Sonora & Visual: Hard Rock de Arena, Sátira Política em 3D e Crônica Cidadã.',
        loreBoxes: [
          { tag: 'CRÔNICA 01 • O TEATRO DO PODER', title: 'Bastidores sob Holofotes', text: 'Desmascarando a distância entre os discursos oficiais e a vida real nas ruas do país.' },
          { tag: 'CRÔNICA 02 • IMPOSTOS & SUOR', title: 'A Conta Sempre Chega', text: 'Músicas que dão voz a quem trabalha de sol a sol para sustentar a máquina pública.' },
          { tag: 'CRÔNICA 03 • MEMÓRIA NACIONAL', title: 'O Que Não Pode Ser Esquecido', text: 'O rock como registro histórico para que o país não repita os mesmos erros.' },
          { tag: 'CRÔNICA 04 • SÁTIRA AFILADA', title: 'Ironia em Alta Voltagem', text: 'Metáforas visuais em 3D que expõem o absurdo com inteligência e impacto.' },
          { tag: 'CRÔNICA 05 • SOM DE ESTRADA', title: 'Feito Para Tocar Alto', text: 'Produção masterizada com graves pesados para ouvir no carro, na estrada ou no treino.' },
          { tag: 'IDENTIDADE VISUAL', title: 'Palco na Praça dos Três Poderes', text: 'A imagem icônica da banda tocando ao vivo diante da arquitetura monumental de Brasília.' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@RockIncorruptivel',
          spotify: 'https://open.spotify.com',
          deezer: 'https://www.deezer.com',
          apple: 'https://music.apple.com',
          amazon: 'https://music.amazon.com.br',
          ytmusic: 'https://music.youtube.com'
        }
      },
      {
        id: 'sacronia',
        slug: 'vortice.media/sacronia',
        name: 'SACRONIA',
        bandFrontName: 'Sacronia',
        hasMusic: true,
        hasApp: false,
        sampleSongTitle: 'A Voz Sobre as Águas',
        sampleAudioUrl: './assets/audio/sacronia_voz_sobre_as_aguas.mp3',
        bannerImg: './assets/banners/sacronia_youtube_banner.jpg',
        coverImg: './assets/banners/sacronia_youtube_banner.jpg',
        logoImg: './assets/logos_color/sacronia_color.png',
        badgeText: 'Gospel Sacro Contemporâneo',
        slogan: '"Onde a solenidade eterna das Escrituras encontra a força sísmica do Rock Sinfônico."',
        description: 'As grandes batalhas espirituais, profecias e passagens épicas da Bíblia transformadas em Gospel Sacro Contemporâneo com orquestração grandiosa.',
        playlist: [
          {
            title: 'A Voz Sobre as Águas — Hino em Processo de Reivindicação & Validação',
            style: '1º LANÇAMENTO • EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/banners/sacronia_youtube_banner.jpg',
            audioUrl: './assets/audio/sacronia_voz_sobre_as_aguas.mp3',
            isValidationCard: true,
            story: 'A primeira música oficial desta nova fase do canal Sacronia já está em processo de validação e reivindicação nas plataformas digitais. Aguarde mais músicas e informações dentro desta seção!'
          }
        ],
        storyHeading: 'A Catedral de Pedra e Fogo: A Essência da Bíblia do Sacronia',
        storyLead: 'A Bíblia não é um livro de histórias suaves — é um épico de mares que se abrem, muralhas que caem, profetas que enfrentam reis e uma Cruz que vence a morte. O Sacronia nasceu para dar a essas passagens a dimensão sonora que elas pedem.',
        storyParagraphs: [
          'Com sua insígnia esculpida em pedra vulcânica, o Sacronia une o peso do Rock Sinfônico à reverência da teologia bíblica. Cada faixa é escrita como um filme sonoro: você sente a poeira do deserto, o trovão no Sinai e o consolo da graça.',
          'É o canal feito para quem busca profundidade bíblica sem clichês — uma trilha sonora de fé inabalável para vencer as batalhas do dia a dia.'
        ],
        personaTitle: 'OS GUARDIÕES DA ROCHA • GOSPEL SACRO CONTEMPORÂNEO',
        personaQuote: 'Não cantamos para entreter o templo; cantamos para lembrar à alma que o Deus que abriu o mar continua governando a tempestade.',
        personaDetails: 'Direção Sonora & Visual: Orquestração Sinfônica, Coros Sacros, Guitarras Pesadas e Narrativa Bíblica 8K.',
        loreBoxes: [
          { tag: 'PILAR 01 • TEOLOGIA ÉPICA', title: 'Fidelidade às Escrituras', text: 'Letras enraizadas nos Salmos, nos Profetas, no Êxodo e no Apocalipse com densidade poética.' },
          { tag: 'PILAR 02 • PESO & ORQUESTRA', title: 'Sinfonia e Distorção', text: 'Violoncelos, coros épicos e guitarras pesadas caminhando juntos em cada arranjo.' },
          { tag: 'PILAR 03 • HERÓIS DA FÉ', title: 'Coragem no Deserto', text: 'Canções sobre Moisés, Elias, Davi e Paulo enfrentando o impossível.' },
          { tag: 'PILAR 04 • BATALHA INTERIOR', title: 'A Guerra Invisível', text: 'Música que fortalece o espírito em dias de dúvida, cansaço e provação.' },
          { tag: 'PILAR 05 • ARTE MONUMENTAL', title: 'Estética de Cinema 8K', text: 'Cenários bíblicos grandiosos iluminados por fogo, tempestade e glória.' },
          { tag: 'IDENTIDADE VISUAL', title: 'O Monólito Sacronia', text: 'Tipografia cravada na rocha que simboliza a Palavra eterna que jamais passa.' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@SacroniaMusic',
          spotify: 'https://open.spotify.com',
          deezer: 'https://www.deezer.com',
          apple: 'https://music.apple.com',
          amazon: 'https://music.amazon.com.br',
          ytmusic: 'https://music.youtube.com/channel/UCbpf2WHDz57FW3QCcftc_2A'
        }
      },
      {
        id: 'neon-asher',
        slug: 'vortice.media/neon-asher',
        name: 'NEON ASHER',
        bandFrontName: 'Neon Asher',
        hasMusic: true,
        hasApp: false,
        sampleSongTitle: 'Neon Asher',
        sampleAudioUrl: './assets/audio/neon_asher_theme.mp3',
        bannerImg: './assets/banners/neon_youtube_banner.jpg',
        coverImg: './assets/banners/neon_youtube_banner.jpg',
        logoImg: './assets/logos_color/neon_color.jpg',
        badgeText: 'Rock Gótico',
        slogan: '"Às duas da manhã, no silêncio da noite, toda cicatriz vira melodia."',
        description: 'Rock gótico melódico, violinos dramáticos e arranjos noturnos que contam histórias de amor partido, a dor da separação, despedidas, estradas solitárias e superação.',
        playlist: [
          {
            title: 'What Remains When The Lights Go Out — Neon Asher',
            style: 'MÚSICA & CLIPE NO AR • EPISÓDIO 01',
            rawImg: './assets/episodes/neon_real_ep01.jpg',
            audioUrl: './assets/audio/neon_asher_theme.mp3',
            youtubeUrl: 'https://www.youtube.com/watch?v=GtTA4sO7X-g',
            story: 'A faixa-assinatura de Neon Asher: guitarras intensas e violinos marcantes cortando a madrugada quando as luzes da cidade se apagam.'
          },
          {
            title: 'The Last Time I Saw You — Em Processo de Validação & Reivindicação',
            style: 'EM PROCESSO DE VALIDAÇÃO • EPISÓDIO 02',
            rawImg: './assets/episodes/neon_real_ep02.jpg',
            audioUrl: './assets/audio/neon_last_time_i_saw_you.mp3',
            isValidationCard: true,
            story: 'O último olhar na despedida antes que dois destinos tomassem estradas opostas — próximo lançamento oficial em validação nas plataformas. Aguarde mais músicas dentro desta seção!'
          }
        ],
        storyHeading: 'Crônicas da Madrugada: A Dor da Separação, Violinos e Superação',
        storyLead: 'Quem nunca atravessou a madrugada em silêncio tentando entender o fim de uma história? Neon Asher é o refúgio sonoro para as horas em que a cidade dorme e a memória acorda.',
        storyParagraphs: [
          'O universo de Neon Asher une a força dramática dos violinos ao peso do Rock Gótico Melódico. Suas músicas falam sem filtros sobre a dor da separação, amor partido, promessas quebradas, despedidas e a reconstrução da própria força.',
          'Combinando violinos intensos, pianos noturnos e guitarras marcantes, cada faixa funciona tanto para momentos de reflexão profunda quanto para estradas noturnas, foco e superação.'
        ],
        personaTitle: 'NEON ASHER • ROCK GÓTICO MELÓDICO',
        personaQuote: 'O tempo não apaga o que aconteceu, mas transforma cada cicatriz na força que te leva adiante pela estrada.',
        personaDetails: 'Direção Sonora & Visual: Rock Gótico Melódico, Violinos Dramáticos e Estética Noturna.',
        loreBoxes: [
          { tag: 'CAPÍTULO 01 • A DESPEDIDA', title: 'A Dor da Separação', text: 'Canções intensas e honestas sobre o instante em que dois caminhos se dividem.' },
          { tag: 'CAPÍTULO 02 • VIOLINOS & GUITARRAS', title: 'Melancolia Cinematográfica', text: 'O encontro entre o violino clássico emocionante e o peso do rock gótico melódico.' },
          { tag: 'CAPÍTULO 03 • ESTRADA & FOCO', title: 'Estradas Solitárias', text: 'A trilha sonora ideal para dirigir à noite, focar nos projetos, estudar ou treinar.' },
          { tag: 'CAPÍTULO 04 • AMOR PARTIDO', title: 'Cicatrizes que Viram Força', text: 'Transformando a decepção afetiva e as despedidas em coragem para recomeçar.' },
          { tag: 'CAPÍTULO 05 • ESTÉTICA NOTURNA', title: 'Contraste & Profundidade', text: 'Identidade visual marcante inspirada no cinema noturno e na arquitetura clássica.' },
          { tag: 'REPERTÓRIO GLOBAL', title: 'Vozes & Cordas Emotivas', text: 'Vozes profundas e arranjos de violino que conectam ouvintes no mundo inteiro.' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@NeonAsherDarkRock',
          spotify: 'https://open.spotify.com',
          deezer: 'https://www.deezer.com',
          apple: 'https://music.apple.com/br/artist/neon-asher/6819336396',
          amazon: 'https://music.amazon.com.br',
          ytmusic: 'https://music.youtube.com/channel/UCiVaYR4-N9BBmS9ORhDP4qg'
        }
      },
      {
        id: 'iago-cordeiro',
        slug: 'vortice.media/iago-cordeiro',
        name: 'IAGO CORDEIRO',
        bandFrontName: 'Iago Cordeiro',
        hasMusic: true,
        hasApp: false,
        sampleSongTitle: 'Cordeiro de Deus',
        sampleAudioUrl: './assets/audio/iago_cordeiro_de_deus.mp3',
        bannerImg: './assets/banners/iago_youtube_banner.jpg',
        coverImg: './assets/banners/iago_youtube_banner.jpg',
        logoImg: './assets/logos_color/iago_color.png',
        badgeText: 'Louvor Congregacional',
        slogan: '"Onde o rugido do Leão de Judá se encontra com a mansidão do Cordeiro no simples dedilhar de um violão."',
        description: 'Canções cristãs de louvor congregacional e voz e violão nascidas na oração, trazendo paz espiritual, consolo nas lutas e comunhão verdadeira com Deus.',
        playlist: [
          {
            title: '1º Louvor Oficial — Em Processo de Validação & Reivindicação',
            style: '1º LANÇAMENTO • EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/episodes/iago_real_ep01.jpg',
            audioUrl: './assets/audio/iago_cordeiro_de_deus.mp3',
            isValidationCard: true,
            story: 'A primeira música oficial de Iago Cordeiro já está em processo final de validação e reivindicação e subirá em breve nas plataformas digitais. Aguarde mais informações dentro desta seção!'
          }
        ],
        storyHeading: 'O Quarto Secreto e o Violão: A Essência de Iago Cordeiro',
        storyLead: 'Longe dos grandes espetáculos vazios, a fé mais profunda nasce na sinceridade da oração — com uma Bíblia aberta, um violão acústico e um coração rendido a Deus.',
        storyParagraphs: [
          'A identidade de Iago Cordeiro reflete a sobriedade da adoração sincera: tipografia limpa em branco puro sobre fundo negro e a atmosfera acolhedora da capela de pedra e madeira, onde o piano de cauda, o violão acústico e a Bíblia aberta conduzem cada canção.',
          'Cada letra é escrita como um devocional cantado sobre a graça, o perdão, a família e a esperança cristã, criando um ambiente de paz para o culto doméstico, para a igreja e para suas manhãs de oração.'
        ],
        personaTitle: 'IAGO CORDEIRO • LOUVOR CONGREGACIONAL & DEVOCIONAL',
        personaQuote: 'Deus não procura perfeição de palco; Ele procura um coração sincero que não tem medo de se derramar diante da Cruz.',
        personaDetails: 'Direção Sonora & Visual: Louvor Congregacional, Piano, Violão Acústico e Adoração Cristocêntrica.',
        loreBoxes: [
          { tag: 'ESSÊNCIA 01 • CRISTOCENTRISMO', title: 'A Cruz no Centro', text: 'Letras bíblicas focadas na pessoa de Jesus, na graça redentora e no consolo do Espírito Santo.' },
          { tag: 'ESSÊNCIA 02 • VERDADE ACÚSTICA', title: 'Piano, Violão & Alma', text: 'Arranjos orgânicos onde cada acorde e cada palavra da letra são ouvidos com clareza.' },
          { tag: 'ESSÊNCIA 03 • DEVOCIONAL DIÁRIO', title: 'Para Começar o Dia em Paz', text: 'Repertório pensado para acompanhar sua leitura bíblica matinal e o café em família.' },
          { tag: 'ESSÊNCIA 04 • CURA INTERIOR', title: 'Canções para Dias Difíceis', text: 'Louvores que falam sobre vencer a ansiedade, o medo e o deserto espiritual.' },
          { tag: 'ESSÊNCIA 05 • IDENTIDADE SÓBRIA', title: 'A Capela e a Palavra', text: 'A união entre a reverência das Escrituras e a simplicidade da adoração sincera.' },
          { tag: 'CULTO DOMÉSTICO', title: 'Edificando o Lar', text: 'Músicas que trazem a presença de Deus para dentro da sala da sua casa.' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@iagocordeiromusic',
          spotify: 'https://open.spotify.com',
          deezer: 'https://www.deezer.com',
          apple: 'https://music.apple.com',
          amazon: 'https://music.amazon.com.br',
          ytmusic: 'https://music.youtube.com/channel/UCK5Sgoev9Uvf_dexv77GftQ'
        }
      },
      {
        id: 'patinhas-e-cancoes',
        slug: 'vortice.media/patinhas-e-cancoes',
        name: 'PATINHAS & CANÇÕES',
        bandFrontName: 'Patinhas e Canções',
        hasMusic: true,
        hasApp: false,
        sampleSongTitle: 'Alguém Ouviu Meu Silêncio',
        sampleAudioUrl: './assets/audio/patinhas_silencio.mp3',
        bannerImg: './assets/banners/patinhas_youtube_banner.jpg',
        coverImg: './assets/banners/patinhas_youtube_banner.jpg',
        logoImg: './assets/logos_color/patinhas_color.png',
        badgeText: 'Amor por Pets',
        slogan: '"Dando voz, melodia e um final feliz ao olhar silencioso de cada cãozinho e gatinho."',
        description: 'Músicas profundamente emocionantes e animações 3D estilo cinema que contam histórias reais de abandono, resgate, saudade e o amor puro dos pets.',
        playlist: [
          {
            title: 'Olhos no Céu — "Toda Noite Ela Faz Isso... Você Já Reparou no Olhar do Seu Pet?"',
            style: 'MÚSICA & CLIPE NO AR • EPISÓDIO 01',
            rawImg: './assets/episodes/patinhas_real_ep01.jpg',
            audioUrl: './assets/audio/patinhas_silencio.mp3',
            youtubeUrl: 'https://www.youtube.com/watch?v=dOXLD2OdOYk',
            story: 'A história emocionante da gatinha Penélope olhando para o céu estrelado no jardim — uma canção sobre saudade, fidelidade e o amor eterno entre um pet e sua família.'
          },
          {
            title: 'O Resgate na Chuva (Alguém Ouviu Meu Silêncio) — "O Resgate do Cão Feijão!"',
            style: 'MÚSICA & CLIPE NO AR • EPISÓDIO 02',
            rawImg: './assets/episodes/patinhas_real_ep02.jpg',
            audioUrl: './assets/audio/patinhas_silencio.mp3',
            youtubeUrl: 'https://www.youtube.com/watch?v=vlLEym6b8Lo',
            story: 'Do chão molhado ao abraço mais quente: cantada pela perspectiva do cãozinho Feijão abandonado na chuva até o momento em que uma mão amiga se abaixa para resgatá-lo.'
          },
          {
            title: 'Próxima Música em Processo de Validação & Estreia',
            style: 'EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/banners/patinhas_youtube_banner.jpg',
            audioUrl: './assets/audio/patinhas_agora_eu_vou_ficar.mp3',
            isValidationCard: true,
            story: 'A próxima música e clipe 3D do canal Patinhas & Canções já está em fase final de validação para subir nas plataformas. Aguarde mais músicas dentro desta seção!'
          }
        ],
        storyHeading: 'Se Eles Pudessem Cantar: A Bíblia Emocional do Patinhas & Canções',
        storyLead: 'O que passa no coração de um cãozinho que espera no portão ou de um gatinho encolhido sob a marquise num dia frio? O Patinhas & Canções nasceu para traduzir em música a lealdade mais pura que existe na Terra.',
        storyParagraphs: [
          'Guiado pela figura acolhedora do Menestrel dos Bichinhos e seu inseparável cãozinho caramelo Pingo, o canal transforma histórias reais de resgate animal, adoção responsável e saudade eterna em curtas-metragens musicais em 3D.',
          'É impossível ouvir sem se emocionar: cada canção desperta nas crianças e nos adultos a compaixão, o respeito à criação e a gratidão por esses pequenos anjos de quatro patas que mudam nossas vidas.'
        ],
        personaTitle: 'O MENESTREL DOS BICHINHOS & O CÃOZINHO PINGO',
        personaQuote: 'Eles não pedem luxo nem explicações; pedem apenas um canto seguro e alguém para amar com toda a alma.',
        personaDetails: 'Direção Sonora & Visual: Histórias Cantadas Emotivas e Animação 3D Cinematográfica.',
        loreBoxes: [
          { tag: 'HISTÓRIA 01 • DO ABANDONO AO LAR', title: 'A Voz do Resgate', text: 'Músicas que conscientizam contra o abandono e celebram a beleza da adoção responsável.' },
          { tag: 'HISTÓRIA 02 • LEALDADE ETERNA', title: 'Quem Espera no Portão', text: 'Homenagens emocionantes aos cães e gatos que fazem parte da nossa família.' },
          { tag: 'HISTÓRIA 03 • CONSOLO & SAUDADE', title: 'Olhos no Céu', text: 'Canções de conforto para quem já precisou se despedir de um amigo de quatro patas.' },
          { tag: 'HISTÓRIA 04 • ANIMAÇÃO 3D CINEMA', title: 'Expressão em Cada Olhar', text: 'Clipes em 3D onde cada movimento de orelha e cada olhar contam uma história viva.' },
          { tag: 'HISTÓRIA 05 • EDUCAÇÃO COM AFETO', title: 'Ensinando Crianças a Amar', text: 'Conteúdo 100% seguro que planta a semente da bondade no coração dos pequenos.' },
          { tag: 'BANNER OFICIAL', title: 'Duas Mãos que Protegem', text: 'O símbolo oficial do canal: um filhote de cão e um gatinho acolhidos com amor e segurança.' }
        ],
        claimedPlatforms: ['youtube', 'spotify', 'deezer'],
        links: {
          youtube: 'https://www.youtube.com/@patinhasecancoes',
          spotify: 'https://open.spotify.com/artist/3SEifUH8nuzlsklxiyVgGC',
          deezer: 'https://www.deezer.com/br/artist/4418835',
          apple: 'https://music.apple.com/br/artist/patinhas/6818166842',
          amazon: 'https://music.amazon.com.br/search/Patinhas+%26+Can%C3%A7%C3%B5es',
          ytmusic: 'https://music.youtube.com/channel/UCBZPZYSwUmrEsWu4-E9OxPg'
        }
      },
      {
        id: 'aguas-de-descanso',
        slug: 'vortice.media/aguas-de-descanso',
        name: 'ÁGUAS DE DESCANSO',
        hasMusic: false,
        hasApp: false,
        bannerImg: './assets/banners/aguas_youtube_banner.jpg',
        coverImg: './assets/banners/aguas_youtube_banner.jpg',
        logoImg: './assets/logos_color/aguas_color.png',
        badgeText: 'Leitura da Bíblia & Descanso com Chuva',
        slogan: '"Deitar-me-ei em paz e logo pegarei no sono, porque só Tu, Senhor, me fazes repousar seguro." (Salmo 4:8)',
        description: 'Sessões longas de leitura pausada da Bíblia, Salmos, frequências suaves e chuva serena no telhado para vencer a insônia e descansar em paz.',
        episodes: [
          {
            style: 'VÍDEO NO AR • SALMOS 1 A 10',
            rawImg: './assets/episodes/aguas_real_ep01.jpg',
            title: 'Salmos 1 a 10 — A Escolha do Caminho do Justo com Chuva Suave',
            story: 'Leitura calma e acolhedora sob o som contínuo de chuva suave na floresta e lareira acesa, desenhada com baixa luminosidade para induzir o sono profundo.',
            url: 'https://www.youtube.com/watch?v=pupK264Aq94'
          },
          {
            style: 'VÍDEO NO AR • SALMOS 59 A 66',
            rawImg: './assets/episodes/aguas_real_ep08.jpg',
            title: 'O Fardo Que Você Pode Soltar Agora: A Paz dos Salmos 59 a 66',
            story: 'Leitura serena das Escrituras acompanhada de chuva suave para desacelerar os pensamentos e descansar o coração após um dia intenso.',
            url: 'https://www.youtube.com/watch?v=dwYiOzptAPM'
          },
          {
            style: 'VÍDEO NO AR • SALMOS 67 A 71',
            rawImg: './assets/episodes/aguas_real_ep09.jpg',
            title: 'Não Me Rejeites na Minha Fraqueza: O Amparo Eterno dos Salmos 67 a 71',
            story: 'Sessão de longa duração com narração pausada e chuva serena para preencher a casa de paz durante toda a noite.',
            url: 'https://www.youtube.com/watch?v=nyya4Aah1Rc'
          }
        ],
        storyHeading: 'O Refúgio na Tempestade: A Cabana Iluminada de Águas de Descanso',
        storyLead: 'Quando a noite chega e o silêncio da casa faz as preocupações parecerem maiores do que são, milhões de pessoas lutam contra a insônia. Águas de Descanso foi criado para ser uma janela acesa na madrugada.',
        storyParagraphs: [
          'A imagem oficial do canal retrata exatamente essa experiência: uma cabana acolhedora de madeira às margens de um rio sereno, cercada pela chuva suave da noite, onde uma luz aconchegante convida você a entrar e descansar.',
          'Sem gritos, sem cortes bruscos e sem claridade agressiva na tela, cada vídeo combina a leitura reverente da Bíblia com o som relaxante da chuva para que você e sua família durmam em profunda paz.'
        ],
        personaTitle: 'O GUARDIÃO DA VIGÍLIA • LEITURA BÍBLICA & CHUVA SERENA',
        personaQuote: 'Feche os olhos e solte o peso do dia. Aquele que guarda a sua vida não dorme e já está cuidando do seu amanhã.',
        personaDetails: 'Direção Sonora & Visual: Narração Bíblica Pausada, Chuva Contínua e Cenários Noturnos Relaxantes.',
        loreBoxes: [
          { tag: 'PILAR 01 • SONO PROFUNDO', title: 'Zero Claridade Agressiva', text: 'Cenários noturnos pensados para não cansar a vista no celular ou na TV do quarto.' },
          { tag: 'PILAR 02 • VOZ SERENA', title: 'Leitura Pausada da Bíblia', text: 'Narração grave, pausada e acolhedora das Escrituras que conduz a mente ao relaxamento.' },
          { tag: 'PILAR 03 • CHUVA & NATUREZA', title: 'Paisagem Sonora Terapêutica', text: 'Som contínuo de chuva no telhado, águas correntes e ambiência suave ao fundo.' },
          { tag: 'PILAR 04 • PAZ INTERIOR', title: 'Descanso para a Mente', text: 'Leituras bíblicas selecionadas para acalmar o coração após a rotina diária.' },
          { tag: 'PILAR 05 • LONGA DURAÇÃO', title: 'Companhia para a Noite Toda', text: 'Vídeos longos sem interrupções bruscas para acompanhar todo o seu ciclo de sono.' },
          { tag: 'IDENTIDADE VISUAL', title: 'A Cabana às Margens das Águas', text: 'O símbolo clássico do Salmo 23: "Guia-me mansamente a águas tranquilas."' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@AguasDeDescanso'
        }
      },
      {
        id: 'trono-da-promessa',
        slug: 'vortice.media/trono-da-promessa',
        name: 'TRONO DA PROMESSA',
        hasMusic: false,
        hasApp: true,
        bannerImg: './assets/banners/trono_youtube_banner.jpg',
        coverImg: './assets/banners/trono_youtube_banner.jpg',
        logoImg: './assets/logos_color/trono_color.png',
        badgeText: 'Série Bíblica Kids',
        slogan: '"Ensinando a Bíblia às crianças com a doçura de um avô e a magia da animação."',
        description: 'As histórias da Bíblia contadas pelo querido Vovô Nésio em sua poltrona ao pé da lareira para Pedrinho, Aninha e a Ovelhinha.',
        episodes: [
          {
            style: '1º EPISÓDIO • EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/banners/trono_youtube_banner.jpg',
            title: 'A Criação do Mundo & O Jardim de Deus — Em Processo de Validação',
            story: 'O primeiro episódio oficial da Série Criação com o Vovô Nésio, Pedrinho e Aninha já está em processo final de validação para estreia nas plataformas. Aguarde mais informações dentro desta seção!',
            url: '#em-breve',
            isComingSoon: true
          }
        ],
        storyHeading: 'A Poltrona do Vovô Nésio: Onde a Bíblia Ganha Vida para as Crianças',
        storyLead: 'Em um mundo digital cheio de conteúdos agitados e vazios para os pequenos, o Trono da Promessa resgata a memória afetiva mais bonita da infância: sentar no tapete da sala para ouvir um avô contar as histórias de Deus.',
        storyParagraphs: [
          'No banner oficial do canal, vemos o Vovô Nésio em sua poltrona azul-real, com a Bíblia aberta no colo, cercado por Pedrinho, Aninha e sua ovelhinha branca. Sempre que ele começa a ler, a sala se ilumina e a narrativa ganha vida.',
          'Além dos episódios no YouTube, o canal prepara o Aplicativo Oficial Trono da Promessa Kids — um ambiente 100% seguro, sem anúncios de terceiros, criado para apoiar pais, avós e professores da Escola Bíblica Dominical (EBD).'
        ],
        personaTitle: 'VOVÔ NÉSIO, PEDRINHO, ANINHA & A OVELHINHA',
        personaQuote: 'Cada página da Bíblia guarda um tesouro do céu esperando para brilhar no coração de uma criança.',
        personaDetails: 'Direção Sonora & Visual: Animação 3D Infantil Cristã, Ensino Bíblico e Apoio à EBD.',
        loreBoxes: [
          { tag: 'UNIVERSO 01 • VOVÔ NÉSIO', title: 'Sabedoria & Acolhimento', text: 'O contador de histórias que ensina princípios eternos com paciência, ternura e bom humor.' },
          { tag: 'UNIVERSO 02 • PEDRINHO & ANINHA', title: 'Perguntas de Criança', text: 'As dúvidas sinceras dos netinhos que ajudam todas as crianças a entenderem a Palavra.' },
          { tag: 'UNIVERSO 03 • APP EDUCATIVO KIDS', title: 'Aprender Brincando (Em Breve)', text: 'Quiz bíblico, pintura digital, jogo da memória e álbum de figurinhas dos heróis da fé.' },
          { tag: 'UNIVERSO 04 • APOIO À EBD', title: 'Para Pais e Igrejas', text: 'Ferramenta aliada do ministério infantil e do culto doméstico em família.' },
          { tag: 'UNIVERSO 05 • 100% PROTEGIDO', title: 'Infância Segura', text: 'Conteúdo livre de sustos, com valores cristãos sólidos e respeito ao ritmo infantil.' },
          { tag: 'IDENTIDADE VISUAL', title: 'A Bíblia Aberta na Sala', text: 'Cores vibrantes que encantam os olhos e gravam a mensagem no coração.' }
        ],
        links: {
          appOpenUrl: '#em-breve',
          youtube: 'https://www.youtube.com/@TronoDaPromessa'
        }
      },
      {
        id: 'incorruptivel',
        slug: 'vortice.media/incorruptivel',
        name: 'INCORRUPTÍVEL',
        hasMusic: false,
        hasApp: false,
        bannerImg: './assets/banners/incorruptivel_youtube_banner.jpg',
        coverImg: './assets/banners/incorruptivel_youtube_banner.jpg',
        logoImg: './assets/logos_color/incorruptivel_color.jpg',
        badgeText: 'Crítica Política',
        slogan: '"Onde os fatos falam mais alto que a propaganda e a cidadania não se curva."',
        description: 'Crítica política, análise investigativa e dossiês audiovisuais sobre as instituições, a economia e os bastidores do poder no Brasil.',
        episodes: [
          {
            style: '1º EPISÓDIO • EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/banners/incorruptivel_youtube_banner.jpg',
            title: 'Quarenta e Oito Horas — Em Processo de Validação & Estreia',
            story: 'O primeiro episódio em animação 3D com as raposas, lobos e ovelhas nos bastidores da República já está em processo final de validação para estreia. Aguarde mais informações dentro desta seção!',
            url: '#em-breve',
            isComingSoon: true
          }
        ],
        storyHeading: 'A Lente da Verdade: A Missão Editorial do Canal Incorruptível',
        storyLead: 'Compreender o que acontece nos bastidores do poder não deveria ser privilégio de especialistas. O canal Incorruptível nasceu para traduzir a política, as leis e a economia em uma linguagem direta, documentada e acessível.',
        storyParagraphs: [
          'Enquanto o canal irmão Rock Incorruptível expressa a indignação através da música, o Incorruptível mergulha na crítica política e na análise dos fatos. Cada episódio examina documentos, votações e decisões que impactam diretamente a mesa e o futuro do cidadão.',
          'Com ritmo documental cinematográfico e compromisso inegociável com os fatos, o canal defende a transparência, a responsabilidade fiscal e a liberdade com consciência.'
        ],
        personaTitle: 'O CRONISTA INCORRUPTÍVEL • CRÍTICA POLÍTICA SEM CONCESSÕES',
        personaQuote: 'Um povo que conhece os mecanismos do poder jamais aceita ser tratado como plateia.',
        personaDetails: 'Direção Sonora & Visual: Jornalismo Analítico, Dossiês Documentais e Investigação Cidadã.',
        loreBoxes: [
          { tag: 'DIRETRIZ 01 • CLAREZA DOCUMENTAL', title: 'Fatos Acima de Narrativas', text: 'Explicações diretas que mostram o impacto real de cada decisão política no dia a dia.' },
          { tag: 'DIRETRIZ 02 • FISCALIZAÇÃO CIDADÃ', title: 'Olho no Dinheiro Público', text: 'Acompanhamento constante de gastos, privilégios e prioridades do Estado.' },
          { tag: 'DIRETRIZ 03 • INDEPENDÊNCIA', title: 'Voz Livre', text: 'Compromisso exclusivo com a verdade e com quem trabalha e produz no país.' },
          { tag: 'DIRETRIZ 04 • ECONOMIA DESCOMPLICADA', title: 'Do Congresso ao Seu Bolso', text: 'Tradução simples de temas econômicos e tributários que afetam as famílias.' },
          { tag: 'DIRETRIZ 05 • DOSSIÊS VISUAIS', title: 'Ritmo Cinematográfico', text: 'Edição dinâmica que prende a atenção do início ao fim de cada análise.' },
          { tag: 'CONEXÃO DIRETA', title: 'Irmão do Rock Incorruptível', text: 'A união entre a crítica política falada e o rock de protesto no ecossistema Vórtice.' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@CanalIncorruptivel'
        }
      },
      {
        id: 'aliens-da-biblia',
        slug: 'vortice.media/aliens-da-biblia',
        name: 'ALIENS DA BÍBLIA',
        hasMusic: false,
        hasApp: false,
        bannerImg: './assets/banners/aliens_youtube_banner.jpg',
        coverImg: './assets/banners/aliens_youtube_banner.jpg',
        logoImg: './assets/logos_color/aliens_color.jpg',
        badgeText: 'Mistérios da Bíblia',
        slogan: '"O que os profetas da antiguidade realmente viram quando os céus se abriram?"',
        description: 'Documentários cinematográficos em 8K investigando as carruagens de fogo de Ezequiel, os Vigilantes do Livro de Enoque e os grandes enigmas dos textos antigos.',
        episodes: [
          {
            style: '1º DOCUMENTÁRIO • EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/banners/aliens_youtube_banner.jpg',
            title: 'A Roda Dentro da Roda (Ezequiel) — Em Processo de Validação & Estreia',
            story: 'O primeiro documentário oficial em 8K do canal Aliens da Bíblia já está em processo final de validação para estreia nas plataformas. Aguarde mais informações dentro desta seção!',
            url: '#em-breve',
            isComingSoon: true
          }
        ],
        storyHeading: 'Quando o Céu Tocou a Terra: A Bíblia Cósmica de Aliens da Bíblia',
        storyLead: 'Por milênios, profetas e escribas registraram visões que desafiavam o vocabulário humano da época: rodas de berilo girando no ar, carruagens de fogo, escadas que tocavam o cosmos e seres resplandecentes.',
        storyParagraphs: [
          'O canal Aliens da Bíblia mergulha nesses textos milenares com rigor documental e reconstrução visual em 8K, unindo arqueologia bíblica, análise de manuscritos antigos e ficção científica reverente.',
          'Guiado pelo universo narrativo das Quatro Testemunhas (Aurelion, Kael, Drakhor e Vhakar), cada episódio examina palavra por palavra o hebraico e o aramaico antigos para revelar a grandiosidade dos mistérios bíblicos.'
        ],
        personaTitle: 'AS 4 TESTEMUNHAS • AURELION, KAEL, DRAKHOR & VHAKAR',
        personaQuote: 'Os antigos não escreveram lendas; eles descreveram com as palavras que tinham aquilo que seus olhos contemplaram no céu.',
        personaDetails: 'Direção Sonora & Visual: Documentários 8K, Arqueologia Bíblica e Reconstrução Visual.',
        loreBoxes: [
          { tag: 'ENIGMA 01 • AS RODAS DE EZEQUIEL', title: 'Merkabah em 8K', text: 'Análise visual e textual da visão mais detalhada de todo o Antigo Testamento.' },
          { tag: 'ENIGMA 02 • OS VIGILANTES', title: 'Gênesis 6 & Enoque', text: 'Os relatos sobre os filhos do céu, os Nefilins e o mundo antes do Dilúvio.' },
          { tag: 'ENIGMA 03 • ARQUEOLOGIA BÍBLICA', title: 'Manuscritos do Mar Morto', text: 'O que os pergaminhos encontrados em Qumran revelam sobre o cosmos antigo.' },
          { tag: 'ENIGMA 04 • AS 4 TESTEMUNHAS', title: 'Guardiões da Memória', text: 'Aurelion, Kael, Drakhor e Vhakar apresentando diferentes ângulos de cada mistério.' },
          { tag: 'ENIGMA 05 • DIREÇÃO DE ARTE 8K', title: 'Imersão Cinematográfica', text: 'Reconstruções visuais de tirar o fôlego com trilha sonora épica de mistério.' },
          { tag: 'BANNER OFICIAL', title: 'O Portal entre os Pergaminhos e as Estrelas', text: 'A identidade visual que une a sabedoria bíblica milenar à imensidão do universo.' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@AliensDaBiblia'
        }
      },
      {
        id: 'aquario-dos-felinos',
        slug: 'vortice.media/aquario-dos-felinos',
        name: 'AQUÁRIO DOS FELINOS',
        hasMusic: false,
        hasApp: false,
        bannerImg: './assets/banners/aquario_youtube_banner.jpg',
        coverImg: './assets/banners/aquario_youtube_banner.jpg',
        logoImg: './assets/logos_color/aquario_color.png',
        badgeText: 'Aventura Pet Infantil',
        slogan: '"Quatro gatinhos curiosos, um aquário luminoso cheio de segredos e muita amizade!"',
        description: 'Série animada infantil em 3D acompanhando as aventuras de Mike, Tufão, Penélope e Feijão enquanto protegem um aquário mágico e aprendem sobre trabalho em equipe.',
        episodes: [
          {
            style: '1º EPISÓDIO • EM PROCESSO DE VALIDAÇÃO',
            rawImg: './assets/banners/aquario_youtube_banner.jpg',
            title: 'O Mistério da Pérola Brilhante do Aquário — Em Processo de Validação',
            story: 'A primeira aventura oficial em 3D de Mike, Tufão, Penélope e Feijão já está em processo final de validação para estreia. Aguarde mais informações dentro desta seção!',
            url: '#em-breve',
            isComingSoon: true
          }
        ],
        storyHeading: 'O Mundo Mágico de Mike, Tufão, Penélope e Feijão',
        storyLead: 'Todo mundo sabe que gatinhos são fascinados por aquários — mas no universo do Aquário dos Felinos, os amigos não querem pescar os peixinhos: eles são os guardiões secretos de um mundo subaquático encantado!',
        storyParagraphs: [
          'Extraído da Bíblia oficial do canal, o grupo é formado por personalidades que as crianças amam de imediato: Mike (o líder corajoso), Tufão (o aventureiro cheio de energia), Penélope (a gatinha inteligente e observadora) e seus amigos inseparáveis.',
          'Com textura 3D fofinha de cinema e iluminação bioluminescente, cada episódio diverte as crianças enquanto ensina valores de amizade, partilha, paciência e cuidado com os animais.'
        ],
        personaTitle: 'A TURMA OFICIAL • MIKE, TUFÃO, PENÉLOPE & AMIGOS',
        personaQuote: 'Quando quatro patinhas trabalham juntas, qualquer mistério vira uma grande brincadeira!',
        personaDetails: 'Direção Sonora & Visual: Animação 3D Infantil, Aventuras com Pets e Valores Familiares.',
        loreBoxes: [
          { tag: 'PERSONAGEM 01 • MIKE', title: 'O Líder Corajoso', text: 'Sempre pronto para organizar a missão e proteger toda a turma.' },
          { tag: 'PERSONAGEM 02 • TUFÃO', title: 'Energia & Alegria', text: 'O mais rápido e brincalhão, que transforma qualquer dia comum em festa.' },
          { tag: 'PERSONAGEM 03 • PENÉLOPE', title: 'Mente Brilhante', text: 'Observadora e criativa, sempre encontra a solução para os enigmas do aquário.' },
          { tag: 'PERSONAGEM 04 • FEIJÃO & TURMA', title: 'Amizade Verdadeira', text: 'Curiosos e cheios de ternura, conquistam o coração de todas as crianças.' },
          { tag: 'CENÁRIO MÁGICO', title: 'O Grande Aquário Luminoso', text: 'Um universo bioluminescente cheio de cores que estimula a imaginação infantil.' },
          { tag: 'DIVERSÃO SEGURA', title: 'Para Toda a Família', text: 'Animação 3D leve, alegre e educativa, livre de qualquer violência.' }
        ],
        links: {
          youtube: 'https://www.youtube.com/@AquarioDosFelinos'
        }
      }
    ];

    /* =========================================================================
       CONFIGURAÇÃO DAS 10 PLACAS DE TRÂNSITO PADRÃO CTB + LOGO E ESCRITA OFICIAL DE CADA CANAL!
       ========================================================================= */
    const SIGN_STYLES = {
      'rock-incorruptivel': {
        img: './assets/signs/sign_01_rock.png',
        lockupImg: './assets/sign_logos/lockup_01_rock.png',
        padding: '12px 24px 8px'
      },
      'sacronia': {
        img: './assets/signs/sign_02_sacronia.png',
        lockupImg: './assets/sign_logos/lockup_02_sacronia.png',
        padding: '12px 24px 8px'
      },
      'neon-asher': {
        img: './assets/signs/sign_03_neon.png',
        lockupImg: './assets/sign_logos/lockup_03_neon.png',
        padding: '12px 24px 8px'
      },
      'iago-cordeiro': {
        img: './assets/signs/sign_04_iago.png',
        lockupImg: './assets/sign_logos/lockup_04_iago.png',
        padding: '12px 24px 8px'
      },
      'patinhas-e-cancoes': {
        img: './assets/signs/sign_05_patinhas.png',
        lockupImg: './assets/sign_logos/lockup_05_patinhas.png',
        padding: '12px 24px 8px'
      },
      'aguas-de-descanso': {
        img: './assets/signs/sign_06_aguas.png',
        lockupImg: './assets/sign_logos/lockup_06_aguas.png',
        padding: '12px 24px 8px'
      },
      'trono-da-promessa': {
        img: './assets/signs/sign_07_trono.png',
        lockupImg: './assets/sign_logos/lockup_07_trono.png',
        padding: '12px 24px 8px'
      },
      'incorruptivel': {
        img: './assets/signs/sign_08_incorruptivel.png',
        lockupImg: './assets/sign_logos/lockup_08_incorruptivel.png',
        padding: '12px 24px 8px'
      },
      'aliens-da-biblia': {
        img: './assets/signs/sign_09_aliens.png',
        lockupImg: './assets/sign_logos/lockup_09_aliens.png',
        padding: '12px 24px 8px'
      },
      'aquario-dos-felinos': {
        img: './assets/signs/sign_10_aquario.png',
        lockupImg: './assets/sign_logos/lockup_10_aquario.png',
        padding: '12px 24px 8px'
      }
    };

    const orbitStage = document.getElementById('vortex-orbit-stage');
    const cardStates = [];

    /* Controle de Alinhamento ao Clicar na Logo da Vórtice Mídia */
    let isGridAligned = false;
    let gridBlend = 0.0; // 0.0 = Girando no Vórtice | 1.0 = Alinhadas de Frente na Tela

    function toggleHeroSignsAlignment() {
      isGridAligned = !isGridAligned;
      const btnWrap = document.getElementById('vortice-logo-toggle-btn');
      if (btnWrap) {
        btnWrap.classList.toggle('is-aligned', isGridAligned);
      }
    }

    /* Alturas verticais descentralizadas no funil do furacão (sem fila indiana!) */
    const STAGGERED_ALTITUDES = [-0.27, 0.21, -0.11, 0.30, 0.04, -0.22, 0.14, -0.31, 0.25, -0.04];
    const STAGGERED_RADIUS_MULT = [0.92, 1.08, 0.85, 1.03, 0.96, 1.11, 0.88, 1.05, 0.94, 1.09];
    const STAGGERED_TUMBLE_SPEED = [0.75, -0.68, 0.82, -0.74, 0.64, -0.79, 0.71, -0.66, 0.85, -0.72];

    /* =========================================================================
       CONTROLE DE PLATAFORMAS REIVINDICADAS vs. PÁGINA INTERNA EM REIVINDICAÇÃO
       - YouTube ('youtube') está 100% ativo para todos os 10 canais -> abre direto!
       - Patinhas & Canções já possui Spotify e Deezer reivindicados e ativos -> abrem direto!
       - Demais plataformas (Spotify, Deezer, Apple Music, Amazon Music, YT Music,
         Instagram, TikTok) que ainda estão em processo de reivindicação de artista
         abrem a página oficial interna (#platform-claim-overlay), NUNCA uma home genérica!
       ========================================================================= */
    const PLATFORM_META = {
      spotify: {
        name: 'Spotify for Artists',
        shortName: 'Spotify',
        color: '#1DB954',
        iconKey: 'spotify',
        stage: 'Homologação de Perfil Oficial de Artista (Spotify for Artists)'
      },
      deezer: {
        name: 'Deezer for Creators',
        shortName: 'Deezer',
        color: '#A238FF',
        iconKey: 'deezer',
        stage: 'Unificação de Catálogo & Reivindicação de Artista (Deezer Creators)'
      },
      apple: {
        name: 'Apple Music for Artists',
        shortName: 'Apple Music',
        color: '#FA243C',
        iconKey: 'apple',
        stage: 'Verificação Oficial de Identidade Musical (Apple Music for Artists)'
      },
      amazon: {
        name: 'Amazon Music for Artists',
        shortName: 'Amazon Music',
        color: '#00A8E1',
        iconKey: 'amazon',
        stage: 'Vinculação de ISRC/UPC & Perfil Oficial (Amazon Music for Artists)'
      },
      ytmusic: {
        name: 'YouTube Music (OAC)',
        shortName: 'YouTube Music',
        color: '#FF0033',
        iconKey: 'ytmusic',
        stage: 'Fusão de Canal Oficial de Artista (Official Artist Channel — OAC)'
      },
      instagram: {
        name: 'Instagram Oficial',
        shortName: 'Instagram',
        color: '#E1306C',
        iconKey: 'instagram',
        stage: 'Configuração de Perfil Oficial & Bastidores (@vorticemidia)'
      },
      tiktok: {
        name: 'TikTok Oficial',
        shortName: 'TikTok',
        color: '#00F2FE',
        iconKey: 'tiktok',
        stage: 'Configuração de Perfil Oficial & Cortes Musicais'
      }
    };

    function isPlatformClaimed(ch, platKey) {
      if (!ch) return false;
      if (platKey === 'youtube') return Boolean(ch.links && ch.links.youtube);
      const claimed = Array.isArray(ch.claimedPlatforms) ? ch.claimedPlatforms : ['youtube'];
      return claimed.includes(platKey) && Boolean(ch.links && ch.links[platKey]);
    }

    function getPlatformLinkAttrs(ch, platKey, customTitle) {
      const pMeta = PLATFORM_META[platKey] || { shortName: platKey };
      if (isPlatformClaimed(ch, platKey)) {
        const url = ch.links[platKey];
        const title = customTitle || `${pMeta.shortName || 'Canal'} Oficial de ${ch.name}`;
        return `href="${url}" target="_blank" rel="noopener" title="${title}"`;
      }
      const title = `${pMeta.shortName} de ${ch.name} — Perfil Oficial em Reivindicação (Em Breve)`;
      return `href="#reivindicacao-${ch.id}-${platKey}" onclick="openPlatformClaimPage(event, '${ch.id}', '${platKey}')" title="${title}"`;
    }

    function openPlatformClaimPage(e, chId, platKey) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      const ch = VORTICE_CHANNELS.find(c => c.id === chId) || VORTICE_CHANNELS[0];
      const pMeta = PLATFORM_META[platKey] || PLATFORM_META.spotify;

      const logoEl = document.getElementById('claim-channel-logo');
      if (logoEl) {
        logoEl.src = ch.logoImg || ch.coverImg;
        logoEl.alt = ch.name;
      }

      const badgeWrap = document.getElementById('claim-platform-badge');
      if (badgeWrap) {
        badgeWrap.style.background = `linear-gradient(135deg, ${pMeta.color} 0%, #09121f 100%)`;
        badgeWrap.innerHTML = SVG_ICONS[pMeta.iconKey] || SVG_ICONS.spotify;
      }

      const titleEl = document.getElementById('claim-title-heading');
      if (titleEl) {
        titleEl.innerHTML = `${ch.name} &bull; <span style="color:#f7d07a;">${pMeta.shortName}</span>`;
      }

      const descEl = document.getElementById('claim-desc-text');
      if (descEl) {
        descEl.innerHTML = `O perfil oficial de <strong>${ch.name}</strong> na plataforma <strong>${pMeta.name}</strong> está atualmente em <strong>processo de reivindicação, verificação de autenticidade e sincronização de catálogo</strong> junto à nossa distribuidora internacional.<br><br>Na Vórtice Mídia, não direcionamos você para links genéricos: este botão será liberado automaticamente assim que a homologação oficial da conta estiver 100% concluída.`;
      }

      const stepEl = document.getElementById('claim-step2-text');
      if (stepEl) {
        stepEl.textContent = pMeta.stage;
      }

      const actionsEl = document.getElementById('claim-actions-container');
      if (actionsEl) {
        let actHtml = '';
        if (ch.links && ch.links.youtube) {
          actHtml += `
            <a href="${ch.links.youtube}" target="_blank" rel="noopener" class="claim-btn-primary">
              <span class="claim-btn-PrimarySvg">${SVG_ICONS.youtube}</span>
              <span>Assistir Agora no YouTube Oficial</span>
            </a>
          `;
        }
        if (isPlatformClaimed(ch, 'spotify')) {
          actHtml += `
            <a href="${ch.links.spotify}" target="_blank" rel="noopener" class="claim-btn-secondary">
              <span class="claim-btn-PrimarySvg">${SVG_ICONS.spotify}</span>
              <span>Ouvir no Spotify Oficial</span>
            </a>
          `;
        }
        if (isPlatformClaimed(ch, 'deezer')) {
          actHtml += `
            <a href="${ch.links.deezer}" target="_blank" rel="noopener" class="claim-btn-secondary" style="background:linear-gradient(180deg,#a238ff 0%,#6b21a8 100%);">
              <span class="claim-btn-PrimarySvg">${SVG_ICONS.deezer}</span>
              <span>Ouvir no Deezer Oficial</span>
            </a>
          `;
        }
        actHtml += `
          <button type="button" class="claim-btn-back" onclick="closePlatformClaimPage()">
            &larr; Voltar
          </button>
        `;
        actionsEl.innerHTML = actHtml;
      }

      const overlay = document.getElementById('platform-claim-overlay');
      if (overlay) {
        overlay.classList.add('open');
      }
    }

    function closePlatformClaimPage() {
      const overlay = document.getElementById('platform-claim-overlay');
      if (overlay) {
        overlay.classList.remove('open');
      }
    }

    function renderHeroChannels() {
      orbitStage.innerHTML = '';
      cardStates.length = 0;

      VORTICE_CHANNELS.forEach((ch, idx) => {
        const sCfg = SIGN_STYLES[ch.id] || SIGN_STYLES['rock-incorruptivel'];
        const card = document.createElement('div');
        card.className = 'vortice-channel-btn';
        card.style.backgroundImage = `url('${sCfg.img}')`;
        card.style.padding = sCfg.padding;

        let leftIconsHtml = '';
        if (ch.hasMusic) {
          leftIconsHtml = `
            <div class="streaming-icons-group">
              <a ${getPlatformLinkAttrs(ch, 'spotify')} class="platform-icon-link spotify">${SVG_ICONS.spotify}</a>
              <a ${getPlatformLinkAttrs(ch, 'deezer')} class="platform-icon-link deezer">${SVG_ICONS.deezer}</a>
              <a ${getPlatformLinkAttrs(ch, 'apple')} class="platform-icon-link apple">${SVG_ICONS.apple}</a>
              <a ${getPlatformLinkAttrs(ch, 'amazon')} class="platform-icon-link amazon">${SVG_ICONS.amazon}</a>
              <a ${getPlatformLinkAttrs(ch, 'youtube')} class="platform-icon-link youtube">${SVG_ICONS.youtube}</a>
            </div>
          `;
        } else {
          leftIconsHtml = `
            <div class="streaming-icons-group">
              <a ${getPlatformLinkAttrs(ch, 'youtube')} class="platform-icon-link youtube">${SVG_ICONS.youtube}</a>
            </div>
          `;
        }

        card.innerHTML = `
          <div class="sign-stamped-surface">
            <div class="channel-name-row" data-portal-idx="${idx}">
              <img class="sign-channel-lockup-img" src="${sCfg.lockupImg}" alt="${ch.name}">
            </div>
            <div class="btn-actions-bar">
              ${leftIconsHtml}
              <div class="right-links-group">
                <button type="button" class="vortice-pagina-btn" data-portal-idx="${idx}" title="Abrir Página do Canal no Portal Vórtice">
                  ${SVG_ICONS.vorticeFunnel}
                  <span>Página</span>
                </button>
              </div>
            </div>
          </div>
        `;

        card.querySelectorAll('[data-portal-idx]').forEach(el => {
          el.addEventListener('click', (e) => {
            e.stopPropagation();
            openChannelPortal(ch);
          });
        });

        const state = {
          el: card,
          idx,
          sCfg,
          orbitAngle: (idx / VORTICE_CHANNELS.length) * Math.PI * 2,
          altitudeOffset: STAGGERED_ALTITUDES[idx % STAGGERED_ALTITUDES.length],
          radiusMult: STAGGERED_RADIUS_MULT[idx % STAGGERED_RADIUS_MULT.length],
          tumbleSpeed: STAGGERED_TUMBLE_SPEED[idx % STAGGERED_TUMBLE_SPEED.length],
          selfSpinAngle: idx * 0.95,
          phaseX: idx * 1.15 + 0.3,
          phaseY: idx * 0.85 + 0.2,
          phaseRot: idx * 1.35,
          screenX: 0,
          screenY: 0,
          depth: 0,
          hovered: false
        };

        /* Pausa INDIVIDUAL: somente a placa onde o mouse está em cima para de girar! */
        card.addEventListener('mouseenter', () => { state.hovered = true; });
        card.addEventListener('mouseleave', () => { state.hovered = false; });

        orbitStage.appendChild(card);
        cardStates.push(state);
      });
    }

    renderHeroChannels();

    /* =========================================================================
       RÁDIO VÓRTICE MUSIC + MODO EXCLUSIVO POR CANAL ("OUVIR AGORA") + AS MAIS TOCADAS
       - Se clicar em "Ouvir Agora" de um canal (ex: Rock Incorruptível ou Patinhas & Canções),
         toca SOMENTE as músicas daquele canal em sequência!
       - Se clicar na Rádio Vórtice Music (topo direito) ou em As Mais Tocadas, toca a programação geral!
       ========================================================================= */
    const inlineAudio = document.getElementById('vortice-inline-audio');
    const radioWidget = document.getElementById('vortice-radio-widget');
    const radioTrackLabel = document.getElementById('radio-track-label');
    const musicChannels = VORTICE_CHANNELS.filter(c => c.hasMusic);

    let activePlayMode = 'all'; // 'all' (Rádio Geral) | 'channel' (Somente músicas do canal escolhido)
    let currentPlayingIdx = 0;  // Índice em musicChannels
    let activeChannelId = musicChannels[0] ? musicChannels[0].id : '';
    let activeChannelTrackIdx = 0;
    let currentSongTitle = musicChannels[0] ? musicChannels[0].sampleSongTitle : '';

    function renderTop5() {
      const container = document.getElementById('top5-list-container');
      container.innerHTML = '';

      musicChannels.forEach((ch, mIdx) => {
        const card = document.createElement('div');
        card.className = 'top5-wine-card';
        card.id = `top5-card-${mIdx}`;
        card.innerHTML = `
          <div class="top5-left-group">
            <img class="top5-cover-thumb" src="${ch.logoImg || ch.coverImg}" alt="${ch.bandFrontName}">
            <div class="top5-song-and-band">
              <span class="top5-song-name">${ch.sampleSongTitle}</span>
              <span class="top5-band-front">${ch.bandFrontName}</span>
            </div>
          </div>
          <div class="top5-right-controls">
            <button type="button" class="top5-play-action" id="top5-btn-${mIdx}">
              <span class="tri" id="top5-tri-${mIdx}">▶</span>
              <span id="top5-lbl-${mIdx}">OUVIR</span>
            </button>
          </div>
        `;
        card.querySelector(`#top5-btn-${mIdx}`).addEventListener('click', () => toggleTop5Track(mIdx));
        container.appendChild(card);
      });
    }

    function playUrlAndRefresh(audioUrl, songTitle, chIdx, chId, trkIdx, mode) {
      activePlayMode = mode;
      currentPlayingIdx = chIdx;
      activeChannelId = chId;
      activeChannelTrackIdx = trkIdx;
      currentSongTitle = songTitle;

      const cleanTarget = audioUrl.replace('./', '');
      if (!inlineAudio.src || !inlineAudio.src.endsWith(cleanTarget)) {
        inlineAudio.src = audioUrl;
      }
      inlineAudio.play().then(() => {
        refreshTop5UI(true);
      }).catch(() => {
        refreshTop5UI(false);
      });
    }

    function playTrackByIndex(mIdx) {
      if (!musicChannels.length) return;
      const safeIdx = ((mIdx % musicChannels.length) + musicChannels.length) % musicChannels.length;
      const ch = musicChannels[safeIdx];
      playUrlAndRefresh(ch.sampleAudioUrl, ch.sampleSongTitle, safeIdx, ch.id, 0, 'all');
    }

    function playSpecificChannelTrack(channelId, trackIdx) {
      const mIdx = musicChannels.findIndex(c => c.id === channelId);
      if (mIdx === -1) return;
      const ch = musicChannels[mIdx];
      const tracks = (ch.playlist && ch.playlist.length)
        ? ch.playlist
        : [{ title: ch.sampleSongTitle, audioUrl: ch.sampleAudioUrl }];
      const safeTrk = ((trackIdx % tracks.length) + tracks.length) % tracks.length;
      const trk = tracks[safeTrk];
      playUrlAndRefresh(trk.audioUrl, trk.title, mIdx, ch.id, safeTrk, 'channel');
    }

    function toggleTop5Track(mIdx) {
      const ch = musicChannels[mIdx];
      if (!ch) return;

      if (currentPlayingIdx === mIdx && !inlineAudio.paused && activePlayMode === 'all') {
        inlineAudio.pause();
        refreshTop5UI(false);
        return;
      }
      playTrackByIndex(mIdx);
    }

    function toggleVorticeRadio() {
      if (!musicChannels.length) return;
      if (!inlineAudio.paused) {
        inlineAudio.pause();
        refreshTop5UI(false);
      } else {
        if (activePlayMode === 'channel' && activeChannelId) {
          playSpecificChannelTrack(activeChannelId, activeChannelTrackIdx);
        } else {
          playTrackByIndex(currentPlayingIdx >= 0 ? currentPlayingIdx : 0);
        }
      }
    }

    function nextVorticeRadioTrack(e) {
      if (e) e.stopPropagation();
      if (activePlayMode === 'channel' && activeChannelId) {
        playSpecificChannelTrack(activeChannelId, activeChannelTrackIdx + 1);
      } else {
        playTrackByIndex(currentPlayingIdx + 1);
      }
    }

    /* Acionado pelos botões "Ouvir Agora" da Seção 1 (Escolha Sua Sintonia Agora):
       Toca SOMENTE as músicas daquele canal escolhido em sequência! */
    function playChannelMusicById(channelId) {
      const mIdx = musicChannels.findIndex(c => c.id === channelId);
      if (mIdx === -1) return;

      if (activePlayMode === 'channel' && activeChannelId === channelId && !inlineAudio.paused) {
        inlineAudio.pause();
        refreshTop5UI(false);
      } else {
        playSpecificChannelTrack(channelId, 0);
      }
    }

    /* Quando uma música termina:
       - Se estiver no modo exclusivo de um canal, avança para a PRÓXIMA música daquele mesmo canal!
       - Se estiver no modo Rádio Geral, avança para o próximo canal! */
    inlineAudio.addEventListener('ended', () => {
      if (activePlayMode === 'channel' && activeChannelId) {
        playSpecificChannelTrack(activeChannelId, activeChannelTrackIdx + 1);
      } else {
        playTrackByIndex(currentPlayingIdx + 1);
      }
    });

    function refreshTop5UI(isPlaying) {
      const activeCh = musicChannels[currentPlayingIdx] || musicChannels[0];
      if (radioWidget) {
        radioWidget.classList.toggle('is-playing', isPlaying);
      }
      if (radioTrackLabel && activeCh) {
        const modePrefix = activePlayMode === 'channel' ? `[Canal ${activeCh.bandFrontName}] ` : '';
        radioTrackLabel.textContent = isPlaying
          ? `${modePrefix}${currentSongTitle || activeCh.sampleSongTitle} • ${activeCh.bandFrontName}`
          : 'Clique para Sintonizar ▶';
      }

      /* Atualiza os botões "Ouvir Agora" da Seção 1 (Escolha Sua Sintonia Agora) */
      document.querySelectorAll('.sintonia-play-music-btn').forEach(btn => {
        const chId = btn.getAttribute('data-sintonia-channel');
        const isThisChannel = isPlaying && activeCh && activeCh.id === chId;
        btn.classList.toggle('active-playing', isThisChannel);
        btn.innerHTML = isThisChannel ? '❚❚ Tocando Canal' : '▶ Ouvir Agora';
      });

      /* Atualiza também os cards de faixa dentro da Página do Canal caso esteja aberta */
      document.querySelectorAll('.ch-track-card[data-ch-id]').forEach(card => {
        const cId = card.getAttribute('data-ch-id');
        const tIdx = parseInt(card.getAttribute('data-trk-idx') || '0', 10);
        const isTrackActive = isPlaying && activeChannelId === cId && activeChannelTrackIdx === tIdx;
        card.classList.toggle('playing-now', isTrackActive);
        const btn = card.querySelector('.ch-track-play-btn');
        if (btn) {
          btn.innerHTML = isTrackActive ? '❚❚ Tocando Agora' : '▶ Ouvir Esta Música';
        }
      });

      musicChannels.forEach((_, idx) => {
        const card = document.getElementById(`top5-card-${idx}`);
        const tri = document.getElementById(`top5-tri-${idx}`);
        const lbl = document.getElementById(`top5-lbl-${idx}`);
        const active = (idx === currentPlayingIdx && isPlaying);
        if (card) card.classList.toggle('playing', active);
        if (tri) tri.textContent = active ? '❚❚' : '▶';
        if (lbl) lbl.textContent = active ? 'TOCANDO' : 'OUVIR';
      });
    }

    renderTop5();

    /* =========================================================================
       SINCRONIZAÇÃO AUTOMÁTICA DO ÚLTIMO VÍDEO POSTADO NO YOUTUBE
       ========================================================================= */
    const YOUTUBE_CHANNEL_IDS = {
      'AguasDeDescanso': 'UCQlciPfUTpLt5CLcHog56lA',
      'RockIncorruptivel': 'UCie7z4E8dXBRz46XfvuwH7Q',
      'SacroniaMusic': 'UCbpf2WHDz57FW3QCcftc_2A',
      'NeonAsherDarkRock': 'UCiVaYR4-N9BBmS9ORhDP4qg',
      'iagocordeiromusic': 'UCK5Sgoev9Uvf_dexv77GftQ',
      'patinhasecancoes': 'UCBZPZYSwUmrEsWu4-E9OxPg',
      'TronoDaPromessa': 'UC8Xl0b3y4NAAfThZ9pbPiiw',
      'CanalIncorruptivel': 'UCmbmta-uQ9tWUKI7285BGAw',
      'AliensDaBiblia': 'UCCYBtb5aHCWltAXBdX9PMYg',
      'AquarioDosFelinos': 'UCj3tQwJmthEbNAZa_1tD-0w'
    };

    async function syncLatestYouTubeVideos() {
      const cards = document.querySelectorAll('#latest-yt-videos-grid .universo-poster-card[data-yt-handle]');
      for (const card of cards) {
        const handle = card.getAttribute('data-yt-handle');
        const channelId = YOUTUBE_CHANNEL_IDS[handle];
        if (!channelId) continue;
        try {
          const rssUrl = `https://www.youtube.com/feeds/videos.xml?channel_id=${encodeURIComponent(channelId)}`;
          const apiUrl = `https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(rssUrl)}`;
          const res = await fetch(apiUrl);
          if (!res.ok) continue;
          const data = await res.json();
          if (data && data.items && data.items.length > 0) {
            const latest = data.items[0];
            const videoMatch = (latest.guid || latest.link || '').match(/(?:v=|video:)([a-zA-Z0-9_-]{11})/);
            const videoId = videoMatch ? videoMatch[1] : null;
            const linkEl = card.querySelector('.yt-auto-link');
            if (videoId && linkEl) {
              linkEl.href = `https://www.youtube.com/watch?v=${videoId}`;
            } else if (latest.link && linkEl) {
              linkEl.href = latest.link;
            }
          }
        } catch (err) {
          /* Mantém o banner oficial do YouTube do canal */
        }
      }
    }
    syncLatestYouTubeVideos();

    /* =========================================================================
       PÁGINA EXCLUSIVA DE CADA CANAL (#channel-portal-overlay)
       - Padronizada em todas as 10 páginas com o contraste Noir-Neon (Preto + Ciano + Roxo/Magenta)!
       - Sem botões de seção no topo, sem bordas amarelas e sem caixas fechando seções!
       - 7 Seções Completas com Imagens Cruas nos cards e Botões Grandes das Plataformas!
       ========================================================================= */
    const portalOverlay = document.getElementById('channel-portal-overlay');

    function openChannelById(id) {
      const ch = VORTICE_CHANNELS.find(c => c.id === id);
      if (ch) openChannelPortal(ch);
    }

    function openChannelPortal(ch) {
      /* Padronização total: Fundo 100% transparente (vendo o Vórtice girar ao fundo) + Cinza Escuro Translúcido igual à Página Principal! */
      portalOverlay.style.setProperty('--ch-accent', '#f7d07a');
      portalOverlay.style.setProperty('--ch-secondary', '#ffffff');
      portalOverlay.style.setProperty('--ch-glow-a', 'rgba(255, 255, 255, 0.24)');
      portalOverlay.style.setProperty('--ch-glow-b', 'rgba(247, 208, 122, 0.24)');
      portalOverlay.style.setProperty('--ch-bg', 'transparent');
      portalOverlay.style.setProperty('--ch-font', "'Cinzel', Georgia, serif");
      portalOverlay.style.backgroundColor = 'transparent';

      /* SEÇÃO 1: Banner Full-Bleed com Degradê Preto nas Bordas + Logo + Título + Slogan + CTAs */
      document.getElementById('ch-page-bg').src = ch.bannerImg || ch.coverImg;
      document.getElementById('ch-page-logo').src = ch.logoImg || ch.coverImg;
      document.getElementById('portal-title-text').textContent = ch.name;
      document.getElementById('portal-slogan-text').textContent = ch.slogan || '';
      document.getElementById('portal-desc-text').textContent = ch.description;

      const heroCtas = document.getElementById('portal-hero-ctas');
      let ctaHtml = '';
      if (ch.hasMusic) {
        ctaHtml += `
          <div class="ch-pure-icons-row">
            <a ${getPlatformLinkAttrs(ch, 'spotify', 'Ouvir no Spotify')} class="ch-plat-icon-3d spotify">${SVG_ICONS.spotify}</a>
            <a ${getPlatformLinkAttrs(ch, 'deezer', 'Ouvir no Deezer')} class="ch-plat-icon-3d deezer">${SVG_ICONS.deezer}</a>
            <a ${getPlatformLinkAttrs(ch, 'apple', 'Ouvir no Apple Music')} class="ch-plat-icon-3d apple">${SVG_ICONS.apple}</a>
            <a ${getPlatformLinkAttrs(ch, 'amazon', 'Ouvir no Amazon Music')} class="ch-plat-icon-3d amazon">${SVG_ICONS.amazon}</a>
            <a ${getPlatformLinkAttrs(ch, 'youtube', 'Assistir no YouTube Oficial')} class="ch-plat-icon-3d youtube">${SVG_ICONS.youtube}</a>
          </div>
        `;
      } else if (ch.links && ch.links.youtube) {
        ctaHtml += `
          <div class="ch-pure-icons-row">
            <a ${getPlatformLinkAttrs(ch, 'youtube', 'Assistir no YouTube Oficial')} class="ch-plat-icon-3d youtube">${SVG_ICONS.youtube}</a>
          </div>
        `;
      }
      heroCtas.innerHTML = ctaHtml;

      /* SEÇÃO 2: Sobre o Canal, Propósito & Identidade Canônica */
      document.getElementById('portal-story-heading').textContent = ch.storyHeading || `Sobre ${ch.name} & Sua Essência`;
      document.getElementById('portal-story-left').innerHTML = `
        <div class="ch-story-lead">${ch.storyLead || ''}</div>
        ${(ch.storyParagraphs || []).map(p => `<p class="ch-story-p">${p}</p>`).join('')}
      `;
      document.getElementById('portal-story-right').innerHTML = `
        <span class="ch-persona-tag">${ch.personaTitle || 'IDENTIDADE CANÔNICA'}</span>
        <h3 style="font-family:'Playfair Display',Georgia,serif;font-size:21.5px;font-weight:800;color:#ffffff;margin:4px 0 10px;">A Voz &amp; O Espírito do Canal</h3>
        <blockquote class="ch-persona-quote">${ch.personaQuote || ch.slogan || ''}</blockquote>
        <p style="font-size:13.8px;line-height:1.65;color:rgba(255,255,255,0.88);margin:12px 0 0;">${ch.personaDetails || ''}</p>
      `;

      /* SEÇÃO 3: Catálogo de 6 Músicas / Episódios com IMAGEM CRUA (Sem texto)
         + Ícones 3D Puros das Plataformas (Sem botão de tocar música no site!) */
      const repTitle = document.getElementById('portal-rep-title');
      const repSub = document.getElementById('portal-rep-sub');
      const repRightAction = document.getElementById('portal-rep-right-action');
      const tracksContainer = document.getElementById('portal-tracks-container');

      if (ch.hasMusic && ch.playlist && ch.playlist.length) {
        tracksContainer.classList.toggle('single-card-mode', ch.playlist.length === 1);
        repTitle.textContent = `Músicas & Clipes Oficiais de ${ch.name}`;
        if (repSub) {
          repSub.textContent = 'Cenas originais sem texto sobreposto — clique no símbolo 3D da sua plataforma preferida para ouvir ou assistir.';
        }
        repRightAction.innerHTML = `
          <div class="ch-pure-icons-row">
            <a ${getPlatformLinkAttrs(ch, 'spotify', 'Spotify')} class="ch-plat-icon-3d spotify">${SVG_ICONS.spotify}</a>
            <a ${getPlatformLinkAttrs(ch, 'deezer', 'Deezer')} class="ch-plat-icon-3d deezer">${SVG_ICONS.deezer}</a>
            <a ${getPlatformLinkAttrs(ch, 'apple', 'Apple Music')} class="ch-plat-icon-3d apple">${SVG_ICONS.apple}</a>
            <a ${getPlatformLinkAttrs(ch, 'amazon', 'Amazon Music')} class="ch-plat-icon-3d amazon">${SVG_ICONS.amazon}</a>
            <a ${getPlatformLinkAttrs(ch, 'youtube', 'YouTube Oficial')} class="ch-plat-icon-3d youtube">${SVG_ICONS.youtube}</a>
          </div>
        `;
        tracksContainer.innerHTML = ch.playlist.map((trk, idx) => {
          const ytAttrs = trk.youtubeUrl
            ? `href="${trk.youtubeUrl}" target="_blank" rel="noopener" title="Assistir Clipe Oficial no YouTube"`
            : getPlatformLinkAttrs(ch, 'youtube', 'Assistir no YouTube Oficial');
          return `
          <div class="ch-track-card" data-ch-id="${ch.id}" data-trk-idx="${idx}">
            <div>
              <div class="ch-track-raw-thumb-wrap">
                <img src="${trk.rawImg || ch.bannerImg}" alt="${trk.title}" loading="lazy">
                <span class="ch-track-style-chip">${trk.style || ch.badgeText}</span>
              </div>
              <div class="ch-track-body">
                <div>
                  <h3 class="ch-track-title">${trk.title}</h3>
                  <p class="ch-track-story">${trk.story}</p>
                </div>
                <div class="ch-track-actions-stack" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
                  ${trk.isValidationCard ? `<span class="ch-validation-status-pill">&#9203; Em Processo de Validação &amp; Reivindicação</span>` : ''}
                  <div class="ch-pure-icons-row">
                    <a ${getPlatformLinkAttrs(ch, 'spotify', 'Ouvir no Spotify')} class="ch-plat-icon-3d spotify">
                      ${SVG_ICONS.spotify}
                    </a>
                    <a ${getPlatformLinkAttrs(ch, 'deezer', 'Ouvir no Deezer')} class="ch-plat-icon-3d deezer">
                      ${SVG_ICONS.deezer}
                    </a>
                    <a ${getPlatformLinkAttrs(ch, 'apple', 'Ouvir no Apple Music')} class="ch-plat-icon-3d apple">
                      ${SVG_ICONS.apple}
                    </a>
                    <a ${getPlatformLinkAttrs(ch, 'amazon', 'Ouvir no Amazon Music')} class="ch-plat-icon-3d amazon">
                      ${SVG_ICONS.amazon}
                    </a>
                    <a ${ytAttrs} class="ch-plat-icon-3d youtube">
                      ${SVG_ICONS.youtube}
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          `;
        }).join('');
      } else {
        const epList = ch.episodes || [];
        tracksContainer.classList.toggle('single-card-mode', epList.length === 1);
        repTitle.textContent = `Episódios & Produções de ${ch.name}`;
        if (repSub) {
          repSub.textContent = 'Cenas originais em alta definição — clique no símbolo 3D do YouTube para assistir no canal oficial.';
        }
        repRightAction.innerHTML = ch.links.youtube ? `
          <div class="ch-pure-icons-row">
            <a href="${ch.links.youtube}/videos" target="_blank" rel="noopener" class="ch-plat-icon-3d youtube" title="Ver Vídeos no YouTube Oficial">
              ${SVG_ICONS.youtube}
            </a>
          </div>
        ` : '';
        tracksContainer.innerHTML = epList.map((ep) => `
          <div class="ch-track-card">
            <div>
              <div class="ch-track-raw-thumb-wrap">
                <img src="${ep.rawImg || ch.bannerImg}" alt="${ep.title}" loading="lazy">
                <span class="ch-track-style-chip">${ep.style || ch.badgeText}</span>
              </div>
              <div class="ch-track-body">
                <div>
                  <h3 class="ch-track-title">${ep.title}</h3>
                  <p class="ch-track-story">${ep.story}</p>
                </div>
                <div class="ch-track-actions-stack" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
                  ${ep.isComingSoon ? `<span class="ch-validation-status-pill">&#9203; Em Processo de Validação &amp; Estreia</span>` : ''}
                  <div class="ch-pure-icons-row">
                    <a href="${ep.isComingSoon ? (ch.links.youtube || '#') : ep.url}" target="_blank" rel="noopener" class="ch-plat-icon-3d youtube" title="Canal Oficial no YouTube">
                      ${SVG_ICONS.youtube}
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        `).join('');
      }

      /* SEÇÃO 3B: Loja Oficial Exclusiva Deste Canal */
      renderChannelStore(ch);

      /* SEÇÃO 4: O Que Movimenta Este Universo (Pilares Temáticos) */
      const loreContainer = document.getElementById('portal-lore-container');
      loreContainer.innerHTML = (ch.loreBoxes || []).map(b => `
        <div class="ch-neon-pillar-card">
          <div class="ch-neon-pillar-tag">${b.tag}</div>
          <h3 class="ch-neon-pillar-title">${b.title}</h3>
          <p class="ch-neon-pillar-text">${b.text}</p>
        </div>
      `).join('');

      /* SEÇÃO 5: Produção de Estúdio, Estética Visual & Experiência */
      const prodContainer = document.getElementById('portal-production-container');
      if (prodContainer) {
        const prodCards = ch.hasMusic ? [
          {
            tag: 'ENGENHARIA DE ÁUDIO & ARRANJO',
            title: 'Produção Musical de Estúdio',
            text: `Cada faixa de ${ch.name} passa por composição autoral detalhada, mixagem com espacialidade 3D e masterização para entregar máxima nitidez tanto nos fones de ouvido quanto no som automotivo ou na TV da sala.`
          },
          {
            tag: 'DIREÇÃO DE ARTE & CINEMA DIGITAL',
            title: 'Identidade Visual & Cenários 8K',
            text: `Os videoclipes e artes originais de ${ch.name} utilizam iluminação dramática, cenários tridimensionais livres de poluição visual e narrativa cinematográfica fiel à essência do canal.`
          },
          {
            tag: 'EXPERIÊNCIA DO OUVINTE',
            title: 'Quando & Onde Ouvir',
            text: `Disponível nas principais plataformas globais de streaming (Spotify, Deezer, Apple Music, Amazon Music e YouTube) para acompanhar sua rotina diária.`
          }
        ] : [
          {
            tag: 'ROTEIRO & NARRATIVA ORIGINAL',
            title: 'Rigor Editorial & Imersão',
            text: `Cada produção de ${ch.name} é desenvolvida com pesquisa cuidadosa, locução envolvente e ritmo pensado para entregar conteúdo relevante, edificante e memorável.`
          },
          {
            tag: 'DIREÇÃO DE ARTE 8K & 3D',
            title: 'Cenários Originais de Cinema',
            text: `Utilizamos modelagem e direção visual em altíssima definição para dar vida a cada cena, criando uma atmosfera única para quem assiste pelo celular, computador ou Smart TV.`
          },
          {
            tag: 'EXPERIÊNCIA DO ESPECTADOR',
            title: 'Feito Para Acompanhar Você',
            text: `Episódios estruturados para assistir individualmente ou em família, com acesso gratuito e direto pelo canal oficial de ${ch.name} no YouTube.`
          }
        ];
        prodContainer.innerHTML = prodCards.map(c => `
          <div class="ch-neon-pillar-card">
            <div class="ch-neon-pillar-tag">${c.tag}</div>
            <h3 class="ch-neon-pillar-title">${c.title}</h3>
            <p class="ch-neon-pillar-text">${c.text}</p>
          </div>
        `).join('');
      }

      /* SEÇÃO 6: Guia do Público & Perguntas Frequentes */
      const faqContainer = document.getElementById('portal-faq-container');
      if (faqContainer) {
        const faqItems = ch.hasMusic ? [
          {
            tag: 'STREAMING & PLATAFORMAS',
            title: `Onde posso ouvir as músicas de ${ch.name}?`,
            text: `Clique nos símbolos 3D de cada faixa para ouvir o catálogo completo diretamente no Spotify, Deezer, Apple Music, Amazon Music e no canal oficial do YouTube.`
          },
          {
            tag: 'NOVOS LANÇAMENTOS',
            title: 'Como saber quando sai música ou clipe novo?',
            text: `Inscreva-se no canal oficial de ${ch.name} no YouTube e cadastre seu WhatsApp no Portal Vórtice Mídia para receber o aviso assim que um novo lançamento estrear.`
          },
          {
            tag: 'USO PELO PÚBLICO',
            title: 'Posso compartilhar os vídeos e playlists com amigos e família?',
            text: `Sim! Todas as músicas e videoclipes oficiais foram criados para serem compartilhados livremente em grupos de família, redes sociais e momentos especiais.`
          },
          {
            tag: 'ECOSSISTEMA VÓRTICE MÍDIA',
            title: 'Como funciona a Rádio Vórtice no canto superior da tela?',
            text: `A placa Mercosul da Rádio Vórtice no canto superior direito toca uma seleção especial das principais faixas da Vórtice Mídia enquanto você navega pelo portal.`
          }
        ] : [
          {
            tag: 'ACESSO AOS EPISÓDIOS',
            title: `Onde assistir aos vídeos completos de ${ch.name}?`,
            text: `Todos os episódios longos e séries completas estão disponíveis gratuitamente no canal oficial de ${ch.name} no YouTube — basta clicar no botão "Assistir Episódio no YouTube" em qualquer card acima.`
          },
          {
            tag: 'NOVOS EPISÓDIOS',
            title: 'Como acompanhar as próximas estreias do canal?',
            text: `Inscreva-se no YouTube oficial de ${ch.name} ativando o sininho de notificações e cadastre seu WhatsApp na página inicial da Vórtice Mídia.`
          },
          {
            tag: 'CONTEÚDO SEGURO & FAMILIAR',
            title: 'Os vídeos podem ser assistidos na Smart TV da sala?',
            text: `Sim! Todos os episódios de ${ch.name} são masterizados em alta definição widescreen (16:9), ideais para assistir na TV da sala, no celular ou no computador.`
          },
          {
            tag: 'PRODUÇÃO ORIGINAL VÓRTICE',
            title: `Qual é a proposta editorial de ${ch.name}?`,
            text: `${ch.name} integra os 10 universos originais da Vórtice Mídia, unindo direção visual cinematográfica, roteiro autoral e valores sólidos em cada vídeo publicado.`
          }
        ];
        faqContainer.innerHTML = faqItems.map(f => `
          <div class="ch-neon-pillar-card">
            <div class="ch-neon-pillar-tag">${f.tag}</div>
            <h3 class="ch-neon-pillar-title">${f.title}</h3>
            <p class="ch-neon-pillar-text">${f.text}</p>
          </div>
        `).join('');
      }

      /* SEÇÃO 7: Acesse o Canal nas Plataformas Oficiais (Placas de Trânsito 3D reais em movimento!) */
      const actionsContainer = document.getElementById('portal-actions-container');
      let buttonsHtml = '';

      if (ch.hasApp && ch.links.appOpenUrl) {
        buttonsHtml += `
          <a href="#em-breve" onclick="event.preventDefault(); alert('Em breve! O aplicativo Trono da Promessa Kids estará disponível em breve.');" class="social-road-sign" style="background-image:url('./assets/signs/sign_07_trono.png');--s-tilt:-7.2deg;--s-roty:17deg;--s-dx:15px;--s-delay:0.1s;">
            <div class="social-official-3d-badge badge-sp">
              <svg viewBox="0 0 24 24"><path d="M17 1.01L7 1c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-1.99-2-1.99zM17 19H7V5h10v14z"/></svg>
              <div class="social-badge-col">
                <span>APP KIDS</span>
                <span class="social-badge-sub">EM BREVE</span>
              </div>
            </div>
          </a>
        `;
      }

      if (ch.links.youtube) {
        buttonsHtml += `
          <a href="${ch.links.youtube}" target="_blank" rel="noopener" class="social-road-sign" style="background-image:url('./assets/signs/sign_01_rock.png');--s-tilt:7.5deg;--s-roty:-18deg;--s-dx:-16px;--s-delay:0s;">
            <div class="social-official-3d-badge badge-yt">
              ${SVG_ICONS.youtube}
              <div class="social-badge-col">
                <span>YOUTUBE</span>
                <span class="social-badge-sub">CANAL OFICIAL</span>
              </div>
            </div>
          </a>
        `;
      }

      if (ch.hasMusic) {
        const spSub = isPlatformClaimed(ch, 'spotify') ? 'OUVIR AGORA' : 'EM REIVINDICAÇÃO';
        const dzSub = isPlatformClaimed(ch, 'deezer') ? 'OUVIR AGORA' : 'EM REIVINDICAÇÃO';
        const apSub = isPlatformClaimed(ch, 'apple') ? 'LOSSLESS AUDIO' : 'EM REIVINDICAÇÃO';
        const amSub = isPlatformClaimed(ch, 'amazon') ? 'STREAMING HD' : 'EM REIVINDICAÇÃO';
        const ymSub = isPlatformClaimed(ch, 'ytmusic') ? 'FAIXAS OFICIAIS' : 'EM REIVINDICAÇÃO';

        buttonsHtml += `
          <a ${getPlatformLinkAttrs(ch, 'spotify')} class="social-road-sign" style="background-image:url('./assets/signs/sign_04_iago.png');--s-tilt:-7.0deg;--s-roty:16deg;--s-dx:15px;--s-delay:0.25s;">
            <div class="social-official-3d-badge badge-sp">
              ${SVG_ICONS.spotify}
              <div class="social-badge-col">
                <span>SPOTIFY</span>
                <span class="social-badge-sub">${spSub}</span>
              </div>
            </div>
          </a>
          <a ${getPlatformLinkAttrs(ch, 'deezer')} class="social-road-sign" style="background-image:url('./assets/signs/sign_10_aquario.png');--s-tilt:7.8deg;--s-roty:-18deg;--s-dx:-17px;--s-delay:0.5s;">
            <div class="social-official-3d-badge badge-dz">
              ${SVG_ICONS.deezer}
              <div class="social-badge-col">
                <span>DEEZER</span>
                <span class="social-badge-sub">${dzSub}</span>
              </div>
            </div>
          </a>
          <a ${getPlatformLinkAttrs(ch, 'apple')} class="social-road-sign" style="background-image:url('./assets/signs/sign_09_aliens.png');--s-tilt:-7.4deg;--s-roty:17deg;--s-dx:16px;--s-delay:0.75s;">
            <div class="social-official-3d-badge badge-ap">
              ${SVG_ICONS.apple}
              <div class="social-badge-col">
                <span>APPLE MUSIC</span>
                <span class="social-badge-sub">${apSub}</span>
              </div>
            </div>
          </a>
          <a ${getPlatformLinkAttrs(ch, 'amazon')} class="social-road-sign" style="background-image:url('./assets/signs/sign_07_trono.png');--s-tilt:6.8deg;--s-roty:-16deg;--s-dx:-15px;--s-delay:0.4s;">
            <div class="social-official-3d-badge badge-am">
              ${SVG_ICONS.amazon}
              <div class="social-badge-col">
                <span>AMAZON MUSIC</span>
                <span class="social-badge-sub">${amSub}</span>
              </div>
            </div>
          </a>
          <a ${getPlatformLinkAttrs(ch, 'ytmusic')} class="social-road-sign" style="background-image:url('./assets/signs/sign_05_patinhas.png');--s-tilt:-7.2deg;--s-roty:18deg;--s-dx:16px;--s-delay:0.65s;">
            <div class="social-official-3d-badge badge-ym">
              ${SVG_ICONS.ytmusic}
              <div class="social-badge-col">
                <span>YT MUSIC</span>
                <span class="social-badge-sub">${ymSub}</span>
              </div>
            </div>
          </a>
        `;
      }

      buttonsHtml += `
        <a ${getPlatformLinkAttrs(ch, 'instagram')} class="social-road-sign" style="background-image:url('./assets/signs/sign_02_sacronia.png');--s-tilt:7.1deg;--s-roty:-17deg;--s-dx:-15px;--s-delay:0.85s;">
          <div class="social-official-3d-badge badge-ig">
            ${SVG_ICONS.instagram}
            <div class="social-badge-col">
              <span>INSTAGRAM</span>
              <span class="social-badge-sub">EM REIVINDICAÇÃO</span>
            </div>
          </div>
        </a>
        <a ${getPlatformLinkAttrs(ch, 'tiktok')} class="social-road-sign" style="background-image:url('./assets/signs/sign_08_incorruptivel.png');--s-tilt:-7.6deg;--s-roty:18deg;--s-dx:16px;--s-delay:1.05s;">
          <div class="social-official-3d-badge badge-tk">
            ${SVG_ICONS.tiktok}
            <div class="social-badge-col">
              <span>TIKTOK</span>
              <span class="social-badge-sub">EM REIVINDICAÇÃO</span>
            </div>
          </div>
        </a>
      `;

      actionsContainer.innerHTML = buttonsHtml;
      portalOverlay.scrollTop = 0;
      document.body.classList.add('channel-view-active');
      portalOverlay.classList.add('open');
      refreshTop5UI(!inlineAudio.paused);
      history.replaceState(null, '', `#/${ch.id}`);
    }

    /* =========================================================================
       CATÁLOGO DA LOJA OFICIAL VÓRTICE MÍDIA + LOJA EXCLUSIVA DE CADA CANAL
       - Na Home (#loja-vortice): Vitrine Geral com filtro por categoria/linha
       - Dentro de cada Canal (#ch-sec-loja): 4 produtos específicos daquele universo
       ========================================================================= */
    const CHANNEL_STORE_CATALOG = {
      "rock-incorruptivel": [
            {
                  "asin": "B0HD8MW2J8",
                  "category": "Bandeira do Brasil de Mesa",
                  "title": "2 Bandeiras do Brasil em Poliéster para Decoração (150 Cm x 90 cm) Kit 2 Bandeiras Do Brasil)",
                  "img": "https://m.media-amazon.com/images/I/61I3zsS7uML._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HD8MW2J8?tag=vorticemidia-20"
            },
            {
                  "asin": "B0G837NXLX",
                  "category": "Bandeira do Brasil Oficial",
                  "title": "Kit Bandeira de Mesa Brasil e Rio Grande do Sul, Decorativa, Dupla Face, Multicolorido, 19x13cm, Bas...",
                  "img": "https://m.media-amazon.com/images/I/71Xizvj2NDL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0G837NXLX?tag=vorticemidia-20"
            },
            {
                  "asin": "B0HM434N7W",
                  "category": "Vestuário Patriota",
                  "title": "Camisa Masculina Patriota BRK Agro Bandeira Brasil Preta | Proteção Solar UV50+ com Zíper e Gola Padre",
                  "img": "https://m.media-amazon.com/images/I/61Snm+5Uf7L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HM434N7W?tag=vorticemidia-20"
            },
            {
                  "asin": "B0GPP8X9LC",
                  "category": "Acessório Patriota",
                  "title": "Boné Brasil Bandeira Brasileira Bordada Tático Militar Ajustável Aba Curva Patriota Nacional Alpha B...",
                  "img": "https://m.media-amazon.com/images/I/618BEYrLWVL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0GPP8X9LC?tag=vorticemidia-20"
            },
            {
                  "asin": "B0D2XRXNGY",
                  "category": "Fone de Ouvido Rock / Estúdio",
                  "title": "soundcore V20i da Anker, Fone de Ouvido Bluetooth Aberto e Esportivo, 36H | Bass Up, IP55, Luzes Led com sincronização de música Open Ear, Ganchos ajustáveis Ultraconfortáveis, Encaixe perfeito Clip On",
                  "img": "https://m.media-amazon.com/images/I/6181jAbkbOL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0D2XRXNGY?tag=vorticemidia-20"
            },
            {
                  "asin": "B0FK18FNYH",
                  "category": "Caixa de Som Bluetooth",
                  "title": "Caixa de Som Portátil JBL Boombox 4, Bluetooth, Branco | JBL Pro Sound, AI Sound Boost, 210W RMS, At...",
                  "img": "https://m.media-amazon.com/images/I/718KNSMkqJL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0FK18FNYH?tag=vorticemidia-20"
            },
            {
                  "asin": "B0H5W4474J",
                  "category": "Instrumentos & Guitarra",
                  "title": "38 Polegadas Guitarra Acústico com Cutaway Kit, Corpo de Violão em Tília | 6 Cordas de Nylon, com Af...",
                  "img": "https://m.media-amazon.com/images/I/71kLPRZ9FvL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0H5W4474J?tag=vorticemidia-20"
            },
            {
                  "asin": "B0G5L9T9C2",
                  "category": "Decoração Rock / Estúdio",
                  "title": "Placa Decorativa Lar Doce Lar com Gancho",
                  "img": "https://m.media-amazon.com/images/I/412mqc8iNBL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0G5L9T9C2?tag=vorticemidia-20"
            }
      ],
      "sacronia": [
            {
                  "asin": "6583509792",
                  "category": "Bíblia de Estudo King James",
                  "title": "Bíblia de Estudo King James 1611 | KJA 400 Anos | Full Collor | Capa Dura",
                  "img": "https://m.media-amazon.com/images/I/61EtgxaIWbL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6583509792?tag=vorticemidia-20"
            },
            {
                  "asin": "6552650272",
                  "category": "Bíblia de Estudo NVI / NAA",
                  "title": "Bíblia Solas Reformata",
                  "img": "https://m.media-amazon.com/images/I/81AisEw3RjL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6552650272?tag=vorticemidia-20"
            },
            {
                  "asin": "1680430009",
                  "category": "Devocional Clássico",
                  "title": "Dia a dia com Spurgeon - Devocional Diário - Luxo: Manhã e noite",
                  "img": "https://m.media-amazon.com/images/I/51DgwkHYiRL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/1680430009?tag=vorticemidia-20"
            },
            {
                  "asin": "857860184X",
                  "category": "Livro Cristão Best-Seller",
                  "title": "Cartas de um diabo a seu aprendiz",
                  "img": "https://m.media-amazon.com/images/I/91w74bA251L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/857860184X?tag=vorticemidia-20"
            },
            {
                  "asin": "0000188654",
                  "category": "Box / Teologia & História",
                  "title": "Coleção Grandes Sucesso de C.S. Lewis",
                  "img": "https://m.media-amazon.com/images/I/71YikhmqKKL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/0000188654?tag=vorticemidia-20"
            },
            {
                  "asin": "B087K9P25C",
                  "category": "Harpa & Hinário / Louvor",
                  "title": "Biblia Slim Harpa Grande Luxo (Vinho)",
                  "img": "https://m.media-amazon.com/images/I/51IS6QBXdeL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B087K9P25C?tag=vorticemidia-20"
            },
            {
                  "asin": "B0FGLZNB66",
                  "category": "Quadro Decorativo Sacro",
                  "title": "Kit 3 Quadro Decorativo Sala Quarto Leão Judá Nunca Foi Sorte Motivacional (15)",
                  "img": "https://m.media-amazon.com/images/I/61Hqd4xPh9L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0FGLZNB66?tag=vorticemidia-20"
            },
            {
                  "asin": "B09PSM4SHN",
                  "category": "Caneca Cristã Fé",
                  "title": "Caneca evangelica Salmos 23",
                  "img": "https://m.media-amazon.com/images/I/71iSu7rGn5L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B09PSM4SHN?tag=vorticemidia-20"
            }
      ],
      "neon-asher": [
            {
                  "asin": "B0B6P9J3J5",
                  "category": "Luminária LED / Neon Gamer",
                  "title": "Quntis Light Bar PRO+, Barra de Luz para Monitor com Controle Remoto, Compatível com Monitores Curvos e Planos, Proteção Ocular, Brilho Ajustável com Escurecimento Automático, Sem Reflexo",
                  "img": "https://m.media-amazon.com/images/I/61ZPUe0nvkL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0B6P9J3J5?tag=vorticemidia-20"
            },
            {
                  "asin": "B0FCB2VKVR",
                  "category": "Headphone Over-Ear",
                  "title": "Basike Fone de Ouvido Bluetooth, ANC Cancelamento de Ruído, LE29 (Rosa) | Headphone com Bluetooth 5.4, Headset com Microfone, Certificação Hi-Res Audio, 30 horas reprodução, Carregamento USB-C",
                  "img": "https://m.media-amazon.com/images/I/51n+edKvBPL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0FCB2VKVR?tag=vorticemidia-20"
            },
            {
                  "asin": "B0H7MR969P",
                  "category": "Violino Acústico Clássico",
                  "title": "VEDO Conjunto de Violino 4/4 Tamanho Normal Fosco | Adequado para Iniciantes e Adultos, Inclui Estoj...",
                  "img": "https://m.media-amazon.com/images/I/712FpgIjTzL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0H7MR969P?tag=vorticemidia-20"
            },
            {
                  "asin": "B0H5WQPQXR",
                  "category": "Caneca Preta Fosca",
                  "title": "Caneca Térmica 360ml Aço Inoxidável com Tampa Hermética Antivazamento Quente e Gelado (Preto)",
                  "img": "https://m.media-amazon.com/images/I/61IrDWv-nfL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0H5WQPQXR?tag=vorticemidia-20"
            },
            {
                  "asin": "B09JG62KDJ",
                  "category": "Microfone Condensador USB",
                  "title": "FIFINE A6V Microfone USB Para Jogos Para PS5 PC Para Twitch Podcasts | Microfone Condensador Com Mud...",
                  "img": "https://m.media-amazon.com/images/I/61ciiEJ7HRL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B09JG62KDJ?tag=vorticemidia-20"
            }
      ],
      "iago-cordeiro": [
            {
                  "asin": "6552650272",
                  "category": "Bíblia da Família Letra Gigante",
                  "title": "Bíblia Solas Reformata",
                  "img": "https://m.media-amazon.com/images/I/81AisEw3RjL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6552650272?tag=vorticemidia-20"
            },
            {
                  "asin": "6555843179",
                  "category": "Devocional Café com Deus Pai",
                  "title": "Café com Deus Pai - Teens",
                  "img": "https://m.media-amazon.com/images/I/51mcGQ8D0dL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6555843179?tag=vorticemidia-20"
            },
            {
                  "asin": "B0GNBBDJ4Q",
                  "category": "Diário / Caderno de Oração",
                  "title": "Caderno Devocional Em Sintonia com Deus | Diário de Oração e Reflexão - Capa Dura, 238 páginas, Pape...",
                  "img": "https://m.media-amazon.com/images/I/61MT-osDF+L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0GNBBDJ4Q?tag=vorticemidia-20"
            },
            {
                  "asin": "6552174721",
                  "category": "Livro Casamento & Família",
                  "title": "As Cinco Linguagens do Amor Contadas às Crianças, Gary Chapman - Thomas Nelson",
                  "img": "https://m.media-amazon.com/images/I/71UB-2RliyL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6552174721?tag=vorticemidia-20"
            },
            {
                  "asin": "B079ZJMZCS",
                  "category": "Violão Sertanejo / Louvor",
                  "title": "Violão Eletroacústico Dreadnought Folk Cutaway Aço GF-1D CEQ Translucent",
                  "img": "https://m.media-amazon.com/images/I/51X2uc9iU+L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B079ZJMZCS?tag=vorticemidia-20"
            },
            {
                  "asin": "B087K9P25C",
                  "category": "Harpa & Hinário / Louvor",
                  "title": "Biblia Slim Harpa Grande Luxo (Vinho)",
                  "img": "https://m.media-amazon.com/images/I/51IS6QBXdeL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B087K9P25C?tag=vorticemidia-20"
            },
            {
                  "asin": "1680430009",
                  "category": "Devocional Clássico",
                  "title": "Dia a dia com Spurgeon - Devocional Diário - Luxo: Manhã e noite",
                  "img": "https://m.media-amazon.com/images/I/51DgwkHYiRL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/1680430009?tag=vorticemidia-20"
            },
            {
                  "asin": "6584956393",
                  "category": "Clássico Cristão — Edição de Luxo",
                  "title": "Confissões de Santo Agostinho - Edição de Luxo Almofadada",
                  "img": "https://m.media-amazon.com/images/I/91mYAMQ785L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6584956393?tag=vorticemidia-20"
            }
      ],
      "patinhas-e-cancoes": [
            {
                  "asin": "B0HFQ53P8M",
                  "category": "Caminha Pet Nuvem Macia",
                  "title": "Cama Pet Sofá Gigante 120x80cm Cachorro Porte Grande Lavável Borda Alta Confortável Marrom",
                  "img": "https://m.media-amazon.com/images/I/61h+9ewmAUL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HFQ53P8M?tag=vorticemidia-20"
            },
            {
                  "asin": "B07KCLC6J3",
                  "category": "Fonte Bebedouro Água Pet",
                  "title": "Fonte Bebedouro de Água Portátil Amicus 1,2L para Gatos e Cães",
                  "img": "https://m.media-amazon.com/images/I/71gUUBWN9SL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B07KCLC6J3?tag=vorticemidia-20"
            },
            {
                  "asin": "B0H4HTZGRF",
                  "category": "Comedouro Automático / Duplo",
                  "title": "Mordedor Center Cut Branqueado Bovino PETSKO 100% Natural Para Cães - 2 Unidades",
                  "img": "https://m.media-amazon.com/images/I/61iQq3+quCL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0H4HTZGRF?tag=vorticemidia-20"
            },
            {
                  "asin": "B0FPBV6GN2",
                  "category": "Peitoral & Guia Passeio",
                  "title": "Peitoral H para Cães, Antipuxão com 2 Pontos de Engate, Ajustável Tamanhos P/M/G, para Passeio e Ade...",
                  "img": "https://m.media-amazon.com/images/I/71qo1OtVhTL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0FPBV6GN2?tag=vorticemidia-20"
            },
            {
                  "asin": "B0HGMDBSQ1",
                  "category": "Tapete Higiênico / Impermeável",
                  "title": "Tapete Higiênico para Cães Mozão Aroma Neutro 50x60cm 30 Unidades 6 Camadas Super Absorvente com Gel Anti Vazamento e Controle de Odores - TOICE",
                  "img": "https://m.media-amazon.com/images/I/61YkQKdS6BL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HGMDBSQ1?tag=vorticemidia-20"
            },
            {
                  "asin": "B0795T91YP",
                  "category": "Arranhador Torre para Gatos",
                  "title": "Feandrea Árvore para Gatos, 84 cm, Tamanho G, para Gatos Grandes até 7 kg, Poleiro Amplo, 2 Tocas, Poste Arranhador, Cinza Claro BRPCT61WV2",
                  "img": "https://m.media-amazon.com/images/I/81Jo-RtW8RL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0795T91YP?tag=vorticemidia-20"
            },
            {
                  "asin": "B07YBNLXH6",
                  "category": "Brinquedo Interativo Cães",
                  "title": "Mordedor Pet Games Monstrinho Azul, Tamanho Médio",
                  "img": "https://m.media-amazon.com/images/I/71CnYh8YNNL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B07YBNLXH6?tag=vorticemidia-20"
            },
            {
                  "asin": "B0CKT43D9Q",
                  "category": "Mochila / Bolsa Transporte Pet",
                  "title": "Bolsa Transporte Pet Ventilação em 4 lados 42 * 26 * 27 cm Não Se Deforma Facilmente Bolsa Transport...",
                  "img": "https://m.media-amazon.com/images/I/71TsGRxSLVL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0CKT43D9Q?tag=vorticemidia-20"
            }
      ],
      "aguas-de-descanso": [
            {
                  "asin": "B0HKLPW4VJ",
                  "category": "Difusor de Aromas Ultrassônico",
                  "title": "Umidificador de Ar Difusor de Ambiente Ultrassônico 700ml LED | Aromas Óleo Essencial com Controle R...",
                  "img": "https://m.media-amazon.com/images/I/613g5n0gTwL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HKLPW4VJ?tag=vorticemidia-20"
            },
            {
                  "asin": "B0CM4NT481",
                  "category": "Kit Óleos Essenciais Lavanda",
                  "title": "Óleo de Rosa Mosqueta - Puro, Uniformizador, Hidratante e Antioxidante - Para Manchas, Rugas, Estrias e Melhor Elasticidade - Uso Facial, Oleo Corporal e Cabelos - 100% Pura Natural Vegano - 30 mL Beauts",
                  "img": "https://m.media-amazon.com/images/I/81IHn4DCtnL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0CM4NT481?tag=vorticemidia-20"
            },
            {
                  "asin": "655265040X",
                  "category": "Bíblia Salmos Letra Gigante",
                  "title": "Bíblia Trindade - Marrom - Heziom - Letra Grande",
                  "img": "https://m.media-amazon.com/images/I/81DYHIHkrlL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/655265040X?tag=vorticemidia-20"
            },
            {
                  "asin": "B0C3Q7152B",
                  "category": "Luminária Lua Cheia Cabeceira",
                  "title": "Luminatti by Danuri Luminária Pixar E27 30W - Preto | Articulada de Mesa para Escritório, Estudo, Le...",
                  "img": "https://m.media-amazon.com/images/I/51dh3ERsgdL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0C3Q7152B?tag=vorticemidia-20"
            },
            {
                  "asin": "B0HG6HT49F",
                  "category": "Chá Relaxante / Infusor",
                  "title": "Garrafa Térmica 2000ml Aço Inoxidável com Alça e Canudo - Preto | Bico Duplo, Gancho Incluso, Capacidade 2L, Tampa com Trava, Uso Esportivo",
                  "img": "https://m.media-amazon.com/images/I/71s0y7YgSZL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HG6HT49F?tag=vorticemidia-20"
            },
            {
                  "asin": "B0CRGR2TS5",
                  "category": "Máscara de Dormir Conforto",
                  "title": "soundcore Sleep A20 da Anker Fone para Dormir Bluetooth 5.3 Antirruído ANC | 80H, Conforto Superior , Compacto e Confortável para Dormir de Lado, Áudio com IA, Monitor de Sono e Alarme Personalizado",
                  "img": "https://m.media-amazon.com/images/I/418EcYAOCbL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0CRGR2TS5?tag=vorticemidia-20"
            },
            {
                  "asin": "B0GH17SBYW",
                  "category": "Travesseiro Nasa / Ortopédico",
                  "title": "TOKE DIN DON 1 Kit Travesseiro Nasa de Verdade Viscoelástico Ajustável | Antialérgico, com Capa 50x7...",
                  "img": "https://m.media-amazon.com/images/I/717sedux3SL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0GH17SBYW?tag=vorticemidia-20"
            },
            {
                  "asin": "B0HCDQBVHB",
                  "category": "Caixa de Som Ruído Branco",
                  "title": "Aparelho Ruído Branco Bebês e Adultos com Luz Noturna, Sons Relaxantes Sono | Maquina de som 20 son...",
                  "img": "https://m.media-amazon.com/images/I/616Re1xmAaL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HCDQBVHB?tag=vorticemidia-20"
            }
      ],
      "trono-da-promessa": [
            {
                  "asin": "655217201X",
                  "category": "Bíblia Infantil Ilustrada",
                  "title": "Bíblia Aventura para crianças NVI, Capa dura com fechamento em ímã, Leão, Leitura Perfeita",
                  "img": "https://m.media-amazon.com/images/I/81azmSNhAuL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/655217201X?tag=vorticemidia-20"
            },
            {
                  "asin": "8595200629",
                  "category": "365 Histórias Bíblicas",
                  "title": "365 Historias Bíblicas",
                  "img": "https://m.media-amazon.com/images/I/81m74G-S1fL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8595200629?tag=vorticemidia-20"
            },
            {
                  "asin": "6555001992",
                  "category": "Livros de Colorir Cristão Kids",
                  "title": "365 Desenhos da Bíblia para colorir",
                  "img": "https://m.media-amazon.com/images/I/71mfwkzNXHL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6555001992?tag=vorticemidia-20"
            },
            {
                  "asin": "B0G2SWWR5V",
                  "category": "Pelúcia Ovelhinha / Leãozinho",
                  "title": "LEGO Creator 3 em 1 Animais da Floresta: Lobo-cinzento; Brinquedo 31393",
                  "img": "https://m.media-amazon.com/images/I/81HF3FdNjyL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0G2SWWR5V?tag=vorticemidia-20"
            },
            {
                  "asin": "B077PLFYWF",
                  "category": "Jogo Educativo Família",
                  "title": "Jogo Imagem e Ação 2 Grow, Multicor",
                  "img": "https://m.media-amazon.com/images/I/51XF78npGsL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B077PLFYWF?tag=vorticemidia-20"
            },
            {
                  "asin": "B0DSXYB3PD",
                  "category": "Projetor de Estrelas Quarto Kids",
                  "title": "Projetor Luminaria de luz da galáxia do astronauta Luz Noturna LED com Céu Estrelado, Aurora, Contro...",
                  "img": "https://m.media-amazon.com/images/I/61WQ7fpHs1L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0DSXYB3PD?tag=vorticemidia-20"
            },
            {
                  "asin": "B0G2T4739R",
                  "category": "Blocos de Montar Criativos",
                  "title": "LEGO NINJAGO Pack de Combate Dragão Meca do Lloyd 71862 | Brinquedos De Construção, Meninos E Meninas, Anos 6+, Figuras De Ação, 3 Minifiguras, 81 Peças",
                  "img": "https://m.media-amazon.com/images/I/81zcdle7-cL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0G2T4739R?tag=vorticemidia-20"
            },
            {
                  "asin": "B0FXZVDG74",
                  "category": "Garrafinha Infantil Escola",
                  "title": "MODUS Garrafa Térmica Esportiva De Inox Com Isolamento A Vácuo 950ML | Azul",
                  "img": "https://m.media-amazon.com/images/I/61AWuRvjq+L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0FXZVDG74?tag=vorticemidia-20"
            }
      ],
      "incorruptivel": [
            {
                  "asin": "8501402516",
                  "category": "Olavo de Carvalho — Best-Seller",
                  "title": "O mínimo que você precisa saber para não ser um idiota — Olavo de Carvalho",
                  "img": "https://m.media-amazon.com/images/I/718qyVMPR7L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8501402516?tag=vorticemidia-20"
            },
            {
                  "asin": "6587138691",
                  "category": "Olavo de Carvalho — Clássico",
                  "title": "O Imbecil Coletivo — Atualidades inculturais brasileiras (Olavo de Carvalho)",
                  "img": "https://m.media-amazon.com/images/I/71g22PdHYrL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6587138691?tag=vorticemidia-20"
            },
            {
                  "asin": "8567394511",
                  "category": "Olavo de Carvalho — Filosofia",
                  "title": "O Jardim das Aflições — Olavo de Carvalho",
                  "img": "https://m.media-amazon.com/images/I/619dC2skyQL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8567394511?tag=vorticemidia-20"
            },
            {
                  "asin": "8595074186",
                  "category": "Olavo de Carvalho — Antologia",
                  "title": "O Essencial de Olavo de Carvalho",
                  "img": "https://m.media-amazon.com/images/I/51d7QNeh8gL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8595074186?tag=vorticemidia-20"
            },
            {
                  "asin": "8567394260",
                  "category": "Olavo de Carvalho — Cultura & Política",
                  "title": "A Nova Era e a Revolução Cultural: Fritjof Capra e Antonio Gramsci — Olavo de Carvalho",
                  "img": "https://m.media-amazon.com/images/I/51AqekpukSL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8567394260?tag=vorticemidia-20"
            },
            {
                  "asin": "8595071217",
                  "category": "Olavo de Carvalho — Geopolítica",
                  "title": "O Foro de São Paulo: A ascensão do comunismo latino-americano — Olavo de Carvalho",
                  "img": "https://m.media-amazon.com/images/I/61IW0oP4b4L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8595071217?tag=vorticemidia-20"
            },
            {
                  "asin": "8593751253",
                  "category": "As Seis Lições - Mises",
                  "title": "As seis lições",
                  "img": "https://m.media-amazon.com/images/I/71M-fsD472L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8593751253?tag=vorticemidia-20"
            },
            {
                  "asin": "6586029724",
                  "category": "O Caminho da Servidão - Hayek",
                  "title": "O caminho da servidão: 2ª Edição",
                  "img": "https://m.media-amazon.com/images/I/61XgkB3IDBL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6586029724?tag=vorticemidia-20"
            },
            {
                  "asin": "8562409715",
                  "category": "A Lei - Frédéric Bastiat",
                  "title": "A lei: por que a esquerda não funciona",
                  "img": "https://m.media-amazon.com/images/I/81l+1yVENCL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8562409715?tag=vorticemidia-20"
            },
            {
                  "asin": "B08ZK6N3XZ",
                  "category": "1984 - George Orwell (Edição Especial)",
                  "title": "As obras revolucionárias de George Orwell - Box com 3 livros",
                  "img": "https://m.media-amazon.com/images/I/61F-KPiT4KL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B08ZK6N3XZ?tag=vorticemidia-20"
            },
            {
                  "asin": "B0HD8MW2J8",
                  "category": "Bandeira do Brasil de Mesa",
                  "title": "2 Bandeiras do Brasil em Poliéster para Decoração (150 Cm x 90 cm) Kit 2 Bandeiras Do Brasil)",
                  "img": "https://m.media-amazon.com/images/I/61I3zsS7uML._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HD8MW2J8?tag=vorticemidia-20"
            }
      ],
      "aliens-da-biblia": [
            {
                  "asin": "6559579611",
                  "category": "O Livro de Enoque",
                  "title": "O livro de Enoque: Inclui – O testamento de Salomão",
                  "img": "https://m.media-amazon.com/images/I/71XC87bA64L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6559579611?tag=vorticemidia-20"
            },
            {
                  "asin": "6555393971",
                  "category": "Eram os Deuses Astronautas",
                  "title": "Eram os deuses astronautas? (Edição comemorativa - 50 anos)",
                  "img": "https://m.media-amazon.com/images/I/71-OO+glHtL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6555393971?tag=vorticemidia-20"
            },
            {
                  "asin": "6552650272",
                  "category": "Bíblia de Estudo Arqueológica",
                  "title": "Bíblia Solas Reformata",
                  "img": "https://m.media-amazon.com/images/I/81AisEw3RjL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/6552650272?tag=vorticemidia-20"
            },
            {
                  "asin": "8537642673",
                  "category": "Atlas Histórico da Bíblia",
                  "title": "Atlas Bíblico Ilustrado",
                  "img": "https://m.media-amazon.com/images/I/71t3RjohqaL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8537642673?tag=vorticemidia-20"
            },
            {
                  "asin": "B0HK1HQTBP",
                  "category": "Telescópio / Luneta Astronômica",
                  "title": "Kit Telescópio e Microscópio Infantil 2 em 1 com Tripé | Ampliação até 450x, A partir de 8 anos, Mat...",
                  "img": "https://m.media-amazon.com/images/I/61S2W7rFcuL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HK1HQTBP?tag=vorticemidia-20"
            },
            {
                  "asin": "B0H7NSWW95",
                  "category": "Luminária Projetor Galáxia",
                  "title": "Projetor Astronauta Galáxia com Nebulosa e Estrelas | Controle Remoto, Timer, Cabeça Ajustável, Luz ...",
                  "img": "https://m.media-amazon.com/images/I/61mFMGAtNiL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0H7NSWW95?tag=vorticemidia-20"
            },
            {
                  "asin": "B076H4QDNN",
                  "category": "Globo Terrestre Iluminado",
                  "title": "Globo Terrestre Studio Politico, ProCalc, Multicor",
                  "img": "https://m.media-amazon.com/images/I/61OHQBgOMoL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B076H4QDNN?tag=vorticemidia-20"
            },
            {
                  "asin": "8572441786",
                  "category": "Livro Mistérios da Antiguidade",
                  "title": "As primeiras civilizações",
                  "img": "https://m.media-amazon.com/images/I/71jk7fDJINL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/8572441786?tag=vorticemidia-20"
            }
      ],
      "aquario-dos-felinos": [
            {
                  "asin": "B0795T91YP",
                  "category": "Arranhador Torre para Gatos",
                  "title": "Feandrea Árvore para Gatos, 84 cm, Tamanho G, para Gatos Grandes até 7 kg, Poleiro Amplo, 2 Tocas, Poste Arranhador, Cinza Claro BRPCT61WV2",
                  "img": "https://m.media-amazon.com/images/I/81Jo-RtW8RL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0795T91YP?tag=vorticemidia-20"
            },
            {
                  "asin": "B07KCLC6J3",
                  "category": "Fonte de Água Inox para Gatos",
                  "title": "Fonte Bebedouro de Água Portátil Amicus 1,2L para Gatos e Cães",
                  "img": "https://m.media-amazon.com/images/I/71gUUBWN9SL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B07KCLC6J3?tag=vorticemidia-20"
            },
            {
                  "asin": "B0HH5TJNV6",
                  "category": "Brinquedo Peixe Elétrico / Interativo",
                  "title": "Bola Interativa para Gatos Automática com Movimento e Cordão | Brinquedo interativo com movimento qu...",
                  "img": "https://m.media-amazon.com/images/I/51a49NUqjOL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0HH5TJNV6?tag=vorticemidia-20"
            },
            {
                  "asin": "B0H4HP5XPW",
                  "category": "Túnel Dobrável para Gatos",
                  "title": "Tunel para Gatos em Poliester Colorido Formato T | Uso recomendado para interacao de pets combater o...",
                  "img": "https://m.media-amazon.com/images/I/51tjuK9s-VL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0H4HP5XPW?tag=vorticemidia-20"
            },
            {
                  "asin": "B0GS7MBF5C",
                  "category": "Rede de Janela para Gatos",
                  "title": "Caminha Suspensa para Gatos com Ventosas | Cama de Janela para Gato | Rede para Janela Super Resiste...",
                  "img": "https://m.media-amazon.com/images/I/418fEAmfw+L._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0GS7MBF5C?tag=vorticemidia-20"
            },
            {
                  "asin": "B0H2XL7SL7",
                  "category": "Caixa de Areia Fechada / Furba",
                  "title": "Caixa de Areia Fechada para Gatos, Aço Inoxidável, Extra Grande, 62x38x34cm | Três formas de uso",
                  "img": "https://m.media-amazon.com/images/I/71pkJ59BIKL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0H2XL7SL7?tag=vorticemidia-20"
            },
            {
                  "asin": "B0G4HLLKP7",
                  "category": "Varinha com Penas e Guizo",
                  "title": "Kit 3 Brinquedo Gato Varinha Pássaro Com Ventosa Fixa Chao Parede Janela Bolinha Catnip",
                  "img": "https://m.media-amazon.com/images/I/51NLJWfycvL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0G4HLLKP7?tag=vorticemidia-20"
            },
            {
                  "asin": "B0DS6HFWKQ",
                  "category": "Caneca Gateiros / Gatinho",
                  "title": "Caneca de Gato Fofa 325ml | Presente Criativo para Quem Ama Gatos | Caneca Engraçada para Café | Ide...",
                  "img": "https://m.media-amazon.com/images/I/61rvZDSGVOL._AC_UL600_.jpg",
                  "url": "https://www.amazon.com.br/dp/B0DS6HFWKQ?tag=vorticemidia-20"
            }
      ]
};

    function trackStoreProductClick(prodTitle, chId, chName, url) {
      try {
        fetch('https://vortice-cloud-bot.onrender.com/api/site/track', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            type: 'click',
            channel: chId || 'loja-amazon',
            label: '🛒 Amazon (' + (chName || 'Loja') + '): ' + prodTitle,
            path: window.location.pathname
          }),
          keepalive: true
        }).catch(() => {});
      } catch (e) {}
      if (url) {
        window.open(url, '_blank', 'noopener,noreferrer');
      }
    }

    function openChannelStoreDirect(chId) {
      openChannelById(chId);
      setTimeout(() => {
        const storeSec = document.getElementById('ch-sec-loja');
        if (storeSec && portalOverlay) {
          portalOverlay.scrollTo({ top: storeSec.offsetTop - 20, behavior: 'smooth' });
        }
      }, 180);
    }

    function renderChannelStore(ch) {
      const storeTitle = document.getElementById('portal-store-title');
      const storeContainer = document.getElementById('portal-store-container');
      if (!storeContainer) return;

      if (storeTitle) {
        storeTitle.textContent = `Loja Oficial • ${ch.name}`;
      }

      const items = CHANNEL_STORE_CATALOG[ch.id] || CHANNEL_STORE_CATALOG['rock-incorruptivel'];
      storeContainer.innerHTML = items.map(prod => {
        const safeTitle = (prod.title || '').replace(/'/g, "\'").replace(/"/g, '&quot;');
        const safeChName = (ch.name || '').replace(/'/g, "\'").replace(/"/g, '&quot;');
        return `
        <div class="store-product-card">
          <div>
            <div class="store-prod-visual" onclick="trackStoreProductClick('${safeTitle}', '${ch.id}', '${safeChName}', '${prod.url}')" title="Ver oferta oficial na Amazon">
              <img src="${prod.img}" alt="${safeTitle}" class="store-prod-real-img" loading="lazy">
            </div>
            <div class="store-prod-body">
              <h3 class="store-prod-title">${prod.title}</h3>
            </div>
          </div>
          <div class="store-prod-actions">
            <a href="${prod.url}" target="_blank" rel="noopener noreferrer" class="store-btn-buy" onclick="trackStoreProductClick('${safeTitle}', '${ch.id}', '${safeChName}', '')">
              Ver Oferta na Amazon
            </a>
          </div>
        </div>
      `}).join('');
    }

    let storeConveyorPaused = false;
    let storeConveyorPos = 0;

    function renderHomeStoreConveyor() {
      const channelsBar = document.getElementById('home-store-channels-bar');
      const track = document.getElementById('vortice-home-store-track');
      const viewport = document.getElementById('home-store-conveyor-viewport');
      const wrap = document.getElementById('home-store-conveyor-wrap');
      if (!track || !viewport) return;

      /* Renderiza os 10 botões no topo para abrir direto a Loja de cada Canal */
      if (channelsBar) {
        channelsBar.innerHTML = VORTICE_CHANNELS.map(ch => `
          <button type="button" class="store-channel-ShortcutBtn" onclick="openChannelStoreDirect('${ch.id}')" title="Abrir Loja Oficial de ${ch.name}">
            <span>Loja ${ch.name}</span>
          </button>
        `).join('');
      }

      /* Junta todos os produtos de todos os canais na esteira intercalando para variedade máxima */
      const allProducts = [];
      const maxLen = Math.max(...VORTICE_CHANNELS.map(ch => (CHANNEL_STORE_CATALOG[ch.id] || []).length));
      for (let i = 0; i < maxLen; i++) {
        VORTICE_CHANNELS.forEach(ch => {
          const prods = CHANNEL_STORE_CATALOG[ch.id] || [];
          if (prods[i]) {
            allProducts.push({
              ...prods[i],
              chId: ch.id,
              chName: ch.name
            });
          }
        });
      }

      /* Duplica a lista na esteira para permitir rolagem infinita contínua */
      const loopList = [...allProducts, ...allProducts];

      track.innerHTML = loopList.map(prod => {
        const safeTitle = (prod.title || '').replace(/'/g, "\'").replace(/"/g, '&quot;');
        const safeChName = (prod.chName || '').replace(/'/g, "\'").replace(/"/g, '&quot;');
        return `
        <div class="store-product-card">
          <div>
            <div class="store-prod-visual" onclick="trackStoreProductClick('${safeTitle}', '${prod.chId}', '${safeChName}', '${prod.url}')" title="Ver oferta oficial na Amazon">
              <img src="${prod.img}" alt="${safeTitle}" class="store-prod-real-img" loading="lazy">
            </div>
            <div class="store-prod-body">
              <h3 class="store-prod-title">${prod.title}</h3>
            </div>
          </div>
          <div class="store-prod-actions">
            <a href="${prod.url}" target="_blank" rel="noopener noreferrer" class="store-btn-buy" onclick="trackStoreProductClick('${safeTitle}', '${prod.chId}', '${safeChName}', '')">
              Ver Oferta na Amazon
            </a>
            <button type="button" class="store-btn-channel" onclick="openChannelStoreDirect('${prod.chId}')" title="Ir para a Loja de ${safeChName}">
              Loja do Canal
            </button>
          </div>
        </div>
      `}).join('');

      if (wrap) {
        wrap.addEventListener('mouseenter', () => { storeConveyorPaused = true; });
        wrap.addEventListener('mouseleave', () => { storeConveyorPaused = false; });
        wrap.addEventListener('touchstart', () => { storeConveyorPaused = true; }, { passive: true });
        wrap.addEventListener('touchend', () => { storeConveyorPaused = false; }, { passive: true });
      }

      function stepConveyor() {
        if (!storeConveyorPaused && viewport && track.scrollWidth > 0) {
          storeConveyorPos += 0.85;
          const halfWidth = track.scrollWidth / 2;
          if (storeConveyorPos >= halfWidth) {
            storeConveyorPos -= halfWidth;
          }
          viewport.scrollLeft = storeConveyorPos;
        } else if (viewport) {
          storeConveyorPos = viewport.scrollLeft;
        }
        requestAnimationFrame(stepConveyor);
      }
      requestAnimationFrame(stepConveyor);
    }

    function scrollStoreConveyor(dir) {
      const viewport = document.getElementById('home-store-conveyor-viewport');
      const track = document.getElementById('vortice-home-store-track');
      if (!viewport || !track) return;
      const firstCard = track.querySelector('.store-product-card');
      const cardUnit = firstCard ? (firstCard.offsetWidth + 12) : 246;
      const halfWidth = track.scrollWidth / 2;
      const currentIdx = Math.round(viewport.scrollLeft / cardUnit);
      let target = (currentIdx + dir) * cardUnit;
      if (target < 0) target += halfWidth;
      if (target >= halfWidth) target -= halfWidth;
      storeConveyorPos = target;
      viewport.scrollTo({ left: target, behavior: 'smooth' });
    }

    renderHomeStoreConveyor();

    function closeChannelPortal() {
      portalOverlay.classList.remove('open');
      document.body.classList.remove('channel-view-active');
      if (window.location.hash.startsWith('#/')) {
        history.replaceState(null, '', window.location.pathname);
      }
    }

    window.addEventListener('load', () => {
      if (window.location.hash.startsWith('#/')) {
        openChannelById(window.location.hash.replace('#/', '').trim());
      }
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const claimOverlay = document.getElementById('platform-claim-overlay');
        if (claimOverlay && claimOverlay.classList.contains('open')) {
          closePlatformClaimPage();
        } else {
          closeChannelPortal();
        }
      }
    });

    /* =========================================================================
       MOTOR DO TORNADO 8K + ÓRBITA 3D FLUIDA 60 FPS (ZERO PIPOCOS / ZERO TRAVAMENTO!)
       - Sem saltos de colisão discretos e sem blur dinâmico pesado por frame!
       - Quando a placa vai lá para trás do tornado (depth próximo de -1), ela fica
         BEM MIUDINHA (scale 0.08) e APAGA lá atrás (opacity 0.01) antes de voltar crescendo!
       ========================================================================= */
    const canvas = document.getElementById('vortex-canvas');
    const ctx = canvas.getContext('2d');
    const bgImage = new Image();
    bgImage.src = './assets/tornado/tornado_dunes_8k.jpg';

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    const DUST_PARTICLES = Array.from({ length: 340 }, () => ({
      angle: Math.random() * Math.PI * 2,
      heightRatio: Math.random(),
      radiusOffset: (Math.random() - 0.5) * 140,
      speed: 0.014 + Math.random() * 0.028,
      size: 1.5 + Math.random() * 5.2,
      alpha: 0.18 + Math.random() * 0.55,
      isDebris: Math.random() > 0.45,
      debrisShape: Math.floor(Math.random() * 3)
    }));

    const SAND_STREAMS = Array.from({ length: 24 }, () => ({
      x: Math.random() * window.innerWidth,
      y: window.innerHeight * (0.38 + Math.random() * 0.58),
      length: 200 + Math.random() * 380,
      speed: 3.2 + Math.random() * 6.0,
      alpha: 0.04 + Math.random() * 0.11,
      thickness: 14 + Math.random() * 38
    }));

    let timeTick = 0;

    function animateScene() {
      timeTick += 0.016;
      const W = canvas.width;
      const H = canvas.height;

      ctx.clearRect(0, 0, W, H);
      const funnelCenterX = W * 0.52;

      if (bgImage.complete && bgImage.naturalWidth > 0) {
        const imgAspect = bgImage.naturalWidth / bgImage.naturalHeight;
        const winAspect = W / H;
        let drawW, drawH, startX, startY;

        if (winAspect > imgAspect) {
          drawW = W * 1.05;
          drawH = drawW / imgAspect;
        } else {
          drawH = H * 1.05;
          drawW = drawH * imgAspect;
        }
        startX = (W - drawW) / 2 + Math.sin(timeTick * 0.35) * 4;
        startY = (H - drawH) / 2 + Math.cos(timeTick * 0.25) * 3;

        ctx.drawImage(bgImage, startX, startY, drawW, drawH);
      }

      /* Destroços e poeira girando no tornado (sem fatias duplicadas com borda marcada!) */
      for (const p of DUST_PARTICLES) {
        p.angle += p.speed;
        p.heightRatio -= 0.0014;
        if (p.heightRatio < 0.05) p.heightRatio = 0.90;

        const y = H * (0.06 + p.heightRatio * 0.78);
        const coneRadius = (1 - p.heightRatio) * (W * 0.19) + Math.pow(p.heightRatio, 2.5) * (W * 0.11) + 28;
        const x = funnelCenterX + Math.cos(p.angle) * (coneRadius + p.radiusOffset);
        const zDepth = Math.sin(p.angle);

        ctx.save();
        if (p.isDebris) {
          ctx.fillStyle = `rgba(34, 26, 20, ${p.alpha * (0.50 + 0.50 * zDepth)})`;
          ctx.translate(x, y);
          ctx.rotate(p.angle * 3.6);
          if (p.debrisShape === 0) {
            ctx.fillRect(-p.size * 1.4, -p.size * 0.7, p.size * 2.8, p.size * 1.4);
          } else if (p.debrisShape === 1) {
            ctx.beginPath();
            ctx.moveTo(0, -p.size * 1.3);
            ctx.lineTo(p.size * 1.3, p.size * 0.9);
            ctx.lineTo(-p.size * 1.2, p.size * 0.7);
            ctx.closePath();
            ctx.fill();
          } else {
            ctx.fillRect(-p.size, -p.size, p.size * 1.8, p.size * 1.8);
          }
        } else {
          const grad = ctx.createRadialGradient(x, y, 0, x, y, p.size * 7.5);
          grad.addColorStop(0, `rgba(188, 155, 118, ${p.alpha * 0.28})`);
          grad.addColorStop(1, 'rgba(188, 155, 118, 0)');
          ctx.fillStyle = grad;
          ctx.beginPath();
          ctx.arc(x, y, p.size * 7.5, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.restore();
      }

      /* =======================================================================
         ÓRBITA 3D CONTÍNUA E SUAVE DAS 10 PLACAS + MODO ALINHADO AO CLICAR NA LOGO!
         - Se isGridAligned = false (gridBlend -> 0): gira em órbita 3D no tornado,
           ficando miudinha (scale 0.08) e apagando lá atrás (opacity 0.01).
         - Se isGridAligned = true (gridBlend -> 1): todas as 10 placas vêm rapidinho
           e ficam alinhadinhas de frente (grade 5x2 abaixo da logo) com leve flutuação!
         ======================================================================= */
      const targetBlend = isGridAligned ? 1.0 : 0.0;
      gridBlend += (targetBlend - gridBlend) * (isGridAligned ? 0.13 : 0.08);
      if (Math.abs(targetBlend - gridBlend) < 0.001) gridBlend = targetBlend;

      const orbitCenterX = W * 0.54;
      const orbitCenterY = H * 0.51;
      const baseRadiusX = Math.min(W * 0.37, 545);
      const baseRadiusY = Math.min(H * 0.13, 115);

      /* Geometria da Grade Alinhada (5 colunas x 2 fileiras abaixo da logo) */
      const cols = W < 900 ? 2 : 5;
      const colStep = cols === 5 ? Math.min(282, (W - 60) / 5) : Math.min(280, (W - 36) / 2);
      const rowStep = cols === 5 ? Math.min(146, H * 0.20) : 132;
      const gridStartY = cols === 5 ? Math.max(255, H * 0.44) : 230;

      for (const st of cardStates) {
        if (!st.hovered && gridBlend < 0.98) {
          st.orbitAngle += 0.0034 * (1.0 - gridBlend * 0.85);
          st.selfSpinAngle += 0.016 * st.tumbleSpeed;
        }

        const cosA = Math.cos(st.orbitAngle);
        const sinA = Math.sin(st.orbitAngle);

        const coneSpread = 1.0 - st.altitudeOffset * 0.22;
        const rX = baseRadiusX * st.radiusMult * coneSpread;
        const rY = baseRadiusY * st.radiusMult;

        const verticalWave = Math.sin(timeTick * 1.15 + st.phaseY) * 22;
        const altitudePx = st.altitudeOffset * (H * 0.72);

        st.screenX = orbitCenterX + cosA * rX;
        st.screenY = orbitCenterY + altitudePx + sinA * rY + verticalWave;
        st.depth = sinA;

        const depth = st.depth;
        const normDepth = (depth + 1) * 0.5;

        const orbitX = Math.max(150, Math.min(W - 150, st.screenX));
        const orbitY = Math.max(82, Math.min(H - 82, st.screenY));

        /* Posição Alvo na Grade Alinhada abaixo da Logo */
        const col = st.idx % cols;
        const row = Math.floor(st.idx / cols);
        const floatX = Math.cos(timeTick * 1.7 + st.idx * 0.8) * 3.5;
        const floatY = Math.sin(timeTick * 2.1 + st.idx * 0.65) * 5.0;
        const gridX = (W * 0.50) + (col - (cols - 1) * 0.5) * colStep + floatX;
        const gridY = gridStartY + row * rowStep + floatY;

        const finalX = orbitX * (1.0 - gridBlend) + gridX * gridBlend;
        const finalY = orbitY * (1.0 - gridBlend) + gridY * gridBlend;

        if (st.hovered) {
          st.el.style.zIndex = 240;
          st.el.style.opacity = '1';
          st.el.style.transform = `translate3d(${(finalX - 134).toFixed(1)}px, ${(finalY - 62.5).toFixed(1)}px, 130px) scale(1.10) rotateZ(0deg) rotateY(0deg) rotateX(0deg)`;
        } else {
          /* Valores da Órbita do Vórtice */
          const orbitScale = 0.08 + Math.pow(normDepth, 1.65) * 0.86;
          let orbitOpacity;
          if (depth < -0.55) {
            const backFade = (depth + 1) / 0.45;
            orbitOpacity = 0.01 + Math.pow(Math.max(0, backFade), 2.4) * 0.24;
          } else {
            const frontFade = (depth + 0.55) / 1.55;
            orbitOpacity = 0.25 + Math.pow(Math.max(0, frontFade), 0.85) * 0.75;
          }

          const windFactor = 0.48 + (1 - normDepth) * 0.72;
          const orbitRotZ = Math.sin(st.selfSpinAngle) * (20 * windFactor) + cosA * 10;
          const orbitRotY = Math.cos(st.selfSpinAngle * 0.85 + st.phaseX) * (24 * windFactor) - cosA * 14;
          const orbitRotX = Math.sin(st.selfSpinAngle * 1.15 + st.phaseY) * (15 * windFactor);
          const orbitZ = depth * 90;

          /* Valores do Modo Alinhado de Frente (com leve movimento vivo!) */
          const alignScale = cols === 5 ? Math.min(1.0, (W - 70) / (5 * 276)) : 0.92;
          const alignOpacity = 1.0;
          const alignRotZ = Math.sin(timeTick * 1.6 + st.idx * 0.9) * 1.5;
          const alignRotY = Math.cos(timeTick * 1.8 + st.idx * 0.6) * 3.8;
          const alignRotX = Math.sin(timeTick * 1.5 + st.idx * 0.7) * 2.2;
          const alignZ = 75;

          const scale = orbitScale * (1.0 - gridBlend) + alignScale * gridBlend;
          const opacity = orbitOpacity * (1.0 - gridBlend) + alignOpacity * gridBlend;
          const selfRotZ = orbitRotZ * (1.0 - gridBlend) + alignRotZ * gridBlend;
          const selfRotY = orbitRotY * (1.0 - gridBlend) + alignRotY * gridBlend;
          const selfRotX = orbitRotX * (1.0 - gridBlend) + alignRotX * gridBlend;
          const zPos = orbitZ * (1.0 - gridBlend) + alignZ * gridBlend;

          const baseZIdx = Math.round(20 + normDepth * 80) + st.idx;
          st.el.style.zIndex = gridBlend > 0.5 ? (120 + st.idx) : baseZIdx;
          st.el.style.opacity = opacity.toFixed(3);
          st.el.style.transform = `translate3d(${(finalX - 134).toFixed(1)}px, ${(finalY - 62.5).toFixed(1)}px, ${zPos.toFixed(1)}px) scale(${scale.toFixed(3)}) rotateZ(${selfRotZ.toFixed(2)}deg) rotateY(${selfRotY.toFixed(2)}deg) rotateX(${selfRotX.toFixed(2)}deg)`;
        }
      }

      requestAnimationFrame(animateScene);
    }

    requestAnimationFrame(animateScene);
  </script>
  <script src="/assets/js/vortice-analytics.js" defer></script>
</body>
</html>
"""

out_dir = r"C:\PROJETOS\5-FERRAMENTAS\SITE_VORTICE_MIDIA"

final_html = HTML_TEMPLATE.replace(
    "__MODEL_TITLE__",
    "Portal Oficial — 10 Canais, Música, Séries 3D & Aplicativos"
)

with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(final_html)

with open(os.path.join(out_dir, "index_transparente.html"), "w", encoding="utf-8") as f:
    f.write(final_html)

canais_dir = os.path.join(out_dir, "canais")
if os.path.isdir(canais_dir):
    for fn in os.listdir(canais_dir):
        if fn.endswith(".html"):
            fp = os.path.join(canais_dir, fn)
            with open(fp, "r", encoding="utf-8") as cf:
                ch_html = cf.read()
            if "vortice-analytics.js" not in ch_html:
                ch_html = ch_html.replace("</body>", '  <script src="/assets/js/vortice-analytics.js" defer></script>\n</body>')
                with open(fp, "w", encoding="utf-8") as cf:
                    cf.write(ch_html)

print("Generated unified 3D Orbital Tornado site + Vortice Analytics in index.html and all channel pages successfully!")
