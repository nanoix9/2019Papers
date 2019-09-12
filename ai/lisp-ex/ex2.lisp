(defmacro echo-run-line (&body body)
  (let ((p (car body)))
    (format t "expression: ~c[96m~:a~c[0m~%    result: ~c[93m~:a~c[0m~%~%" 
      #\ESC p #\ESC #\ESC (eval p) #\ESC)))

(defun drop-x (n L)
  (cond ((= n 0) L)
        ((null L) nil)
        (t (drop-x (- n 1) (cdr L)))))

(echo-run-line (drop-x 0 '(a b c d)))
(echo-run-line (drop-x 2 '(a b c d)))
(echo-run-line (drop-x 3 '(a b)))

(defun rdrop-x (n L)
  (cond ((>= n (length L)) nil)
        ((null L) nil)
        (t (cons (car L) (rdrop-x n (cdr L))))))

(echo-run-line (rdrop-x 0 '(a b c d)))
(echo-run-line (rdrop-x 2 '(a b c d)))
(echo-run-line (rdrop-x 3 '(a b)))

(defun combine2 (L)
  (cond ((null L) nil)
        (t 
          (let ((hd (cdr (car L))) 
                (tl (combine2 (cdr L))))
            (if (null hd) tl (cons hd tl))))))

(echo-run-line (combine2 '((1 2 3) (a) (4 5 6) (7 8 9))))
;; ((2 3) (5 6) (8 9))

(defun ddrop-x (n m L) (drop-x n (rdrop-x m L)))
(defun combine3 (L)
  (cond ((null L) nil)
        (t (cons (ddrop-x 1 1 (car L)) (combine3 (cdr L))))))

(echo-run-line (combine3 '((1 2 3) (a) (4 5 6) (7 8) (a b c d e))))
;; ((2) () (5) () (b c d))
