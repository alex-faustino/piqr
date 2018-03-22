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

class SpinRates {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motor_one = null;
      this.motor_two = null;
      this.motor_three = null;
      this.motor_four = null;
    }
    else {
      if (initObj.hasOwnProperty('motor_one')) {
        this.motor_one = initObj.motor_one
      }
      else {
        this.motor_one = 0.0;
      }
      if (initObj.hasOwnProperty('motor_two')) {
        this.motor_two = initObj.motor_two
      }
      else {
        this.motor_two = 0.0;
      }
      if (initObj.hasOwnProperty('motor_three')) {
        this.motor_three = initObj.motor_three
      }
      else {
        this.motor_three = 0.0;
      }
      if (initObj.hasOwnProperty('motor_four')) {
        this.motor_four = initObj.motor_four
      }
      else {
        this.motor_four = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SpinRates
    // Serialize message field [motor_one]
    bufferOffset = _serializer.float64(obj.motor_one, buffer, bufferOffset);
    // Serialize message field [motor_two]
    bufferOffset = _serializer.float64(obj.motor_two, buffer, bufferOffset);
    // Serialize message field [motor_three]
    bufferOffset = _serializer.float64(obj.motor_three, buffer, bufferOffset);
    // Serialize message field [motor_four]
    bufferOffset = _serializer.float64(obj.motor_four, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SpinRates
    let len;
    let data = new SpinRates(null);
    // Deserialize message field [motor_one]
    data.motor_one = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [motor_two]
    data.motor_two = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [motor_three]
    data.motor_three = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [motor_four]
    data.motor_four = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'picopter/SpinRates';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fb6650b063ad3f7904bcf518d546f7ec';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 motor_one
    float64 motor_two
    float64 motor_three
    float64 motor_four
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SpinRates(null);
    if (msg.motor_one !== undefined) {
      resolved.motor_one = msg.motor_one;
    }
    else {
      resolved.motor_one = 0.0
    }

    if (msg.motor_two !== undefined) {
      resolved.motor_two = msg.motor_two;
    }
    else {
      resolved.motor_two = 0.0
    }

    if (msg.motor_three !== undefined) {
      resolved.motor_three = msg.motor_three;
    }
    else {
      resolved.motor_three = 0.0
    }

    if (msg.motor_four !== undefined) {
      resolved.motor_four = msg.motor_four;
    }
    else {
      resolved.motor_four = 0.0
    }

    return resolved;
    }
};

module.exports = SpinRates;
