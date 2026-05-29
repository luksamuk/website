// Fix org-reveal syntax highlighting: class="python" -> class="language-python"
// org-reveal generates class="python" but highlight.js expects class="language-*"
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('pre code').forEach(function(block) {
        var cls = block.className.trim();
        if (cls && !cls.startsWith('language-') && !cls.startsWith('hljs')) {
            block.className = 'language-' + cls;
        }
    });
    // Re-trigger highlight.js
    if (typeof hljs !== 'undefined') {
        hljs.highlightAll();
    }
});