/* --- ACSESSIBILITY CONTROLS ---  */

/* DYSLEXIA BUTTON TOGGLE FUNCTIONS  */

/* set variables for dyslexia toggle status */
var modeBtn1 = document.getElementById('mode1');

/* toggle dyslexia controls */
modeBtn1.onchange = (e) => {
  /* toggle on dyslexia control if applicable */
  if (modeBtn1.checked === true) {
    document.documentElement.classList.remove("fontRegular")
    document.documentElement.classList.add("fontDyslexia")
    /* set new toggle status */
    localStorage.setItem('mode1', 'fontDyslexia');
  } 
  /* toggle off dyslexia control if applicable */
  else {
    document.documentElement.classList.remove("fontDyslexia")
    document.documentElement.classList.add("fontRegular")
    /* set new toggle status */
    localStorage.setItem('mode1', 'fontRegular');
  }
}

/* set new dyslexia toggle status */
var mode1 = window.localStorage.getItem('mode1');

/* set toggle state on page reloads */
if (mode1 == 'fontDyslexia') {
  modeBtn1.checked = true;
  document.documentElement.classList.remove("fontRegular")
  document.documentElement.classList.add("fontDyslexia")
}

if (mode1 == 'fontRegular') {
  modeBtn1.checked = false;
  document.documentElement.classList.remove("fontDyslexia")
  document.documentElement.classList.add("fontRegular")
}