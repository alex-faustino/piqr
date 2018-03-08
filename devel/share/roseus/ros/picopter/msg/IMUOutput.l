;; Auto-generated. Do not edit!


(when (boundp 'picopter::IMUOutput)
  (if (not (find-package "PICOPTER"))
    (make-package "PICOPTER"))
  (shadow 'IMUOutput (find-package "PICOPTER")))
(unless (find-package "PICOPTER::IMUOUTPUT")
  (make-package "PICOPTER::IMUOUTPUT"))

(in-package "ROS")
;;//! \htmlinclude IMUOutput.msg.html


(defclass picopter::IMUOutput
  :super ros::object
  :slots (_time _accel_x _accel_y _accel_z _gyro_x _gyro_y _gyro_z ))

(defmethod picopter::IMUOutput
  (:init
   (&key
    ((:time __time) 0.0)
    ((:accel_x __accel_x) 0.0)
    ((:accel_y __accel_y) 0.0)
    ((:accel_z __accel_z) 0.0)
    ((:gyro_x __gyro_x) 0.0)
    ((:gyro_y __gyro_y) 0.0)
    ((:gyro_z __gyro_z) 0.0)
    )
   (send-super :init)
   (setq _time (float __time))
   (setq _accel_x (float __accel_x))
   (setq _accel_y (float __accel_y))
   (setq _accel_z (float __accel_z))
   (setq _gyro_x (float __gyro_x))
   (setq _gyro_y (float __gyro_y))
   (setq _gyro_z (float __gyro_z))
   self)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:accel_x
   (&optional __accel_x)
   (if __accel_x (setq _accel_x __accel_x)) _accel_x)
  (:accel_y
   (&optional __accel_y)
   (if __accel_y (setq _accel_y __accel_y)) _accel_y)
  (:accel_z
   (&optional __accel_z)
   (if __accel_z (setq _accel_z __accel_z)) _accel_z)
  (:gyro_x
   (&optional __gyro_x)
   (if __gyro_x (setq _gyro_x __gyro_x)) _gyro_x)
  (:gyro_y
   (&optional __gyro_y)
   (if __gyro_y (setq _gyro_y __gyro_y)) _gyro_y)
  (:gyro_z
   (&optional __gyro_z)
   (if __gyro_z (setq _gyro_z __gyro_z)) _gyro_z)
  (:serialization-length
   ()
   (+
    ;; float64 _time
    8
    ;; float64 _accel_x
    8
    ;; float64 _accel_y
    8
    ;; float64 _accel_z
    8
    ;; float64 _gyro_x
    8
    ;; float64 _gyro_y
    8
    ;; float64 _gyro_z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _time
       (sys::poke _time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _accel_x
       (sys::poke _accel_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _accel_y
       (sys::poke _accel_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _accel_z
       (sys::poke _accel_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyro_x
       (sys::poke _gyro_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyro_y
       (sys::poke _gyro_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyro_z
       (sys::poke _gyro_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _time
     (setq _time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _accel_x
     (setq _accel_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _accel_y
     (setq _accel_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _accel_z
     (setq _accel_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyro_x
     (setq _gyro_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyro_y
     (setq _gyro_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyro_z
     (setq _gyro_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get picopter::IMUOutput :md5sum-) "f03e5464fec14a666cf3eccb3ae01be0")
(setf (get picopter::IMUOutput :datatype-) "picopter/IMUOutput")
(setf (get picopter::IMUOutput :definition-)
      "float64 time
float64 accel_x
float64 accel_y
float64 accel_z
float64 gyro_x
float64 gyro_y
float64 gyro_z

")



(provide :picopter/IMUOutput "f03e5464fec14a666cf3eccb3ae01be0")


