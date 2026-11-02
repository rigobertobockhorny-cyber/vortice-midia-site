/**
 * VÓRTICE PULSE ANALYTICS v2.0 — Telemetria Fiel de Pessoas Reais
 * - Filtra robôs automáticos da internet (Cloudflare/Googlebot/Render)
 * - Usa localStorage para que a mesma pessoa abrindo várias abas conte como 1 único visitante
 * - Registra cliques nas Placas 3D, Páginas de Canais, Músicas, YouTube, Spotify e Loja
 */
(function () {
  const API_ENDPOINT = "https://vortice-cloud-bot.onrender.com/api/site/track";
  const STORAGE_KEY = "vortice_visitor_uid_v2";

  // 1. Filtra robôs automáticos de verificação de domínio/SSL
  const ua = navigator.userAgent || "";
  if (
    navigator.webdriver ||
    /bot|crawl|spider|slurp|headless|lighthouse|pingdom|uptimerobot|cloudflare|render|curl|python|wget|facebookexternalhit|whatsapp|telegrambot/i.test(ua)
  ) {
    return;
  }

  function getVisitorId() {
    try {
      let uid = localStorage.getItem(STORAGE_KEY);
      if (!uid) {
        uid = "vuser_" + Date.now().toString(36) + "_" + Math.random().toString(36).substring(2, 8);
        localStorage.setItem(STORAGE_KEY, uid);
      }
      return uid;
    } catch (e) {
      return "vuser_" + Date.now().toString(36);
    }
  }

  function getDeviceType() {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(ua)) {
      return "Celular";
    }
    return "Computador";
  }

  const sid = getVisitorId();
  const device = getDeviceType();
  const startTime = Date.now();
  let currentSection = "1. Tornado 3D (Início)";
  const seenSections = new Set(["1. Tornado 3D (Início)"]);

  function sendPulse(payload) {
    const data = Object.assign({
      sid: sid,
      page: window.location.pathname || "/",
      title: "Portal Oficial Vórtice Mídia",
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

  // Dispara visita inicial (e já marca a seção inicial)
  sendPulse({ type: "pageview" });

  // Mapeamento amigável de todas as seções do site
  const sectionLabels = {
    "hero-stage": "1. Tornado 3D (Início)",
    "momentos": "2. Músicas & Clipes em Destaque",
    "top5": "3. Top 5 Mais Tocadas",
    "universos": "4. Últimos Vídeos do YouTube",
    "destinos-vortice": "5. Ecossistema dos 10 Canais",
    "loja-oficial": "6. Vitrine Loja Oficial",
    "sobre": "7. Sobre & Manifesto",
    "contato": "8. Receba os Lançamentos",
    "ch-sec-historia": "Página Interna de Canal",
    "ch-sec-episodios": "Vídeos / Músicas do Canal",
    "ch-sec-loja": "Loja Interna do Canal"
  };

  if ("IntersectionObserver" in window) {
    const obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && entry.intersectionRatio >= 0.3) {
          const id = entry.target.id || "";
          const label = sectionLabels[id] || id;
          if (label) {
            currentSection = label;
            if (!seenSections.has(label)) {
              seenSections.add(label);
              sendPulse({ type: "section", section: label });
            }
          }
        }
      });
    }, { threshold: [0.3] });

    document.querySelectorAll("section[id], div[id^='ch-sec-']").forEach(function (el) {
      obs.observe(el);
    });
  }

  // Intercepta abertura de páginas de canais, players de música e lojas
  window.addEventListener("load", function () {
    if (typeof window.openChannelPortal === "function") {
      const origOpen = window.openChannelPortal;
      window.openChannelPortal = function (ch) {
        if (ch && ch.name) {
          sendPulse({
            type: "click",
            label: "Abriu Página do Canal: " + ch.name,
            url: "#/" + (ch.id || "")
          });
        }
        return origOpen.apply(this, arguments);
      };
    }

    if (typeof window.playChannelMusicById === "function") {
      const origPlay = window.playChannelMusicById;
      window.playChannelMusicById = function (chId) {
        sendPulse({
          type: "click",
          label: "Deu Play na Música: " + chId,
          url: "#play-" + chId
        });
        return origPlay.apply(this, arguments);
      };
    }

    if (typeof window.openPlatformClaimPage === "function") {
      const origClaim = window.openPlatformClaimPage;
      window.openPlatformClaimPage = function (chId, platKey, platName) {
        sendPulse({
          type: "click",
          label: "Clicou em " + (platName || platKey) + " (" + chId + ")",
          url: "#claim-" + chId + "-" + platKey
        });
        return origClaim.apply(this, arguments);
      };
    }
  });

  // Captura cliques em links externos (YouTube, Spotify, etc.), placas 3D e botões
  document.addEventListener("click", function (e) {
    const el = e.target.closest("a, button, .vortex-sign-wrapper, .top5-wine-card, .universo-poster-card, .ep-card");
    if (!el) return;

    const href = el.getAttribute("href") || "";
    const onclickAttr = el.getAttribute("onclick") || "";

    // Se já foi capturado pelas funções interceptadas acima, evita duplicar
    if (onclickAttr.includes("openChannelById") || onclickAttr.includes("playChannelMusicById") || onclickAttr.includes("openPlatformClaimPage")) {
      return;
    }

    let label = "";
    if (href.includes("youtube.com") || href.includes("youtu.be")) {
      const cardTitle = el.closest(".ep-card, .universo-poster-card, .momento-card");
      const h3 = cardTitle ? cardTitle.querySelector("h3, h4, .ep-title") : null;
      const channelTitle = document.getElementById("portal-title-text");
      const ctxName = h3 ? h3.textContent.trim() : (channelTitle && document.body.classList.contains("channel-view-active") ? channelTitle.textContent.trim() : href);
      label = "Abriu YouTube: " + ctxName.substring(0, 55);
    } else if (href.includes("spotify.com")) {
      label = "Abriu Spotify";
    } else if (el.classList.contains("top5-play-action") || el.closest(".top5-wine-card")) {
      const row = el.closest(".top5-wine-card");
      const song = row ? row.querySelector(".top5-song-name") : null;
      const band = row ? row.querySelector(".top5-band-front") : null;
      if (song) {
        label = "Ouviu Top 5: " + song.textContent.trim() + (band ? " (" + band.textContent.trim() + ")" : "");
      }
    } else if (el.id === "vortice-logo-toggle-btn") {
      label = "Clicou na Logo Vórtice (Alinhar Placas)";
    } else if (el.closest("#vortice-radio-widget")) {
      label = "Sintonizou Rádio Vórtice";
    }

    if (label) {
      sendPulse({
        type: "click",
        label: label,
        url: href
      });
    }
  }, true);

  // Captura inscrições no formulário "Receba os Lançamentos"
  document.addEventListener("submit", function (e) {
    const form = e.target;
    if (!form) return;
    const input = form.querySelector("input[type='email'], input[type='text'], input[type='tel']");
    if (input && input.value.trim()) {
      sendPulse({
        type: "lead",
        contact: input.value.trim()
      });
    }
  }, true);

  // Heartbeat a cada 15 segundos para atualizar o tempo de permanência da pessoa
  setInterval(function () {
    if (document.visibilityState === "visible") {
      sendPulse({ type: "heartbeat" });
    }
  }, 15000);

  window.addEventListener("pagehide", function () {
    sendPulse({ type: "heartbeat" });
  });
})();
