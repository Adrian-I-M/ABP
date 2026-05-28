const API_BASE = 'http://192.168.116.40:5000';

// NORMALIZACION BD → FRONTEND

function normalizarEstado(estadoBD) {
  return (estadoBD || '').toLowerCase().replace(/_/g, '-');
}

function normalizarPerro(p) {
  return {
    ...p,
    estado:   normalizarEstado(p.estado),
    edadNum:  p.edad,
    edad:     p.edad != null ? `${p.edad} año${p.edad === 1 ? '' : 's'}` : '—',
    sexo:     p.genero === 'M' ? 'Macho' : p.genero === 'F' ? 'Hembra' : (p.sexo || '—'),
    raza:     (p.raza   || '').replace(/_/g, ' '),
    historia: p.descripcion || p.historia || '',
    imagen:   p.imagen  || null,
    tamano:   p.tamano  || null
  };
}

// PERROS: ARRAY GLOBAL Y CARGA API

let PERROS = [];

async function cargarPerros() {
  try {
    const res = await fetch(`${API_BASE}/perros`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    PERROS = data.map(normalizarPerro);
  } catch (err) {
    console.warn('API no disponible:', err.message);
    PERROS = [];
    const errorEl = document.getElementById('dogsError');
    if (errorEl) errorEl.hidden = false;
  }
  document.dispatchEvent(new Event('perrosCargados'));
}

// ESTADOS
const ESTADO_LABELS = {
  "sin-adopcion": "Sin adopción",
  "en-proceso":   "En proceso",
  "adoptado":     "Adoptado"
};

// PLACEHOLDER SIN IMAGEN
function placeholderSVG(nombre) {
  const initial = (nombre || "?").charAt(0).toUpperCase();
  const svg = `
    <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 500'>
      <defs>
        <pattern id='p' width='14' height='14' patternUnits='userSpaceOnUse' patternTransform='rotate(35)'>
          <rect width='14' height='14' fill='%23ECE4DA'/>
          <line x1='0' y1='0' x2='0' y2='14' stroke='%23E0D5C5' stroke-width='1'/>
        </pattern>
      </defs>
      <rect width='400' height='500' fill='url(%23p)'/>
      <text x='200' y='280' text-anchor='middle' font-family='Georgia, serif' font-size='180' fill='%23C75A5A' opacity='0.7'>${initial}</text>
    </svg>`;
  return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
}

// GRID, FILTROS Y MODAL

const grid       = document.getElementById('dogGrid');
const emptyState = document.getElementById('dogsEmpty');
const countEl    = document.getElementById('filtersCount');

document.addEventListener('perrosCargados', () => {

  if (grid) {
    let activeFilter = 'todos';

    function renderPerros() {
      const filtered = activeFilter === 'todos'
        ? PERROS
        : PERROS.filter(p => p.estado === activeFilter);

      countEl.textContent = `${filtered.length} ${filtered.length === 1 ? 'perro' : 'perros'}`;

      if (filtered.length === 0) {
        grid.innerHTML = '';
        emptyState.hidden = false;
        return;
      }
      emptyState.hidden = true;

      grid.innerHTML = filtered.map(perro => {
        const img      = perro.imagen || placeholderSVG(perro.nombre);
        const adoptado = perro.estado === 'adoptado' ? ' dog-card--adoptado' : '';
        const idTxt    = '#' + String(perro.id).padStart(3, '0');
        return `
          <li class="dog-card${adoptado}" data-id="${perro.id}">
            <div class="dog-card__media">
              <img class="dog-card__img"
                   src="${img}"
                   alt="Foto de ${perro.nombre}, ${perro.raza}"
                   loading="lazy"
                   onerror="this.onerror=null;this.src='${placeholderSVG(perro.nombre)}'" />
              <span class="dog-card__badge badge--${perro.estado}">
                <span class="dot"></span>${ESTADO_LABELS[perro.estado] || perro.estado}
              </span>
              <span class="dog-card__id">${idTxt}</span>
            </div>
            <div class="dog-card__body">
              <h3 class="dog-card__name">${perro.nombre}</h3>
              <div class="dog-card__meta">
                <span>${perro.raza}</span>
                <span class="sep"></span>
                <span>${perro.edad}</span>
              </div>
              <button class="dog-card__cta" type="button" data-action="open" data-id="${perro.id}">
                Ver ficha
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14M13 6l6 6-6 6"/>
                </svg>
              </button>
            </div>
          </li>`;
      }).join('');
    }

    document.querySelectorAll('.filter').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.filter').forEach(b => {
          b.classList.remove('is-active');
          b.setAttribute('aria-selected', 'false');
        });
        btn.classList.add('is-active');
        btn.setAttribute('aria-selected', 'true');
        activeFilter = btn.dataset.filter;
        renderPerros();
      });
    });

    const modal      = document.getElementById('dogModal');
    const modalBody  = document.getElementById('modalBody');
    const modalClose = document.getElementById('modalClose');

    function openDog(id) {
      const perro = PERROS.find(p => p.id === Number(id));
      if (!perro) return;
      const img = perro.imagen || placeholderSVG(perro.nombre);

      modalBody.innerHTML = `
        <div class="dog-modal__media">
          <img src="${img}" alt="Foto de ${perro.nombre}"
               onerror="this.onerror=null;this.src='${placeholderSVG(perro.nombre)}'" />
        </div>
        <div class="dog-modal__info">
          <span class="dog-card__badge badge--${perro.estado}" style="align-self:flex-start;position:static">
            <span class="dot"></span>${ESTADO_LABELS[perro.estado] || perro.estado}
          </span>
          <h2 class="dog-modal__name" id="modalName">${perro.nombre}</h2>
          <dl class="dog-modal__facts">
            <div><dt>Raza</dt><dd>${perro.raza}</dd></div>
            <div><dt>Edad</dt><dd>${perro.edad}</dd></div>
            <div><dt>Sexo</dt><dd>${perro.sexo || '—'}</dd></div>
            <div><dt>Tamaño</dt><dd>${perro.tamano || '—'}</dd></div>
          </dl>
          <p class="dog-modal__story">${perro.historia || 'Pronto añadiremos más detalles sobre ' + perro.nombre + '.'}</p>
          <div class="dog-modal__actions">
            ${perro.estado === 'adoptado'
              ? `<button class="btn btn--ghost" disabled style="flex:1;justify-content:center;cursor:default">Ya tiene familia ♥</button>`
              : `<a class="btn btn--primary" href="reserva.html?perro=${perro.id}">Reservar visita con ${perro.nombre}</a>
                 <button class="btn btn--ghost" type="button">Compartir</button>`
            }
          </div>
        </div>`;
      if (typeof modal.showModal === 'function') modal.showModal();
      else modal.setAttribute('open', '');
    }

    grid.addEventListener('click', (e) => {
      const card = e.target.closest('.dog-card');
      if (!card) return;
      openDog(card.dataset.id);
    });

    modalClose.addEventListener('click', () => modal.close());
    modal.addEventListener('click', (e) => {
      const rect = modal.getBoundingClientRect();
      if (e.clientX < rect.left || e.clientX > rect.right ||
          e.clientY < rect.top  || e.clientY > rect.bottom) {
        modal.close();
      }
    });

    renderPerros();
  }

});

// DROPDOWN NAV
const dropBtn  = document.querySelector('.nav__dropdown-btn');
const dropMenu = document.querySelector('.nav__dropdown-menu');
if (dropBtn && dropMenu) {
  dropBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = dropMenu.classList.toggle('is-open');
    dropBtn.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', (e) => {
    if (!dropBtn.contains(e.target)) {
      dropMenu.classList.remove('is-open');
      dropBtn.setAttribute('aria-expanded', 'false');
    }
  });
}

// MOBILE MENU
const burger = document.getElementById('burger');
const navEl  = document.querySelector('.nav');
burger?.addEventListener('click', () => {
  const open = navEl.classList.toggle('is-open');
  burger.setAttribute('aria-expanded', open ? 'true' : 'false');
});
navEl?.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    if (window.innerWidth <= 900) {
      navEl.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });
});

// INICIO
cargarPerros();
