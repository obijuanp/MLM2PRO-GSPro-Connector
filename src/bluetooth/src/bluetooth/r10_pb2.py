# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/bluetooth/r10.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17src/bluetooth/r10.proto\x12\x13LaunchMonitor.Proto\"\x9c\x01\n\x0cWrapperProto\x12\x35\n\x05\x65vent\x18\x1e \x01(\x0b\x32!.LaunchMonitor.Proto.EventSharingH\x00\x88\x01\x01\x12?\n\x07service\x18& \x01(\x0b\x32).LaunchMonitor.Proto.LaunchMonitorServiceH\x01\x88\x01\x01\x42\x08\n\x06_eventB\n\n\x08_service\"\xa4\t\n\x14LaunchMonitorService\x12?\n\x0estatus_request\x18\x01 \x01(\x0b\x32\".LaunchMonitor.Proto.StatusRequestH\x00\x88\x01\x01\x12\x41\n\x0fstatus_response\x18\x02 \x01(\x0b\x32#.LaunchMonitor.Proto.StatusResponseH\x01\x88\x01\x01\x12@\n\x0fwake_up_request\x18\x03 \x01(\x0b\x32\".LaunchMonitor.Proto.WakeUpRequestH\x02\x88\x01\x01\x12\x42\n\x10wake_up_response\x18\x04 \x01(\x0b\x32#.LaunchMonitor.Proto.WakeUpResponseH\x03\x88\x01\x01\x12;\n\x0ctilt_request\x18\x05 \x01(\x0b\x32 .LaunchMonitor.Proto.TiltRequestH\x04\x88\x01\x01\x12=\n\rtilt_response\x18\x06 \x01(\x0b\x32!.LaunchMonitor.Proto.TiltResponseH\x05\x88\x01\x01\x12U\n\x16start_tilt_cal_request\x18\x07 \x01(\x0b\x32\x30.LaunchMonitor.Proto.StartTiltCalibrationRequestH\x06\x88\x01\x01\x12W\n\x17start_tilt_cal_response\x18\x08 \x01(\x0b\x32\x31.LaunchMonitor.Proto.StartTiltCalibrationResponseH\x07\x88\x01\x01\x12U\n\x16reset_tilt_cal_request\x18\t \x01(\x0b\x32\x30.LaunchMonitor.Proto.ResetTiltCalibrationRequestH\x08\x88\x01\x01\x12W\n\x17reset_tilt_cal_response\x18\n \x01(\x0b\x32\x31.LaunchMonitor.Proto.ResetTiltCalibrationResponseH\t\x88\x01\x01\x12H\n\x13shot_config_request\x18\x0b \x01(\x0b\x32&.LaunchMonitor.Proto.ShotConfigRequestH\n\x88\x01\x01\x12J\n\x14shot_config_response\x18\x0c \x01(\x0b\x32\'.LaunchMonitor.Proto.ShotConfigResponseH\x0b\x88\x01\x01\x42\x11\n\x0f_status_requestB\x12\n\x10_status_responseB\x12\n\x10_wake_up_requestB\x13\n\x11_wake_up_responseB\x0f\n\r_tilt_requestB\x10\n\x0e_tilt_responseB\x19\n\x17_start_tilt_cal_requestB\x1a\n\x18_start_tilt_cal_responseB\x19\n\x17_reset_tilt_cal_requestB\x1a\n\x18_reset_tilt_cal_responseB\x16\n\x14_shot_config_requestB\x17\n\x15_shot_config_response\"\x0f\n\rStatusRequest\"J\n\x0eStatusResponse\x12.\n\x05state\x18\x01 \x01(\x0b\x32\x1a.LaunchMonitor.Proto.StateH\x00\x88\x01\x01\x42\x08\n\x06_state\"\x0f\n\rWakeUpRequest\"\xa9\x01\n\x0eWakeUpResponse\x12G\n\x06status\x18\x01 \x01(\x0e\x32\x32.LaunchMonitor.Proto.WakeUpResponse.ResponseStatusH\x00\x88\x01\x01\"C\n\x0eResponseStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x11\n\rALREADY_AWAKE\x10\x01\x12\x11\n\rUNKNOWN_ERROR\x10\x02\x42\t\n\x07_status\"\r\n\x0bTiltRequest\"E\n\x0cTiltResponse\x12,\n\x04tilt\x18\x01 \x01(\x0b\x32\x19.LaunchMonitor.Proto.TiltH\x00\x88\x01\x01\x42\x07\n\x05_tilt\"\x1d\n\x1bStartTiltCalibrationRequest\"\xc1\x01\n\x1cStartTiltCalibrationResponse\x12X\n\x06status\x18\x01 \x01(\x0e\x32\x43.LaunchMonitor.Proto.StartTiltCalibrationResponse.CalibrationStatusH\x00\x88\x01\x01\"<\n\x11\x43\x61librationStatus\x12\x0b\n\x07STARTED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x42\t\n\x07_status\"I\n\x1bResetTiltCalibrationRequest\x12\x19\n\x0cshould_reset\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\x0f\n\r_should_reset\"\xd9\x01\n\x1cResetTiltCalibrationResponse\x12M\n\x06status\x18\x01 \x01(\x0e\x32\x38.LaunchMonitor.Proto.ResetTiltCalibrationResponse.StatusH\x00\x88\x01\x01\"_\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tCAN_RESET\x10\x01\x12\x11\n\rALREADY_RESET\x10\x02\x12\x14\n\x10RESET_SUCCESSFUL\x10\x03\x12\x10\n\x0c\x43\x41NNOT_RESET\x10\x04\x42\t\n\x07_status\"\xd5\x01\n\x11ShotConfigRequest\x12\x18\n\x0btemperature\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x15\n\x08humidity\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x15\n\x08\x61ltitude\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x18\n\x0b\x61ir_density\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x16\n\ttee_range\x18\x05 \x01(\x02H\x04\x88\x01\x01\x42\x0e\n\x0c_temperatureB\x0b\n\t_humidityB\x0b\n\t_altitudeB\x0e\n\x0c_air_densityB\x0c\n\n_tee_range\"6\n\x12ShotConfigResponse\x12\x14\n\x07success\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\n\n\x08_success\"\xd8\x03\n\x0c\x45ventSharing\x12\x45\n\x11subscribe_request\x18\x01 \x01(\x0b\x32%.LaunchMonitor.Proto.SubscribeRequestH\x00\x88\x01\x01\x12\x46\n\x11subscribe_respose\x18\x02 \x01(\x0b\x32&.LaunchMonitor.Proto.SubscribeResponseH\x01\x88\x01\x01\x12\x41\n\x0cnotification\x18\x03 \x01(\x0b\x32&.LaunchMonitor.Proto.AlertNotificationH\x02\x88\x01\x01\x12\x46\n\x0fsupport_request\x18\x04 \x01(\x0b\x32(.LaunchMonitor.Proto.AlertSupportRequestH\x03\x88\x01\x01\x12H\n\x10support_response\x18\x05 \x01(\x0b\x32).LaunchMonitor.Proto.AlertSupportResponseH\x04\x88\x01\x01\x42\x14\n\x12_subscribe_requestB\x14\n\x12_subscribe_resposeB\x0f\n\r_notificationB\x12\n\x10_support_requestB\x13\n\x11_support_response\"E\n\x10SubscribeRequest\x12\x31\n\x06\x61lerts\x18\x01 \x03(\x0b\x32!.LaunchMonitor.Proto.AlertMessage\"\xd1\x02\n\x11SubscribeResponse\x12O\n\x0c\x61lert_status\x18\x01 \x03(\x0b\x32\x39.LaunchMonitor.Proto.SubscribeResponse.AlertStatusMessage\x1a\xea\x01\n\x12\x41lertStatusMessage\x12_\n\x10subscribe_status\x18\x01 \x01(\x0e\x32@.LaunchMonitor.Proto.SubscribeResponse.AlertStatusMessage.StatusH\x00\x88\x01\x01\x12\x34\n\x04type\x18\x02 \x01(\x0b\x32!.LaunchMonitor.Proto.AlertMessageH\x01\x88\x01\x01\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x42\x13\n\x11_subscribe_statusB\x07\n\x05_type\"\x15\n\x13\x41lertSupportRequest\"\x92\x01\n\x14\x41lertSupportResponse\x12J\n\x10supported_alerts\x18\x01 \x03(\x0e\x32\x30.LaunchMonitor.Proto.AlertNotification.AlertType\x12\x1b\n\x0eversion_number\x18\x02 \x01(\rH\x00\x88\x01\x01\x42\x11\n\x0f_version_number\"\x80\x01\n\x0c\x41lertMessage\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x30.LaunchMonitor.Proto.AlertNotification.AlertTypeH\x00\x88\x01\x01\x12\x15\n\x08interval\x18\x02 \x01(\rH\x01\x88\x01\x01\x42\x07\n\x05_typeB\x0b\n\t_interval\"\x83\x02\n\x11\x41lertNotification\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x30.LaunchMonitor.Proto.AlertNotification.AlertTypeH\x00\x88\x01\x01\x12\x42\n\x11\x41lertNotification\x18\xe9\x07 \x01(\x0b\x32!.LaunchMonitor.Proto.AlertDetailsH\x01\x88\x01\x01\"F\n\tAlertType\x12\x12\n\x0e\x41\x43TIVITY_START\x10\x00\x12\x11\n\rACTIVITY_STOP\x10\x01\x12\x12\n\x0eLAUNCH_MONITOR\x10\x08\x42\x07\n\x05_typeB\x14\n\x12_AlertNotification\"\x9e\x02\n\x0c\x41lertDetails\x12.\n\x05state\x18\x01 \x01(\x0b\x32\x1a.LaunchMonitor.Proto.StateH\x00\x88\x01\x01\x12\x32\n\x07metrics\x18\x02 \x01(\x0b\x32\x1c.LaunchMonitor.Proto.MetricsH\x01\x88\x01\x01\x12.\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1a.LaunchMonitor.Proto.ErrorH\x02\x88\x01\x01\x12\x45\n\x10tilt_calibration\x18\x04 \x01(\x0b\x32&.LaunchMonitor.Proto.CalibrationStatusH\x03\x88\x01\x01\x42\x08\n\x06_stateB\n\n\x08_metricsB\x08\n\x06_errorB\x13\n\x11_tilt_calibration\"\xb3\x01\n\x05State\x12\x38\n\x05state\x18\x01 \x01(\x0e\x32$.LaunchMonitor.Proto.State.StateTypeH\x00\x88\x01\x01\"f\n\tStateType\x12\x0b\n\x07STANDBY\x10\x00\x12\x15\n\x11INTERFERENCE_TEST\x10\x01\x12\x0b\n\x07WAITING\x10\x02\x12\r\n\tRECORDING\x10\x03\x12\x0e\n\nPROCESSING\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x42\x08\n\x06_state\"\xe1\x02\n\x11\x43\x61librationStatus\x12\x46\n\x06status\x18\x01 \x01(\x0e\x32\x31.LaunchMonitor.Proto.CalibrationStatus.StatusTypeH\x00\x88\x01\x01\x12M\n\x06result\x18\x02 \x01(\x0e\x32\x38.LaunchMonitor.Proto.CalibrationStatus.CalibrationResultH\x01\x88\x01\x01\"a\n\nStatusType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tIN_BOUNDS\x10\x01\x12\x1b\n\x17RECALIBRATION_SUGGESTED\x10\x02\x12\x1a\n\x16RECALIBRATION_REQUIRED\x10\x03\"<\n\x11\x43\x61librationResult\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0f\n\x0bUNIT_MOVING\x10\x02\x42\t\n\x07_statusB\t\n\x07_result\"\xdc\x02\n\x05\x45rror\x12\x37\n\x04\x63ode\x18\x01 \x01(\x0e\x32$.LaunchMonitor.Proto.Error.ErrorCodeH\x00\x88\x01\x01\x12:\n\x08severity\x18\x02 \x01(\x0e\x32#.LaunchMonitor.Proto.Error.SeverityH\x01\x88\x01\x01\x12\x32\n\ndeviceTilt\x18\x03 \x01(\x0b\x32\x19.LaunchMonitor.Proto.TiltH\x02\x88\x01\x01\"T\n\tErrorCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bOVERHEATING\x10\x01\x12\x14\n\x10RADAR_SATURATION\x10\x02\x12\x13\n\x0fPLATFORM_TILTED\x10\x03\"/\n\x08Severity\x12\x0b\n\x07WARNING\x10\x00\x12\x0b\n\x07SERIOUS\x10\x01\x12\t\n\x05\x46\x41TAL\x10\x02\x42\x07\n\x05_codeB\x0b\n\t_severityB\r\n\x0b_deviceTilt\"@\n\x04Tilt\x12\x11\n\x04roll\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x12\n\x05pitch\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\x07\n\x05_rollB\x08\n\x06_pitch\"\x8b\x03\n\x07Metrics\x12\x14\n\x07shot_id\x18\x01 \x01(\rH\x00\x88\x01\x01\x12=\n\tshot_type\x18\x02 \x01(\x0e\x32%.LaunchMonitor.Proto.Metrics.ShotTypeH\x01\x88\x01\x01\x12;\n\x0c\x62\x61ll_metrics\x18\x03 \x01(\x0b\x32 .LaunchMonitor.Proto.BallMetricsH\x02\x88\x01\x01\x12;\n\x0c\x63lub_metrics\x18\x04 \x01(\x0b\x32 .LaunchMonitor.Proto.ClubMetricsH\x03\x88\x01\x01\x12=\n\rswing_metrics\x18\x05 \x01(\x0b\x32!.LaunchMonitor.Proto.SwingMetricsH\x04\x88\x01\x01\"$\n\x08ShotType\x12\x0c\n\x08PRACTICE\x10\x00\x12\n\n\x06NORMAL\x10\x01\x42\n\n\x08_shot_idB\x0c\n\n_shot_typeB\x0f\n\r_ball_metricsB\x0f\n\r_club_metricsB\x10\n\x0e_swing_metrics\"\xbd\x04\n\x0b\x42\x61llMetrics\x12\x19\n\x0claunch_angle\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1d\n\x10launch_direction\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x17\n\nball_speed\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x16\n\tspin_axis\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x17\n\ntotal_spin\x18\x05 \x01(\x02H\x04\x88\x01\x01\x12X\n\x15spin_calculation_type\x18\x06 \x01(\x0e\x32\x34.LaunchMonitor.Proto.BallMetrics.SpinCalculationTypeH\x05\x88\x01\x01\x12J\n\x0egolf_ball_type\x18\x07 \x01(\x0e\x32-.LaunchMonitor.Proto.BallMetrics.GolfBallTypeH\x06\x88\x01\x01\"J\n\x13SpinCalculationType\x12\t\n\x05RATIO\x10\x00\x12\x0f\n\x0b\x42\x41LL_FLIGHT\x10\x01\x12\t\n\x05OTHER\x10\x02\x12\x0c\n\x08MEASURED\x10\x03\"9\n\x0cGolfBallType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0c\x43ONVENTIONAL\x10\x01\x12\n\n\x06MARKED\x10\x02\x42\x0f\n\r_launch_angleB\x13\n\x11_launch_directionB\r\n\x0b_ball_speedB\x0c\n\n_spin_axisB\r\n\x0b_total_spinB\x18\n\x16_spin_calculation_typeB\x11\n\x0f_golf_ball_type\"\xcf\x01\n\x0b\x43lubMetrics\x12\x1c\n\x0f\x63lub_head_speed\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1c\n\x0f\x63lub_angle_face\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x1c\n\x0f\x63lub_angle_path\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x19\n\x0c\x61ttack_angle\x18\x04 \x01(\x02H\x03\x88\x01\x01\x42\x12\n\x10_club_head_speedB\x12\n\x10_club_angle_faceB\x12\n\x10_club_angle_pathB\x0f\n\r_attack_angle\"\xae\x02\n\x0cSwingMetrics\x12\"\n\x15\x62\x61\x63k_swing_start_time\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\"\n\x15\x64own_swing_start_time\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x18\n\x0bimpact_time\x18\x03 \x01(\rH\x02\x88\x01\x01\x12$\n\x17\x66ollow_through_end_time\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x1f\n\x12\x65nd_recording_time\x18\x05 \x01(\rH\x04\x88\x01\x01\x42\x18\n\x16_back_swing_start_timeB\x18\n\x16_down_swing_start_timeB\x0e\n\x0c_impact_timeB\x1a\n\x18_follow_through_end_timeB\x15\n\x13_end_recording_timeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.bluetooth.r10_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WRAPPERPROTO']._serialized_start=49
  _globals['_WRAPPERPROTO']._serialized_end=205
  _globals['_LAUNCHMONITORSERVICE']._serialized_start=208
  _globals['_LAUNCHMONITORSERVICE']._serialized_end=1396
  _globals['_STATUSREQUEST']._serialized_start=1398
  _globals['_STATUSREQUEST']._serialized_end=1413
  _globals['_STATUSRESPONSE']._serialized_start=1415
  _globals['_STATUSRESPONSE']._serialized_end=1489
  _globals['_WAKEUPREQUEST']._serialized_start=1491
  _globals['_WAKEUPREQUEST']._serialized_end=1506
  _globals['_WAKEUPRESPONSE']._serialized_start=1509
  _globals['_WAKEUPRESPONSE']._serialized_end=1678
  _globals['_WAKEUPRESPONSE_RESPONSESTATUS']._serialized_start=1600
  _globals['_WAKEUPRESPONSE_RESPONSESTATUS']._serialized_end=1667
  _globals['_TILTREQUEST']._serialized_start=1680
  _globals['_TILTREQUEST']._serialized_end=1693
  _globals['_TILTRESPONSE']._serialized_start=1695
  _globals['_TILTRESPONSE']._serialized_end=1764
  _globals['_STARTTILTCALIBRATIONREQUEST']._serialized_start=1766
  _globals['_STARTTILTCALIBRATIONREQUEST']._serialized_end=1795
  _globals['_STARTTILTCALIBRATIONRESPONSE']._serialized_start=1798
  _globals['_STARTTILTCALIBRATIONRESPONSE']._serialized_end=1991
  _globals['_STARTTILTCALIBRATIONRESPONSE_CALIBRATIONSTATUS']._serialized_start=1920
  _globals['_STARTTILTCALIBRATIONRESPONSE_CALIBRATIONSTATUS']._serialized_end=1980
  _globals['_RESETTILTCALIBRATIONREQUEST']._serialized_start=1993
  _globals['_RESETTILTCALIBRATIONREQUEST']._serialized_end=2066
  _globals['_RESETTILTCALIBRATIONRESPONSE']._serialized_start=2069
  _globals['_RESETTILTCALIBRATIONRESPONSE']._serialized_end=2286
  _globals['_RESETTILTCALIBRATIONRESPONSE_STATUS']._serialized_start=2180
  _globals['_RESETTILTCALIBRATIONRESPONSE_STATUS']._serialized_end=2275
  _globals['_SHOTCONFIGREQUEST']._serialized_start=2289
  _globals['_SHOTCONFIGREQUEST']._serialized_end=2502
  _globals['_SHOTCONFIGRESPONSE']._serialized_start=2504
  _globals['_SHOTCONFIGRESPONSE']._serialized_end=2558
  _globals['_EVENTSHARING']._serialized_start=2561
  _globals['_EVENTSHARING']._serialized_end=3033
  _globals['_SUBSCRIBEREQUEST']._serialized_start=3035
  _globals['_SUBSCRIBEREQUEST']._serialized_end=3104
  _globals['_SUBSCRIBERESPONSE']._serialized_start=3107
  _globals['_SUBSCRIBERESPONSE']._serialized_end=3444
  _globals['_SUBSCRIBERESPONSE_ALERTSTATUSMESSAGE']._serialized_start=3210
  _globals['_SUBSCRIBERESPONSE_ALERTSTATUSMESSAGE']._serialized_end=3444
  _globals['_SUBSCRIBERESPONSE_ALERTSTATUSMESSAGE_STATUS']._serialized_start=3383
  _globals['_SUBSCRIBERESPONSE_ALERTSTATUSMESSAGE_STATUS']._serialized_end=3414
  _globals['_ALERTSUPPORTREQUEST']._serialized_start=3446
  _globals['_ALERTSUPPORTREQUEST']._serialized_end=3467
  _globals['_ALERTSUPPORTRESPONSE']._serialized_start=3470
  _globals['_ALERTSUPPORTRESPONSE']._serialized_end=3616
  _globals['_ALERTMESSAGE']._serialized_start=3619
  _globals['_ALERTMESSAGE']._serialized_end=3747
  _globals['_ALERTNOTIFICATION']._serialized_start=3750
  _globals['_ALERTNOTIFICATION']._serialized_end=4009
  _globals['_ALERTNOTIFICATION_ALERTTYPE']._serialized_start=3908
  _globals['_ALERTNOTIFICATION_ALERTTYPE']._serialized_end=3978
  _globals['_ALERTDETAILS']._serialized_start=4012
  _globals['_ALERTDETAILS']._serialized_end=4298
  _globals['_STATE']._serialized_start=4301
  _globals['_STATE']._serialized_end=4480
  _globals['_STATE_STATETYPE']._serialized_start=4368
  _globals['_STATE_STATETYPE']._serialized_end=4470
  _globals['_CALIBRATIONSTATUS']._serialized_start=4483
  _globals['_CALIBRATIONSTATUS']._serialized_end=4836
  _globals['_CALIBRATIONSTATUS_STATUSTYPE']._serialized_start=4655
  _globals['_CALIBRATIONSTATUS_STATUSTYPE']._serialized_end=4752
  _globals['_CALIBRATIONSTATUS_CALIBRATIONRESULT']._serialized_start=4754
  _globals['_CALIBRATIONSTATUS_CALIBRATIONRESULT']._serialized_end=4814
  _globals['_ERROR']._serialized_start=4839
  _globals['_ERROR']._serialized_end=5187
  _globals['_ERROR_ERRORCODE']._serialized_start=5017
  _globals['_ERROR_ERRORCODE']._serialized_end=5101
  _globals['_ERROR_SEVERITY']._serialized_start=5103
  _globals['_ERROR_SEVERITY']._serialized_end=5150
  _globals['_TILT']._serialized_start=5189
  _globals['_TILT']._serialized_end=5253
  _globals['_METRICS']._serialized_start=5256
  _globals['_METRICS']._serialized_end=5651
  _globals['_METRICS_SHOTTYPE']._serialized_start=5537
  _globals['_METRICS_SHOTTYPE']._serialized_end=5573
  _globals['_BALLMETRICS']._serialized_start=5654
  _globals['_BALLMETRICS']._serialized_end=6227
  _globals['_BALLMETRICS_SPINCALCULATIONTYPE']._serialized_start=5967
  _globals['_BALLMETRICS_SPINCALCULATIONTYPE']._serialized_end=6041
  _globals['_BALLMETRICS_GOLFBALLTYPE']._serialized_start=6043
  _globals['_BALLMETRICS_GOLFBALLTYPE']._serialized_end=6100
  _globals['_CLUBMETRICS']._serialized_start=6230
  _globals['_CLUBMETRICS']._serialized_end=6437
  _globals['_SWINGMETRICS']._serialized_start=6440
  _globals['_SWINGMETRICS']._serialized_end=6742
# @@protoc_insertion_point(module_scope)