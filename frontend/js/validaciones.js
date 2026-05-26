/* =====================================================
   PawFamily — validaciones.js
   Validaciones de frontend para login, reserva y voluntariado.
   Las validaciones reales (seguridad) van en el backend.
   ===================================================== */

/* ========== UTILIDADES ========== */

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

/* ========== VALIDACIÓN LOGIN ========== */

const loginForm = document.getElementById('loginForm');
if (loginForm) {
  const campoLogin    = document.getElementById('login');
  const campoPassword = document.getElementById('password');

  // Validar al perder el foco
  campoLogin.addEventListener('blur', () => {
    if (!campoLogin.value.trim()) {
      mostrarError(campoLogin, 'El usuario o email no puede estar vacío.');
    } else if (campoLogin.value.includes('@') && !esEmailValido(campoLogin.value)) {
      mostrarError(campoLogin, 'El email no tiene un formato válido.');
    } else {
      limpiarError(campoLogin);
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

  // Limpiar error al escribir
  [campoLogin, campoPassword].forEach(campo => {
    campo.addEventListener('input', () => limpiarError(campo));
  });

  // Validar al enviar
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let valido = true;

    if (!campoLogin.value.trim()) {
      mostrarError(campoLogin, 'El usuario o email no puede estar vacío.');
      valido = false;
    } else if (campoLogin.value.includes('@') && !esEmailValido(campoLogin.value)) {
      mostrarError(campoLogin, 'El email no tiene un formato válido.');
      valido = false;
    }

    if (!campoPassword.value.trim()) {
      mostrarError(campoPassword, 'La contraseña no puede estar vacía.');
      valido = false;
    } else if (campoPassword.value.length < 6) {
      mostrarError(campoPassword, 'La contraseña debe tener al menos 6 caracteres.');
      valido = false;
    }

    if (valido) {
      // Credenciales admin simuladas — reemplazar por fetch('/api/login', ...) cuando el backend esté listo
      if (campoLogin.value.trim() === 'admin' && campoPassword.value === 'admin123') {
        window.location.href = 'admin.html';
      } else {
        window.location.href = 'index.html';
      }
    }
  });
}

/* ========== VALIDACIÓN RESERVA ========== */

const reservaForm = document.getElementById('reservaForm');
if (reservaForm) {
  const campoNombre = document.getElementById('nombre');
  const campoEmail  = document.getElementById('email');
  const campoPerro  = document.getElementById('perro');
  const campoFecha  = document.getElementById('fecha');

  const camposReserva = [campoNombre, campoEmail, campoPerro, campoFecha];

  camposReserva.forEach(campo => {
    campo.addEventListener('blur', () => validarCampoReserva(campo));
    campo.addEventListener('input', () => limpiarError(campo));
    campo.addEventListener('change', () => validarCampoReserva(campo));
  });

  function validarCampoReserva(campo) {
    if (campo === campoNombre) {
      if (!campo.value.trim()) {
        mostrarError(campo, 'El nombre no puede estar vacío.');
      } else if (campo.value.trim().length < 3) {
        mostrarError(campo, 'El nombre debe tener al menos 3 caracteres.');
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
  }

  reservaForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let valido = true;

    camposReserva.forEach(campo => {
      validarCampoReserva(campo);
      const error = campo.closest('.form-group').querySelector('.form-error');
      if (error && error.textContent) valido = false;
    });

    if (valido) {
      // fetch('/api/visitas', { method: 'POST', body: JSON.stringify({...}) })
      alert('Reserva OK — pendiente de conectar con la API');
    }
  });
}

/* ========== VALIDACIÓN REGISTRO ========== */

const registroForm = document.getElementById('registroForm');
if (registroForm) {
  const campoNombre   = document.getElementById('nombre_completo');
  const campoUsername = document.getElementById('username');
  const campoEmail    = document.getElementById('email');
  const campoPassword = document.getElementById('password');
  const campoConfirm  = document.getElementById('confirm_password');

  const camposRegistro = [campoNombre, campoUsername, campoEmail, campoPassword, campoConfirm];

  function validarCampoRegistro(campo) {
    if (campo === campoNombre) {
      if (!campo.value.trim()) {
        mostrarError(campo, 'El nombre completo no puede estar vacío.');
      } else {
        limpiarError(campo);
      }
    }
    if (campo === campoUsername) {
      if (!campo.value.trim()) {
        mostrarError(campo, 'El nombre de usuario no puede estar vacío.');
      } else if (/\s/.test(campo.value)) {
        mostrarError(campo, 'El nombre de usuario no puede contener espacios.');
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

  registroForm.addEventListener('submit', (e) => {
    e.preventDefault();

    camposRegistro.forEach(campo => validarCampoRegistro(campo));

    const hayErrores = camposRegistro.some(campo => {
      const err = campo.closest('.form-group').querySelector('.form-error');
      return err && err.textContent;
    });

    if (!hayErrores) {
      const fecha_alta = new Date().toISOString();
      // fetch('/api/usuarios', { method: 'POST', body: JSON.stringify({ nombre_completo, username, email, password, fecha_alta }) })
      document.getElementById('registroExito').style.display = 'block';
      registroForm.querySelectorAll('input, button').forEach(el => el.disabled = true);
      setTimeout(() => { window.location.href = 'login.html'; }, 2000);
    }
  });
}

/* ========== VALIDACIÓN VOLUNTARIADO ========== */

const voluntarioForm = document.getElementById('voluntarioForm');
if (voluntarioForm) {
  const campoNombre   = document.getElementById('nombre');
  const campoEmail    = document.getElementById('email');
  const campoTelefono = document.getElementById('telefono');
  const campoRol      = document.getElementById('rol');

  const camposVol = [campoNombre, campoEmail, campoRol];

  camposVol.forEach(campo => {
    campo.addEventListener('blur', () => validarCampoVol(campo));
    campo.addEventListener('input', () => limpiarError(campo));
    campo.addEventListener('change', () => validarCampoVol(campo));
  });

  // Teléfono opcional pero si se rellena debe ser válido
  campoTelefono.addEventListener('blur', () => {
    if (campoTelefono.value.trim() && !/^[+\d\s]{7,15}$/.test(campoTelefono.value)) {
      mostrarError(campoTelefono, 'Introduce un teléfono válido.');
    } else {
      limpiarError(campoTelefono);
    }
  });

  function validarCampoVol(campo) {
    if (campo === campoNombre) {
      if (!campo.value.trim()) {
        mostrarError(campo, 'El nombre no puede estar vacío.');
      } else if (campo.value.trim().length < 3) {
        mostrarError(campo, 'El nombre debe tener al menos 3 caracteres.');
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
    if (campo === campoRol) {
      if (!campo.value) {
        mostrarError(campo, 'Selecciona un área de voluntariado.');
      } else {
        limpiarError(campo);
      }
    }
  }

  voluntarioForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let valido = true;

    camposVol.forEach(campo => {
      validarCampoVol(campo);
      const error = campo.closest('.form-group').querySelector('.form-error');
      if (error && error.textContent) valido = false;
    });

    if (valido) {
      // fetch('/api/voluntarios', { method: 'POST', body: JSON.stringify({...}) })
      alert('Solicitud OK — pendiente de conectar con la API');
    }
  });
}