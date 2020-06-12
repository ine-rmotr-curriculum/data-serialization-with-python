;; specific styles for two-level testaments (like Old Testament,
;;   New Testament, Book of Mormon; note that the last has suras!)

(element BOOK ($booklevel-division$))
(element SURA ($booklevel-division$))

(define ($booklevel-division$)
 (let ((page-header-left
	(make sequence
	      use: headerfooter-style
	      font-posture: 'italic
	      (with-mode hf-mode
		(process-node-list
		 (select-elements
		  (descendants (ancestor "TSTMT"))
		  "TITLE")))))
       (page-header-right
	(make sequence
	      use: headerfooter-style
	      font-posture: 'italic
	      (with-mode hf-mode (process-first-descendant "BKTSHORT"))))
       (page-folio
	(make sequence
	      use: headerfooter-style
	      font-posture: 'upright
	      (page-number-sosofo))))
   (make simple-page-sequence
	   page-number-restart?: (absolute-first-sibling?)
	   use: page-style
	   page-n-columns: (if large 1 2)
	   page-balance-columns?: #t
	   left-header: page-header-left
	   right-header: page-header-right
	   center-footer: page-folio
	   input-whitespace-treatment: 'collapse
	   quadding: 'justify)))

(element CHAPTER (process-children))

(element BKTLONG
  (make paragraph
	space-before: 0pt
	space-after: %bktitle-size%
	font-size: %bktitle-size%
	line-spacing: (* %bktitle-size% %line-spacing-factor%)
	font-family-name: %title-font-family%
	font-weight: 'bold
	quadding: 'center
	(process-children)))

(element BKTSHORT (empty-sosofo))

(element CHTITLE
  (make paragraph
	quadding: 'center
	keep-with-next?: #t
	space-before: (/ (* %chtitle-size% 5) 3)
	space-after: %chtitle-size%
	font-size: %chtitle-size%
	font-family-name: %title-font-family%
	font-weight: 'bold))

(element CHSTITLE
  (make paragraph
	quadding: 'center
	keep-with-next?: #t
	space-before: %chstitle-size%
	space-after: %chstitle-size%
	font-size: %chstitle-size%
	font-family-name: %title-font-family%))

(element (BKSUM P) ($summary-para$))
(element (CHSUM P) ($summary-para$))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; the table of contents
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(element BOOKCOLL
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
  (process-children)))
