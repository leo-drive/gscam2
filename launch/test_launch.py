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
                {'gscam_config':'udpsrc buffer_size=9216000 port=10002 caps ="application/x-rtp, media=(string)video, encoding-name=(string)H264, clock-rate=(int)90000, packetization-mode=(int)1, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvideoconvert ! videoflip method=rotate-180'},                
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'my_camera_frame'},
                {'camera_info_url': 'file:///home/leo/workspaces/gscam2_ws/src/gscam2/cfg/camera1_info.yaml'},
                # {'sync_sink': False},
                ],
            ),
    ]
    node_2 = [Node(
            namespace='camera2',
            package='gscam2',
            executable='gscam_main',
            output='screen',
            parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10003 caps ="application/x-rtp, media=(string)video, encoding-name=(string)H264, clock-rate=(int)90000, packetization-mode=(int)1, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvideoconvert ! videoflip method=rotate-180'},
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'my_camera_frame'},
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
                {'gscam_config':'udpsrc buffer_size=9216000 port=10004 caps ="application/x-rtp, media=(string)video, encoding-name=(string)H264, clock-rate=(int)90000, packetization-mode=(int)1, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvideoconvert ! videoflip method=rotate-180'},
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'camera3/camera_link'},
                {'camera_info_url': 'file:///home/leo/workspaces/gscam2_ws/src/gscam2/cfg/camera3_info.yaml'},
                {'sync_sink': True},
                ],
            ),
    ]
    node_4 = [Node(
            namespace='camera4',
            package='gscam2',
            executable='gscam_main',
            output='screen',
            parameters=[
                {'gscam_config':'udpsrc buffer_size=9216000 port=10005 caps ="application/x-rtp, media=(string)video, encoding-name=(string)H264, clock-rate=(int)90000, packetization-mode=(int)1, payload=(int)96, a-framerate=(string)60" ! rtpjitterbuffer ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvideoconvert ! videoflip method=rotate-180'},
                {'preroll': False},
                {'use_gst_timestamps': True},
                {'frame_id': 'my_camera_frame'},
                {'camera_info_url': 'file:///home/leo/workspaces/gscam2_ws/src/gscam2/cfg/camera4_info.yaml'},
                {'sync_sink': True},
                ],
            ),
    ]

    return LaunchDescription( node_3 )
