(load "print-util.cl")

;; uncomment this function if you want print nil as ()
;; (print-nil-as-empty)


(defun my-adjoin (n L)
  (cond ((member n L) L)
		    (t (cons n L))))

(echo-run-line (adjoin 'a '(b c d a)))
(echo-run-line (my-adjoin 'a '(b c d a)))
;; (b c d a)

(echo-run-line (adjoin 2 '(3 4 5)))
(echo-run-line (my-adjoin 2 '(3 4 5)))
;; (2 3 4 5)
