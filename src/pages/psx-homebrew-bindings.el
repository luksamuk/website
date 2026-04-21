;; PSX Homebrew bindings — uses navbar.el as single source of truth
(load-file "./src/navbar.el")

(setq org-html-preamble-format
      `(("en" ,(concat luksamuk-nav-wrapper-with-title "<h1 class=\"title\">%t</h1>"))
        ("pt_BR" ,(concat luksamuk-nav-wrapper-with-title "<h1 class=\"title\">%t</h1>")))
      org-html-postamble-format
      '(("en" "") ("pt_BR" "")))