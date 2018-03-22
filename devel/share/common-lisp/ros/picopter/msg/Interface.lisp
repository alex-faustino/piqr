; Auto-generated. Do not edit!


(cl:in-package picopter-msg)


;//! \htmlinclude Interface.msg.html

(cl:defclass <Interface> (roslisp-msg-protocol:ros-message)
  ((is_calibrated
    :reader is_calibrated
    :initarg :is_calibrated
    :type cl:boolean
    :initform cl:nil)
   (flight_mode
    :reader flight_mode
    :initarg :flight_mode
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Interface (<Interface>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Interface>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Interface)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name picopter-msg:<Interface> is deprecated: use picopter-msg:Interface instead.")))

(cl:ensure-generic-function 'is_calibrated-val :lambda-list '(m))
(cl:defmethod is_calibrated-val ((m <Interface>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader picopter-msg:is_calibrated-val is deprecated.  Use picopter-msg:is_calibrated instead.")
  (is_calibrated m))

(cl:ensure-generic-function 'flight_mode-val :lambda-list '(m))
(cl:defmethod flight_mode-val ((m <Interface>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader picopter-msg:flight_mode-val is deprecated.  Use picopter-msg:flight_mode instead.")
  (flight_mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Interface>) ostream)
  "Serializes a message object of type '<Interface>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'is_calibrated) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'flight_mode) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Interface>) istream)
  "Deserializes a message object of type '<Interface>"
    (cl:setf (cl:slot-value msg 'is_calibrated) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'flight_mode) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Interface>)))
  "Returns string type for a message object of type '<Interface>"
  "picopter/Interface")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Interface)))
  "Returns string type for a message object of type 'Interface"
  "picopter/Interface")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Interface>)))
  "Returns md5sum for a message object of type '<Interface>"
  "aa23f60b03916a655a96c1c5cac351ad")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Interface)))
  "Returns md5sum for a message object of type 'Interface"
  "aa23f60b03916a655a96c1c5cac351ad")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Interface>)))
  "Returns full string definition for message of type '<Interface>"
  (cl:format cl:nil "bool is_calibrated~%bool flight_mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Interface)))
  "Returns full string definition for message of type 'Interface"
  (cl:format cl:nil "bool is_calibrated~%bool flight_mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Interface>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Interface>))
  "Converts a ROS message object to a list"
  (cl:list 'Interface
    (cl:cons ':is_calibrated (is_calibrated msg))
    (cl:cons ':flight_mode (flight_mode msg))
))
