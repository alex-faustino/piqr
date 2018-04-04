// This program is adapted from the AprilTags demo written by Michael 
// Kaess at MIT. It publishes an AprilTags pose relative to the camera 
// to the topic tag_detector/tag_pose as well as printing to the 
// terminal. The pose is given as position in meters and a unit 
// quaternion. 

#include <picopter/tag_detector.h>

#ifndef PI
const double PI = 3.14159265358979323846;
#endif
const double TWOPI = 2.0*PI;

/**
 * Normalize angle to be within the interval [-pi,pi].
 */
inline double standardRad(double t) {
  if (t >= 0.) {
    t = fmod(t+PI, TWOPI) - PI;
  } else {
    t = fmod(t-PI, -TWOPI) + PI;
  }
  return t;
}

/**
 * Convert rotation matrix to Euler angles
 */
void wRo_to_euler(const Eigen::Matrix3d& wRo, double& yaw, double& pitch, double& roll) {
    yaw = standardRad(atan2(wRo(1,0), wRo(0,0)));
    // double c = cos(yaw);
    // double s = sin(yaw);
    // pitch = standardRad(atan2(-wRo(2,0), wRo(0,0)*c + wRo(1,0)*s));
    // roll  = standardRad(atan2(wRo(0,2)*s - wRo(1,2)*c, -wRo(0,1)*s + wRo(1,1)*c));
    
    // From LaValle
    pitch = standardRad(atan2(-wRo(2,0), sqrt(pow(wRo(2,1), 2.0) + pow(wRo(2,2), 2.0))));
    roll = standardRad(atan2(wRo(2,1), wRo(2,2)));
}

// Convert rotation matrix to Quaternion
void rot_to_quat(const Eigen::Matrix3d& rot, Eigen::Quaterniond& quat)
{
	double theta = acos((rot.trace() - 1.0)/2.0);
	double kCoeff = 1.0/(2.0*sin(theta));
	double sOverTwo = sin(theta/2.0);
	
	quat.x() = kCoeff*(rot(2,1) - rot(1,2))*sOverTwo;
	quat.y() = kCoeff*(rot(0,2) - rot(2,0))*sOverTwo;
	quat.z() = kCoeff*(rot(1,0) - rot(0,1))*sOverTwo;
	
	quat.w() = cos(theta/2.0);
}

// Callback function
void TagDetector::imageCb(const sensor_msgs::ImageConstPtr& msg)
{
	cv_bridge::CvImagePtr cv_ptr;
	namespace enc = sensor_msgs::image_encodings;
	try
	{
		cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
	}
	catch (cv_bridge::Exception& e)
	{
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}

	// Detect AprilTags and publish image
	Process_Image(cv_ptr->image);
	//image_pub_.publish(cv_ptr->toImageMsg());
} // imageCb
  
void TagDetector::Process_Image(cv::Mat img)
{
	cv::Mat image, image_gray;
	// Create copy of cv image
	img.copyTo(image);

	// Convert to gray scale and detect AprilTags
	cv::cvtColor(image, image_gray, CV_BGR2GRAY );
	vector<AprilTags::TagDetection> detections = tagDetector->extractTags(image_gray);
  	
	// Print out and publish each detection
	cout << detections.size() << " tags detected:" << endl;
	for (int i=0; i<detections.size(); i++) 
	{
		Print_Detection(detections[i]);
	}
	
	// Draw detections on image
	for (int i=0; i<detections.size(); i++)
	{
		detections[i].draw(image);
	}
     
	//cv::imshow(WINDOWNAME, image);
	//cv::waitKey(3);
} // processImage
 
void TagDetector::Print_Detection(AprilTags::TagDetection& detection) const 
{
	// Message containing detected tag pose
	picopter::CamMeasurement pose_msg;
		
	Eigen::Vector3d o_tag_in_cam;
	Eigen::Matrix3d R_tag_in_cam;
	detection.getRelativeTranslationRotation(tagSize, fx, fy, px, py, o_tag_in_cam, R_tag_in_cam);
	
	Eigen::Vector3d o_cam_in_tag;
	Eigen::Matrix3d R_cam_in_tag;
	/*
	Eigen::Matrix3d F;
	Eigen::Matrix3d fixed_R;
	F << 1,  0,  0,
		 0, -1,  0,
		 0,  0, -1;
	R_cam_in_tag = R_tag_in_cam.transpose();
	fixed_R = F*R_cam_in_tag;
	double yaw, pitch, roll;
    wRo_to_euler(fixed_R, yaw, pitch, roll);
	*/
	
	R_cam_in_tag = R_tag_in_cam.transpose();
	o_cam_in_tag = (-1.0*R_cam_in_tag)*o_tag_in_cam;
	double yaw, pitch, roll;
    wRo_to_euler(R_cam_in_tag, yaw, pitch, roll);
    
	/*
	Eigen::Quaterniond quat;
	rot_to_quat(rotation, quat);
	quat.normalize();
	*/
    
/*	cout << "  x=" << translation(0)
		 << ", y=" << translation(1)
		 << ", z=" << translation(2)
		 << ", Q_w=" << quat.w()
		 << ", Q_x=" << quat.x()
		 << ", Q_y=" << quat.y()
		 << ", Q_z=" << quat.z()
		 << endl;
*/	
	/*
	pose_msg.position.x = translation(0);
	pose_msg.position.y = translation(1);
	pose_msg.position.z = translation(2);
	pose_msg.orientation.w = quat.w();
	pose_msg.orientation.x = quat.x();
	pose_msg.orientation.y = quat.y();
	pose_msg.orientation.z = quat.z();
	*/
	
	pose_msg.x = o_cam_in_tag(0);
	pose_msg.y = o_cam_in_tag(1);
	pose_msg.z = o_cam_in_tag(2);
	pose_msg.yaw = yaw;
	pose_msg.pitch = pitch;
	pose_msg.roll = roll;
	pose_pub.publish(pose_msg);
} // printDetection
	
void TagDetector::setup()
{
	tagDetector = new AprilTags::TagDetector(tagCode);
}

