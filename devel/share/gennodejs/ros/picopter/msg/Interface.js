// Auto-generated. Do not edit!

// (in-package picopter.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Interface {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.is_calibrated = null;
      this.arm_esc = null;
      this.flight_mode = null;
      this.stop_motors = null;
      this.shutdown = null;
    }
    else {
      if (initObj.hasOwnProperty('is_calibrated')) {
        this.is_calibrated = initObj.is_calibrated
      }
      else {
        this.is_calibrated = false;
      }
      if (initObj.hasOwnProperty('arm_esc')) {
        this.arm_esc = initObj.arm_esc
      }
      else {
        this.arm_esc = false;
      }
      if (initObj.hasOwnProperty('flight_mode')) {
        this.flight_mode = initObj.flight_mode
      }
      else {
        this.flight_mode = false;
      }
      if (initObj.hasOwnProperty('stop_motors')) {
        this.stop_motors = initObj.stop_motors
      }
      else {
        this.stop_motors = false;
      }
      if (initObj.hasOwnProperty('shutdown')) {
        this.shutdown = initObj.shutdown
      }
      else {
        this.shutdown = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Interface
    // Serialize message field [is_calibrated]
    bufferOffset = _serializer.bool(obj.is_calibrated, buffer, bufferOffset);
    // Serialize message field [arm_esc]
    bufferOffset = _serializer.bool(obj.arm_esc, buffer, bufferOffset);
    // Serialize message field [flight_mode]
    bufferOffset = _serializer.bool(obj.flight_mode, buffer, bufferOffset);
    // Serialize message field [stop_motors]
    bufferOffset = _serializer.bool(obj.stop_motors, buffer, bufferOffset);
    // Serialize message field [shutdown]
    bufferOffset = _serializer.bool(obj.shutdown, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Interface
    let len;
    let data = new Interface(null);
    // Deserialize message field [is_calibrated]
    data.is_calibrated = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [arm_esc]
    data.arm_esc = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [flight_mode]
    data.flight_mode = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [stop_motors]
    data.stop_motors = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [shutdown]
    data.shutdown = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'picopter/Interface';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd48df5094a97ac2271d10199017658de';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool is_calibrated
    bool arm_esc
    bool flight_mode
    bool stop_motors
    bool shutdown
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Interface(null);
    if (msg.is_calibrated !== undefined) {
      resolved.is_calibrated = msg.is_calibrated;
    }
    else {
      resolved.is_calibrated = false
    }

    if (msg.arm_esc !== undefined) {
      resolved.arm_esc = msg.arm_esc;
    }
    else {
      resolved.arm_esc = false
    }

    if (msg.flight_mode !== undefined) {
      resolved.flight_mode = msg.flight_mode;
    }
    else {
      resolved.flight_mode = false
    }

    if (msg.stop_motors !== undefined) {
      resolved.stop_motors = msg.stop_motors;
    }
    else {
      resolved.stop_motors = false
    }

    if (msg.shutdown !== undefined) {
      resolved.shutdown = msg.shutdown;
    }
    else {
      resolved.shutdown = false
    }

    return resolved;
    }
};

module.exports = Interface;
