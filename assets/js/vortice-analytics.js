/**
 * VÓRTICE PULSE ANALYTICS — Telemetria em Tempo Real do Portal Vórtice Mídia
 * Registra visitantes, tempo de permanência, seções lidas, cliques em canais/músicas e leads VIP.
 */
(function () {
  const API_ENDPOINT = "https://vortice-cloud-bot.onrender.com/api/site/track";
  const STORAGE_KEY = "vortice_pulse_sid_v1";

  function getSessionId() {
    try {
      let sid = sessionStorage.getItem(STORAGE_KEY);
      if (!sid) {
        sid = "vx_" + Date.now().toString(36) + "_" + Math.random().toString(36).substring(2, 8);
        sessionStorage.setItem(STORAGE_KEY, sid);
      }
      return sid;
    } catch (e) {
      return "vx_" + Date.now().toString(36);
    }
  }

  function getDeviceType() {
    const ua = navigator.userAgent || "";
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(ua) || window.innerWidth < 800) {
      return "Celular";
    }
    return "Computador";
  }

  const sid = getSessionId();
  const device = getDeviceType();
  const startTime = Date.now();
  let currentSection = "Topo / Vórtice 3D";
  const seenSections = new Set();

  function sendPulse(payload) {
    const data = Object.assign({
      sid: sid,
      page: window.location.pathname || "/",
      title: document.title.replace("— Vórtice Mídia", "").trim(),
      referrer: document.referrer || "",
      device: device,
      duration: Math.round((Date.now() - startTime) / 1000),
      section: currentSection
    }, payload);

    try {
      if (navigator.sendBeacon && (payload.type === "heartbeat" || payload.type === "click")) {
        const blob = new Blob([JSON.stringify(data)], { type: "application/json" });
        navigator.sendBeacon(API_ENDPOINT, blob);
        return;
      }
    } catch (e) {}

    fetch(API_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
      keepalive: true
    }).catch(function () {});
  }

  // 1. Dispara Pageview ao abrir a página
  sendPulse({ type: "pageview" });

  // 2. Observa em qual seção o visitante está navegando
  const sectionLabels = {
    "vortexStage": "1. Vórtice 3D (Home)",
    "top5-section": "2. Top 5 Músicas",
    "lancamentos": "2. Top 5 Músicas",
    "universos": "3. Últimos Vídeos YouTube",
    "ecossistema": "4. Ecossistema de Canais",
    "sobre": "5. Sobre & Manifesto",
    "contato": "6. Contato & Inscritos"
  };

  if ("IntersectionObserver" in window) {
    const obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && entry.intersectionRatio >= 0.35) {
          const id = entry.target.id || entry.target.getAttribute("data-section-name") || "";
          const label = sectionLabels[id] || id || "Conteúdo do Canal";
          currentSection = label;
          if (!seenSections.has(label)) {
            seenSections.add(label);
            sendPulse({ type: "section", section: label });
          }
        }
      });
    }, { threshold: [0.35] });

    document.querySelectorAll("section[id], #vortexStage, .channel-hero, .episodes-section").forEach(function (el) {
      if (!el.id && el.classList.contains("channel-hero")) el.setAttribute("data-section-name", "Topo do Canal");
      if (!el.id && el.classList.contains("episodes-section")) el.setAttribute("data-section-name", "Episódios & Clipes do Canal");
      obs.observe(el);
    });
  }

  // 3. Captura todos os cliques em Canais, Músicas, Botões de Play, YouTube e Spotify
  document.addEventListener("click", function (e) {
    const link = e.target.closest("a, button, .vortex-card, .top5-item-row, .universo-poster-card, .episode-card");
    if (!link) return;

    let label = "";
    let targetUrl = link.getAttribute("href") || link.getAttribute("data-href") || "";

    if (link.classList.contains("vortex-card")) {
      const titleEl = link.querySelector(".vc-name, h3, h4");
      label = "Card 3D: " + (titleEl ? titleEl.textContent.trim() : (targetUrl || "Canal"));
    } else if (link.classList.contains("top5-item-row") || link.closest(".top5-item-row")) {
      const row = link.classList.contains("top5-item-row") ? link : link.closest(".top5-item-row");
      const song = row.querySelector(".top5-song-name");
      const band = row.querySelector(".top5-band-front");
      label = "Top 5 Play: " + (song ? song.textContent.trim() : "Música") + (band ? " (" + band.textContent.trim() + ")" : "");
    } else if (link.classList.contains("universo-poster-card")) {
      const titleEl = link.querySelector("h3, h4, .uni-title");
      label = "Vídeo YouTube: " + (titleEl ? titleEl.textContent.trim() : targetUrl);
    } else if (link.classList.contains("episode-card")) {
      const titleEl = link.querySelector(".ep-title, h3, h4");
      label = "Episódio: " + (titleEl ? titleEl.textContent.trim() : (targetUrl || "Card"));
    } else {
      const text = (link.innerText || link.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim();
      if (targetUrl.includes("youtube.com") || targetUrl.includes("youtu.be")) {
        label = "YouTube Externo: " + (text || targetUrl).substring(0, 50);
      } else if (targetUrl.includes("spotify.com")) {
        label = "Spotify: " + (text || "Ouvir no Spotify").substring(0, 50);
      } else if (targetUrl.includes("/canais/")) {
        label = "Abriu Canal: " + (text || targetUrl.split("/").pop().replace(".html", ""));
      } else if (text && text.length < 60) {
        label = "Botão: " + text;
      }
    }

    if (label) {
      sendPulse({
        type: "click",
        label: label,
        url: targetUrl
      });
    }
  }, true);

  // 4. Conecta todos os formulários "Receba os Lançamentos" / Newsletter para salvar e avisar no Telegram
  document.addEventListener("submit", function (e) {
    const form = e.target;
    if (!form) return;
    const input = form.querySelector("input[type='email'], input[type='text'], input[type='tel']");
    if (input && input.value.trim()) {
      const contactVal = input.value.trim();
      sendPulse({
        type: "lead",
        contact: contactVal
      });
    }
  }, true);

  // 5. Heartbeat a cada 15 segundos para medir o tempo exato de permanência
  setInterval(function () {
    if (document.visibilityState === "visible") {
      sendPulse({ type: "heartbeat" });
    }
  }, 15000);

  window.addEventListener("pagehide", function () {
    sendPulse({ type: "heartbeat" });
  });
})();
