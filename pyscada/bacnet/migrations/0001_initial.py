# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-08 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyscada', '0042_auto_20180604_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='BACnetDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200)),
                ('vendor_id', models.PositiveIntegerField()),
                ('product_name', models.CharField(max_length=200)),
                ('product_model_number', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=400)),
                ('device_id', models.PositiveIntegerField(unique=True)),
                ('mac', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='BACnetDeviceProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.PositiveIntegerField()),
                ('value', models.CharField(max_length=200)),
                ('bacnet_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bacnet.BACnetDevice')),
            ],
        ),
        migrations.CreateModel(
            name='BACnetObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_identifier', models.PositiveIntegerField()),
                ('object_type', models.PositiveIntegerField(choices=[(13, b'multiStateInput'), (25, b'eventLog'), (54, b'lightingOutput'), (48, b'positiveIntegerValue'), (36, b'accessZone'), (11, b'group'), (29, b'structuredView'), (16, b'program'), (46, b'largeAnalogValue'), (32, b'accessCredential'), (43, b'datetimePatternValue'), (4, b'binaryOutput'), (21, b'lifeSafetyPoint'), (33, b'accessPoint'), (2, b'analogValue'), (0, b'analogInput'), (41, b'datePatternValue'), (50, b'timeValue'), (51, b'notificationForwarder'), (23, b'accumulator'), (19, b'multiStateValue'), (44, b'datetimeValue'), (9, b'eventEnrollment'), (45, b'integerValue'), (12, b'loop'), (18, b'averaging'), (15, b'notificationClass'), (1, b'analogOutput'), (35, b'accessUser'), (27, b'trendLogMultiple'), (47, b'octetstringValue'), (10, b'file'), (6, b'calendar'), (40, b'characterstringValue'), (52, b'alertEnrollment'), (22, b'lifeSafetyZone'), (53, b'channel'), (24, b'pulseConverter'), (26, b'globalGroup'), (14, b'multiStateOutput'), (17, b'schedule'), (34, b'accessRights'), (30, b'accessDoor'), (3, b'binaryInput'), (5, b'binaryValue'), (42, b'dateValue'), (8, b'device'), (37, b'credentialDataInput'), (28, b'loadControl'), (20, b'trendLog'), (38, b'networkSecurity'), (7, b'command'), (49, b'timePatternValue'), (39, b'bitstringValue')])),
                ('bacnet_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bacnet.BACnetDevice')),
            ],
        ),
        migrations.CreateModel(
            name='BACnetObjectProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.PositiveIntegerField(choices=[(8, b'all'), (37, b'eventType'), (368, b'executionDelay'), (172, b'slaveProxyEnable'), (144, b'stopWhenFull'), (50, b'integralConstantUnits'), (140, b'recordsSinceNotification'), (364, b'authorizationExemptions'), (173, b'lastNotifyRecord'), (65, b'maxPresValue'), (343, b'bitText'), (235, b'securedStatus'), (102, b'recipientList'), (277, b'lastCredentialAdded'), (233, b'lockStatus'), (371, b'propertyList'), (260, b'authenticationStatus'), (33, b'elapsedActiveTime'), (300, b'passbackMode'), (228, b'doorMembers'), (182, b'limitMonitoringInterval'), (39, b'faultValues'), (379, b'instantaneousPower'), (88, b'priorityForWriting'), (55, b'listOfSessionKeys'), (333, b'packetReorderTime'), (31, b'deviceType'), (166, b'lifeSafetyAlarmValues'), (331, b'lastKeyServer'), (208, b'nodeType'), (184, b'loggingRecord'), (338, b'backupAndRestoreState'), (306, b'threatAuthority'), (168, b'profileName'), (351, b'eventMessageTexts'), (188, b'scaleFactor'), (176, b'adjustValue'), (2, b'action'), (169, b'autoSlaveDiscovery'), (134, b'logInterval'), (219, b'shedDuration'), (210, b'subordinateAnnotations'), (112, b'systemStatus'), (79, b'objectType'), (386, b'egressActive'), (85, b'presentValue'), (262, b'belongsTo'), (77, b'objectName'), (289, b'numberOfAuthenticationPolicies'), (257, b'authenticationFactors'), (41, b'fileAccessMethod'), (131, b'logBuffer'), (118, b'updateInterval'), (174, b'scheduleDefault'), (287, b'musterPoint'), (366, b'channelNumber'), (35, b'eventEnable'), (355, b'eventAlgorithmInhibitRef'), (211, b'subordinateList'), (27, b'derivativeConstantUnits'), (139, b'protocolRevision'), (71, b'modificationDate'), (126, b'bufferSize'), (68, b'minimumOutput'), (278, b'lastCredentialAddedTime'), (383, b'minActualValue'), (19, b'controlledVariableReference'), (44, b'firmwareRevision'), (93, b'proportionalConstant'), (299, b'passbackExemption'), (28, b'description'), (179, b'countChangeTime'), (339, b'backupPreparationTime'), (311, b'userInformationReference'), (292, b'occupancyCountEnable'), (142, b'startTime'), (284, b'masterExemption'), (183, b'loggingObject'), (372, b'serialNumber'), (231, b'doorStatus'), (62, b'maxApduLengthAccepted'), (349, b'covuPeriod'), (48, b'instanceOf'), (357, b'reliabilityEvaluationInhibit'), (20, b'controlledVariableUnits'), (323, b'globalIdentifier'), (365, b'allowGroupDelayInhibit'), (10, b'apduSegmentTimeout'), (291, b'occupancyCountAdjust'), (1, b'ackRequired'), (258, b'authenticationPolicyList'), (212, b'actualShedLevel'), (47, b'inProcess'), (156, b'directReading'), (145, b'totalRecordCount'), (76, b'objectList'), (222, b'stateDescription'), (346, b'groupMemberNames'), (288, b'negativeAccessRules'), (151, b'varianceValue'), (290, b'occupancyCount'), (282, b'lockout'), (160, b'mode'), (161, b'operationExpected'), (218, b'requestedShedLevel'), (245, b'accessAlarmEvents'), (61, b'maximumOutput'), (247, b'accessEvent'), (215, b'fullDutyBaseline'), (382, b'maxActualValue'), (279, b'lastCredentialRemoved'), (202, b'restartNotificationRecipients'), (369, b'lastPriority'), (283, b'lockoutRelinquishTime'), (275, b'lastAccessEvent'), (303, b'reasonForDisable'), (32, b'effectivePeriod'), (302, b'positiveAccessRules'), (354, b'eventAlgorithmInhibit'), (75, b'objectIdentifier'), (286, b'members'), (327, b'baseDeviceSecurityPolicy'), (264, b'credentialStatus'), (69, b'minPresValue'), (123, b'weeklySchedule'), (385, b'transition'), (336, b'supportedSecurityAlgorithms'), (181, b'inputReference'), (91, b'programLocation'), (248, b'accessEventAuthenticationFactor'), (7, b'alarmValues'), (285, b'maxFailedAttempts'), (335, b'securityTimeWindow'), (165, b'zoneMembers'), (86, b'priority'), (72, b'notifyType'), (152, b'activeCovSubscriptions'), (56, b'localDate'), (266, b'credentialsInZone'), (84, b'polarity'), (308, b'traceFlag'), (15, b'changeOfStateCount'), (137, b'notificationThreshold'), (270, b'expiryTime'), (21, b'controlledVariableValue'), (252, b'accompaniment'), (70, b'modelName'), (16, b'changeOfStateTime'), (356, b'timeDelayNormal'), (141, b'recordCount'), (295, b'occupancyLowerLimitEnforced'), (375, b'defaultRampRate'), (24, b'daylightSavingsStatus'), (40, b'feedbackValue'), (380, b'lightingCommand'), (64, b'maxMaster'), (361, b'processIdentifierFilter'), (359, b'faultType'), (22, b'covIncrement'), (125, b'averageValue'), (267, b'daysRemaining'), (254, b'activationTime'), (261, b'authorizationMode'), (143, b'stopTime'), (352, b'eventMessageTextsConfig'), (332, b'networkAccessSecurityPolicies'), (60, b'manipulatedVariableReference'), (45, b'highLimit'), (329, b'doNotHide'), (334, b'securityPDUTimeout'), (52, b'limitEnable'), (317, b'userName'), (3, b'actionText'), (36, b'eventState'), (304, b'supportedFormats'), (87, b'priorityArray'), (234, b'maskedAlarmValues'), (220, b'shedLevelDescriptions'), (377, b'egressTime'), (367, b'controlGroups'), (114, b'timeOfActiveTimeReset'), (34, b'errorLimit'), (180, b'covPeriod'), (67, b'minimumOnTime'), (320, b'zoneFrom'), (347, b'memberStatusFlags'), (209, b'structuredObjectList'), (115, b'timeOfStateCountReset'), (344, b'isUtc'), (345, b'groupMembers'), (294, b'occupancyLowerLimit'), (246, b'accessDoors'), (92, b'programState'), (193, b'alignIntervals'), (155, b'databaseRevision'), (251, b'accessTransactionEvents'), (97, b'protocolServicesSupported'), (203, b'timeOfDeviceRestart'), (148, b'windowSamples'), (253, b'accompanimentTime'), (6, b'alarmValue'), (360, b'localForwardingOnly'), (330, b'keySets'), (74, b'numberOfStates'), (376, b'defaultStepIncrement'), (122, b'vtClassesSupported'), (309, b'transactionNotificationClass'), (89, b'processIdentifier'), (297, b'occupancyUpperLimit'), (90, b'programChange'), (80, b'optional'), (381, b'lightingCommandDefaultPriority'), (293, b'occupancyExemption'), (110, b'stateText'), (186, b'pulseRate'), (42, b'fileSize'), (301, b'passbackTimeout'), (326, b'verificationTime'), (130, b'eventTimeStamps'), (370, b'writeStatus'), (11, b'apduTimeout'), (230, b'doorPulseTime'), (272, b'failedAttemptEvents'), (73, b'numberOfApduRetries'), (296, b'occupancyState'), (373, b'blinkWarnEnable'), (205, b'trigger'), (96, b'protocolObjectTypesSupported'), (259, b'authenticationPolicyNames'), (197, b'loggingType'), (133, b'enable'), (111, b'statusFlags'), (163, b'silenced'), (268, b'entryPoints'), (340, b'restoreCompletionTime'), (53, b'listOfGroupMembers'), (4, b'activeText'), (189, b'updateTime'), (128, b'covResubscriptionInterval'), (146, b'validSamples'), (17, b'notificationClass'), (229, b'doorOpenTooLongTime'), (318, b'userType'), (14, b'bias'), (9, b'allWritesSuccessful'), (94, b'proportionalConstantUnits'), (113, b'timeDelay'), (298, b'occupancyUpperLimitEnforced'), (273, b'failedAttempts'), (46, b'inactiveText'), (206, b'utcTimeSynchronizationRecipients'), (362, b'subscribedRecipients'), (116, b'timeSynchronizationRecipients'), (117, b'units'), (307, b'threatLevel'), (255, b'activeAuthenticationPolicy'), (83, b'eventParameters'), (363, b'portFilter'), (271, b'extendedTimeEnable'), (124, b'attemptedSamples'), (192, b'valueChangeTime'), (23, b'dateList'), (150, b'minimumValueTimestamp'), (57, b'localTime'), (63, b'maxInfoFrames'), (132, b'logDeviceObjectProperty'), (99, b'readOnly'), (164, b'trackingValue'), (196, b'lastRestartReason'), (378, b'inProgress'), (43, b'fileType'), (358, b'faultParameters'), (256, b'assignedAccessRights'), (232, b'doorUnlockDelayTime'), (170, b'manualSlaveAddressBinding'), (153, b'backupFailureTimeout'), (58, b'location'), (157, b'lastRestoreTime'), (276, b'lastAccessPoint'), (310, b'userExternalIdentifier'), (109, b'setpointReference'), (342, b'bitMask'), (322, b'accessEventTag'), (185, b'prescale'), (265, b'credentials'), (337, b'updateKeySetTimeout'), (104, b'relinquishDefault'), (26, b'derivativeConstant'), (353, b'eventDetectionEnable'), (341, b'restorePreparationTime'), (159, b'memberOf'), (49, b'integralConstant'), (305, b'supportedFormatClasses'), (214, b'expectedShedLevel'), (191, b'valueSet'), (195, b'intervalOffset'), (171, b'slaveAddressBinding'), (167, b'maxSegmentsAccepted'), (78, b'objectPropertyReference'), (98, b'protocolVersion'), (221, b'shedLevels'), (274, b'failedAttemptsTime'), (38, b'exceptionSchedule'), (187, b'scale'), (269, b'exitPoints'), (250, b'accessEventTime'), (107, b'segmentationSupported'), (25, b'deadband'), (384, b'power'), (29, b'descriptionOfHalt'), (147, b'windowInterval'), (280, b'lastCredentialRemovedTime'), (319, b'usesRemaining'), (59, b'lowLimit'), (66, b'minimumOffTime'), (127, b'clientCovIncrement'), (348, b'requestedUpdateInterval'), (227, b'doorExtendedPulseTime'), (321, b'zoneTo'), (0, b'ackedTransitions'), (135, b'maximumValue'), (281, b'lastUseTime'), (120, b'vendorIdentifier'), (121, b'vendorName'), (108, b'setpoint'), (100, b'reasonForHalt'), (213, b'dutyWindow'), (177, b'count'), (82, b'outputUnits'), (5, b'activeVtSessions'), (178, b'countBeforeChange'), (374, b'defaultFadeTime'), (103, b'reliability'), (226, b'doorAlarmState'), (158, b'maintenanceRequired'), (136, b'minimumValue'), (13, b'archive'), (30, b'deviceAddressBinding'), (204, b'timeSynchronizationInterval'), (149, b'maximumValueTimestamp'), (162, b'setting'), (263, b'credentialDisable'), (350, b'covuRecipients'), (175, b'acceptedModes'), (244, b'absenteeLimit'), (54, b'listOfObjectPropertyReferences'), (154, b'configurationFiles'), (81, b'outOfService'), (12, b'applicationSoftwareVersion'), (105, b'required'), (249, b'accessEventCredential'), (207, b'nodeSubtype'), (119, b'utcOffset'), (328, b'distributionKeyRevision'), (190, b'valueBeforeChange'), (106, b'resolution')])),
                ('priority', models.PositiveIntegerField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('bacnet_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bacnet.BACnetObject')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedBACnetDevice',
            fields=[
            ],
            options={
                'verbose_name': 'BACnet Device',
                'proxy': True,
                'verbose_name_plural': 'BACnet Devices',
                'indexes': [],
            },
            bases=('pyscada.device',),
        ),
        migrations.CreateModel(
            name='ExtendedBACnetVariable',
            fields=[
            ],
            options={
                'verbose_name': 'BACnet Variable',
                'proxy': True,
                'verbose_name_plural': 'BACnet Variables',
                'indexes': [],
            },
            bases=('pyscada.variable',),
        ),
        migrations.AddField(
            model_name='bacnetobject',
            name='bacnet_variable',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='bacnetdevice',
            name='bacnet_device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Device'),
        ),
    ]