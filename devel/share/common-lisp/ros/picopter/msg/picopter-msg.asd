
(cl:in-package :asdf)

(defsystem "picopter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IMUOutput" :depends-on ("_package_IMUOutput"))
    (:file "_package_IMUOutput" :depends-on ("_package"))
  ))