// Generated by gencpp from file bebop_msgs/Ardrone3CameraStatedefaultCameraOrientationV2.msg
// DO NOT EDIT!


#ifndef BEBOP_MSGS_MESSAGE_ARDRONE3CAMERASTATEDEFAULTCAMERAORIENTATIONV2_H
#define BEBOP_MSGS_MESSAGE_ARDRONE3CAMERASTATEDEFAULTCAMERAORIENTATIONV2_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace bebop_msgs
{
template <class ContainerAllocator>
struct Ardrone3CameraStatedefaultCameraOrientationV2_
{
  typedef Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> Type;

  Ardrone3CameraStatedefaultCameraOrientationV2_()
    : header()
    , tilt(0.0)
    , pan(0.0)  {
    }
  Ardrone3CameraStatedefaultCameraOrientationV2_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , tilt(0.0)
    , pan(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _tilt_type;
  _tilt_type tilt;

   typedef float _pan_type;
  _pan_type pan;





  typedef boost::shared_ptr< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> const> ConstPtr;

}; // struct Ardrone3CameraStatedefaultCameraOrientationV2_

typedef ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<std::allocator<void> > Ardrone3CameraStatedefaultCameraOrientationV2;

typedef boost::shared_ptr< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2 > Ardrone3CameraStatedefaultCameraOrientationV2Ptr;
typedef boost::shared_ptr< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2 const> Ardrone3CameraStatedefaultCameraOrientationV2ConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace bebop_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'bebop_msgs': ['/home/rian/Documents/BosRepo/bebop_ws/src/bebop_autonomy/bebop_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8721413d79d1a8c88529f47de1a5ecb0";
  }

  static const char* value(const ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8721413d79d1a8c8ULL;
  static const uint64_t static_value2 = 0x8529f47de1a5ecb0ULL;
};

template<class ContainerAllocator>
struct DataType< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bebop_msgs/Ardrone3CameraStatedefaultCameraOrientationV2";
  }

  static const char* value(const ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Ardrone3CameraStatedefaultCameraOrientationV2\n\
# auto-generated from up stream XML files at\n\
#   github.com/Parrot-Developers/libARCommands/tree/master/Xml\n\
# To check upstream commit hash, refer to last_build_info file\n\
# Do not modify this file by hand. Check scripts/meta folder for generator files.\n\
#\n\
# SDK Comment: Orientation of the center of the camera.\\n This is the value to send when you want to center the camera.\n\
\n\
Header header\n\
\n\
# Tilt value [deg]\n\
float32 tilt\n\
# Pan value [deg]\n\
float32 pan\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.tilt);
      stream.next(m.pan);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Ardrone3CameraStatedefaultCameraOrientationV2_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bebop_msgs::Ardrone3CameraStatedefaultCameraOrientationV2_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "tilt: ";
    Printer<float>::stream(s, indent + "  ", v.tilt);
    s << indent << "pan: ";
    Printer<float>::stream(s, indent + "  ", v.pan);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEBOP_MSGS_MESSAGE_ARDRONE3CAMERASTATEDEFAULTCAMERAORIENTATIONV2_H
