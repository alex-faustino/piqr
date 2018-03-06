#include <picopter/tag_detector.h>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "Tag_Detector");
  TagDetector ic;
  ros::spin();
  return 0;
}
