(function () {
  'use strict';
  const key = role => 'urguru-' + role + '-signed-out';
  const storage = {
    signedOut(role) { try { return sessionStorage.getItem(key(role)) === '1'; } catch (_) { return false; } },
    markSignedOut(role) { try { sessionStorage.setItem(key(role), '1'); } catch (_) {} },
    markSignedIn(role) { try { sessionStorage.removeItem(key(role)); } catch (_) {} }
  };

  function confirm(role, onConfirm) {
    if (document.getElementById('urguru-logout-dialog')) return;
    const opener = document.activeElement;
    const dialog = document.createElement('dialog');
    dialog.id = 'urguru-logout-dialog';
    dialog.className = 'urguru-logout-dialog';
    dialog.setAttribute('aria-labelledby', 'urguru-logout-title');
    dialog.setAttribute('aria-describedby', 'urguru-logout-description');
    dialog.innerHTML = '<h2 id="urguru-logout-title">Log out?</h2>' +
      '<p id="urguru-logout-description">You will return to the sign in screen. Your saved preferences and demo content will stay here.</p>' +
      '<div class="urguru-logout-actions"><button type="button" data-cancel>Cancel</button><button type="button" data-confirm>Log out</button></div>';
    document.body.append(dialog);
    let confirmed = false;
    dialog.addEventListener('close', () => {
      dialog.remove();
      if (!confirmed && opener && opener.isConnected) opener.focus({preventScroll: true});
    }, {once: true});
    dialog.querySelector('[data-cancel]').addEventListener('click', () => dialog.close());
    dialog.querySelector('[data-confirm]').addEventListener('click', () => {
      confirmed = true;
      dialog.close();
      storage.markSignedOut(role);
      onConfirm();
    });
    dialog.showModal();
    dialog.querySelector('[data-cancel]').focus();
  }
  window.urGuruLogout = {...storage, confirm};
})();
