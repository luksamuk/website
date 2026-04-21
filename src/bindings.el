;; Posts bindings — uses navbar.el as single source of truth
(load-file "./src/navbar.el")

(setq org-html-preamble-format
      `(("en" ,(concat luksamuk-nav-wrapper-with-title "<h1 class=\"title\">%t</h1><p><i>Written in %d by %a</i></p>"))
        ("pt_BR" ,(concat luksamuk-nav-wrapper-with-title "<h1 class=\"title\">%t</h1><p><i>Escrito em %d por %a</i></p>")))
       ;; Postamble com aviso sobre Lei Felca em vez de comentários
       org-html-postamble-format
      '(("en" "<h3><a href=\"/pages/blog.html\">&#8592; Back to Blog</a></h3><p style=\"font-size: 0.85em; color: #888; margin-top: 1em; padding: 0.5em; border-left: 3px solid #555;\">Comments have been disabled due to Brazil's <a href=\"https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15211.htm\" style=\"color: #888; text-decoration: underline;\">Law 15.211/2025</a> (ECA Digital). This law imposes heavy moderation requirements even on small personal sites, making interactive features impractical for independent creators.</p>")
        ("pt_BR" "<h3><a href=\"/pages/blog.html\">&#8592; Voltar ao Blog</a></h3><p style=\"font-size: 0.85em; color: #888; margin-top: 1em; padding: 0.5em; border-left: 3px solid #555;\">Os comentários foram desativados em razão da <a href=\"https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15211.htm\" style=\"color: #888; text-decoration: underline;\">Lei 15.211/2025</a> (ECA Digital, \"Lei Felca\"). A legislação impõe exigências de moderação que inviabilizam recursos interativos em sites pessoais sem estrutura para tanto.</p>")))