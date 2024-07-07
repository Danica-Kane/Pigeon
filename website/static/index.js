document.documentElement.classList.add("fontRegular")
document.documentElement.classList.add("sizeRegular")
document.documentElement.classList.add("lightMode")

/* FADE FLASH ALERTS */
window.setTimeout(function() {
  var alert = document.getElementById("alert");
  $(".alert").fadeTo(500, 0) 
  alert.remove();
}, 4000);

/* TOGGLE PASSWORD VISIBILITY */

function showPassword() {
  var x = document.getElementById("password1");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function showPassword2() {
  var x = document.getElementById("password2");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

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

/* ---------------------------------- */

/* FONT SIZE TOGGLE FUNCTIONS  */

/* set variables for font size toggle status */
var modeBtn2 = document.getElementById('mode2');

/* toggle font size controls */
modeBtn2.onchange = (e) => {
   /* toggle on font size control if applicable */
  if (modeBtn2.checked === true) {
    document.documentElement.classList.remove("sizeRegular")
    document.documentElement.classList.add("sizeIncreased")
    /* set new toggle status */
    localStorage.setItem('mode2', 'sizeIncreased');
  } 
   /* toggle off font size control if applicable */
  else {
    document.documentElement.classList.remove("sizeIncreased")
    document.documentElement.classList.add("sizeRegular")
    /* set new toggle status */
    localStorage.setItem('mode2', 'sizeRegular');
  }
}

/* set new font size toggle status */
var mode2 = window.localStorage.getItem('mode2');

/* set toggle state on page reloads */
if (mode2 == 'sizeIncreased') {
  modeBtn2.checked = true;
  document.documentElement.classList.remove("sizeRegular")
  document.documentElement.classList.add("sizeIncreased")
}

if (mode2 == 'sizeRegular') {
  modeBtn2.checked = false;
  document.documentElement.classList.remove("sizeIncreased")
  document.documentElement.classList.add("sizeRegular")
}

/* ---------------------------------- */

/* DARK MODE TOGGLE FUNCTIONS  */

/* set variables for font size toggle status */
var modeBtn3 = document.getElementById('mode3');

/* toggle font size controls */
modeBtn3.onchange = (e) => {
   /* toggle on font size control if applicable */
  if (modeBtn3.checked === true) {
    document.documentElement.classList.remove("lightMode")
    document.documentElement.classList.add("darkMode")
    /* set new toggle status */
    localStorage.setItem('mode3', 'darkMode');
  } 
   /* toggle off font size control if applicable */
  else {
    document.documentElement.classList.remove("darkMode")
    document.documentElement.classList.add("lightMode")
    /* set new toggle status */
    localStorage.setItem('mode3', 'lightMode');
  }
}

/* set new font size toggle status */
var mode3 = window.localStorage.getItem('mode3');

/* set toggle state on page reloads */
if (mode3 == 'darkMode') {
  modeBtn3.checked = true;
  document.documentElement.classList.remove("lightMode")
  document.documentElement.classList.add("darkMode")
}

if (mode3 == 'lightMode') {
  modeBtn3.checked = false;
  document.documentElement.classList.remove("darkMode")
  document.documentElement.classList.add("lightMode")
}