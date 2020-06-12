;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Base style sheet for testaments (RTF version)
;; Jon Bosak 1998.09.26
;;   Note that this version assumes 8.5 x 11 inch paper (US and Canada)
;;     and assumes that Word for Windows will be used for printouts
;;   This base file gets put together with either a set of styles
;;     peculiar to two-level testaments (NT, OT, BOM) or a set of
;;     styles peculiar to one-level testaments (Quran)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(declare-characteristic page-number-restart?
   "UNREGISTERED::James Clark//Characteristic::page-number-restart?" #f)

(declare-characteristic page-n-columns
   "UNREGISTERED::James Clark//Characteristic::page-n-columns" 1)

(declare-characteristic page-column-sep
   "UNREGISTERED::James Clark//Characteristic::page-column-sep" 2pica)

(declare-characteristic page-number-format
   "UNREGISTERED::James Clark//Characteristic::page-number-format" "1")

(declare-characteristic page-balance-columns?
   "UNREGISTERED::James Clark//Characteristic::page-balance-columns" #t)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; layout parameters
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define large #f) ;; can be overridden from the command line

(define %body-font-family% "Garamond")
(define %hf-font-family% "Garamond")
(define %title-font-family% "Garamond")
(define %line-spacing-factor% 1.2)
(define %bf-size% (if large 24pt 12pt))
(define %hf-size% (* %bf-size% 1.0))
(define %title-size% (* %bf-size% 3.0))
(define %title2-size% (* %bf-size% 2.0))
(define %subtitle-size% (* %bf-size% 1.5))
(define %ptitle-size% (* %bf-size% 1.25))
(define %bktitle-size% (* %bf-size% 1.6))
(define %chtitle-size% (* %bf-size% 1.5))
(define %chstitle-size% (* %bf-size% 0.9))
(define %tp-para-size% (* %bf-size% 1.25))
(define %preface-size% (* %bf-size% 0.96))
(define %toc-size% (* %bf-size% 1.0))
(define %summary-size% (* %bf-size% 0.9))
(define %vnum-size% (* %bf-size% 1.25))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; overall style
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define page-style
  (style
   page-width: 8.5in
   page-height: 11in
   left-margin: 6pica
   right-margin: 6pica
   top-margin: 6pica
   bottom-margin: 6pica
   header-margin: 3pica
   footer-margin: 3.5pica
   font-family-name: %body-font-family%
   font-size: %bf-size%
   line-spacing: (* %bf-size% %line-spacing-factor%)))

(define headerfooter-style
  (style
   font-size: %hf-size%
   font-family-name: %hf-font-family%
   line-spacing: (* %hf-size% %line-spacing-factor%)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; big pieces
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(element TSTMT
  (process-children))

(mode hf-mode
  (element TITLE (empty-sosofo))
  (element (COVERPG TITLE)
	   (make sequence
		 use: headerfooter-style))
  (element TITLE2 (empty-sosofo))
  (element BKTSHORT (process-children)))


(element COVERPG ($title-page$))
(element TITLEPG ($title-page$))

(define ($title-page$)
  (make simple-page-sequence
	use: page-style
	page-n-columns: 1))

(element PREFACE
  (make simple-page-sequence
	use: page-style
	page-balance-columns?: #f
	page-n-columns: 1
	page-number-restart?: #t))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; titles
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(element (COVERPG TITLE) ($titlepage-title$ 2.0))
(element (TITLEPG TITLE) ($titlepage-title$ 1.0))

(define ($titlepage-title$ vspace-factor)
  (make paragraph
	space-before: (* %title-size% vspace-factor)
	space-after: (* %title-size% vspace-factor)
	font-size: %title-size%
	font-family-name: %title-font-family%
	quadding: 'center
	font-weight: 'bold
	line-spacing: (* %title-size% %line-spacing-factor%)))

(element (COVERPG TITLE2) ($titlepage-title2$ (if large 1.0 2.0)))
(element (TITLEPG TITLE2) ($titlepage-title2$ (if large 0.5 1.0)))

(define ($titlepage-title2$ vspace-factor)
  (make paragraph
	space-before: (* %title2-size% vspace-factor 2.0)
	space-after: (if (last-sibling?)
			 0pt
		       (* %title2-size% vspace-factor 2.0))
	font-size: %title2-size%
	font-family-name: %title-font-family%
	quadding: 'center
	font-weight: 'bold
	line-spacing: (* %title2-size% %line-spacing-factor%)))

(element (COVERPG SUBTITLE) ($titlepage-subtitle$ (if large 1.5 3.0)))
(element (TITLEPG SUBTITLE) ($titlepage-subtitle$ (if large 1.5 3.0)))

(define ($titlepage-subtitle$ vspace-factor)
  (make paragraph
	space-before: (* %subtitle-size% vspace-factor)
	space-after: (if (last-sibling?)
			 0pt
		       (* %subtitle-size% vspace-factor))
	font-size: %subtitle-size%
	font-family-name: %title-font-family%
	quadding: 'center
	line-spacing: (* %subtitle-size% %line-spacing-factor%)))

(element (SUBTITLE P)
  (make paragraph
	space-before: 0pt
	space-after: 0pt))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; the toc mode (shared by both one-level and two-level testaments)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(mode toc
      (element BOOK (process-children))
      (element SURA (process-children))
      (element BKTLONG
	       (make paragraph
		     quadding: 'start
		     font-size: %toc-size%
		     space-before: (/ %toc-size% (if large 1.5 2.0))
		     space-after: (/ %toc-size% (if large 1.5 2.0))
		     (sosofo-append
		      (make link
			    destination: (current-node-address)
			    (with-mode #f (process-children)))
		      (make leader (literal "."))
		      (current-node-page-number-sosofo)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; lists
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(element WITLIST
  (make display-group
	space-before: %bf-size%
	space-after: %bf-size%))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; paragraphs
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(element (TITLEPG SUBTITLE P)
  (make paragraph
	space-before: (* %subtitle-size% (if large 1.5 2.0))
	space-after: (* %subtitle-size% (if large 1.5 2.0))))

(element (COVERPG P) ($title-para$))
(element (TITLEPG P) ($title-para$))

(define ($title-para$)
  (make paragraph
	space-before: (* %tp-para-size% (if large 0.5 1.0))
	space-after: (* %tp-para-size% (if large 0.5 1.0))
        font-size: %tp-para-size%
	line-spacing: (* %tp-para-size% %line-spacing-factor%)
	font-family-name: %title-font-family%
	quadding: 'center))

(element WITNESS
  (make paragraph
	space-before: 0pt
	space-after: 0pt
	font-posture: 'italic))

(element PTITLE0
  (make paragraph
	keep-with-next?: #t
	space-before: (* %bf-size% (if large 1.5 2.0))
	space-after: (* %bf-size% (if large 1.5 2.0))
	font-size: (* %bf-size% (if large 1.5 2.0))
	quadding: 'center
	font-family-name: %title-font-family%
	font-weight: 'bold))

(element PTITLE
  (make paragraph
	keep-with-next?: #t
	space-before: (if (first-sibling?)
			  0pt
			(* %ptitle-size% (if large 0.5 1.0)))
	space-after: (* %ptitle-size% (if large 0.5 1.0))
	font-size: %ptitle-size%
	line-spacing: (* %ptitle-size% %line-spacing-factor%)
	quadding: 'center
	font-family-name: %title-font-family%
	font-weight: 'bold))

(element P
  (make paragraph
	space-before: (* %bf-size% (if large 0.5 1.0))
	space-after: (* %bf-size% (if large 0.5 1.0))))

(element (PREFACE P)
  (make paragraph
	quadding: 'justify
	space-before: %preface-size%
	space-after: %preface-size%
	font-family-name: %title-font-family%
	font-size: %preface-size%))

(define ($summary-para$)
  (make paragraph
	quadding: 'justify
	keep-with-next?: #t
	space-before: (* (if large 1.25 1.5) %bf-size%)
	space-after: (* (if large 1.25 1.5) %bf-size%)
	font-size: %summary-size%
	font-posture: 'italic))

(element V
  (make paragraph
	space-before: (* %bf-size% (if large 0.5 1.0))
	space-after: (* %bf-size% (if large 0.5 1.0))
	(make sequence
	      font-size: %vnum-size%
	      font-weight: 'bold
	      font-family-name: %title-font-family%
	      (literal
	       (string-append
		(format-number (child-number)
			       "1") "\U-00A0" "\U-00A0")))
	(process-children)))

(element EPIGRAPH
  (make paragraph
	keep-with-next?: #t
	space-before: (* %bf-size% (if large 0.5 1.0))
	space-after: (* %bf-size% (if large 0.5 1.0))
	font-posture: 'italic))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; inlines
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(element I
  (make sequence
	font-posture: 'italic))