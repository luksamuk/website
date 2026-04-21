function slugify(title) {
  if (!title) return '';
  // normalize Unicode, remove diacritics, remove non-word chars, collapse spaces -> dash
  return title
    .trim()
    .toLowerCase()
    .normalize('NFKD')           // decompose accents
    .replace(/[\u0300-\u036f]/g, '') // remove diacritic marks
    .replace(/[^\w\s-]/g, '')    // remove non-word chars
    .replace(/\s+/g, '-')        // spaces -> dashes
    .replace(/^-+|-+$/g, '');    // trim leading/trailing dashes
}

var pageTitle = document.title || '';
var rawPath = (window.location.pathname || '/').replace(/\/index\.html$/, '/');
// canonical URL without query string or hash
var canonicalUrl = window.location.origin + rawPath.replace(/\/*$/, '/');
var pageIdentifier = slugify(pageTitle) || slugify(rawPath);

var disqus_config = function () {
  this.page.url = canonicalUrl;
  this.page.identifier = pageIdentifier;
};

(function() {
  var d = document, s = d.createElement('script');
  s.src = 'https://luksamuk-codes.disqus.com/embed.js';
  s.setAttribute('data-timestamp', +new Date());
  (d.head || d.body).appendChild(s);
})();
