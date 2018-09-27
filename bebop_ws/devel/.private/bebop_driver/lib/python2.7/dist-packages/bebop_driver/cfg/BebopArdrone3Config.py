## *********************************************************
##
## File autogenerated for the bebop_driver package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'PILOTINGSETTINGS', 'lower': 'pilotingsettings', 'srcline': 124, 'name': 'pilotingsettings', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::PILOTINGSETTINGS', 'field': 'DEFAULT::pilotingsettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 16, 'description': 'Current altitude max in m', 'max': 160.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsMaxAltitudeCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 18, 'description': 'Current tilt max in degree', 'max': 180.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsMaxTiltCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -180.0, 'type': 'double'}, {'srcline': 24, 'description': '1 to enable, 0 to disable', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsAbsolutControlOn', 'edit_method': "{'enum_description': '1 to enable, 0 to disable', 'enum': [{'srcline': 21, 'description': 'Disabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsAbsolutControlOn_OFF'}, {'srcline': 22, 'description': 'Enabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsAbsolutControlOn_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 26, 'description': 'Current max distance in meter', 'max': 2000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsMaxDistanceValue', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 32, 'description': '1 if the drone cant fly further than max distance, 0 if no limitation on the drone should be done', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover', 'edit_method': "{'enum_description': '1 if the drone cant fly further than max distance, 0 if no limitation on the drone should be done', 'enum': [{'srcline': 29, 'description': 'Disabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_OFF'}, {'srcline': 30, 'description': 'Enabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 38, 'description': '1 to enable, 0 to disable', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsBankedTurnValue', 'edit_method': "{'enum_description': '1 to enable, 0 to disable', 'enum': [{'srcline': 35, 'description': 'Disabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsBankedTurnValue_OFF'}, {'srcline': 36, 'description': 'Enabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsBankedTurnValue_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 40, 'description': 'Current altitude min in m', 'max': 160.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsMinAltitudeCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 46, 'description': 'The circling direction', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsCirclingDirectionValue', 'edit_method': "{'enum_description': 'The circling direction', 'enum': [{'srcline': 43, 'description': 'Circling ClockWise', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsCirclingDirectionValue_CW'}, {'srcline': 44, 'description': 'Circling Counter ClockWise', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsCirclingDirectionValue_CCW'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 48, 'description': 'The circling radius in meter', 'max': 160, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsCirclingRadiusValue', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 50, 'description': 'The circling altitude in meter', 'max': 160, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsCirclingAltitudeValue', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 56, 'description': 'The Pitch mode', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PilotingSettingsPitchModeValue', 'edit_method': "{'enum_description': 'The Pitch mode', 'enum': [{'srcline': 53, 'description': 'Positive pitch values will make the drone lower its nose. Negative pitch values will make the drone raise its nose.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsPitchModeValue_NORMAL'}, {'srcline': 54, 'description': 'Pitch commands are inverted. Positive pitch values will make the drone raise its nose. Negative pitch values will make the drone lower its nose.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PilotingSettingsPitchModeValue_INVERTED'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 1}, {'upper': 'SPEEDSETTINGS', 'lower': 'speedsettings', 'srcline': 124, 'name': 'speedsettings', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::SPEEDSETTINGS', 'field': 'DEFAULT::speedsettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 61, 'description': 'Current max vertical speed in m/s', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsMaxVerticalSpeedCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 63, 'description': 'Current max yaw rotation speed in degree/s', 'max': 900.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsMaxRotationSpeedCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 69, 'description': '1 if present, 0 if not present', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsHullProtectionPresent', 'edit_method': "{'enum_description': '1 if present, 0 if not present', 'enum': [{'srcline': 66, 'description': 'Disabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsHullProtectionPresent_OFF'}, {'srcline': 67, 'description': 'Enabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsHullProtectionPresent_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 75, 'description': '1 if outdoor flight, 0 if indoor flight', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsOutdoorOutdoor', 'edit_method': "{'enum_description': '1 if outdoor flight, 0 if indoor flight', 'enum': [{'srcline': 72, 'description': 'Disabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsOutdoorOutdoor_OFF'}, {'srcline': 73, 'description': 'Enabled', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SpeedSettingsOutdoorOutdoor_ON'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 77, 'description': 'Current max pitch/roll rotation speed in degree/s', 'max': 900.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'SpeedSettingsMaxPitchRollRotationSpeedCurrent', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 2}, {'upper': 'NETWORKSETTINGS', 'lower': 'networksettings', 'srcline': 124, 'name': 'networksettings', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::NETWORKSETTINGS', 'field': 'DEFAULT::networksettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 86, 'description': 'The type of wifi selection (auto, manual)', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'NetworkSettingsWifiSelectionType', 'edit_method': "{'enum_description': 'The type of wifi selection (auto, manual)', 'enum': [{'srcline': 83, 'description': 'Auto selection', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionType_auto'}, {'srcline': 84, 'description': 'Manual selection', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionType_manual'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 92, 'description': 'The allowed band(s) : 2.4 Ghz, 5 Ghz, or all', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'NetworkSettingsWifiSelectionBand', 'edit_method': "{'enum_description': 'The allowed band(s) : 2.4 Ghz, 5 Ghz, or all', 'enum': [{'srcline': 88, 'description': '2.4 GHz band', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionBand_2_4ghz'}, {'srcline': 89, 'description': '5 GHz band', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionBand_5ghz'}, {'srcline': 90, 'description': 'Both 2.4 and 5 GHz bands', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'NetworkSettingsWifiSelectionBand_all'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 93, 'description': 'The channel (not used in auto mode)', 'max': 50, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'NetworkSettingsWifiSelectionChannel', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 3}, {'upper': 'PICTURESETTINGS', 'lower': 'picturesettings', 'srcline': 124, 'name': 'picturesettings', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::PICTURESETTINGS', 'field': 'DEFAULT::picturesettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 104, 'description': 'Video stabilization mode', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PictureSettingsVideoStabilizationModeMode', 'edit_method': "{'enum_description': 'Video stabilization mode', 'enum': [{'srcline': 99, 'description': 'Video flat on roll and pitch', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoStabilizationModeMode_roll_pitch'}, {'srcline': 100, 'description': 'Video flat on pitch only', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoStabilizationModeMode_pitch'}, {'srcline': 101, 'description': 'Video flat on roll only', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoStabilizationModeMode_roll'}, {'srcline': 102, 'description': 'Video follows drone angles', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoStabilizationModeMode_none'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 110, 'description': 'Video recording mode', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PictureSettingsVideoRecordingModeMode', 'edit_method': "{'enum_description': 'Video recording mode', 'enum': [{'srcline': 107, 'description': 'Maximize recording quality.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoRecordingModeMode_quality'}, {'srcline': 108, 'description': 'Maximize recording time.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoRecordingModeMode_time'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 117, 'description': 'Video framerate', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PictureSettingsVideoFramerateFramerate', 'edit_method': "{'enum_description': 'Video framerate', 'enum': [{'srcline': 113, 'description': '23.976 frames per second.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoFramerateFramerate_24_FPS'}, {'srcline': 114, 'description': '25 frames per second.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoFramerateFramerate_25_FPS'}, {'srcline': 115, 'description': '29.97 frames per second.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoFramerateFramerate_30_FPS'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 123, 'description': 'Video streaming and recording resolutions', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'PictureSettingsVideoResolutionsType', 'edit_method': "{'enum_description': 'Video streaming and recording resolutions', 'enum': [{'srcline': 120, 'description': '1080p recording, 480p streaming.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoResolutionsType_rec1080_stream480'}, {'srcline': 121, 'description': '720p recording, 720p streaming.', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'PictureSettingsVideoResolutionsType_rec720_stream720'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 4}, {'upper': 'GPSSETTINGS', 'lower': 'gpssettings', 'srcline': 124, 'name': 'gpssettings', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::GPSSETTINGS', 'field': 'DEFAULT::gpssettings', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 133, 'description': 'The type of the home position', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'GPSSettingsHomeTypeType', 'edit_method': "{'enum_description': 'The type of the home position', 'enum': [{'srcline': 129, 'description': 'The drone will try to return to the take off position', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'GPSSettingsHomeTypeType_TAKEOFF'}, {'srcline': 130, 'description': 'The drone will try to return to the pilot position', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'GPSSettingsHomeTypeType_PILOT'}, {'srcline': 131, 'description': 'The drone will try to return to the target of the current (or last) follow me', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'GPSSettingsHomeTypeType_FOLLOWEE'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 135, 'description': 'Delay in second', 'max': 120, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/rian/bebop_ws/src/bebop_autonomy/bebop_driver/cfg/autogenerated/BebopArdrone3.cfg', 'name': 'GPSSettingsReturnHomeDelayDelay', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 5}], 'parameters': [], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

BebopArdrone3_PilotingSettingsAbsolutControlOn_OFF = 0
BebopArdrone3_PilotingSettingsAbsolutControlOn_ON = 1
BebopArdrone3_PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_OFF = 0
BebopArdrone3_PilotingSettingsNoFlyOverMaxDistanceShouldnotflyover_ON = 1
BebopArdrone3_PilotingSettingsBankedTurnValue_OFF = 0
BebopArdrone3_PilotingSettingsBankedTurnValue_ON = 1
BebopArdrone3_PilotingSettingsCirclingDirectionValue_CW = 0
BebopArdrone3_PilotingSettingsCirclingDirectionValue_CCW = 1
BebopArdrone3_PilotingSettingsPitchModeValue_NORMAL = 0
BebopArdrone3_PilotingSettingsPitchModeValue_INVERTED = 1
BebopArdrone3_SpeedSettingsHullProtectionPresent_OFF = 0
BebopArdrone3_SpeedSettingsHullProtectionPresent_ON = 1
BebopArdrone3_SpeedSettingsOutdoorOutdoor_OFF = 0
BebopArdrone3_SpeedSettingsOutdoorOutdoor_ON = 1
BebopArdrone3_NetworkSettingsWifiSelectionType_auto = 0
BebopArdrone3_NetworkSettingsWifiSelectionType_manual = 1
BebopArdrone3_NetworkSettingsWifiSelectionBand_2_4ghz = 0
BebopArdrone3_NetworkSettingsWifiSelectionBand_5ghz = 1
BebopArdrone3_NetworkSettingsWifiSelectionBand_all = 2
BebopArdrone3_PictureSettingsVideoStabilizationModeMode_roll_pitch = 0
BebopArdrone3_PictureSettingsVideoStabilizationModeMode_pitch = 1
BebopArdrone3_PictureSettingsVideoStabilizationModeMode_roll = 2
BebopArdrone3_PictureSettingsVideoStabilizationModeMode_none = 3
BebopArdrone3_PictureSettingsVideoRecordingModeMode_quality = 0
BebopArdrone3_PictureSettingsVideoRecordingModeMode_time = 1
BebopArdrone3_PictureSettingsVideoFramerateFramerate_24_FPS = 0
BebopArdrone3_PictureSettingsVideoFramerateFramerate_25_FPS = 1
BebopArdrone3_PictureSettingsVideoFramerateFramerate_30_FPS = 2
BebopArdrone3_PictureSettingsVideoResolutionsType_rec1080_stream480 = 0
BebopArdrone3_PictureSettingsVideoResolutionsType_rec720_stream720 = 1
BebopArdrone3_GPSSettingsHomeTypeType_TAKEOFF = 0
BebopArdrone3_GPSSettingsHomeTypeType_PILOT = 1
BebopArdrone3_GPSSettingsHomeTypeType_FOLLOWEE = 2
