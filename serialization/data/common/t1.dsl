;; specific styles for one-level testaments (like the Quran)
;;   that consist entirely of suras

(element SURACOLL
 (let ((page-header-center
	(make sequence
	      use: headerfooter-style
	      (with-mode hf-mode
		(process-node-list
		 (select-elements
		  (descendants (ancestor "TSTMT"))
		  "TITLE")))))
       (page-folio
	(make sequence
	      use: headerfooter-style
	      (page-number-sosofo))))
   (sosofo-append
    (make simple-page-sequence
	  use: page-style
	  page-n-columns: 1
	  page-number-restart?: #t
	  (make paragraph
		quadding: 'center
		keep-with-next?: #t
		font-family-name: %title-font-family%
		font-weight: 'bold
		font-size: %title2-size%
		line-spacing: (* %title2-size% %line-spacing-factor%)
		space-after: (* %title2-size% 1.5)
		(literal "Table of Contents"))
	  (with-mode toc ;; defined in base.dsl
		     (sosofo-append
		      (process-node-list
		       (select-elements
			(descendants (ancestor "TSTMT"))
			"BKTLONG")))))
    (make simple-page-sequence
	  page-number-restart?: #t
	  use: page-style
	  page-n-columns: (if large 1 2)
	  page-balance-columns?: #t
	  center-header: page-header-center
	  center-footer: page-folio
	  input-whitespace-treatment: 'collapse
	  quadding: 'justify
	  (process-children)))))

(element SURA (process-children))

(element BKTLONG
	 (make paragraph
	       quadding: 'center
	       keep-with-next?: #t
	       space-before: (/ (* %chtitle-size% 5) 3)
	       space-after: %chtitle-size%
	       font-size: %chtitle-size%
	       font-family-name: %title-font-family%
	       font-weight: 'bold))

(element BKTSHORT (empty-sosofo))

