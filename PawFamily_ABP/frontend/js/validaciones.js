// UTILIDADES

function mostrarError(campo, mensaje) {
  const grupo = campo.closest('.form-group');
  let error = grupo.querySelector('.form-error');
  if (!error) {
    error = document.createElement('span');
    error.className = 'form-error';
    grupo.appendChild(error);
  }
  error.textContent = mensaje;
  campo.classList.add('campo-error');
}
  
function limpiarError(campo) {
  const grupo = campo.closest('.form-group');
  const error = grupo.querySelector('.form-error');
  if (error) error.textContent = '';
  campo.classList.remove('campo-error');
}

function esEmailValido(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function esFechaFutura(fecha) {
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);
  return new Date(fecha) >= hoy;
}

// VALIDACION LOGIN

const loginForm = document.getElementById('loginForm');
if (loginForm) {
  const campoEmail    = document.getElementById('login');
  const campoPassword = document.getElementById('password');

  campoEmail.addEventListener('blur', () => {
    if (!campoEmail.value.trim()) {
      mostrarError(campoEmail, 'El email no puede estar vacío.');
    } else if (!esEmailValido(campoEmail.value)) {
      mostrarError(campoEmail, 'El email no tiene un formato válido.');
    } else {
      limpiarError(campoEmail);
    }
  });

  campoPassword.addEventListener('blur', () => {
    if (!campoPassword.value.trim()) {
      mostrarError(campoPassword, 'La contraseña no puede estar vacía.');
    } else if (campoPassword.value.length < 6) {
      mostrarError(campoPassword, 'La contraseña debe tener al menos 6 caracteres.');
    } else {
      limpiarError(campoPassword);
    }
  });

  [campoEmail, campoPassword].forEach(campo => {
    campo.addEventListener('input', () => limpiarError(campo));
  });

  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    let valido = true;

    if (!campoEmail.value.trim()) {
      mostrarError(campoEmail, 'El email no puede estar vacío.');
      valido = false;
    } else if (!esEmailValido(campoEmail.value)) {
      mostrarError(campoEmail, 'El email no tiene un formato válido.');
      valido = false;
    }

    if (!campoPassword.value.trim()) {
      mostrarError(campoPassword, 'La contraseña no puede estar vacía.');
      valido = false;
    } else if (campoPassword.value.length < 6) {
      mostrarError(campoPassword, 'La contraseña debe tener al menos 6 caracteres.');
      valido = false;
    }

    if (!valido) return;

    const btnSubmit = loginForm.querySelector('button[type="submit"]');
    btnSubmit.disabled = true;
    btnSubmit.textContent = 'Iniciando sesión...';

    try {
      const res = await fetch(`${API_BASE}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          correo:    campoEmail.value.trim(),
          contrasena: campoPassword.value
        })
      });

      const data = await res.json();

      if (res.ok && data.ok) {
        sessionStorage.setItem('usuario', JSON.stringify(data.usuario));
        window.location.href = data.usuario.rol === 'Administrador' ? 'admin.html' : 'index.html';
      } else {
        mostrarError(campoPassword, data.error || 'Credenciales incorrectas.');
        btnSubmit.disabled = false;
        btnSubmit.textContent = 'Iniciar sesión';
      }
    } catch {
      mostrarError(campoPassword, 'No se pudo conectar con el servidor. Inténtalo de nuevo.');
      btnSubmit.disabled = false;
      btnSubmit.textContent = 'Iniciar sesión';
    }
  });
}

// VALIDACION RESERVA

const reservaForm = document.getElementById('reservaForm');
if (reservaForm) {
  const usuarioSesion = JSON.parse(sessionStorage.getItem('usuario') || 'null');
  if (!usuarioSesion) {
    window.location.href = 'login.html';
} else {
    const infoEl = document.getElementById('reservaUsuarioInfo');
    if (infoEl) infoEl.textContent = `Reservando como: ${usuarioSesion.nombre} (${usuarioSesion.email})`;
}

  const campoPerro = document.getElementById('perro');
  const campoFecha = document.getElementById('fecha');
  const campoHora  = document.getElementById('hora');

  const camposReserva = [campoPerro, campoFecha, campoHora];

  camposReserva.forEach(campo => {
    campo.addEventListener('blur',   () => validarCampoReserva(campo));
    campo.addEventListener('input',  () => limpiarError(campo));
    campo.addEventListener('change', () => validarCampoReserva(campo));
  });

  function validarCampoReserva(campo) {
    if (campo === campoPerro) {
      if (!campo.value) {
        mostrarError(campo, 'Selecciona un perro para visitar.');
      } else {
        limpiarError(campo);
      }
    }
    if (campo === campoFecha) {
      if (!campo.value) {
        mostrarError(campo, 'Selecciona una fecha para la visita.');
      } else if (!esFechaFutura(campo.value)) {
        mostrarError(campo, 'La fecha debe ser hoy o en el futuro.');
      } else {
        limpiarError(campo);
      }
    }
    if (campo === campoHora) {
      if (!campo.value) {
        mostrarError(campo, 'Selecciona una hora para la visita.');
      } else {
        limpiarError(campo);
      }
    }
  }

  reservaForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    camposReserva.forEach(campo => validarCampoReserva(campo));

    const hayErrores = camposReserva.some(campo => {
      const err = campo.closest('.form-group').querySelector('.form-error');
      return err && err.textContent;
    });

    if (hayErrores) return;

    const btnSubmit = reservaForm.querySelector('button[type="submit"]');
    btnSubmit.disabled = true;
    btnSubmit.textContent = 'Confirmando...';

    try {
      const res = await fetch(`${API_BASE}/citas`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id_usuario: usuarioSesion.id,
          id_perro:   Number(campoPerro.value),
          fecha_cita: campoFecha.value,
          hora_cita:  campoHora.value
        })
      });

      const data = await res.json();

      if (res.ok && data.ok) {
        reservaForm.innerHTML = `
          <div style="text-align:center;padding:2rem 0">
            <p style="font-size:1.3rem;font-weight:600;color:var(--teal);margin-bottom:0.5rem">¡Visita reservada!</p>
            <p style="color:var(--ink)">Te esperamos el <strong>${campoFecha.value}</strong> a las <strong>${campoHora.value}</strong>.</p>
            <a href="index.html" class="btn btn--primary" style="margin-top:1.5rem;display:inline-block">Volver al inicio</a>
          </div>`;
      } else {
        const msgError = reservaForm.querySelector('.form-error-general') || (() => {
          const span = document.createElement('span');
          span.className = 'form-error form-error-general';
          span.style.display = 'block';
          span.style.marginBottom = '12px';
          reservaForm.prepend(span);
          return span;
        })();
        msgError.textContent = data.error || 'Error al crear la reserva. Inténtalo de nuevo.';
        btnSubmit.disabled = false;
        btnSubmit.textContent = 'Confirmar reserva';
      }
    } catch {
      const msgError = reservaForm.querySelector('.form-error-general') || (() => {
        const span = document.createElement('span');
        span.className = 'form-error form-error-general';
        span.style.display = 'block';
        span.style.marginBottom = '12px';
        reservaForm.prepend(span);
        return span;
      })();
      msgError.textContent = 'No se pudo conectar con el servidor.';
      btnSubmit.disabled = false;
      btnSubmit.textContent = 'Confirmar reserva';
    }
  });
}

// VALIDACION REGISTRO

const registroForm = document.getElementById('registroForm');
if (registroForm) {
  const campoNombre   = document.getElementById('nombre_completo');
  const campoEmail    = document.getElementById('email');
  const campoPassword = document.getElementById('password');
  const campoConfirm  = document.getElementById('confirm_password');

  const camposRegistro = [campoNombre, campoEmail, campoPassword, campoConfirm];

  function validarCampoRegistro(campo) {
    if (campo === campoNombre) {
      if (!campo.value.trim()) {
        mostrarError(campo, 'El nombre completo no puede estar vacío.');
      } else {
        limpiarError(campo);
      }
    }
    if (campo === campoEmail) {
      if (!campo.value.trim()) {
        mostrarError(campo, 'El email no puede estar vacío.');
      } else if (!esEmailValido(campo.value)) {
        mostrarError(campo, 'Introduce un email válido (ejemplo@dominio.com).');
      } else {
        limpiarError(campo);
      }
    }
    if (campo === campoPassword) {
      if (!campo.value) {
        mostrarError(campo, 'La contraseña no puede estar vacía.');
      } else if (campo.value.length < 8) {
        mostrarError(campo, 'La contraseña debe tener al menos 8 caracteres.');
      } else {
        limpiarError(campo);
      }
    }
    if (campo === campoConfirm) {
      if (!campo.value) {
        mostrarError(campo, 'Debes confirmar la contraseña.');
      } else if (campo.value !== campoPassword.value) {
        mostrarError(campo, 'Las contraseñas no coinciden.');
      } else {
        limpiarError(campo);
      }
    }
  }

  camposRegistro.forEach(campo => {
    campo.addEventListener('blur', () => validarCampoRegistro(campo));
    campo.addEventListener('input', () => limpiarError(campo));
  });

  registroForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    camposRegistro.forEach(campo => validarCampoRegistro(campo));

    const hayErrores = camposRegistro.some(campo => {
      const err = campo.closest('.form-group').querySelector('.form-error');
      return err && err.textContent;
    });

    if (hayErrores) return;

    const btnSubmit = registroForm.querySelector('button[type="submit"]');
    btnSubmit.disabled = true;
    btnSubmit.textContent = 'Creando cuenta...';

    try {
      const res = await fetch(`${API_BASE}/usuarios`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nombre:     campoNombre.value.trim(),
          correo:     campoEmail.value.trim(),
          contrasena: campoPassword.value
        })
      });

      const data = await res.json();

      if (res.ok) {
        document.getElementById('registroExito').style.display = 'block';
        registroForm.querySelectorAll('input, button').forEach(el => el.disabled = true);
        setTimeout(() => { window.location.href = 'login.html'; }, 2000);
      } else {
        const msgError = registroForm.querySelector('.form-error-general') || (() => {
          const span = document.createElement('span');
          span.className = 'form-error form-error-general';
          span.style.display = 'block';
          span.style.marginBottom = '12px';
          registroForm.prepend(span);
          return span;
        })();
        msgError.textContent = data.error || 'Error al crear la cuenta. Inténtalo de nuevo.';
        btnSubmit.disabled = false;
        btnSubmit.textContent = 'Crear cuenta';
      }
    } catch {
      mostrarError(campoEmail, 'No se pudo conectar con el servidor.');
      btnSubmit.disabled = false;
      btnSubmit.textContent = 'Crear cuenta';
    }
  });
}

