// Generated by gencpp from file bebop_msgs/CommonCommonStateCountryListKnown.msg
// DO NOT EDIT!


#ifndef BEBOP_MSGS_MESSAGE_COMMONCOMMONSTATECOUNTRYLISTKNOWN_H
#define BEBOP_MSGS_MESSAGE_COMMONCOMMONSTATECOUNTRYLISTKNOWN_H


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
struct CommonCommonStateCountryListKnown_
{
  typedef CommonCommonStateCountryListKnown_<ContainerAllocator> Type;

  CommonCommonStateCountryListKnown_()
    : header()
    , listFlags(0)
    , countryCodes()  {
    }
  CommonCommonStateCountryListKnown_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , listFlags(0)
    , countryCodes(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _listFlags_type;
  _listFlags_type listFlags;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _countryCodes_type;
  _countryCodes_type countryCodes;





  typedef boost::shared_ptr< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> const> ConstPtr;

}; // struct CommonCommonStateCountryListKnown_

typedef ::bebop_msgs::CommonCommonStateCountryListKnown_<std::allocator<void> > CommonCommonStateCountryListKnown;

typedef boost::shared_ptr< ::bebop_msgs::CommonCommonStateCountryListKnown > CommonCommonStateCountryListKnownPtr;
typedef boost::shared_ptr< ::bebop_msgs::CommonCommonStateCountryListKnown const> CommonCommonStateCountryListKnownConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace bebop_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'bebop_msgs': ['/home/rian/bebop_ws/src/bebop_autonomy/bebop_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
{
  static const char* value()
  {
    return "86539e5f9157f2f0855dd0d95cb534f2";
  }

  static const char* value(const ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x86539e5f9157f2f0ULL;
  static const uint64_t static_value2 = 0x855dd0d95cb534f2ULL;
};

template<class ContainerAllocator>
struct DataType< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bebop_msgs/CommonCommonStateCountryListKnown";
  }

  static const char* value(const ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# CommonCommonStateCountryListKnown\n\
# auto-generated from up stream XML files at\n\
#   github.com/Parrot-Developers/libARCommands/tree/master/Xml\n\
# To check upstream commit hash, refer to last_build_info file\n\
# Do not modify this file by hand. Check scripts/meta folder for generator files.\n\
#\n\
# SDK Comment: List of countries known by the drone.\n\
\n\
Header header\n\
\n\
# List entry attribute Bitfield. 0x01: First: indicate its the first element of the list. 0x02: Last: indicate its the last element of the list. 0x04: Empty: indicate the list is empty (implies First/Last). All other arguments should be ignored.\n\
uint8 listFlags\n\
# Following of country code with ISO 3166 format, separated by ;. Be careful of the command size allowed by the network used. If necessary, split the list in several commands.\n\
string countryCodes\n\
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

  static const char* value(const ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.listFlags);
      stream.next(m.countryCodes);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CommonCommonStateCountryListKnown_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bebop_msgs::CommonCommonStateCountryListKnown_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "listFlags: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.listFlags);
    s << indent << "countryCodes: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.countryCodes);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEBOP_MSGS_MESSAGE_COMMONCOMMONSTATECOUNTRYLISTKNOWN_H
