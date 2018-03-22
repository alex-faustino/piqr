; Auto-generated. Do not edit!


(cl:in-package picopter-msg)


;//! \htmlinclude SpinRates.msg.html

(cl:defclass <SpinRates> (roslisp-msg-protocol:ros-message)
  ((motor_one
    :reader motor_one
    :initarg :motor_one
    :type cl:float
    :initform 0.0)
   (motor_two
    :reader motor_two
    :initarg :motor_two
    :type cl:float
    :initform 0.0)
   (motor_three
    :reader motor_three
    :initarg :motor_three
    :type cl:float
    :initform 0.0)
   (motor_four
    :reader motor_four
    :initarg :motor_four
    :type cl:float
    :initform 0.0))
)

(cl:defclass SpinRates (<SpinRates>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SpinRates>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SpinRates)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name picopter-msg:<SpinRates> is deprecated: use picopter-msg:SpinRates instead.")))

(cl:ensure-generic-function 'motor_one-val :lambda-list '(m))
(cl:defmethod motor_one-val ((m <SpinRates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader picopter-msg:motor_one-val is deprecated.  Use picopter-msg:motor_one instead.")
  (motor_one m))

(cl:ensure-generic-function 'motor_two-val :lambda-list '(m))
(cl:defmethod motor_two-val ((m <SpinRates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader picopter-msg:motor_two-val is deprecated.  Use picopter-msg:motor_two instead.")
  (motor_two m))

(cl:ensure-generic-function 'motor_three-val :lambda-list '(m))
(cl:defmethod motor_three-val ((m <SpinRates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader picopter-msg:motor_three-val is deprecated.  Use picopter-msg:motor_three instead.")
  (motor_three m))

(cl:ensure-generic-function 'motor_four-val :lambda-list '(m))
(cl:defmethod motor_four-val ((m <SpinRates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader picopter-msg:motor_four-val is deprecated.  Use picopter-msg:motor_four instead.")
  (motor_four m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SpinRates>) ostream)
  "Serializes a message object of type '<SpinRates>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'motor_one))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'motor_two))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'motor_three))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'motor_four))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SpinRates>) istream)
  "Deserializes a message object of type '<SpinRates>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_one) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_two) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_three) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_four) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SpinRates>)))
  "Returns string type for a message object of type '<SpinRates>"
  "picopter/SpinRates")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SpinRates)))
  "Returns string type for a message object of type 'SpinRates"
  "picopter/SpinRates")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SpinRates>)))
  "Returns md5sum for a message object of type '<SpinRates>"
  "fb6650b063ad3f7904bcf518d546f7ec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SpinRates)))
  "Returns md5sum for a message object of type 'SpinRates"
  "fb6650b063ad3f7904bcf518d546f7ec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SpinRates>)))
  "Returns full string definition for message of type '<SpinRates>"
  (cl:format cl:nil "float64 motor_one~%float64 motor_two~%float64 motor_three~%float64 motor_four~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SpinRates)))
  "Returns full string definition for message of type 'SpinRates"
  (cl:format cl:nil "float64 motor_one~%float64 motor_two~%float64 motor_three~%float64 motor_four~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SpinRates>))
  (cl:+ 0
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SpinRates>))
  "Converts a ROS message object to a list"
  (cl:list 'SpinRates
    (cl:cons ':motor_one (motor_one msg))
    (cl:cons ':motor_two (motor_two msg))
    (cl:cons ':motor_three (motor_three msg))
    (cl:cons ':motor_four (motor_four msg))
))
