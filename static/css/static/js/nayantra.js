// NAYANTRA-360° - Female Welcome Voice + Translation + Dark/Light
let isLight = false;

function toggleMode(){
  isLight = !isLight;
  document.body.classList.toggle('light-mode', isLight);
  localStorage.setItem('nayan-mode', isLight?'light':'dark');
}

// Welcome Voice - Natural Female
function welcomeVoice(){
  let text = "Welcome to NAYANTRA 360 degree. Your Eyes Everywhere. Multipurpose AI Platform for Health, Factory Safety, School Monitoring and Accessibility.";
  let utter = new SpeechSynthesisUtterance(text);
  utter.voice = speechSynthesis.getVoices().find(v=>v.name.includes('Female')||v.name.includes('Google'))||null;
  utter.lang='en-IN'; utter.rate=0.9;
  speechSynthesis.speak(utter);
}

// Translation
function translatePage(lang){
  // Simple - for full, integrate Google Translate API
  // Here we store language and show message
  localStorage.setItem('nayan-lang', lang);
  alert("Language switched to: "+lang+" - Full translation via Google Translate API in production");
  // For Hindi: use googletrans in backend
}

// Auto welcome on load
window.onload = ()=>{
  if(localStorage.getItem('nayan-mode')=='light') toggleMode();
  setTimeout(welcomeVoice, 800);
}

function scrollUp(){window.scrollTo({top:0,behavior:'smooth'})}
function scrollDown(){window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'})}
function nextPage(url){window.location.href=url}
