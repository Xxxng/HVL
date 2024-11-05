# Copyright 2018 Lucas Walter
# All rights reserved.
#
# Software License Agreement (BSD License 2.0)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Lucas Walter nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import argparse
import os
import sys

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    parser = argparse.ArgumentParser(description='usb_cam launch')
    parser.add_argument('-n', '--node-name', dest='node_name', type=str,
                        help='name for device', default='usb_cam')

    args, unknown = parser.parse_known_args(sys.argv[4:])

    usb_cam_dir = get_package_share_directory('pixkit_sensor_kit_launch')
  
    node_name = args.node_name
    # get path to params file
    parameters={
        "video_device": "/dev/camera/top_6mm",
        "framerate": 30.0,
        "io_method": "mmap",
        "frame_id": "camera_top_link",
        "pixel_format": "uyvy2rgb",
        # "pixel_format": "yuyv2rgb",
        "image_width": 1920 ,
        "image_height": 1080,
        "camera_name": "camera_top_6mm",
        "camera_info_url": "file://${ROS_HOME}/../pix/parameter/sensor_kit/pixkit_sensor_kit_description/intrinsic_parameters/camera_top_6mm.yaml",
        # reusing same camera intrinsics only for demo, should really be unique for camera2"
        "brightness": -1,
        "contrast": -1,
        "saturation": -1,
        "sharpness": -1,
        "gain": -1,
        "auto_white_balance": True,
        "white_balance": 4000,
        "autoexposure": True,
        "exposure": 100,
        "autofocus": False,
        "focus": -1,
        # resize
        "image_resize": 2,
        "camera_lifetime": 33,
    }
    parameters["video_device"] = os.path.realpath(parameters["video_device"])
    ld.add_action(Node(
        package='usb_cam', executable='usb_cam_node_exe', output='screen',
        name=node_name,
        namespace="top/gmsl",
        parameters=[parameters]
        ))
    return ld
