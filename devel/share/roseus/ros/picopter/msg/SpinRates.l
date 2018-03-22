;; Auto-generated. Do not edit!


(when (boundp 'picopter::SpinRates)
  (if (not (find-package "PICOPTER"))
    (make-package "PICOPTER"))
  (shadow 'SpinRates (find-package "PICOPTER")))
(unless (find-package "PICOPTER::SPINRATES")
  (make-package "PICOPTER::SPINRATES"))

(in-package "ROS")
;;//! \htmlinclude SpinRates.msg.html


(defclass picopter::SpinRates
  :super ros::object
  :slots (_motor_one _motor_two _motor_three _motor_four ))

(defmethod picopter::SpinRates
  (:init
   (&key
    ((:motor_one __motor_one) 0.0)
    ((:motor_two __motor_two) 0.0)
    ((:motor_three __motor_three) 0.0)
    ((:motor_four __motor_four) 0.0)
    )
   (send-super :init)
   (setq _motor_one (float __motor_one))
   (setq _motor_two (float __motor_two))
   (setq _motor_three (float __motor_three))
   (setq _motor_four (float __motor_four))
   self)
  (:motor_one
   (&optional __motor_one)
   (if __motor_one (setq _motor_one __motor_one)) _motor_one)
  (:motor_two
   (&optional __motor_two)
   (if __motor_two (setq _motor_two __motor_two)) _motor_two)
  (:motor_three
   (&optional __motor_three)
   (if __motor_three (setq _motor_three __motor_three)) _motor_three)
  (:motor_four
   (&optional __motor_four)
   (if __motor_four (setq _motor_four __motor_four)) _motor_four)
  (:serialization-length
   ()
   (+
    ;; float64 _motor_one
    8
    ;; float64 _motor_two
    8
    ;; float64 _motor_three
    8
    ;; float64 _motor_four
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _motor_one
       (sys::poke _motor_one (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _motor_two
       (sys::poke _motor_two (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _motor_three
       (sys::poke _motor_three (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _motor_four
       (sys::poke _motor_four (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _motor_one
     (setq _motor_one (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _motor_two
     (setq _motor_two (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _motor_three
     (setq _motor_three (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _motor_four
     (setq _motor_four (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get picopter::SpinRates :md5sum-) "fb6650b063ad3f7904bcf518d546f7ec")
(setf (get picopter::SpinRates :datatype-) "picopter/SpinRates")
(setf (get picopter::SpinRates :definition-)
      "float64 motor_one
float64 motor_two
float64 motor_three
float64 motor_four

")



(provide :picopter/SpinRates "fb6650b063ad3f7904bcf518d546f7ec")


