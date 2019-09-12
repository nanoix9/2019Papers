(defun print-null (stream obj)
  (format stream "()") )

(defun print-nil-as-empty ()
  (set-pprint-dispatch 'null #'print-null))

(defmacro echo-run-line (expr expected)
  (format t "expression: ~c[95m~a~c[0m~%  expected: ~c[96m~a~c[0m~%    result: ~c[93m~a~c[0m~%~%" 
    #\ESC expr #\ESC #\ESC expected #\ESC #\ESC (eval expr) #\ESC))
