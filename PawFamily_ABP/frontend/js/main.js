/* =====================================================
   PawFamily — app.js
   ---
   Cuando conectes la API REST de Python, sustituye el
   array PERROS por:

     const PERROS = await fetch('/api/dogs').then(r => r.json());

   La estructura mínima esperada por cada perro es:
     { id, nombre, raza, edad, estado }
   Los campos extra (imagen, historia, peso, etc.) son
   opcionales: si no llegan, la UI muestra un placeholder.
   ===================================================== */

const PERROS = [
  {
    id: 1,
    nombre: "Bruno",
    raza: "Mestizo Labrador",
    edad: "3 años",
    estado: "sin-adopcion",
    sexo: "Macho",
    tamano: "Grande · 28 kg",
    imagen: "https://images.unsplash.com/photo-1561037404-61cd46aa615b?w=800&q=80&auto=format&fit=crop",
    historia: "Bruno llegó al refugio hace 8 meses, abandonado en una gasolinera. Es tranquilo, le encantan los paseos largos y se lleva bien con niños. Busca una familia activa con jardín o paseos diarios."
  },
  {
    id: 2,
    nombre: "Luna",
    raza: "Border Collie",
    edad: "2 años",
    estado: "en-proceso",
    sexo: "Hembra",
    tamano: "Mediana · 18 kg",
    imagen: "https://images.unsplash.com/photo-1568572933382-74d440642117?w=800&q=80&auto=format&fit=crop",
    historia: "Inteligente como ella sola. Luna sabe sentarse, dar la pata y hasta abrir puertas (cuidado). Necesita estimulación mental diaria. Actualmente en periodo de adaptación con una familia."
  },
  {
    id: 3,
    nombre: "Toby",
    raza: "Beagle",
    edad: "5 años",
    estado: "sin-adopcion",
    sexo: "Macho",
    tamano: "Mediano · 14 kg",
    imagen: "https://images.unsplash.com/photo-1505628346881-b72b27e84530?w=800&q=80&auto=format&fit=crop",
    historia: "Toby es puro corazón. Cinco años, vacunas al día, esterilizado. Le encanta olfatear, comer y dormir, en ese orden. Compatible con otros perros y con gatos calmados."
  },
  {
    id: 4,
    nombre: "Nala",
    raza: "Mestiza pequeña",
    edad: "1 año",
    estado: "sin-adopcion",
    sexo: "Hembra",
    tamano: "Pequeña · 7 kg",
    imagen: "https://images.unsplash.com/photo-1583512603805-3cc6b41f3edb?w=800&q=80&auto=format&fit=crop",
    historia: "Nala fue rescatada de una camada en un descampado. Tímida al principio, pero cuando coge confianza es la perra más cariñosa del refugio. Ideal para piso."
  },
  {
    id: 5,
    nombre: "Rocco",
    raza: "Pastor Alemán",
    edad: "7 años",
    estado: "adoptado",
    sexo: "Macho",
    tamano: "Grande · 32 kg",
    imagen: "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=800&q=80&auto=format&fit=crop",
    historia: "Rocco encontró familia en marzo de 2026. Vive con Marta y sus dos hijos en Galapagar. Le mandamos un saludo desde aquí."
  },
  {
    id: 6,
    nombre: "Chispa",
    raza: "Jack Russell",
    edad: "4 años",
    estado: "sin-adopcion",
    sexo: "Hembra",
    tamano: "Pequeña · 8 kg",
    imagen: "https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=800&q=80&auto=format&fit=crop",
    historia: "Chispa hace honor a su nombre. Energía infinita, salta más alto de lo que pesa. Busca familia deportista, sin niños muy pequeños porque puede ser revoltosa."
  },
  {
    id: 7,
    nombre: "Olivia",
    raza: "Galgo español",
    edad: "6 años",
    estado: "en-proceso",
    sexo: "Hembra",
    tamano: "Grande · 22 kg",
    imagen: "https://images.unsplash.com/photo-1561948955-570b270e7c36?w=800&q=80&auto=format&fit=crop",
    historia: "Galga rescatada al final de la temporada de caza. Tras un año recuperándose, Olivia está empezando a confiar otra vez en las personas. Visitándola una familia desde hace dos semanas."
  },
  {
    id: 8,
    nombre: "Max",
    raza: "Husky Siberiano",
    edad: "4 años",
    estado: "sin-adopcion",
    sexo: "Macho",
    tamano: "Grande · 26 kg",
    imagen: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=800&q=80&auto=format&fit=crop",
    historia: "Max llegó al refugio porque sus dueños no podían con su nivel de actividad. Necesita ejercicio intenso a diario, mucho. Sin él, se aburre y se mete en líos."
  },
  {
    id: 9,
    nombre: "Pipa",
    raza: "Mestiza Yorkshire",
    edad: "9 años",
    estado: "sin-adopcion",
    sexo: "Hembra",
    tamano: "Pequeña · 5 kg",
    imagen: "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=800&q=80&auto=format&fit=crop",
    historia: "Pipa es senior y lo sabe. Busca un sofá cómodo, una mantita y alguien que la quiera para sus mejores años. Adopción senior — apadrinable si no puedes adoptarla."
  },
  {
    id: 10,
    nombre: "Lobo",
    raza: "Mestizo grande",
    edad: "2 años",
    estado: "adoptado",
    sexo: "Macho",
    tamano: "Grande · 30 kg",
    imagen: "https://images.unsplash.com/photo-1552053831-71594a27632d?w=800&q=80&auto=format&fit=crop",
    historia: "Lobo fue adoptado en abril por Carlos, un veterinario jubilado. Viven juntos en un pueblo de Ávila. Reportan paseos largos y siestas eternas."
  },
  {
    id: 11,
    nombre: "Mila",
    raza: "Cocker Spaniel",
    edad: "3 años",
    estado: "sin-adopcion",
    sexo: "Hembra",
    tamano: "Mediana · 12 kg",
    imagen: "https://images.unsplash.com/photo-1591946614720-90a587da4a36?w=800&q=80&auto=format&fit=crop",
    historia: "Mila es dulce, sociable y muy expresiva con las orejas. Compatible con otros perros, con gatos, con niños — con todo el mundo. La perra más fácil que tenemos."
  },
  {
    id: 12,
    nombre: "Kobi",
    raza: "Mestizo Pitbull",
    edad: "5 años",
    estado: "en-proceso",
    sexo: "Macho",
    tamano: "Grande · 25 kg",
    imagen: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=800&q=80&auto=format&fit=crop",
    historia: "Kobi sufrió maltrato antes de llegar al refugio. Tras dos años con nosotros, vuelve a confiar. Requiere licencia PPP. Familia adoptante en proceso final."
  }
];

/* ========== ESTADOS ========== */
const ESTADO_LABELS = {
  "sin-adopcion": "Sin adopción",
  "en-proceso":   "En proceso",
  "adoptado":     "Adoptado"
};

/* ========== PLACEHOLDER si no hay imagen ========== */
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

/* ========== RENDER TARJETAS ========== */
const grid       = document.getElementById('dogGrid');
const emptyState = document.getElementById('dogsEmpty');
const countEl    = document.getElementById('filtersCount');

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
    const img = perro.imagen || placeholderSVG(perro.nombre);
    const adoptado = perro.estado === 'adoptado' ? ' dog-card--adoptado' : '';
    const idTxt = '#' + String(perro.id).padStart(3, '0');
    return `
      <li class="dog-card${adoptado}" data-id="${perro.id}">
        <div class="dog-card__media">
          <img class="dog-card__img"
               src="${img}"
               alt="Foto de ${perro.nombre}, ${perro.raza}"
               loading="lazy"
               onerror="this.onerror=null;this.src='${placeholderSVG(perro.nombre)}'" />
          <span class="dog-card__badge badge--${perro.estado}">
            <span class="dot"></span>${ESTADO_LABELS[perro.estado]}
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

/* ========== FILTROS ========== */
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

/* ========== MODAL DETALLE ========== */
const modal     = document.getElementById('dogModal');
const modalBody = document.getElementById('modalBody');
const modalClose= document.getElementById('modalClose');

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
        <span class="dot"></span>${ESTADO_LABELS[perro.estado]}
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
          : `<a class="btn btn--primary" href="#reservar">Reservar visita con ${perro.nombre}</a>
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
  // click en backdrop
  const rect = modal.getBoundingClientRect();
  if (e.clientX < rect.left || e.clientX > rect.right ||
      e.clientY < rect.top  || e.clientY > rect.bottom) {
    modal.close();
  }
});

/* ========== MOBILE MENU ========== */
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

/* ========== INIT ========== */
renderPerros();