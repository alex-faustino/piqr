#ifndef PICOPTER_TAG_DETECTOR_H
#define PICOPTER_TAG_DETECTOR_H

#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <cmath>

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <geometry_msgs/Pose.h>
#include <picopter/CamMeasurement.h>
#include "opencv2/opencv.hpp"
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

#include "AprilTags/TagDetector.h"
#include "AprilTags/Tag36h11.h"

static const std::string WINDOWNAME = "Tag Detection";

class TagDetector
{
	private:
	// ROS
	ros::NodeHandle nh_;
	image_transport::ImageTransport it_;
	image_transport::Subscriber image_sub_;
	//image_transport::Publisher image_pub_;
	ros::Publisher pose_pub;
  
	// AprilTag
	AprilTags::TagDetector* tagDetector;
	AprilTags::TagCodes tagCode;
	double tagSize;
	
	// Camera parameters in pixels determined from ROS camera calibration
	double fx;
	double fy;
	double px;
	double py;
  
	public:
	
	// Default constructor
	TagDetector() : 
	it_(nh_),
	tagDetector(NULL),
	tagCode(AprilTags::tagCodes36h11),
	tagSize(0.166), // when printed on normal printer paper
	fx(530),
	fy(530),
	px(320),
	py(240)
	{
		// Subscribe to input video feed and publish output video feed
		image_sub_ = it_.subscribe("/usb_cam/image_raw", 1, &TagDetector::imageCb, this);
		//image_pub_ = it_.advertise("/tag_detector/raw_image", 1);
		pose_pub = nh_.advertise<picopter::CamMeasurement>("tag_detector/tag_pose", 1);
		
		// Prepare the window
		//cv::namedWindow(WINDOWNAME);
		
		// Initialize tagDetector instance
		this->setup();
	} // constructor

	// Destructor, closes video windows
	~TagDetector()
	{
		//cv::destroyWindow(WINDOWNAME);
	} // destructor

	// Callback function
	void imageCb(const sensor_msgs::ImageConstPtr& msg);
  
	void Process_Image(cv::Mat img);
 
	void Print_Detection(AprilTags::TagDetection& detection) const;
	
	void setup();
}; // Tag_Detector
#endif
