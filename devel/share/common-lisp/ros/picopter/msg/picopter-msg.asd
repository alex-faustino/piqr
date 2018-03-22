
(cl:in-package :asdf)

(defsystem "picopter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IMUOutput" :depends-on ("_package_IMUOutput"))
    (:file "_package_IMUOutput" :depends-on ("_package"))
    (:file "Interface" :depends-on ("_package_Interface"))
    (:file "_package_Interface" :depends-on ("_package"))
    (:file "SpinRates" :depends-on ("_package_SpinRates"))
    (:file "_package_SpinRates" :depends-on ("_package"))
  ))