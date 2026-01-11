;; --- Vibe-coded stuff so we can generate og: and twitter: meta tags ---

(defun my/org-expand-head-macros-after-export (output backend info)
  "Replace {{{title}}}, {{{author}}}, {{{date}}}, {{{description}}}, {{{email}}}, and {{{thumbnail}}} in final HTML head.
The {{{email}}} macro is obfuscated as HTML entities. The {{{thumbnail}}} macro looks for a thumbnail image."
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
           (obfuscate-email
            (lambda (email)
              (apply #'concat
                     (mapcar (lambda (c)
                               (format "&#%d;" c))
                             (string-to-list email)))))
           (title  (funcall escape-html (org-export-data (plist-get info :title) info)))
           (author (funcall escape-html (org-export-data (plist-get info :author) info)))
           (date   (funcall escape-html (org-export-data (plist-get info :date) info)))
           (desc   (funcall escape-html (org-export-data (plist-get info :description) info)))
           (email  (funcall obfuscate-email "lucasvieira@protonmail.com"))
           (filename (file-name-sans-extension
                      (file-name-nondirectory (plist-get info :input-file))))
           (thumbnail
            (let ((thumbnail-path (expand-file-name (format "img/thumb-%s.png" filename)
                                                    (file-name-directory (plist-get info :input-file)))))
              (if (file-exists-p thumbnail-path)
                  (concat "https://luksamuk.codes/posts/img/thumb-" filename ".png")
                "https://luksamuk.codes/img/banner-full.png"))))
      (dolist (pair `(("{{{title}}}" . ,title)
                      ("{{{author}}}" . ,author)
                      ("{{{date}}}" . ,date)
                      ("{{{description}}}" . ,desc)
                      ("{{{filename}}}" . ,filename)
                      ("{{{email}}}" . ,email)
                      ("{{{thumbnail}}}" . ,thumbnail)))
        (setq output (replace-regexp-in-string (car pair) (or (cdr pair) "") output t t)))
      output)))

(add-to-list 'org-export-filter-final-output-functions #'my/org-expand-head-macros-after-export)
