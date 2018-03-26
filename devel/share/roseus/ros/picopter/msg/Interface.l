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
  :slots (_is_calibrated _arm_esc _flight_mode _stop_motors _shutdown ))

(defmethod picopter::Interface
  (:init
   (&key
    ((:is_calibrated __is_calibrated) nil)
    ((:arm_esc __arm_esc) nil)
    ((:flight_mode __flight_mode) nil)
    ((:stop_motors __stop_motors) nil)
    ((:shutdown __shutdown) nil)
    )
   (send-super :init)
   (setq _is_calibrated __is_calibrated)
   (setq _arm_esc __arm_esc)
   (setq _flight_mode __flight_mode)
   (setq _stop_motors __stop_motors)
   (setq _shutdown __shutdown)
   self)
  (:is_calibrated
   (&optional __is_calibrated)
   (if __is_calibrated (setq _is_calibrated __is_calibrated)) _is_calibrated)
  (:arm_esc
   (&optional __arm_esc)
   (if __arm_esc (setq _arm_esc __arm_esc)) _arm_esc)
  (:flight_mode
   (&optional __flight_mode)
   (if __flight_mode (setq _flight_mode __flight_mode)) _flight_mode)
  (:stop_motors
   (&optional __stop_motors)
   (if __stop_motors (setq _stop_motors __stop_motors)) _stop_motors)
  (:shutdown
   (&optional __shutdown)
   (if __shutdown (setq _shutdown __shutdown)) _shutdown)
  (:serialization-length
   ()
   (+
    ;; bool _is_calibrated
    1
    ;; bool _arm_esc
    1
    ;; bool _flight_mode
    1
    ;; bool _stop_motors
    1
    ;; bool _shutdown
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _is_calibrated
       (if _is_calibrated (write-byte -1 s) (write-byte 0 s))
     ;; bool _arm_esc
       (if _arm_esc (write-byte -1 s) (write-byte 0 s))
     ;; bool _flight_mode
       (if _flight_mode (write-byte -1 s) (write-byte 0 s))
     ;; bool _stop_motors
       (if _stop_motors (write-byte -1 s) (write-byte 0 s))
     ;; bool _shutdown
       (if _shutdown (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _is_calibrated
     (setq _is_calibrated (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _arm_esc
     (setq _arm_esc (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _flight_mode
     (setq _flight_mode (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _stop_motors
     (setq _stop_motors (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _shutdown
     (setq _shutdown (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get picopter::Interface :md5sum-) "d48df5094a97ac2271d10199017658de")
(setf (get picopter::Interface :datatype-) "picopter/Interface")
(setf (get picopter::Interface :definition-)
      "bool is_calibrated
bool arm_esc
bool flight_mode
bool stop_motors
bool shutdown

")



(provide :picopter/Interface "d48df5094a97ac2271d10199017658de")


