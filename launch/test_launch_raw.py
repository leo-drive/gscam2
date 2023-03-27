from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    node_1 = [Node(
            namespace='camera1',
            package='gscam2',
            executable='gscam_main',
            output='screen',
            parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10002 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},                
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'camera1/camera_link'},
                {'camera_info_url': 'file:///home/leo/workspaces/gscam2_ws/src/gscam2/cfg/camera1_info.yaml'},
                {'sync_sink': False},
                ],
            ),
    ]
    node_2 = [Node(
            namespace='camera2',
            package='gscam2',
            executable='gscam_main',
            output='screen',
            parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10003 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'camera2/camera_link'},
                {'camera_info_url': 'file:///home/leo/workspaces/gscam2_ws/src/gscam2/cfg/camera2_info.yaml'},
                {'sync_sink': True},
                ],
            ),
    ]
    node_3 = [Node(
            namespace='camera3',
            package='gscam2',
            executable='gscam_main',
            output='screen',
            parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10004 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'camera3/camera_link'},
                {'camera_info_url': 'file:///home/leo/workspaces/gscam2_ws/src/gscam2/cfg/camera3_info.yaml'},
                {'sync_sink': True},
                ],
            ),
    ]
    node_4 = [Node(
            namespace='camera0',
            package='gscam2',
            executable='gscam_main',
            output='screen',
            parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10005 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:2, depth=(string)8,  width=(string)1920, height=(string)1080, colorimetry=(string)BT601-5, payload=(int)96, a-framerate=(string)60" ! rtpvrawdepay ! videoconvert ! videoflip method=rotate-180'},
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'camera0/camera_link'},
                {'camera_info_url': 'file:///home/leo/workspaces/gscam2_ws/src/gscam2/cfg/camera0_info.yaml'},
                {'sync_sink': True},
                ],
            ),
    ]

    return LaunchDescription( node_4 )
