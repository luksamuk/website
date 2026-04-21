;; Guilda de IA page bindings — uses navbar.el as single source of truth
;; Postamble returns to guild index
(load-file "./src/navbar.el")

(setq org-html-preamble-format
      `(("en" ,(concat luksamuk-nav-wrapper-with-title "<h1 class=\"title\">%t</h1>"))
        ("pt_BR" ,(concat luksamuk-nav-wrapper-with-title "<h1 class=\"title\">%t</h1>")))
       org-html-postamble-format
      '(("en" "<h3><a href=\"/pages/guilda-ia/\">&#8592; Back to Guilda de IA</a></h3>")
        ("pt_BR" "<h3><a href=\"/pages/guilda-ia/\">&#8592; Voltar para Guilda de IA</a></h3>")))