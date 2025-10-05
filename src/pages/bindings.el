(setq org-html-preamble-format
      '(("en" "<nav><h1><a href=\"../\">The Alchemist's Hideout</a></h1></nav><h1 class=\"title\">%t</h1>")
        ("pt_BR" "<nav><h1><a href=\"../\">The Alchemist's Hideout</a></h1></nav><h1 class=\"title\">%t</h1>"))
      org-html-postamble-format
      '(("en" "<h3><a href=\"../\">Back to last page</a></h3>")
        ("pt_BR" "<h3><a href=\"../\">De volta à página anterior</a></h3>")))

;; --- Vibe-coded stuff so we can generate og: and twitter: meta tags ---

(defun my/org-expand-head-macros-after-export (output backend info)
  "Replace {{{title}}}, {{{author}}}, {{{date}}}, {{{description}}}, and {{{filename}}} in final HTML head."
  (when (org-export-derived-backend-p backend 'html)
    (let* ((escape-html
            (lambda (s)
              (when s
                (replace-regexp-in-string
                 "&" "&amp;"
                 (replace-regexp-in-string
                  "<" "&lt;"
                  (replace-regexp-in-string
                   ">" "&gt;"
                   (replace-regexp-in-string
                    "\"" "&quot;" s)))))))
           (title  (funcall escape-html (org-export-data (plist-get info :title) info)))
           (author (funcall escape-html (org-export-data (plist-get info :author) info)))
           (date   (funcall escape-html (org-export-data (plist-get info :date) info)))
           (desc   (funcall escape-html (org-export-data (plist-get info :description) info)))
           (filename (funcall escape-html (file-name-base (or (buffer-file-name) "")))))
      (dolist (pair `(("{{{title}}}" . ,title)
                      ("{{{author}}}" . ,author)
                      ("{{{date}}}" . ,date)
                      ("{{{description}}}" . ,desc)
                      ("{{{filename}}}" . ,filename)))
        (setq output (replace-regexp-in-string (car pair) (or (cdr pair) "") output t t)))
      output)))

(add-to-list 'org-export-filter-final-output-functions #'my/org-expand-head-macros-after-export)
