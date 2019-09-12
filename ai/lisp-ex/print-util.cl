(defun print-null (stream obj)
  (format stream "()") )

(defun print-nil-as-empty ()
  (set-pprint-dispatch 'null #'print-null))

(defmacro echo-run-line (&body body)
  (let ((p (car body)))
    (format t "expression: ~c[96m~:a~c[0m~%    result: ~c[93m~:a~c[0m~%~%" 
      #\ESC p #\ESC #\ESC (eval p) #\ESC)))
