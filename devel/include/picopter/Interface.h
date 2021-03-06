// Generated by gencpp from file picopter/Interface.msg
// DO NOT EDIT!


#ifndef PICOPTER_MESSAGE_INTERFACE_H
#define PICOPTER_MESSAGE_INTERFACE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace picopter
{
template <class ContainerAllocator>
struct Interface_
{
  typedef Interface_<ContainerAllocator> Type;

  Interface_()
    : is_calibrated(false)
    , arm_esc(false)
    , flight_mode(false)
    , stop_motors(false)
    , shutdown(false)  {
    }
  Interface_(const ContainerAllocator& _alloc)
    : is_calibrated(false)
    , arm_esc(false)
    , flight_mode(false)
    , stop_motors(false)
    , shutdown(false)  {
  (void)_alloc;
    }



   typedef uint8_t _is_calibrated_type;
  _is_calibrated_type is_calibrated;

   typedef uint8_t _arm_esc_type;
  _arm_esc_type arm_esc;

   typedef uint8_t _flight_mode_type;
  _flight_mode_type flight_mode;

   typedef uint8_t _stop_motors_type;
  _stop_motors_type stop_motors;

   typedef uint8_t _shutdown_type;
  _shutdown_type shutdown;





  typedef boost::shared_ptr< ::picopter::Interface_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::picopter::Interface_<ContainerAllocator> const> ConstPtr;

}; // struct Interface_

typedef ::picopter::Interface_<std::allocator<void> > Interface;

typedef boost::shared_ptr< ::picopter::Interface > InterfacePtr;
typedef boost::shared_ptr< ::picopter::Interface const> InterfaceConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::picopter::Interface_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::picopter::Interface_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace picopter

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'picopter': ['/home/pi/picopter/src/picopter/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::picopter::Interface_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::picopter::Interface_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::picopter::Interface_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::picopter::Interface_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::picopter::Interface_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::picopter::Interface_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::picopter::Interface_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d48df5094a97ac2271d10199017658de";
  }

  static const char* value(const ::picopter::Interface_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd48df5094a97ac22ULL;
  static const uint64_t static_value2 = 0x71d10199017658deULL;
};

template<class ContainerAllocator>
struct DataType< ::picopter::Interface_<ContainerAllocator> >
{
  static const char* value()
  {
    return "picopter/Interface";
  }

  static const char* value(const ::picopter::Interface_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::picopter::Interface_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool is_calibrated\n\
bool arm_esc\n\
bool flight_mode\n\
bool stop_motors\n\
bool shutdown\n\
";
  }

  static const char* value(const ::picopter::Interface_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::picopter::Interface_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.is_calibrated);
      stream.next(m.arm_esc);
      stream.next(m.flight_mode);
      stream.next(m.stop_motors);
      stream.next(m.shutdown);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Interface_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::picopter::Interface_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::picopter::Interface_<ContainerAllocator>& v)
  {
    s << indent << "is_calibrated: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_calibrated);
    s << indent << "arm_esc: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.arm_esc);
    s << indent << "flight_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.flight_mode);
    s << indent << "stop_motors: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.stop_motors);
    s << indent << "shutdown: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.shutdown);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PICOPTER_MESSAGE_INTERFACE_H
