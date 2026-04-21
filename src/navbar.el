;; navbar.el — Single source of truth for the site navbar.
;; Loaded by all bindings.el files via (load "./navbar.el")
;; To change the navbar, edit ONLY this file.

;; Navbar HTML snippet WITHOUT site-title (for index.org which has its own hero title)
(defvar luksamuk-nav-wrapper
  "<div id=\"nav-wrapper\"><nav id=\"site-nav\"><a href=\"/\"><i class=\"fa-solid fa-house\"></i> Home</a> <a href=\"/pages/about.html\"><i class=\"fa-solid fa-user\"></i> About</a> <a href=\"/pages/games.html\"><i class=\"fa-solid fa-gamepad\"></i> Games</a> <a href=\"/pages/portfolio.html\"><i class=\"fa-solid fa-briefcase\"></i> Portfolio</a> <a href=\"/pages/learn.html\"><i class=\"fa-solid fa-book-open\"></i> Learn</a> <a href=\"/pages/talks-index.html\"><i class=\"fa-solid fa-chalkboard-user\"></i> Talks</a> <a href=\"/pages/blog.html\"><i class=\"fa-solid fa-rss\"></i> Blog</a> <button id=\"theme-selector\" onclick=\"toggleTheme()\"><i class=\"fa-solid fa-moon\"></i></button></nav></div>"

  "Navbar HTML without site-title — for index.org (has hero).")

;; Navbar HTML snippet WITH site-title (for subpages that need a header anchor)
(defvar luksamuk-nav-wrapper-with-title
  "<div id=\"nav-wrapper\"><nav id=\"site-nav\"><a href=\"/\"><i class=\"fa-solid fa-house\"></i> Home</a> <a href=\"/pages/about.html\"><i class=\"fa-solid fa-user\"></i> About</a> <a href=\"/pages/games.html\"><i class=\"fa-solid fa-gamepad\"></i> Games</a> <a href=\"/pages/portfolio.html\"><i class=\"fa-solid fa-briefcase\"></i> Portfolio</a> <a href=\"/pages/learn.html\"><i class=\"fa-solid fa-book-open\"></i> Learn</a> <a href=\"/pages/talks-index.html\"><i class=\"fa-solid fa-chalkboard-user\"></i> Talks</a> <a href=\"/pages/blog.html\"><i class=\"fa-solid fa-rss\"></i> Blog</a> <button id=\"theme-selector\" onclick=\"toggleTheme()\"><i class=\"fa-solid fa-moon\"></i></button></nav><h1 class=\"site-title\"><a href=\"/\">The Alchemist's Hideout</a></h1></div>"

  "Navbar HTML with site-title — for subpages without hero section.")