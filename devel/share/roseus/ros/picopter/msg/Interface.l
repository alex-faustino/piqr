;; Auto-generated. Do not edit!


(when (boundp 'picopter::Interface)
  (if (not (find-package "PICOPTER"))
    (make-package "PICOPTER"))
  (shadow 'Interface (find-package "PICOPTER")))
(unless (find-package "PICOPTER::INTERFACE")
  (make-package "PICOPTER::INTERFACE"))

(in-package "ROS")
;;//! \htmlinclude Interface.msg.html


(defclass picopter::Interface
  :super ros::object
  :slots (_is_calibrated _flight_mode ))

(defmethod picopter::Interface
  (:init
   (&key
    ((:is_calibrated __is_calibrated) nil)
    ((:flight_mode __flight_mode) nil)
    )
   (send-super :init)
   (setq _is_calibrated __is_calibrated)
   (setq _flight_mode __flight_mode)
   self)
  (:is_calibrated
   (&optional __is_calibrated)
   (if __is_calibrated (setq _is_calibrated __is_calibrated)) _is_calibrated)
  (:flight_mode
   (&optional __flight_mode)
   (if __flight_mode (setq _flight_mode __flight_mode)) _flight_mode)
  (:serialization-length
   ()
   (+
    ;; bool _is_calibrated
    1
    ;; bool _flight_mode
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _is_calibrated
       (if _is_calibrated (write-byte -1 s) (write-byte 0 s))
     ;; bool _flight_mode
       (if _flight_mode (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _is_calibrated
     (setq _is_calibrated (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _flight_mode
     (setq _flight_mode (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get picopter::Interface :md5sum-) "aa23f60b03916a655a96c1c5cac351ad")
(setf (get picopter::Interface :datatype-) "picopter/Interface")
(setf (get picopter::Interface :definition-)
      "bool is_calibrated
bool flight_mode

")



(provide :picopter/Interface "aa23f60b03916a655a96c1c5cac351ad")


