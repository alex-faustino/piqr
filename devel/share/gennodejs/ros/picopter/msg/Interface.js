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
      this.flight_mode = null;
    }
    else {
      if (initObj.hasOwnProperty('is_calibrated')) {
        this.is_calibrated = initObj.is_calibrated
      }
      else {
        this.is_calibrated = false;
      }
      if (initObj.hasOwnProperty('flight_mode')) {
        this.flight_mode = initObj.flight_mode
      }
      else {
        this.flight_mode = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Interface
    // Serialize message field [is_calibrated]
    bufferOffset = _serializer.bool(obj.is_calibrated, buffer, bufferOffset);
    // Serialize message field [flight_mode]
    bufferOffset = _serializer.bool(obj.flight_mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Interface
    let len;
    let data = new Interface(null);
    // Deserialize message field [is_calibrated]
    data.is_calibrated = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [flight_mode]
    data.flight_mode = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'picopter/Interface';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'aa23f60b03916a655a96c1c5cac351ad';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool is_calibrated
    bool flight_mode
    
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

    if (msg.flight_mode !== undefined) {
      resolved.flight_mode = msg.flight_mode;
    }
    else {
      resolved.flight_mode = false
    }

    return resolved;
    }
};

module.exports = Interface;
