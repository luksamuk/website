// email-deobfuscate.js — Inject contact email on page load
// Breaks the OSINT chain: email never appears in raw HTML source
(function() {
    var el = document.getElementById('email-contact');
    if (!el) return;
    var u = 'lucasvieira';
    var d = 'protonmail.com';
    var e = u + '@' + d;
    el.innerHTML = '<a href="mailto:' + e + '">' + e + '</a>';
})();