import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name='gscam_node',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        output='screen',       
        composable_node_descriptions=[   
            ComposableNode(            
                package='gscam2',
                plugin='gscam2::GSCamNode',
                name='gscam_publisher',
                namespace= 'camera0',
                parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10000 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer latency=20 ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},                
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'my_camera_frame'},
                {'camera_info_url': 'file:///home/robione/projects/robione/src/sensor_component/external/gscam2/cfg/camera0_info.yaml'},
                # {'sync_sink': False},     
                ],
            ),
            ComposableNode(            
                package='gscam2',
                plugin='gscam2::GSCamNode',
                name='gscam_publisher',
                namespace= 'camera1',
                parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10001 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer latency=20 ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},                
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'my_camera_frame'},
                {'camera_info_url': 'file:///home/robione/projects/robione/src/sensor_component/external/gscam2/cfg/camera1_info.yaml'},
                # {'sync_sink': False},     
                ],
            ), 
            ComposableNode(            
                package='gscam2',
                plugin='gscam2::GSCamNode',
                name='gscam_publisher',
                namespace= 'camera2',
                parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10002 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer latency=20 ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},                
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'my_camera_frame'},
                {'camera_info_url': 'file:///home/robione/projects/robione/src/sensor_component/external/gscam2/cfg/camera2_info.yaml'},
                # {'sync_sink': False},     
                ],
            ),
            ComposableNode( 
                package='gscam2',
                plugin='gscam2::GSCamNode',
                name='gscam_publisher',
                namespace= 'camera3',
                parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10003 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer latency=20 ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},                
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'my_camera_frame'},
                {'camera_info_url': 'file:///home/robione/projects/robione/src/sensor_component/external/gscam2/cfg/camera3_info.yaml'},
                # {'sync_sink': False},     
                ],
            ),                                           
        ],
    )

    return LaunchDescription([container])


































